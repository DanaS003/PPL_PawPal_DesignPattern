# model_hewan.py
class Vaksin: # Kelas baru
    def __init__(self, nama_vaksin, tanggal_pemberian, tanggal_kadaluarsa=None):
        self.nama_vaksin = nama_vaksin
        self.tanggal_pemberian = tanggal_pemberian
        self.tanggal_kadaluarsa = tanggal_kadaluarsa

    def __str__(self):
        exp_date = f" (Kadaluarsa: {self.tanggal_kadaluarsa})" if self.tanggal_kadaluarsa else ""
        return f"{self.nama_vaksin} ({self.tanggal_pemberian}{exp_date})"

class Hewan:
    # Tambahkan harga_adopsi di __init__
    def __init__(self, nama, jenis, umur, shelter, riwayat_kesehatan="Sehat", daftar_vaksin=None, harga_adopsi=0): 
        self.nama = nama
        self.jenis = jenis
        self.umur = umur
        self.shelter = shelter
        self.steril = True
        self.riwayat_kesehatan = riwayat_kesehatan
        self.daftar_vaksin = daftar_vaksin if daftar_vaksin is not None else []
        self.harga_adopsi = harga_adopsi # Atribut harga adopsi

class HewanFactory:
    @staticmethod
    def buat_hewan(data):
        daftar_vaksin_obj = []
        if "daftar_vaksin" in data and data["daftar_vaksin"]:
            for vaksin_data in data["daftar_vaksin"]:
                daftar_vaksin_obj.append(Vaksin(**vaksin_data))
        data["daftar_vaksin"] = daftar_vaksin_obj
        
        # Pastikan harga_adopsi diteruskan ke konstruktor Hewan
        return Hewan(**data)