# main_observer.py
from observer import Subject, Shelter, Adopter
from util import input_validasi

def main_observer():
    print("--- Demonstrasi Interaktif Observer Pattern ---")

    komunikasi_sistem = Subject()
    all_observers = {}

    print("\n[SETUP AWAL] Menambahkan beberapa Observer default:")
    shelter_a = Shelter("Pawsome Home")
    adopter_x = Adopter("Alice")
    adopter_y = Adopter("Bob")

    komunikasi_sistem.attach(shelter_a)
    komunikasi_sistem.attach(adopter_x)
    komunikasi_sistem.attach(adopter_y)

    all_observers[shelter_a.nama] = shelter_a
    all_observers[adopter_x.nama] = adopter_x
    all_observers[adopter_y.nama] = adopter_y

    print(f"Observer yang terdaftar: {', '.join(all_observers.keys())}")

    while True:
        print("\n--- Menu Observer Demo ---")
        print("1. Tambah Observer Baru")
        print("2. Hapus Observer (Detach)")
        print("3. Kirim Notifikasi ke SEMUA Observer")
        print("4. Kirim Notifikasi ke Observer TERTENTU") # Opsi baru
        print("5. Lihat Notifikasi Observer Tertentu")
        print("6. Lihat Semua Observer Terdaftar")
        print("7. Keluar") # Pilihan keluar berubah

        pilihan = input_validasi("Pilih opsi: ", ["1", "2", "3", "4", "5", "6", "7"])

        if pilihan == "1":
            print("\n--- Tambah Observer Baru ---")
            observer_tipe = input_validasi("Tipe Observer? [1] Shelter, [2] Adopter: ", ["1", "2"])
            nama_observer = input("Masukkan nama Observer baru: ")

            if nama_observer in all_observers:
                print(f"[!] Observer dengan nama '{nama_observer}' sudah ada.")
                continue

            if observer_tipe == "1":
                new_observer = Shelter(nama_observer)
            else:
                new_observer = Adopter(nama_observer)

            komunikasi_sistem.attach(new_observer)
            all_observers[nama_observer] = new_observer
            print(f"✅ Observer '{nama_observer}' ({new_observer.__class__.__name__}) berhasil ditambahkan dan di-attach.")

        elif pilihan == "2":
            print("\n--- Hapus Observer ---")
            if not all_observers:
                print("[!] Tidak ada Observer terdaftar untuk dihapus.")
                continue

            print("Observer yang tersedia:")
            for i, nama in enumerate(all_observers.keys()):
                print(f"[{i+1}] {nama}")

            hapus_pilihan_str = input_validasi("Pilih nomor Observer yang akan dihapus (atau 'batal'): ", 
                                                [str(i+1) for i in range(len(all_observers))] + ["batal"])

            if hapus_pilihan_str == "batal":
                continue

            hapus_index = int(hapus_pilihan_str) - 1
            nama_to_detach = list(all_observers.keys())[hapus_index]
            observer_to_detach = all_observers[nama_to_detach]

            komunikasi_sistem.detach(observer_to_detach)
            del all_observers[nama_to_detach]
            print(f"✅ Observer '{nama_to_detach}' berhasil dihapus (detach).")

        elif pilihan == "3": # Kirim ke semua
            pesan = input("Masukkan pesan yang akan dikirim ke SEMUA Observer: ")
            print("\n--- Mengirim Notifikasi ke Semua Observer ---")
            komunikasi_sistem.notify_observers(pesan) # Tidak ada target_observer_name
            print("✅ Notifikasi berhasil dikirim ke semua Observer yang ter-attach.")

        elif pilihan == "4": # Kirim ke tertentu
            print("\n--- Kirim Notifikasi ke Observer TERTENTU ---")
            if not all_observers:
                print("[!] Tidak ada Observer terdaftar.")
                continue

            print("Pilih Observer penerima:")
            for i, nama in enumerate(all_observers.keys()):
                print(f"[{i+1}] {nama}")

            target_choice_str = input_validasi("Pilih nomor Observer target: ", 
                                                [str(i+1) for i in range(len(all_observers))])
            target_index = int(target_choice_str) - 1
            target_observer_name = list(all_observers.keys())[target_index]

            pesan_spesifik = input(f"Masukkan pesan untuk '{target_observer_name}': ")
            print(f"\n--- Mengirim Notifikasi ke {target_observer_name} ---")
            komunikasi_sistem.notify_observers(pesan_spesifik, target_observer_name=target_observer_name)
            print(f"✅ Notifikasi berhasil dikirim. Hanya '{target_observer_name}' yang seharusnya menerima.")

        elif pilihan == "5": # Lihat Notifikasi Observer Tertentu
            print("\n--- Lihat Notifikasi Observer Tertentu ---")
            if not all_observers:
                print("[!] Tidak ada Observer terdaftar.")
                continue

            print("Observer yang tersedia:")
            for i, nama in enumerate(all_observers.keys()):
                print(f"[{i+1}] {nama}")

            lihat_pilihan_str = input_validasi("Pilih nomor Observer untuk melihat notifikasi: ", 
                                                [str(i+1) for i in range(len(all_observers))])

            lihat_index = int(lihat_pilihan_str) - 1
            nama_observer_selected = list(all_observers.keys())[lihat_index]
            observer_selected = all_observers[nama_observer_selected]

            print(f"\nNotifikasi yang diterima {observer_selected.__class__.__name__} {observer_selected.nama}:")
            if observer_selected.notifikasi_masuk:
                for notif in observer_selected.notifikasi_masuk:
                    print(f"- {notif}")
            else:
                print("Tidak ada notifikasi.")

        elif pilihan == "6": # Lihat Semua Observer Terdaftar
            print("\n--- Semua Observer Terdaftar ---")
            if not all_observers:
                print("Tidak ada observer yang terdaftar saat ini.")
            else:
                for nama, obs_obj in all_observers.items():
                    is_attached = obs_obj in komunikasi_sistem._observers
                    print(f"- {nama} ({obs_obj.__class__.__name__}) - Ter-attach: {'Ya' if is_attached else 'Tidak'} ")

        elif pilihan == "7":
            print("\n=== Terima kasih telah menggunakan demo Observer Pattern! ===")
            break

if __name__ == "__main__":
    main_observer()