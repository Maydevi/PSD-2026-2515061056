## **Binary Search**

Program ini berfungsi untuk mencari lokasi nomor kursi tertentu dalam daftar kursi yang sudah terurut dengan cepat. Setelah pengguna memasukkan nomor kursi yang dicari, program akan menelusuri data tersebut dan memberikan informasi letak kursi apakah berada di "Baris depan" (indeks 0–3) atau "Baris belakang" (indeks 4–7) letak kursi akan diberitahu berdasarkan indeks di mana target ditemukan.

Algoritma yang diterapkan adalah Binary Search (Pencarian Biner), yang sangat efisien untuk mencari elemen didalam array terurut. Algoritma ini bekerja dengan membagi ruang pencarian menjadi dua bagian secara berulang. Dengan membandingkan nilai target dengan elemen tengah, program dapat mengabaikan setengah dari sisa data di setiap langkahnya, sehingga proses pencarian menjadi jauh lebih cepat.

<img width="1292" height="878" alt="Cuplikan layar 2026-05-06 010117" src="https://github.com/user-attachments/assets/4a5277cc-36ae-4e7b-b84d-fe9ad636a5d4" />

Pada baris ke-1, "def binary_search(arr, n, target):" adalah fungsi yang menyimpan paramenter arr (array), n (panjang array/jumlah elemen), dan target(nilai yang ingin dicari).

Pada baris ke-2, "l = 0" l disini adalah left yaitu bagian kiri array, yaitu awal array.

Pada baris ke-3, "r = n - 1" r disini adalah right yaitu bagian kanan array yaitu akhir array. Pada program ini r di dapat dari mengurangi banyaknya elemen dengan 1.

Pada baris ke-4, "pos = -1" yaitu inisialisasi -1 dengan pos yan bearti "data belum ditemukan"

Pada baris ke-5, "while l <= r:" yaitu pengulangan yang terus berjalan jika l lebih kecil sama dengan r.

Pada baris ke-6, "m = l + (r - l) // 2" ini adalah cara menghitung nilai tengah atau median.

Pada baris ke-7, memiliki kondisi "if arr[m] == target:" yang artinya jika nilai di indeks m sama dengan angka yang dicari, kita simpan posisi m ke pos dan segera berhenti (break).

Pada baris ke-10, memiliki kondisi "elif arr[m] < target:" yang artinya jika nilai tengah lebih kecil dari target, berarti angka yang dicari ada di sebelah kanan. Maka, kita geser batas kiri menjadi l = m + 1. 

Pada baris ke-12, memiliki kondisi jika semua kondisi di atasnya tidak terpenuhi berarti angka yang dicari ada di sebelah kiri. atau bisa kita simpulkan bahwa nilai tengah lebih besar dari target, berarti angka ada di sebelah kiri. Maka, kita geser batas kanan menjadi r = m - 1.

Pada baris ke-17, "def main():" yaitu fungsi yang akan berinteraksi dengan pengguna

Pada baris ke-18, "data = [2, 5, 8, 12, 15, 18, 22, 25]" menyimpan data elemen dalam variabel "data"

Pada baris ke-19, "n = len(data)" untuk menghitung panjang data (jumlah elemen)

Pada baris ke-20 sampai baris ke-21, untuk menyimpan teks (tipe data string) ke dalam sebuah wadah bernama variabel (baris_depan dan baris_belakang).

Pada baris ke-22, menaampilkan data kursi, yang ada di array.

Pada baris ke-23, while true adalah pengulangan yang terus terjadi ketika nilai inputannya benar. User akan diminta untuk menginputkan nomor kursi yang ingin dicari sebagai target, apabila yang di masukan bukan angka maka menampilkan "Input tidak valid, silakan masukkan angka!"
try dan except ValueError: Ini adalah standar error handling agar program tidak crash jika pengguna memasukkan huruf atau simbol, bukan angka.

Pada baris ke-29, "pos = binary_search(data, n, target):" yaitu memanggil fungsi pencarian yang kita bahas di atas.

<img width="1276" height="334" alt="Cuplikan layar 2026-05-06 010133" src="https://github.com/user-attachments/assets/9336d5d0-1e83-4fac-8903-b738854d9714" />

Pada baris ke-30, "if pos != -1:" artinya jika ditemukan (indeks bukan -1) maka akan terjadi 2 kondisi yaitu kondisi pertama "if 0 <= pos <= 3:" yaitu mengecek apakah indeks berada di rentang 0-3 (Baris depan), apabila iya akan mencetak "Kursi {target}(nomor kursi yang di cari) ditemukan pada indeks ke-{pos} maka, posisi baris depan". Kondisi Kedua "if 4 <= pos <= 7:" yaitu mengecek apakah indeks berada di rentang 4-7 (Baris belakang),pabila iya akan mencetak "Kursi {target}(nomor kursi yang di cari) ditemukan pada indeks ke-{pos} maka, posisi baris belakang".

Pada baris ke-35, jika semua kondisi di atasnya tidak terpenuhi maka akan mencetak "Nomor kursi tidak ditemukan dalam daftar."

Pada baris ke-39 sampai baris ke-40, "if __name__ == "__main__": main():" Baris ini adalah entry point. Ini memerintahkan Python untuk menjalankan fungsi main() saat file dieksekusi secara langsung.

**OUTPUT**
<img width="815" height="121" alt="Cuplikan layar 2026-05-06 010724" src="https://github.com/user-attachments/assets/fb4843a8-d7ec-42a5-9243-96d43ff5ef0e" />
Pada output pencarian angka 2 dalam list [2, 5, 8, 12, 15, 18, 22, 25] menggunakan algoritma Binary Search dilakukan dengan membagi area pencarian menjadi dua secara berulang: 
Pada iterasi pertama, titik tengah (m) berada di indeks 3 (nilai 12), dan karena 12 > 2, area pencarian dipersempit ke sisi kiri dengan menggeser batas kanan (r) ke indeks 2 

Pada iterasi kedua, titik tengah berada di indeks 1 (nilai 5), dan karena 5 > 2, area pencarian dipersempit kembali ke sisi kiri dengan menggeser r ke indeks 0 

Akhirnya, pada iterasi ketiga, titik tengah berada tepat di indeks 0 (nilai 2), sehingga target ditemukan di indeks 0 dan program mencetak hasil bahwa kursi tersebut berada di "baris depan" karena indeks 0 memenuhi kondisi logika 0 <= pos <= 3.

Link youtube:
