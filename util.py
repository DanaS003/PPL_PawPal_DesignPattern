def input_validasi(prompt, opsi):
    while True:
        inp = input(prompt)
        if inp in opsi:
            return inp
        print("[!] Pilihan tidak valid. Coba lagi.")