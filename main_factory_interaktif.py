# main_factory.py
from model_hewan import HewanFactory, Vaksin
from observer import Shelter # Diperlukan karena Hewan membutuhkan objek Shelter
from util import input_validasi # Import fungsi input_validasi

# List untuk menyimpan objek Hewan yang dibuat
list_hewan_demo = []

# Simulasi objek Shelter yang diperlukan oleh Hewan
# Di sini kita hanya perlu instance sederhana, bukan fungsionalitas penuh Shelter
class MockShelter:
    def __init__(self, nama):
        self.nama = nama
    def update(self, pesan):
        pass # Tidak perlu implementasi update untuk demo Factory

shelter_mock_a = MockShelter("MockShelterA")
shelter_mock_b = MockShelter("MockShelterB")

# Data awal untuk demonstrasi (hanya 1 hewan)
data_hewan_initial = {
    "nama": "Buddy",
    "jenis": "Anjing, Beagle",
    "umur": "3 tahun",
    "shelter": shelter_mock_a,
    "riwayat_kesehatan": "Sehat, aktif",
    "daftar_vaksin": [
        {"nama_vaksin": "Rabies", "tanggal_pemberian": "2024-01-15", "tanggal_kadaluarsa": "2025-01-15"}
    ],
    "harga_adopsi": 300000,
    "steril": True
}
list_hewan_demo.append(HewanFactory.buat_hewan(data_hewan_initial))

def tampilkan_detail_hewan(hewan):
    print(f"\n--- DETAIL HEWAN ---")
    print(f"Nama: {hewan.nama}")
    print(f"Jenis: {hewan.jenis}")
    print(f"Umur: {hewan.umur}")
    print(f"Shelter: {hewan.shelter.nama}")
    print(f"Steril: {'✅' if hewan.steril else '❌'}")
    print(f"Riwayat Kesehatan: {hewan.riwayat_kesehatan}")
    print("Detail Vaksin:")
    if hewan.daftar_vaksin:
        for vaksin in hewan.daftar_vaksin:
            print(f"  - {vaksin}")
    else:
        print("  Tidak ada informasi vaksin yang tersedia.")
    print(f"Harga Adopsi: Rp{hewan.harga_adopsi:,}")
    print(f"Status Adopsi: {hewan.status_adopsi}")

def tambahkan_hewan_interaktif():
    print("\n--- Tambah Hewan Baru (Menggunakan Factory) ---")
    nama = input("Nama hewan: ")
    jenis = input("Jenis hewan (misal: Kucing, Persia): ")
    umur = input("Umur hewan (misal: 1 tahun): ")
    
    # Pilih shelter (simulasi sederhana)
    print("Pilih Shelter untuk hewan ini:")
    print("[1] MockShelterA")
    print("[2] MockShelterB")
    shelter_choice = input_validasi("Pilih (1/2): ", ["1", "2"])
    shelter_obj = shelter_mock_a if shelter_choice == "1" else shelter_mock_b

    riwayat_kesehatan = input("Riwayat Kesehatan: ")
    
    daftar_vaksin_input = []
    while True:
        tambah_vaksin = input_validasi("Tambahkan vaksin? (ya/tidak): ", ["ya", "tidak"])
        if tambah_vaksin == "ya":
            nama_vaksin = input("Nama Vaksin: ")
            tanggal_pemberian = input("Tanggal Pemberian (YYYY-MM-DD): ")
            tanggal_kadaluarsa = input("Tanggal Kadaluarsa (YYYY-MM-DD, kosongkan jika tidak ada): ")
            vaksin_data = {"nama_vaksin": nama_vaksin, "tanggal_pemberian": tanggal_pemberian}
            if tanggal_kadaluarsa:
                vaksin_data["tanggal_kadaluarsa"] = tanggal_kadaluarsa
            daftar_vaksin_input.append(vaksin_data)
        else:
            break
            
    harga_adopsi_str = input("Harga Adopsi (angka, misal: 250000): ")
    try:
        harga_adopsi = int(harga_adopsi_str)
    except ValueError:
        print("[!] Harga tidak valid. Menggunakan default 0.")
        harga_adopsi = 0
    
    steril_input = input_validasi("Sudah steril? (ya/tidak): ", ["ya", "tidak"])
    steril = True if steril_input == "ya" else False

    data_hewan_baru = {
        "nama": nama,
        "jenis": jenis,
        "umur": umur,
        "shelter": shelter_obj,
        "riwayat_kesehatan": riwayat_kesehatan,
        "daftar_vaksin": daftar_vaksin_input,
        "harga_adopsi": harga_adopsi,
        "steril": steril
    }

    hewan_baru = HewanFactory.buat_hewan(data_hewan_baru)
    list_hewan_demo.append(hewan_baru)
    print(f"✅ Hewan '{hewan_baru.nama}' berhasil ditambahkan ke daftar demo!")

def lihat_list_hewan():
    print("\n--- DAFTAR HEWAN SAAT INI ---")
    if not list_hewan_demo:
        print("Tidak ada hewan dalam daftar.")
        return False
    
    for i, h in enumerate(list_hewan_demo):
        print(f"[{i+1}] {h.nama} - {h.jenis} - Umur: {h.umur} - Shelter: {h.shelter.nama}")
    return True

def main_factory():
    print("--- Demonstrasi Factory Pattern (HewanFactory) ---")

    while True:
        print("\nMenu Factory Demo:")
        print("1. Lihat Daftar Hewan")
        print("2. Tambah Hewan Baru")
        print("3. Keluar")
        
        choice = input_validasi("Pilih opsi: ", ["1", "2", "3"])

        if choice == "1":
            if lihat_list_hewan():
                detail_choice = input_validasi("Ingin lihat detail hewan? (ya/tidak): ", ["ya", "tidak"])
                if detail_choice == "ya":
                    try:
                        idx = int(input(f"Pilih nomor hewan untuk detail (1-{len(list_hewan_demo)}): ")) - 1
                        if 0 <= idx < len(list_hewan_demo):
                            tampilkan_detail_hewan(list_hewan_demo[idx])
                        else:
                            print("[!] Pilihan tidak valid.")
                    except ValueError:
                        print("[!] Input tidak valid. Masukkan angka.")
        elif choice == "2":
            tambahkan_hewan_interaktif()
        elif choice == "3":
            print("\nTerima kasih telah menggunakan demo Factory Pattern!")
            break

if __name__ == "__main__":
    main_factory()