import datetime
from data import users, list_hewan
from strategi_pembayaran import TransferBank, EWallet
from form_adopsi import FormAdopsi
from util import input_validasi
from observer import AdoptionMediator # Import AdoptionMediator

strategi_pembayaran = {
    "1": TransferBank(),
    "2": EWallet()
}

def tampilkan_detail_hewan(hewan):
    print(f"\n--- DETAIL HEWAN ---")
    print(f"Nama: {hewan.nama}\nJenis: {hewan.jenis}\nUmur: {hewan.umur}")
    print(f"Steril: {'✅' if hewan.steril else '❌'}")
    print(f"Riwayat Kesehatan: {hewan.riwayat_kesehatan}")
    print("Detail Vaksin:")
    if hewan.daftar_vaksin:
        for vaksin in hewan.daftar_vaksin:
            print(f"  - {vaksin}")
    else:
        print("  Tidak ada informasi vaksin yang tersedia.")

def proses_chat_shelter(hewan):
    print(f"\n--- CHAT SHELTER ({hewan.shelter.nama}) ---")
    print("Anda: Halo, apakah hewan ini masih tersedia?")
    print("Shelter: Ya, masih tersedia. Silakan ajukan adopsi atau kunjungi kami.")

def proses_adopsi(hewan, user):
    # Inisialisasi mediator dan passing ke FormAdopsi
    mediator = AdoptionMediator(hewan.shelter)
    form = FormAdopsi(hewan, user, hewan.shelter, mediator)
    form.ajukan()
    print("[✔] Status: Permintaan adopsi telah dikirim ke shelter. Silakan lanjutkan dengan kunjungan.")

def proses_kunjungan(hewan, user):
    print("\n--- JADWALKAN KUNJUNGAN ---")
    print("Kunjungan ini meliputi:")
    print("- Pengecekan lokasi shelter (untuk memastikan kondisi hewan)")
    print("- Pengecekan kondisi tempat tinggal calon adopter (untuk memastikan kelayakan adopsi)")
    print("Silakan hubungi shelter untuk menjadwalkan waktu yang sesuai.")
    print(f"Kontak Shelter {hewan.shelter.nama}: (contoh: 0812-3456-7890)")

    tanggal_kunjungan = datetime.date.today() + datetime.timedelta(days=3)
    print(f"📅 Permintaan kunjungan Anda akan diteruskan ke shelter. Mohon menunggu konfirmasi jadwal.")
    print(f"✅ Kunjungan dijadwalkan pada: {tanggal_kunjungan.strftime('%d %B %Y')}")

    print("\n--- SIMULASI KUNJUNGAN ---")
    print("🔍 Kunjungan telah dilakukan.")
    print("✅ Shelter menyatakan Anda layak sebagai adopter.")
    print("✅ Data hewan sesuai dan cocok untuk diadopsi.")

    lanjut = input_validasi("Lanjut ke pembayaran adopsi? (ya/tidak): ", ["ya", "tidak"])
    if lanjut == "ya":
        proses_pembayaran(hewan, user)
    else:
        print("❗ Adopsi dibatalkan sebelum pembayaran.")

def proses_pembayaran(hewan, user):
    print("\n--- PEMBAYARAN ADOPSI ---")
    # Inisialisasi mediator dan passing ke FormAdopsi (opsional, tergantung interaksi apa yang ingin dimediasi di sini)
    mediator = AdoptionMediator(hewan.shelter)
    form = FormAdopsi(hewan, user, hewan.shelter, mediator)
    print("Metode Pembayaran:\n[1] Transfer Bank\n[2] E-Wallet")
    metode = input_validasi("Pilih metode: ", ["1", "2"])
    form.set_metode_pembayaran(strategi_pembayaran[metode])
    form.metode.bayar(form.jumlah)
    print(f"✅ Pembayaran berhasil. Invoice ID: {form.invoice_id}")

    konfirmasi_adopsi = input_validasi("Apakah adopsi telah dikonfirmasi dan hewan telah Anda terima? (ya/tidak): ", ["ya", "tidak"])
    if konfirmasi_adopsi == "ya":
        print(f"\n--- Beri Rating/Review untuk {hewan.nama} ---")
        rating = input_validasi("Beri rating (1-5): ", [str(i) for i in range(1, 6)])
        review = input("Tulis review Anda: ")
        print(f"Terima kasih atas rating ({rating}/5) dan review Anda: '{review}' untuk {hewan.nama}!")

def simulasi():
    print("=== Selamat datang di PawPal ===")
    email = input("Masukkan email: ")
    password = input("Masukkan password: ")

    if email not in users or users[email] != password:
        print("[ERROR] Login gagal. Email atau password salah.")
        return

    user = email.split("@")[0].capitalize()
    print(f"\n[INFO] Login berhasil! Selamat datang, {user}!")

    while True:
        print("\n--- MENU UTAMA ---")
        print("1. Lihat Hewan untuk Diadopsi\n2. Keluar")
        opsi = input_validasi("Pilih opsi: ", ["1", "2"])

        if opsi == "2":
            print("\n=== TERIMA KASIH TELAH MENGGUNAKAN PAWPAL ===")
            break

        print("\n--- DAFTAR HEWAN ---")
        for i, h in enumerate(list_hewan):
            print(f"[{i+1}] {h.nama} - {h.jenis} - {h.umur} - Shelter: {h.shelter.nama}")

        idx = int(input_validasi("\nPilih hewan (angka): ", [str(i+1) for i in range(len(list_hewan))])) - 1
        hewan = list_hewan[idx]

        tampilkan_detail_hewan(hewan)

        while True:
            print("\n[1] Chat dengan Shelter\n[2] Ajukan Adopsi\n[3] Jadwalkan Kunjungan\n[4] Bayar Adopsi\n[5] Kembali")
            aksi = input_validasi("Pilih opsi: ", ["1", "2", "3", "4", "5"])

            if aksi == "1":
                proses_chat_shelter(hewan)
            elif aksi == "2":
                proses_adopsi(hewan, user)
            elif aksi == "3":
                proses_kunjungan(hewan, user)
            elif aksi == "4":
                proses_pembayaran(hewan, user)
            elif aksi == "5":
                break

if __name__ == "__main__":
    simulasi()