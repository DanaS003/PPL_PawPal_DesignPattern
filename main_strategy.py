# main_strategy.py
from strategi_pembayaran import TransferBank, EWallet #

class KonteksPembayaran:
    def __init__(self, strategi: object):
        self._strategi = strategi #

    def set_strategi(self, strategi: object):
        self._strategi = strategi #

    def execute_pembayaran(self, jumlah):
        self._strategi.bayar(jumlah) #

def main_strategy():
    print("--- Demonstrasi Strategy Pattern ---")

    # 1. Inisialisasi strategi pembayaran
    transfer_bank = TransferBank() #
    e_wallet = EWallet() #

    # 2. Buat konteks pembayaran dengan strategi awal
    pembayaran_saya = KonteksPembayaran(transfer_bank) #

    print("\n--- Pembayaran pertama (Transfer Bank) ---")
    pembayaran_saya.execute_pembayaran(500000) #

    # 3. Ganti strategi pembayaran saat runtime
    print("\n--- Mengganti strategi ke E-Wallet ---")
    pembayaran_saya.set_strategi(e_wallet) #

    print("\n--- Pembayaran kedua (E-Wallet) ---")
    pembayaran_saya.execute_pembayaran(250000) #

    # 4. Kembali ke Transfer Bank
    print("\n--- Mengganti strategi kembali ke Transfer Bank ---")
    pembayaran_saya.set_strategi(transfer_bank) #

    print("\n--- Pembayaran ketiga (Transfer Bank) ---")
    pembayaran_saya.execute_pembayaran(100000) #

if __name__ == "__main__":
    main_strategy()