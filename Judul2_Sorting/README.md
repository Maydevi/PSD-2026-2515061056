# Bubble Sort

Program ini berfungsi untuk mengurutkan daftar nilai praktikan yang diinputkan oleh pengguna dari nilai terbesar ke nilai terkecil (pengurutan menurun atau descending). Setelah pengguna memasukkan jumlah dan daftar nilai, program akan memproses data tersebut menggunakan teknik pertukaran elemen hingga seluruh urutan nilai menjadi teratur sesuai kriteria tersebut.

Algoritma yang diterapkan adalah Bubble Sort. Algoritma ini bekerja dengan cara membandingkan dua elemen yang bersebelahan dalam sebuah larik (array) secara berulang dan menukarnya jika urutannya tidak sesuai dengan tujuan pengurutan. Dalam kode ini, pengecekan `if arr[j + 1] > arr[j]` memastikan bahwa elemen yang lebih besar akan "terapung" ke posisi yang lebih awal (indeks lebih kecil) di setiap iterasi, yang merupakan karakteristik khas dari algoritma Bubble Sort.

<img width="741" height="629" alt="Cuplikan layar 2026-04-30 200736" src="https://github.com/user-attachments/assets/07ef2830-1403-4998-9110-e9130acd7fd3" />

Pada baris 1, "def tukar(arr, i, j):" mendefinisikan fungsi bernama tukar yang menerima 3 masukan: array arr, posisi i, posisi j.

Pada baris 2, " temp = arr[i]" ini untuk menyimpan nilai di posisi "i" ke variabel sementara "temp".

Pada baris 3, "arr[i] = arr[j]" berfungsi untuk ganti nilai di posisi "i" dengan nilai di posisi "j".

Pada baris 4, "arr[j] = temp" ganti nilai di posisi "j" dengan nilai yang tadi disimpan di "temp". Hasilnya: nilai di "i" dan "j" bertukar tempat.

Pada baris 7, "def bubble_sort(arr, n):" adalah fungsi untuk mengurutkan array "arr" sepanjang "n" elemen.

Pada baris 8, "for i in range(n - 1):" menggunakan for sebagai pengulangan untuk ulangi sebanyak n-1 kali (setiap putaran akan menempatkan satu angka terbesar di akhir).

Pada baris 9, "for j in range(n - i - 1):" adalah pengulangan yg berkerja untuk membandingkan pasangan angka yang belum terurut. Setiap kali i bertambah, jangkauan perbandingan berkurang karena angka terbesar sudah di akhir.

Pada baris 10, "if arr[j + 1] > arr[j]:" artinya jika angka di kanan (posisi j+1) lebih besar dari angka di kiri (posisi j), maka

Pada baris 11, "tukar(arr, j, j + 1)" lanjutan dari baris 10,maka tukar posisi kedua angka tersebut. yang di mana kita akan mengurutkan dari besar ke kecil (descending).

Pada baris 14, def main() adalah fungsi utama yang akan dijalankan pertama kali.

Pada baris 15-16, "try: n = int(input("Masukkan jumlah praktikan: "))" ini untuk meminta user memasukkan jumlah praktikan, lalu ubah ke angka bulat (integer).

Pada baris 17-19, kode ini akan menampilkan pesan eror lalu menghentikan fungsi apabila user memasukan inputan bukan angka.

Pada baris 20, " arr = []" untuk buat array kosong untuk menyimpan nilai praktikan.

Pada baris 21, "print("Masukkan nilai praktikan: ")" menampilkan perintah untuk user memasukkan nilai satu per satu.

<img width="885" height="540" alt="Cuplikan layar 2026-04-30 200804" src="https://github.com/user-attachments/assets/2b1035ec-88b1-4a95-9ef0-0bcb1c96fabb" />


Pada baris 22, "for i in range(n):" pengulangan sebanyak n kali (sesuai jumlah praktikan yang di input user).

Pada baris 23-25, Kode ini meminta user memasukkan angka. Jika nilai inputan yang dimasukkan benar (interger), maka akan lanjut programnya namun jika bukan angka, akan masuk ke except ValueError, maka program tidak akan berhenti, tetapi mengulang perulangan while sampai pengguna memasukkan angka yang benar.

Pada baris 26, "arr.append(nilai)" menambahkan nilai tersebut ke dalam array arr.

Pada baris 27, "break" berfungsi untuk keluar dari while True karena input sudah valid.

Pada baris 28-29, jika input bukan angka, maka akan menampilkan peringatan dan mengulang while sampai benar.

Pada baris 30, mencetak arr, sehingga menampilkan data sebelum diurutkan.

Pada baris 31, "bubble_sort(arr, n)" memanggil fungsi bubble sort untuk mengurutkan arr (dari besar ke kecil).

Pada baris 32-35, menampilkan hasil urutan (besar ke kecil) dalam satu baris.

pada baris 38-39, kode ini artinya yaitu jika file ini dijalankan langsung (bukan dipanggil dari file lain), maka jalankan fungsi main().

**Penjelasan Output**
<img width="1367" height="251" alt="Cuplikan layar 2026-04-30 230704" src="https://github.com/user-attachments/assets/441ecf3e-781a-4ca4-b0af-a50b7bb46150" />
pertama akan menampilkan perintah masukin banyaknya praktikan
<img width="1356" height="232" alt="Cuplikan layar 2026-04-30 230719" src="https://github.com/user-attachments/assets/e9f64ff2-837e-48f8-9c62-997447bba979" />
lalu masukkan nilai-nilai praktikan
<img width="1222" height="268" alt="Cuplikan layar 2026-04-30 230744" src="https://github.com/user-attachments/assets/6f78a5ec-9d0a-4459-973f-8e563f0b3b64" />
hasilnya akan menampilkan array nilai yang belum terurut dan array nilai yang sudah berurutan secara descending

link yt:
