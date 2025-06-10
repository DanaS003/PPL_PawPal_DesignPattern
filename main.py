import datetime
from data import users_db, list_hewan, list_pengajuan_adopsi, registered_users
from strategi_pembayaran import TransferBank, EWallet
from form_adopsi import PengajuanAdopsi
from util import input_validasi
from observer import Adopter, Shelter
from model_hewan import HewanFactory # <-- TAMBAHKAN BARIS INI

strategi_pembayaran = {
    "1": TransferBank(),
    "2": EWallet()
}

def tampilkan_detail_hewan(hewan):
    print(f"\n--- DETAIL HEWAN ---")
    print(f"Nama: {hewan.nama}\nJenis: {hewan.jenis}\nUmur: {hewan.umur}")
    print(f"Shelter: {hewan.shelter.nama}")
    print(f"Steril: {'✅' if hewan.steril else '❌'}")
    print(f"Riwayat Kesehatan: {hewan.riwayat_kesehatan}")
    print("Detail Vaksin:")
    if hewan.daftar_vaksin:
        for vaksin in hewan.daftar_vaksin:
            print(f"  - {vaksin}")
    else:
        print("  Tidak ada informasi vaksin yang tersedia.")
    print(f"Harga Adopsi: Rp{hewan.harga_adopsi:,}")

def proses_chat_shelter(hewan, user): # user di sini adalah objek Adopter atau Shelter
    print(f"\n--- CHAT DENGAN SHELTER ({hewan.shelter.nama}) ---")
    print("Anda: Halo, apakah hewan ini masih tersedia?")
    print("Shelter: Ya, masih tersedia. Silakan ajukan adopsi atau kunjungi kami.")
    chat_message = input("Tulis pesan Anda (atau 'kembali'): ")
    if chat_message.lower() != 'kembali':
        print(f"Pesan Anda terkirim ke {hewan.shelter.nama}: '{chat_message}'")
        hewan.shelter.update(f"Pesan baru dari {user.nama}: {chat_message} (terkait {hewan.nama})")


def proses_pengajuan(hewan, adopter_obj):
    if hewan.status_adopsi != "available":
        print(f"[!] Hewan {hewan.nama} tidak tersedia untuk adopsi saat ini (Status: {hewan.status_adopsi}).")
        return

    pengajuan = PengajuanAdopsi(hewan, adopter_obj, hewan.shelter)
    pengajuan.ajukan()
    list_pengajuan_adopsi.append(pengajuan)
    
    hewan.status_adopsi = "pending_adoption" 
    
    print(f"[✔] Status: Permintaan adopsi untuk {hewan.nama} telah dikirim ke shelter. ID Pengajuan: {pengajuan.id}")
    print(f"[INFO] Status hewan {hewan.nama} diperbarui menjadi: {hewan.status_adopsi}.")
    adopter_obj.update(f"Pengajuan adopsi Anda untuk {hewan.nama} telah diajukan. ID: {pengajuan.id}")

def proses_kunjungan_adopter(pengajuan):
    print(f"\n--- JADWALKAN KUNJUNGAN UNTUK PENGAJUAN {pengajuan.id} ---")
    if pengajuan.status not in ["under_review", "home_visit_scheduled", "payment_successful"]:
        print(f"[!] Kunjungan tidak dapat dijadwalkan pada status pengajuan saat ini ({pengajuan.status}).")
        return

    print("Kunjungan ini meliputi pengecekan lokasi shelter dan kondisi tempat tinggal calon adopter.")
    print(f"Silakan hubungi shelter {pengajuan.shelter.nama} untuk menjadwalkan waktu yang sesuai.")
    print(f"Kontak Shelter {pengajuan.shelter.nama}: (contoh: 0812-3456-7890)")
    
    tanggal_kunjungan_str = input("Masukkan tanggal kunjungan yang diinginkan (YYYY-MM-DD): ")
    try:
        tanggal_kunjungan = datetime.datetime.strptime(tanggal_kunjungan_str, "%Y-%m-%d").date()
    except ValueError:
        print("[!] Format tanggal salah. Menggunakan tanggal default (3 hari dari sekarang).")
        tanggal_kunjungan = datetime.date.today() + datetime.timedelta(days=3)

    pengajuan.set_jadwal_kunjungan(tanggal_kunjungan.strftime('%Y-%m-%d'))
    
    print("\n--- SIMULASI HASIL KUNJUNGAN ---")
    print("🔍 Kunjungan telah dilakukan. Menunggu konfirmasi dari shelter.")
    print("✅ Untuk simulasi, anggap shelter menyatakan Anda layak sebagai adopter.")
    pengajuan.set_hasil_kunjungan("layak")
    
    if pengajuan.status == "home_visit_completed":
        print("\nSekarang Anda bisa melanjutkan ke pembayaran adopsi.")
        
def proses_pembayaran_adopter(pengajuan):
    if pengajuan.status not in ["home_visit_completed", "approved"]:
        print(f"[!] Pembayaran tidak dapat dilakukan pada status pengajuan saat ini ({pengajuan.status}). Mohon selesaikan kunjungan atau tunggu persetujuan.")
        return

    print("\n--- PEMBAYARAN ADOPSI ---")
    print(f"Hewan: {pengajuan.hewan.nama} (Harga: Rp{pengajuan.hewan.harga_adopsi:,})")
    print("Metode Pembayaran:\n[1] Transfer Bank\n[2] E-Wallet")
    metode_pilihan = input_validasi("Pilih metode: ", ["1", "2"])
    
    pengajuan.set_metode_pembayaran(strategi_pembayaran[metode_pilihan])
    pengajuan.proses_pembayaran(pengajuan.hewan.harga_adopsi)

    if pengajuan.status == "payment_successful":
        konfirmasi_adopsi = input_validasi("Apakah adopsi telah dikonfirmasi dan hewan telah Anda terima? (ya/tidak): ", ["ya", "tidak"])
        if konfirmasi_adopsi == "ya":
            pengajuan.set_status("completed")
            pengajuan.hewan.status_adopsi = "adopted"
            print(f"[INFO] Status hewan {pengajuan.hewan.nama} diperbarui menjadi: {pengajuan.hewan.status_adopsi}.")
            print(f"\n--- Adopsi {pengajuan.hewan.nama} selesai! ---")
            print(f"\n--- Beri Rating/Review untuk Shelter {pengajuan.shelter.nama} ---")
            rating = int(input_validasi("Beri rating (1-5): ", [str(i) for i in range(1, 6)]))
            review = input("Tulis review Anda: ")
            pengajuan.beri_rating_review(rating, review)
        else:
            print("❗ Adopsi belum dikonfirmasi selesai. Mohon segera hubungi shelter.")

def proses_add_hewan_shelter(current_shelter):
    print("\n--- TAMBAH HEWAN BARU ---")
    nama = input("Nama hewan: ")
    jenis = input("Jenis hewan (misal: Anjing, Golden Retriever): ")
    umur = input("Umur hewan (misal: 2 tahun): ")
    steril_input = input_validasi("Sudah steril? (ya/tidak): ", ["ya", "tidak"])
    steril = True if steril_input == "ya" else False
    harga_adopsi_str = input("Harga Adopsi (angka, misal: 250000): ")
    try:
        harga_adopsi = int(harga_adopsi_str)
    except ValueError:
        print("[!] Harga tidak valid. Menggunakan default 0.")
        harga_adopsi = 0

    hewan_baru = HewanFactory.buat_hewan({
        "nama": nama,
        "jenis": jenis,
        "umur": umur,
        "shelter": current_shelter,
        "riwayat_kesehatan": "Belum ada informasi medis lengkap.",
        "daftar_vaksin": [],
        "harga_adopsi": harga_adopsi,
        "steril": steril
    })
    list_hewan.append(hewan_baru)
    current_shelter.update(f"Hewan baru ditambahkan: {hewan_baru.nama}")
    print(f"✅ Hewan {hewan_baru.nama} berhasil ditambahkan oleh {current_shelter.nama}!")

