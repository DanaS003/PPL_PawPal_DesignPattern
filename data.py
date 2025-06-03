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
        "daftar_vaksin": [ # Tambahkan ini
            {"nama_vaksin": "Rabies", "tanggal_pemberian": "2024-03-10", "tanggal_kadaluarsa": "2025-03-10"},
            {"nama_vaksin": "Distemper", "tanggal_pemberian": "2024-04-01"}
        ]
    }),
    HewanFactory.buat_hewan({
        "nama": "Luna",
        "jenis": "Kucing, Persia",
        "umur": "1 tahun",
        "shelter": shelter_cat,
        "riwayat_kesehatan": "Sehat, pernah pilek ringan di bulan lalu",
        "daftar_vaksin": [ # Tambahkan ini
            {"nama_vaksin": "Feline Panleukopenia", "tanggal_pemberian": "2024-05-15"},
            {"nama_vaksin": "Calicivirus", "tanggal_pemberian": "2024-05-15"}
        ]
    })
]