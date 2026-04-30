# Bubble Sort

Program ini berfungsi untuk mengurutkan daftar nilai praktikan yang diinputkan oleh pengguna dari nilai terbesar ke nilai terkecil (pengurutan menurun atau descending). Setelah pengguna memasukkan jumlah dan daftar nilai, program akan memproses data tersebut menggunakan teknik pertukaran elemen hingga seluruh urutan nilai menjadi teratur sesuai kriteria tersebut.

Algoritma yang diterapkan adalah Bubble Sort. Algoritma ini bekerja dengan cara membandingkan dua elemen yang bersebelahan dalam sebuah larik (array) secara berulang dan menukarnya jika urutannya tidak sesuai dengan tujuan pengurutan. Dalam kode ini, pengecekan `if arr[j + 1] > arr[j]` memastikan bahwa elemen yang lebih besar akan "terapung" ke posisi yang lebih awal (indeks lebih kecil) di setiap iterasi, yang merupakan karakteristik khas dari algoritma Bubble Sort.

<img width="741" height="629" alt="Cuplikan layar 2026-04-30 200736" src="https://github.com/user-attachments/assets/07ef2830-1403-4998-9110-e9130acd7fd3" />

Pada baris 1, mendefinisikan fungsi bernama tukar yang menerima 3 masukan: array arr, posisi i, posisi j.

Pada baris 2, simpan nilai di posisi i ke variabel sementara temp.

Pada baris 3, ganti nilai di posisi i dengan nilai di posisi j.

Pada baris 4, ganti nilai di posisi j dengan nilai yang tadi disimpan di temp. Hasilnya: nilai di i dan j bertukar tempat.
Pada baris 7, fungsi untuk mengurutkan array arr sepanjang n elemen.
Pada baris 8, ulangi sebanyak n-1 kali (setiap putaran akan menempatkan satu angka terbesar di akhir).
Pada baris 9, Ulangi untuk membandingkan pasangan angka yang belum terurut. Setiap kali i bertambah, jangkauan perbandingan berkurang karena angka terbesar sudah di akhir.
Pada baris 10, Jika angka di kanan (posisi j+1) lebih besar dari angka di kiri (posisi j), maka
Pada baris 11, tukar posisi kedua angka tersebut. Artinya: kita urutkan dari besar ke kecil (descending).



