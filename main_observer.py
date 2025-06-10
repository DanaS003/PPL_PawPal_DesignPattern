# main_observer.py
from data import adopter_john, shelter_happy, list_hewan
from form_adopsi import PengajuanAdopsi
from observer import Adopter, Shelter

def main_observer():
    print("--- Demonstrasi Observer Pattern (Notifikasi Pengajuan Adopsi) ---")

    # Pastikan ada hewan yang tersedia untuk adopsi
    if not list_hewan:
        print("Tidak ada hewan dalam daftar untuk demonstrasi.")
        return

    hewan_demo = list_hewan[0] # Ambil hewan pertama dari data
    print(f"Menggunakan hewan: {hewan_demo.nama} dari shelter {hewan_demo.shelter.nama}")

    # Buat pengajuan adopsi baru
    print(f"\nAdopter {adopter_john.nama} mengajukan adopsi untuk {hewan_demo.nama}.")
    pengajuan = PengajuanAdopsi(hewan_demo, adopter_john, hewan_demo.shelter)
    
    # Pengajuan adopsi akan secara otomatis memberi tahu shelter dan adopter
    pengajuan.ajukan()

    print("\n--- Simulasi Perubahan Status ---")
    
    # Shelter mengkonfirmasi jadwal kunjungan
    print("\nShelter mengatur jadwal kunjungan...")
    pengajuan.set_jadwal_kunjungan("2025-06-20")

    # Shelter mengkonfirmasi hasil kunjungan
    print("\nShelter mengkonfirmasi hasil kunjungan...")
    pengajuan.set_hasil_kunjungan("layak")

    # Adopter melanjutkan pembayaran (ini akan memicu notifikasi)
    # Untuk demo observer, kita tidak perlu detail pembayaran, hanya statusnya
    print("\nAdopter melakukan pembayaran...")
    
    pengajuan.set_status("payment_successful")

    # Adopter memberikan rating dan review setelah adopsi selesai
    print("\nAdopter memberikan rating dan review...")
    pengajuan.beri_rating_review(5, "Anjingnya sehat dan lucu, shelter sangat membantu!")
    
    print("\n--- Notifikasi yang Diterima ---")
    print(f"Notifikasi untuk Adopter {adopter_john.nama}:")
    for notif in adopter_john.notifikasi_masuk:
        print(f"- {notif}")

    print(f"\nNotifikasi untuk Shelter {shelter_happy.nama}:")
    for notif in shelter_happy.notifikasi_masuk:
        print(f"- {notif}")

if __name__ == "__main__":
    main_observer()