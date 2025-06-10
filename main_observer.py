# main_observer.py
from observer import Subject, Shelter, Adopter #

def main_observer():
    print("--- Demonstrasi Observer Pattern ---")

    # 1. Buat Subject
    komunikasi_sistem = Subject() #

    # 2. Buat Observers
    shelter_a = Shelter("Pawsome Home") #
    adopter_x = Adopter("Alice") #
    adopter_y = Adopter("Bob") #

    # 3. Attach Observers ke Subject
    komunikasi_sistem.attach(shelter_a) #
    komunikasi_sistem.attach(adopter_x) #
    komunikasi_sistem.attach(adopter_y) #

    print("\n--- Notifikasi Awal ---")
    komunikasi_sistem.notify_observers("Sistem akan melakukan maintenance dalam 1 jam!") #

    print(f"\nNotifikasi yang diterima Shelter {shelter_a.nama}:") #
    for notif in shelter_a.notifikasi_masuk: #
        print(f"- {notif}")

    print(f"\nNotifikasi yang diterima Adopter {adopter_x.nama}:") #
    for notif in adopter_x.notifikasi_masuk: #
        print(f"- {notif}")

    print(f"\nNotifikasi yang diterima Adopter {adopter_y.nama}:") #
    for notif in adopter_y.notifikasi_masuk: #
        print(f"- {notif}")

    # 4. Detach salah satu observer
    print("\n--- Detach Adopter Bob ---")
    komunikasi_sistem.detach(adopter_y) #

    # 5. Kirim notifikasi lagi
    print("\n--- Notifikasi Kedua ---")
    komunikasi_sistem.notify_observers("Maintenance telah selesai. Sistem kembali normal.") #

    print(f"\nNotifikasi yang diterima Shelter {shelter_a.nama}:") #
    for notif in shelter_a.notifikasi_masuk: #
        print(f"- {notif}")

    print(f"\nNotifikasi yang diterima Adopter {adopter_x.nama}:") #
    for notif in adopter_x.notifikasi_masuk: #
        print(f"- {notif}")

    print(f"\nNotifikasi yang diterima Adopter {adopter_y.nama}:") #
    for notif in adopter_y.notifikasi_masuk: #
        print(f"- {notif}") # Seharusnya tidak ada notifikasi baru untuk Bob

if __name__ == "__main__":
    main_observer()