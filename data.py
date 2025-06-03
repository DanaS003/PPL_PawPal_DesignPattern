from observer import Shelter
from model_hewan import HewanFactory, Vaksin # Import Vaksin

users = {
    "user@example.com": "1234"
}

shelter_happy = Shelter("HappyPaws")
shelter_cat = Shelter("CatLover")

list_hewan = [
    HewanFactory.buat_hewan({
        "nama": "Miko",
        "jenis": "Anjing, Golden Retriever",
        "umur": "2 tahun",
        "shelter": shelter_happy,
        "riwayat_kesehatan": "Sehat, tidak ada alergi diketahui",
        "daftar_vaksin": [
            {"nama_vaksin": "Rabies", "tanggal_pemberian": "2024-03-10", "tanggal_kadaluarsa": "2025-03-10"},
            {"nama_vaksin": "Distemper", "tanggal_pemberian": "2024-04-01"}
        ],
        "harga_adopsi": 250000 # Harga adopsi Miko
    }),
    HewanFactory.buat_hewan({
        "nama": "Luna",
        "jenis": "Kucing, Persia",
        "umur": "1 tahun",
        "shelter": shelter_cat,
        "riwayat_kesehatan": "Sehat, pernah pilek ringan di bulan lalu",
        "daftar_vaksin": [
            {"nama_vaksin": "Feline Panleukopenia", "tanggal_pemberian": "2024-05-15"},
            {"nama_vaksin": "Calicivirus", "tanggal_pemberian": "2024-05-15"}
        ],
        "harga_adopsi": 180000 # Harga adopsi Luna
    }),
    HewanFactory.buat_hewan({
        "nama": "Bobo",
        "jenis": "Kura-kura, Darat",
        "umur": "5 tahun",
        "shelter": shelter_happy,
        "riwayat_kesehatan": "Sehat, aktif",
        "daftar_vaksin": [],
        "harga_adopsi": 100000 # Harga adopsi Bobo
    })
]