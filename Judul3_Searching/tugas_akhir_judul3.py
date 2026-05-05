def binary_search(arr, n, target):
    l = 0
    r = n - 1
    pos = -1
    while l <= r:
        m = l + (r - l) // 2
        if arr[m] == target:
            pos = m
            break
        elif arr[m] < target:
            l = m + 1
        else:
            r = m - 1
    return pos


def main():
    data = [2, 5, 8, 12, 15, 18, 22, 25]
    n = len(data)
    baris_depan = "Baris depan"
    baris_belakang = "Baris belakang"
    print(f"Array: {data}")
    while True:
        try:
            target = int(input("Masukkan nomor kursi yang ingin dicari: "))
            break
        except ValueError:
            print("Input tidak valid, silakan masukkan angka!")
    pos = binary_search(data, n, target)
    if pos != -1:
        if 0 <= pos <= 3:
            print(f"Kursi {target} ditemukan pada indeks ke-{pos} maka, posisi baris depan")
        if 4 <= pos <= 7:
            print(f"Kursi {target} ditemukan pada indeks ke-{pos} maka, posisi baris belakang")
    else:
        print("Nomor kursi tidak ditemukan dalam daftar.")


if __name__ == "__main__":
    main()
