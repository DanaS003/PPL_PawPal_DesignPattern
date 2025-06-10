# data.py
from observer import Shelter, Adopter # Pastikan ini diimport
from model_hewan import HewanFactory, Vaksin # Import Vaksin

# Data pengguna terdaftar (simulasi database)
users_db = {
    "adopter@example.com": {"password": "123", "role": "adopter"},
    "shelter@example.com": {"password": "123", "role": "shelter"},
}

# Objek Adopter dan Shelter (simulasi instance observer)
adopter_john = Adopter("John Doe")
shelter_happy = Shelter("HappyPaws")
shelter_cat = Shelter("CatLover")

# Mapping email ke objek Observer
registered_users = {
    "adopter@example.com": adopter_john,
    "shelter@example.com": shelter_happy # Asumsi shelter login ini adalah happy paws
}

# Daftar hewan (simulasi data dari database)
list_hewan = [
    HewanFactory.buat_hewan({
        "nama": "Miko",
        "jenis": "Anjing, Golden Retriever",
        "umur": "2 tahun",
        "shelter": shelter_happy, # Menggunakan objek shelter_happy
        "riwayat_kesehatan": "Sehat, tidak ada alergi diketahui",
        "daftar_vaksin": [ # Pastikan key ini sesuai dengan yang dipakai di HewanFactory
            {"nama_vaksin": "Rabies", "tanggal_pemberian": "2024-03-10", "tanggal_kadaluarsa": "2025-03-10"},
            {"nama_vaksin": "Distemper", "tanggal_pemberian": "2024-04-01"}
        ],
        "harga_adopsi": 250000,
        "steril": True
    }),
    HewanFactory.buat_hewan({
        "nama": "Luna",
        "jenis": "Kucing, Persia",
        "umur": "1 tahun",
        "shelter": shelter_cat, # Menggunakan objek shelter_cat
        "riwayat_kesehatan": "Sehat, pernah pilek ringan di bulan lalu",
        "daftar_vaksin": [ # Pastikan key ini sesuai dengan yang dipakai di HewanFactory
            {"nama_vaksin": "Feline Panleukopenia", "tanggal_pemberian": "2024-05-15"},
            {"nama_vaksin": "Calicivirus", "tanggal_pemberian": "2024-05-15"}
        ],
        "harga_adopsi": 180000,
        "steril": True
    }),
    HewanFactory.buat_hewan({
        "nama": "Bobo",
        "jenis": "Kura-kura, Darat",
        "umur": "5 tahun",
        "shelter": shelter_happy, # Menggunakan objek shelter_happy
        "riwayat_kesehatan": "Sehat, aktif",
        "daftar_vaksin": [], # Pastikan key ini sesuai dengan yang dipakai di HewanFactory
        "harga_adopsi": 100000,
        "steril": False
    })
]

# Daftar pengajuan adopsi yang sedang berjalan (simulasi database)
list_pengajuan_adopsi = []