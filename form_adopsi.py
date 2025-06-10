# form_adopsi.py
import uuid
import datetime # Import modul datetime

class PengajuanAdopsi: # Menggunakan nama kelas PengajuanAdopsi yang benar
    def __init__(self, hewan, adopter, shelter):
        self.id = str(uuid.uuid4()) # ID unik pengajuan
        self.hewan = hewan
        self.adopter = adopter # Menggunakan adopter objek
        self.shelter = shelter
        self.metode_pembayaran = None
        self.status = "pending" # Status awal pengajuan
        self.invoice_id = None
        self.tanggal_pengajuan = None
        self.tanggal_pembayaran = None
        self.rating_review = None
        self.jadwal_kunjungan = None
        self.hasil_kunjungan = None

    def ajukan(self):
        self.tanggal_pengajuan = str(datetime.datetime.now()) # Menggunakan datetime.datetime.now()
        print(f"📄 Permintaan adopsi {self.id} diajukan untuk {self.hewan.nama} oleh {self.adopter.nama}.")
        self.status = "under_review"
        print(f"Status Pengajuan: {self.status}")
        self.shelter.update(f"Permintaan adopsi baru dari {self.adopter.nama} untuk {self.hewan.nama}. Status: {self.status}")

    def set_metode_pembayaran(self, metode):
        self.metode_pembayaran = metode

    def proses_pembayaran(self, jumlah):
        self.invoice_id = str(uuid.uuid4())
        print(f"Invoice ID Pembayaran: {self.invoice_id}")
        self.metode_pembayaran.bayar(jumlah)
        self.tanggal_pembayaran = str(datetime.datetime.now()) # Menggunakan datetime.datetime.now()
        self.status = "payment_successful"
        print(f"✅ Pembayaran berhasil untuk pengajuan {self.id}. Status: {self.status}")
        self.shelter.update(f"Pembayaran berhasil untuk adopsi {self.hewan.nama} oleh {self.adopter.nama}.")
        self.adopter.update(f"Pembayaran Anda untuk adopsi {self.hewan.nama} berhasil.")

    def set_jadwal_kunjungan(self, tanggal):
        self.jadwal_kunjungan = tanggal
        self.status = "home_visit_scheduled"
        print(f"✅ Jadwal kunjungan untuk pengajuan {self.id} diatur pada: {tanggal}. Status: {self.status}")
        self.shelter.update(f"Jadwal kunjungan untuk {self.adopter.nama} dan {self.hewan.nama} diatur: {tanggal}.")
        self.adopter.update(f"Jadwal kunjungan Anda untuk {self.hewan.nama} diatur: {tanggal}.")
    
    def set_hasil_kunjungan(self, hasil):
        self.hasil_kunjungan = hasil
        self.status = "home_visit_completed" if hasil == "layak" else "home_visit_failed"
        print(f"Hasil kunjungan untuk pengajuan {self.id}: {hasil}. Status: {self.status}")
        self.adopter.update(f"Hasil kunjungan rumah untuk adopsi {self.hewan.nama}: {hasil}.")

    def set_status(self, new_status):
        self.status = new_status
        print(f"Status pengajuan {self.id} diperbarui menjadi: {self.status}")
        self.adopter.update(f"Status pengajuan adopsi Anda untuk {self.hewan.nama} diperbarui menjadi: {self.status}.")
        self.shelter.update(f"Status pengajuan adopsi {self.adopter.nama} untuk {self.hewan.nama} diperbarui menjadi: {self.status}.")

    def beri_rating_review(self, rating, review_text):
        self.rating_review = {"rating": rating, "review": review_text, "tanggal": str(datetime.datetime.now())} # Menggunakan datetime.datetime.now()
        print(f"Terima kasih atas rating ({rating}/5) dan review Anda untuk {self.hewan.nama}: '{review_text}'!")
        self.shelter.update(f"Anda menerima rating {rating}/5 dan review baru untuk {self.hewan.nama} dari {self.adopter.nama}.")