def proses_verifikasi_pengajuan_shelter(current_shelter):
    print("\n--- VERIFIKASI PENGAJUAN ADOPSI ---")
    pengajuan_shelter_ini = [p for p in list_pengajuan_adopsi if p.shelter == current_shelter and p.status != "completed"]

    if not pengajuan_shelter_ini:
        print("Tidak ada pengajuan adopsi yang perlu diverifikasi saat ini.")
        return

    print("Daftar Pengajuan:")
    for i, p in enumerate(pengajuan_shelter_ini):
        print(f"[{i+1}] ID: {p.id}, Hewan: {p.hewan.nama}, Adopter: {p.adopter.nama}, Status: {p.status}")

    idx = int(input_validasi("\nPilih pengajuan untuk diverifikasi (angka): ", [str(i+1) for i in range(len(pengajuan_shelter_ini))])) - 1
    pengajuan_terpilih = pengajuan_shelter_ini[idx]

    print(f"\nDetail Pengajuan ID: {pengajuan_terpilih.id}")
    print(f"Hewan: {pengajuan_terpilih.hewan.nama}, Adopter: {pengajuan_terpilih.adopter.nama}")
    print(f"Status Saat Ini: {pengajuan_terpilih.status}")

    if pengajuan_terpilih.status == "pending" or pengajuan_terpilih.status == "under_review":
        aksi = input_validasi("Aksi: [1] Jadwalkan Kunjungan, [2] Tolak, [3] Kembali: ", ["1", "2", "3"])
        if aksi == "1":
            tanggal_kunjungan_str = input("Masukkan tanggal kunjungan (YYYY-MM-DD): ")
            try:
                tanggal_kunjungan = datetime.datetime.strptime(tanggal_kunjungan_str, "%Y-%m-%d").date()
                pengajuan_terpilih.set_jadwal_kunjungan(tanggal_kunjungan.strftime('%Y-%m-%d'))
            except ValueError:
                print("[!] Format tanggal salah.")
        elif aksi == "2":
            pengajuan_terpilih.set_status("rejected")
            pengajuan_terpilih.hewan.status_adopsi = "available"
            print(f"[INFO] Status hewan {pengajuan_terpilih.hewan.nama} diperbarui menjadi: {pengajuan_terpilih.hewan.status_adopsi}.")
        elif aksi == "3":
            pass
    elif pengajuan_terpilih.status == "home_visit_scheduled":
        aksi = input_validasi("Aksi: [1] Konfirmasi Hasil Kunjungan, [2] Tolak, [3] Kembali: ", ["1", "2", "3"])
        if aksi == "1":
            hasil_kunjungan = input_validasi("Hasil kunjungan: [1] Layak, [2] Tidak Layak: ", ["1", "2"])
            if hasil_kunjungan == "1":
                pengajuan_terpilih.set_hasil_kunjungan("layak")
                pengajuan_terpilih.set_status("approved")
            else:
                pengajuan_terpilih.set_hasil_kunjungan("tidak layak")
                pengajuan_terpilih.set_status("rejected")
                pengajuan_terpilih.hewan.status_adopsi = "available"
                print(f"[INFO] Status hewan {pengajuan_terpilih.hewan.nama} diperbarui menjadi: {pengajuan_terpilih.hewan.status_adopsi}.")
        elif aksi == "2":
            pengajuan_terpilih.set_status("rejected")
            pengajuan_terpilih.hewan.status_adopsi = "available"
            print(f"[INFO] Status hewan {pengajuan_terpilih.hewan.nama} diperbarui menjadi: {pengajuan_terpilih.hewan.status_adopsi}.")
        elif aksi == "3":
            pass
    elif pengajuan_terpilih.status == "payment_successful":
        aksi = input_validasi("Aksi: [1] Konfirmasi Penjemputan, [2] Kembali: ", ["1", "2"])
        if aksi == "1":
            pengajuan_terpilih.set_status("completed")
            pengajuan_terpilih.hewan.status_adopsi = "adopted"
            print(f"[INFO] Status hewan {pengajuan_terpilih.hewan.nama} diperbarui menjadi: {pengajuan_terpilih.hewan.status_adopsi}.")
            print(f"✅ Pengajuan {pengajuan_terpilih.id} selesai. {pengajuan_terpilih.hewan.nama} telah diadopsi!")
        elif aksi == "2":
            pass
    else:
        print("Pengajuan ini tidak memerlukan aksi lebih lanjut dari Anda saat ini.")

