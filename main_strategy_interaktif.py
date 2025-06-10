# main_strategy.py
from strategi_pembayaran import TransferBank, EWallet
from util import input_validasi # Import fungsi input_validasi

class KonteksPembayaran:
    def __init__(self, strategi: object):
        self._strategi = strategi

    def set_strategi(self, strategi: object):
        self._strategi = strategi

    def execute_pembayaran(self, jumlah):
        self._strategi.bayar(jumlah)

def main_strategy():
    print("--- Demonstrasi Interaktif Strategy Pattern ---")

    # Inisialisasi strategi pembayaran yang tersedia
    strategi_yang_tersedia = {
        "1": TransferBank(),
        "2": EWallet()
    }

    # Konteks pembayaran awal (bisa diatur ke strategi default atau None)
    # Kita akan meminta pengguna memilih strategi pertama kali
    pembayaran_saya = None

    while True:
        print("\n--- Menu Pembayaran (Strategy Demo) ---")
        print("1. Lakukan Pembayaran Baru")
        print("2. Keluar")

        pilihan_menu = input_validasi("Pilih opsi: ", ["1", "2"])

        if pilihan_menu == "1":
            print("\n--- Pilihan Metode Pembayaran ---")
            print("[1] Transfer Bank")
            print("[2] E-Wallet")
            
            metode_pilihan = input_validasi("Pilih metode pembayaran: ", ["1", "2"])
            
            # Set strategi sesuai pilihan pengguna
            pembayaran_saya = KonteksPembayaran(strategi_yang_tersedia[metode_pilihan])

            jumlah_str = input("Masukkan jumlah pembayaran (angka, misal: 150000): Rp")
            try:
                jumlah = int(jumlah_str)
                if jumlah <= 0:
                    print("[!] Jumlah pembayaran harus positif.")
                    continue
            except ValueError:
                print("[!] Jumlah pembayaran tidak valid. Masukkan angka.")
                continue

            print(f"\nMelakukan pembayaran sebesar Rp{jumlah:,}...")
            pembayaran_saya.execute_pembayaran(jumlah)
            print("✅ Proses pembayaran selesai.")

        elif pilihan_menu == "2":
            print("\n=== Terima kasih telah menggunakan demo Strategy Pattern! ===")
            break

if __name__ == "__main__":
    main_strategy()