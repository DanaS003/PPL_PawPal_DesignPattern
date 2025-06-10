# main_factory.py
from model_hewan import HewanFactory, Vaksin
from observer import Shelter # Import Shelter untuk objek hewan

def main_factory():
    print("--- Demonstrasi Factory Pattern (Pembuatan Hewan) ---")

    # Membuat objek Shelter untuk digunakan oleh HewanFactory
    shelter_dummy = Shelter("Shelter Factory Demo")

    # Menggunakan HewanFactory untuk membuat objek Hewan
    print("\nMembuat Anjing 'Buddy'...")
    buddy_data = {
        "nama": "Buddy",
        "jenis": "Anjing, Beagle",
        "umur": "3 tahun",
        "shelter": shelter_dummy,
        "riwayat_kesehatan": "Sehat",
        "daftar_vaksin": [
            {"nama_vaksin": "Rabies", "tanggal_pemberian": "2024-01-15"}
        ],
        "harga_adopsi": 300000,
        "steril": True
    }
    buddy = HewanFactory.buat_hewan(buddy_data)
    print(f"Berhasil membuat: {buddy}")
    print(f"Vaksin Buddy: {[str(v) for v in buddy.daftar_vaksin]}")

    print("\nMembuat Kucing 'Whiskers'...")
    whiskers_data = {
        "nama": "Whiskers",
        "jenis": "Kucing, Domestic Shorthair",
        "umur": "1 tahun",
        "shelter": shelter_dummy,
        "riwayat_kesehatan": "Pernah flu ringan",
        "daftar_vaksin": [
            {"nama_vaksin": "Feline Rhinotracheitis", "tanggal_pemberian": "2024-02-20", "tanggal_kadaluarsa": "2025-02-20"}
        ],
        "harga_adopsi": 150000,
        "steril": False
    }
    whiskers = HewanFactory.buat_hewan(whiskers_data)
    print(f"Berhasil membuat: {whiskers}")
    print(f"Vaksin Whiskers: {[str(v) for v in whiskers.daftar_vaksin]}")

    print("\nMembuat Burung 'Chirpy' (tanpa vaksin dan harga adopsi default)...")
    chirpy_data = {
        "nama": "Chirpy",
        "jenis": "Burung, Kenari",
        "umur": "6 bulan",
        "shelter": shelter_dummy,
        "riwayat_kesehatan": "Sehat dan aktif",
        "steril": False
    }
    chirpy = HewanFactory.buat_hewan(chirpy_data)
    print(f"Berhasil membuat: {chirpy}")
    print(f"Vaksin Chirpy: {chirpy.daftar_vaksin}")
    print(f"Harga Adopsi Chirpy: Rp{chirpy.harga_adopsi:,}")

if __name__ == "__main__":
    main_factory()