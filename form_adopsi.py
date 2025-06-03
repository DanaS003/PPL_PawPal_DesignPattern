import uuid # Tambahkan ini

class FormAdopsi:
    def __init__(self, hewan, user, shelter):
        self.hewan = hewan
        self.user = user
        self.shelter = shelter
        self.metode = None
        self.jumlah = 300_000
        self.invoice_id = str(uuid.uuid4()) 

    def set_metode_pembayaran(self, metode):
        self.metode = metode

    def ajukan(self):
        self.metode.bayar(self.jumlah)
        print(f"Invoice created dengan ID: {self.invoice_id}")
        self.shelter.update(f"Permintaan adopsi untuk {self.hewan.nama} dari {self.user}")
        print(f"🎉 Permintaan adopsi telah diajukan untuk {self.hewan.nama} oleh {self.user}\n")