def simulasi():
    print("=== Selamat datang di PawPal ===")
    email = input("Masukkan email: ")
    password = input("Masukkan password: ")

    user_info = users_db.get(email)
    if not user_info or user_info["password"] != password:
        print("[ERROR] Login gagal. Email atau password salah.")
        return

    role = user_info["role"]
    current_user_obj = registered_users[email]

    print(f"\n[INFO] Login berhasil! Selamat datang, {current_user_obj.nama} (Role: {role.upper()})!")

    if role == "adopter":
        while True:
            print("\n--- MENU ADOPTER ---")
            print("1. Lihat Hewan untuk Diadopsi")
            print("2. Lihat Notifikasi Saya")
            print("3. Keluar")
            opsi = input_validasi("Pilih opsi: ", ["1", "2", "3"])

            if opsi == "3":
                print("\n=== TERIMA KASIH TELAH MENGGUNAKAN PAWPAL ===")
                break
            elif opsi == "2":
                print("\n--- NOTIFIKASI SAYA ---")
                if current_user_obj.notifikasi_masuk:
                    for notif in current_user_obj.notifikasi_masuk:
                        print(f"- {notif}")
                else:
                    print("Tidak ada notifikasi baru.")
                continue

            print("\n--- DAFTAR HEWAN ---")
            hewan_tersedia = [h for h in list_hewan if h.status_adopsi == "available"]
            if not hewan_tersedia:
                print("Tidak ada hewan tersedia untuk adopsi saat ini.")
                continue

            for i, h in enumerate(hewan_tersedia):
                print(f"[{i+1}] {h.nama} - {h.jenis} - {h.umur} - Shelter: {h.shelter.nama}")

            idx = int(input_validasi("\nPilih hewan (angka): ", [str(i+1) for i in range(len(hewan_tersedia))])) - 1
            hewan = hewan_tersedia[idx]

            tampilkan_detail_hewan(hewan)

            pengajuan_saat_ini = next((p for p in list_pengajuan_adopsi if p.hewan == hewan and p.adopter == current_user_obj), None)

            while True:
                print("\n--- AKSI ADOPTER ---")
                print("[1] Chat dengan Shelter")
                print("[2] Ajukan Adopsi")
                print("[3] Jadwalkan & Proses Kunjungan (jika pengajuan sudah dibuat)")
                print("[4] Bayar Adopsi (jika pengajuan sudah layak)")
                print("[5] Kembali ke Daftar Hewan")
                aksi = input_validasi("Pilih opsi: ", ["1", "2", "3", "4", "5"])

                if aksi == "1":
                    proses_chat_shelter(hewan, current_user_obj)
                elif aksi == "2":
                    if pengajuan_saat_ini:
                        print("[!] Anda sudah memiliki pengajuan adopsi untuk hewan ini. Status:", pengajuan_saat_ini.status)
                    else:
                        proses_pengajuan(hewan, current_user_obj)
                        pengajuan_saat_ini = next((p for p in list_pengajuan_adopsi if p.hewan == hewan and p.adopter == current_user_obj), None)
                elif aksi == "3":
                    if pengajuan_saat_ini:
                        proses_kunjungan_adopter(pengajuan_saat_ini)
                    else:
                        print("[!] Anda harus mengajukan adopsi terlebih dahulu.")
                elif aksi == "4":
                    if pengajuan_saat_ini:
                        proses_pembayaran_adopter(pengajuan_saat_ini)
                    else:
                        print("[!] Anda harus mengajukan adopsi terlebih dahulu.")
                elif aksi == "5":
                    break

    elif role == "shelter":
        while True:
            print("\n--- MENU SHELTER ---")
            print("1. Lihat Notifikasi Saya")
            print("2. Tambah Hewan Baru")
            print("3. Verifikasi Pengajuan Adopsi")
            print("4. Lihat Daftar Hewan Saya")
            print("5. Keluar")
            opsi = input_validasi("Pilih opsi: ", ["1", "2", "3", "4", "5"])

            if opsi == "5":
                print("\n=== TERIMA KASIH TELAH MENGGUNAKAN PAWPAL ===")
                break
            elif opsi == "1":
                print("\n--- NOTIFIKASI SAYA ---")
                if current_user_obj.notifikasi_masuk:
                    for notif in current_user_obj.notifikasi_masuk:
                        print(f"- {notif}")
                else:
                    print("Tidak ada notifikasi baru.")
                continue
            elif opsi == "2":
                proses_add_hewan_shelter(current_user_obj)
            elif opsi == "3":
                proses_verifikasi_pengajuan_shelter(current_user_obj)
            elif opsi == "4":
                print(f"\n--- DAFTAR HEWAN DI SHELTER {current_user_obj.nama} ---")
                hewan_shelter = [h for h in list_hewan if h.shelter == current_user_obj]
                if not hewan_shelter:
                    print("Tidak ada hewan yang terdaftar di shelter ini.")
                    continue
                for i, h in enumerate(hewan_shelter):
                    print(f"[{i+1}] {h.nama} - {h.jenis} - Umur: {h.umur} - Status: {h.status_adopsi}")
                
                detail_opsi = input_validasi("Lihat detail hewan? (ya/tidak): ", ["ya", "tidak"])
                if detail_opsi == "ya":
                    idx_detail = int(input_validasi("\nPilih hewan untuk detail (angka): ", [str(i+1) for i in range(len(hewan_shelter))])) - 1
                    tampilkan_detail_hewan(hewan_shelter[idx_detail])


if __name__ == "__main__":
    simulasi()