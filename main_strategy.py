# main_strategy.py
from strategi_pembayaran import TransferBank, EWallet, StrategiPembayaran
from data import list_hewan, adopter_john, shelter_happy
from form_adopsi import PengajuanAdopsi 

def main_strategy():
    print("--- Demonstrasi Strategy Pattern (Metode Pembayaran) ---")

    # Asumsi kita memiliki pengajuan adopsi yang siap untuk pembayaran
    # Untuk demo, kita akan membuat pengajuan dummy dan mengatur statusnya
    if not list_hewan:
        print("Tidak ada hewan dalam daftar untuk demonstrasi.")
        return

    hewan_untuk_adopsi = list_hewan[0]
    print(f"Hewan yang akan diadopsi: {hewan_untuk_adopsi.nama} (Harga: Rp{hewan_untuk_adopsi.harga_adopsi:,})")

    # Membuat objek pengajuan adopsi (asumsi sudah melewati tahap verifikasi dan kunjungan)
    pengajuan_demo = PengajuanAdopsi(hewan_untuk_adopsi, adopter_john, shelter_happy)
    pengajuan_demo.set_status("home_visit_completed") # Atur status agar bisa bayar

    print("\nPilih metode pembayaran:")
    print("[1] Transfer Bank")
    print("[2] E-Wallet")

    pilihan = input("Masukkan pilihan Anda (1/2): ")

    if pilihan == "1":
        # Menggunakan strategi Transfer Bank
        metode_pembayaran_terpilih = TransferBank()
    elif pilihan == "2":
        # Menggunakan strategi E-Wallet
        metode_pembayaran_terpilih = EWallet()
    else:
        print("[!] Pilihan tidak valid. Menggunakan Transfer Bank sebagai default.")
        metode_pembayaran_terpilih = TransferBank()

    # Mengatur strategi pembayaran untuk pengajuan adopsi
    pengajuan_demo.set_metode_pembayaran(metode_pembayaran_terpilih)

    # Memproses pembayaran menggunakan strategi yang dipilih
    print(f"\nMemproses pembayaran untuk hewan {hewan_untuk_adopsi.nama}...")
    pengajuan_demo.proses_pembayaran(hewan_untuk_adopsi.harga_adopsi)

    print(f"\nStatus pengajuan setelah pembayaran: {pengajuan_demo.status}")

if __name__ == "__main__":
    main_strategy()