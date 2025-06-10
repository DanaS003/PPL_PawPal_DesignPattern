# model_hewan.py
class Vaksin:
    def __init__(self, nama_vaksin, tanggal_pemberian, tanggal_kadaluarsa=None):
        self.nama_vaksin = nama_vaksin
        self.tanggal_pemberian = tanggal_pemberian
        self.tanggal_kadaluarsa = tanggal_kadaluarsa

    def __str__(self):
        exp_date = f" (Kadaluarsa: {self.tanggal_kadaluarsa})" if self.tanggal_kadaluarsa else ""
        return f"{self.nama_vaksin} ({self.tanggal_pemberian}{exp_date})"

class Hewan:
    def __init__(self, nama, jenis, umur, shelter, riwayat_kesehatan="Sehat", daftar_vaksin=None, harga_adopsi=0, steril=True):
        self.nama = nama
        self.jenis = jenis
        self.umur = umur
        self.shelter = shelter
        self.steril = steril
        self.riwayat_kesehatan = riwayat_kesehatan
        self.daftar_vaksin = daftar_vaksin if daftar_vaksin is not None else []
        self.harga_adopsi = harga_adopsi
        self.status_adopsi = "available" # Default status

    def __str__(self):
        return f"Hewan(Nama: {self.nama}, Jenis: {self.jenis}, Shelter: {self.shelter.nama}, Status: {self.status_adopsi})"

class HewanFactory:
    @staticmethod
    def buat_hewan(data):
        daftar_vaksin_obj = []
        if "daftar_vaksin" in data and data["daftar_vaksin"]:
            # PERBAIKAN UTAMA: Mengganti "vaksin_data" menjadi "daftar_vaksin"
            for vaksin_data_item in data["daftar_vaksin"]: 
                daftar_vaksin_obj.append(Vaksin(**vaksin_data_item))
        data["daftar_vaksin"] = daftar_vaksin_obj
        
        if "steril" not in data:
            data["steril"] = True
        
        return Hewan(**data)