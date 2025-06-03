import uuid

class FormAdopsi:
    def __init__(self, hewan, user, shelter, mediator=None): # Tambahkan mediator
        self.hewan = hewan
        self.user = user
        self.shelter = shelter
        self.metode = None
        self.jumlah = 300_000
        self.invoice_id = str(uuid.uuid4())
        self._mediator = mediator # Simpan referensi mediator

    def set_metode_pembayaran(self, metode):
        self.metode = metode

    def ajukan(self):
        print(f"📄 Permintaan adopsi diajukan untuk {self.hewan.nama} oleh {self.user}.")
        print(f"Invoice ID: {self.invoice_id}")
        if self._mediator: # Gunakan mediator untuk notifikasi
            self._mediator.notify(self, "adopsi_diajukan")
        else:
            self.shelter.update(f"Permintaan adopsi untuk {self.hewan.nama} dari {self.user}")