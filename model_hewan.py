class Vaksin: # Kelas baru
    def __init__(self, nama_vaksin, tanggal_pemberian, tanggal_kadaluarsa=None):
        self.nama_vaksin = nama_vaksin
        self.tanggal_pemberian = tanggal_pemberian
        self.tanggal_kadaluarsa = tanggal_kadaluarsa

    def __str__(self):
        exp_date = f" (Kadaluarsa: {self.tanggal_kadaluarsa})" if self.tanggal_kadaluarsa else ""
        return f"{self.nama_vaksin} ({self.tanggal_pemberian}{exp_date})"

class Hewan:
    def __init__(self, nama, jenis, umur, shelter, riwayat_kesehatan="Sehat", daftar_vaksin=None): # Perubahan di sini
        self.nama = nama
        self.jenis = jenis
        self.umur = umur
        self.shelter = shelter
        self.steril = True
        self.riwayat_kesehatan = riwayat_kesehatan
        self.daftar_vaksin = daftar_vaksin if daftar_vaksin is not None else [] # Perubahan di sini

class HewanFactory:
    @staticmethod
    def buat_hewan(data):
        # Mengelola daftar_vaksin secara terpisah jika ada
        daftar_vaksin_obj = []
        if "daftar_vaksin" in data and data["daftar_vaksin"]:
            for vaksin_data in data["daftar_vaksin"]:
                daftar_vaksin_obj.append(Vaksin(**vaksin_data))
        data["daftar_vaksin"] = daftar_vaksin_obj
        return Hewan(**data)