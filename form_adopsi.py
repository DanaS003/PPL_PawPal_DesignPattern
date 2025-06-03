import uuid

class FormAdopsi:
    def __init__(self, hewan, user, shelter):
        self.hewan = hewan
        self.user = user
        self.shelter = shelter
        self.metode = None
        # self.jumlah = 300_000 # Tidak lagi hardcoded, akan diambil dari hewan.harga_adopsi
        self.invoice_id = str(uuid.uuid4()) 

    def set_metode_pembayaran(self, metode):
        self.metode = metode

    def ajukan(self):
        print(f"📄 Permintaan adopsi diajukan untuk {self.hewan.nama} oleh {self.user}.")
        print(f"Invoice ID: {self.invoice_id}")
        self.shelter.update(f"Permintaan adopsi untuk {self.hewan.nama} dari {self.user}")