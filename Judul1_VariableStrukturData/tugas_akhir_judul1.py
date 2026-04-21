def menu():
    print("1. Tampilkan address array")
    print("2. Tampilkan address dari semua index array")
    print("3. Masukkan nilai kedalam semua index array")
    print("4. Cek isi index array")
    print("5. Keluar")


def main():
    a = [0] * 5
    running = True
    while running:
        menu()
        try:
            choice = int(input("Pilihan: "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue
        if choice == 1:
            print(f"Address array: {id(a)}")
        elif choice == 2:
            for i in range(5):
                print(f"Address a[{i}]: {id(a[i])}")
        elif choice == 3:
            print("Masukkan 5 nilai:")
            for i in range(5):
                while True:
                    try:
                        a[i] = int(input(f"a[{i}] = "))
                        break
                    except ValueError:
                        print("Input tidak valid, silakan masukkan angka!")
            print(f"Array sekarang: {a}")
        elif choice == 4:
            try:
                index = int(input("Masukkan index yang ingin dicek (0-4): "))
                if index == 0:
                    print(f"Nilai a[0] = {a[0]}")
                elif index == 1:
                    print(f"Nilai a[1] = {a[1]}")
                elif index == 2:
                    print(f"Nilai a[2] = {a[2]}")
                elif index == 3:
                    print(f"Nilai a[3] = {a[3]}")
                elif index == 4:
                    print(f"Nilai a[4] = {a[4]}")
                else:
                    print("Index tidak valid! Masukkan angka antara 0 dan 4.")
            except ValueError:
                print("Input tidak valid! Masukkan angka yang benar.")
        elif choice == 5:
            running = False
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
