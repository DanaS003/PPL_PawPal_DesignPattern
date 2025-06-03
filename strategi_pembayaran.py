from abc import ABC, abstractmethod

class StrategiPembayaran(ABC):
    @abstractmethod
    def bayar(self, jumlah):
        pass

class TransferBank(StrategiPembayaran):
    def bayar(self, jumlah):
        print(f"[Transfer Bank] Pembayaran sebesar Rp{jumlah:,} berhasil.")

class EWallet(StrategiPembayaran):
    def bayar(self, jumlah):
        print(f"[E-Wallet] Pembayaran sebesar Rp{jumlah:,} berhasil.")
