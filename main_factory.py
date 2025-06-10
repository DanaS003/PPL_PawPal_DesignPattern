# main_factory.py
from model_hewan import HewanFactory, Vaksin #
from observer import Shelter # Diperlukan karena Hewan membutuhkan objek Shelter

def main_factory():
    print("--- Demonstrasi Factory Pattern (HewanFactory) ---")

    # Simulasi objek Shelter yang diperlukan oleh Hewan
    # Di sini kita hanya perlu instance sederhana, bukan fungsionalitas penuh Shelter
    class MockShelter:
        def __init__(self, nama):
            self.nama = nama
        def update(self, pesan):
            pass # Tidak perlu implementasi update untuk demo Factory

    shelter_mock_a = MockShelter("MockShelterA") #
    shelter_mock_b = MockShelter("MockShelterB") #

    # Data untuk hewan pertama
    data_hewan_1 = {
        "nama": "Buddy",
        "jenis": "Anjing, Beagle",
        "umur": "3 tahun",
        "shelter": shelter_mock_a,
        "riwayat_kesehatan": "Sehat, aktif",
        "daftar_vaksin": [
            {"nama_vaksin": "Rabies", "tanggal_pemberian": "2024-01-15", "tanggal_kadaluarsa": "2025-01-15"},
            {"nama_vaksin": "Parvo", "tanggal_pemberian": "2023-11-01"}
        ],
        "harga_adopsi": 300000,
        "steril": True
    }

    # Data untuk hewan kedua (tanpa vaksin dan tidak steril)
    data_hewan_2 = {
        "nama": "Whiskers",
        "jenis": "Kucing, Domestik",
        "umur": "1 tahun",
        "shelter": shelter_mock_b,
        "riwayat_kesehatan": "Pernah flu ringan",
        "daftar_vaksin": [],
        "harga_adopsi": 150000,
        "steril": False
    }
    
    # Data untuk hewan ketiga (dengan default steril=True)
    data_hewan_3 = {
        "nama": "Goldie",
        "jenis": "Ikan, Mas Koki",
        "umur": "6 bulan",
        "shelter": shelter_mock_a,
        "riwayat_kesehatan": "Sehat",
        "harga_adopsi": 50000,
        # 'steril' tidak disebutkan, harus default ke True
    }


    hewan1 = HewanFactory.buat_hewan(data_hewan_1) #
    hewan2 = HewanFactory.buat_hewan(data_hewan_2) #
    hewan3 = HewanFactory.buat_hewan(data_hewan_3) #

    print("\n--- Detail Hewan 1 ---")
    print(f"Nama: {hewan1.nama}") #
    print(f"Jenis: {hewan1.jenis}") #
    print(f"Umur: {hewan1.umur}") #
    print(f"Shelter: {hewan1.shelter.nama}") #
    print(f"Steril: {hewan1.steril}") #
    print(f"Riwayat Kesehatan: {hewan1.riwayat_kesehatan}") #
    print("Daftar Vaksin:")
    if hewan1.daftar_vaksin: #
        for vaksin in hewan1.daftar_vaksin:
            print(f"  - {vaksin}") #
    else:
        print("  Tidak ada vaksin.")
    print(f"Harga Adopsi: Rp{hewan1.harga_adopsi:,}") #
    print(f"Status Adopsi: {hewan1.status_adopsi}") #


    print("\n--- Detail Hewan 2 ---")
    print(f"Nama: {hewan2.nama}") #
    print(f"Jenis: {hewan2.jenis}") #
    print(f"Umur: {hewan2.umur}") #
    print(f"Shelter: {hewan2.shelter.nama}") #
    print(f"Steril: {hewan2.steril}") #
    print(f"Riwayat Kesehatan: {hewan2.riwayat_kesehatan}") #
    print("Daftar Vaksin:")
    if hewan2.daftar_vaksin: #
        for vaksin in hewan2.daftar_vaksin:
            print(f"  - {vaksin}") #
    else:
        print("  Tidak ada vaksin.")
    print(f"Harga Adopsi: Rp{hewan2.harga_adopsi:,}") #
    print(f"Status Adopsi: {hewan2.status_adopsi}") #

    print("\n--- Detail Hewan 3 ---")
    print(f"Nama: {hewan3.nama}") #
    print(f"Jenis: {hewan3.jenis}") #
    print(f"Umur: {hewan3.umur}") #
    print(f"Shelter: {hewan3.shelter.nama}") #
    print(f"Steril: {hewan3.steril}") # Seharusnya True karena default
    print(f"Riwayat Kesehatan: {hewan3.riwayat_kesehatan}") #
    print("Daftar Vaksin:")
    if hewan3.daftar_vaksin: #
        for vaksin in hewan3.daftar_vaksin:
            print(f"  - {vaksin}") #
    else:
        print("  Tidak ada vaksin.")
    print(f"Harga Adopsi: Rp{hewan3.harga_adopsi:,}") #
    print(f"Status Adopsi: {hewan3.status_adopsi}") #


if __name__ == "__main__":
    main_factory()