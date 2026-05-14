## **Queue Array**

Program ini berfungsi sebagai sistem manajemen antrian pasien di sebuah rumah sakit secara digital. Melalui antarmuka menu sederhana, pengguna dapat menambahkan nama pasien baru ke dalam daftar, menghapus pasien yang telah selesai dilayani, serta melihat siapa pasien yang berada di urutan paling depan tanpa menghapusnya. Program ini memastikan proses pelayanan berjalan tertib sesuai urutan kedatangan, sehingga meminimalisir kesalahan dalam pemanggilan pasien.

Struktur data yang diterapkan dalam kode ini adalah Circular Queue (Antrian Melingkar) berbasis Array. Algoritma ini menggunakan prinsip FIFO (First-In, First-Out), di mana pasien yang pertama kali mendaftar akan menjadi yang pertama dilayani. Penggunaan logika circular (menggunakan operator modulo %) bertujuan untuk mengoptimalkan penggunaan memori; ketika posisi akhir array tercapai, indeks akan kembali berputar ke posisi awal selama masih ada ruang kosong, sehingga mencegah terjadinya pemborosan memori yang sering terjadi pada antrian linear statis.
<img width="649" height="497" alt="Cuplikan layar 2026-05-13 135336" src="https://github.com/user-attachments/assets/d72132c5-5f7a-468d-9eaf-07c6c40ace1b" />

Baris ke-1,"class QueueArray:" Ini adalah deklarasi sebuah kelas bernama QueueArray. Kelas ini dirancang untuk membungkus semua logika dan data yang berkaitan dengan antrian (seperti menambah, menghapus, dan mengecek isi antrian) ke dalam satu unit.

Baris ke-2, "def **init**(self, max_size=100):"

"**init**" ini adalah metode khusus yang otomatis dijalankan saat Anda membuat objek baru (misalnya antrian = QueueArray()).

"self:" Parameter ini merujuk pada objek itu sendiri agar variabel di dalamnya bisa diakses oleh metode lain dalam kelas yang sama.

"max_size=100:" Ini adalah parameter dengan nilai default. Jika Anda tidak menentukan ukuran saat membuat objek, maka kapasitas maksimal antrian secara otomatis diset menjadi 100.

Baris ke-3, "self.MAXN = max_size" ini untuk menyimpan angka batas maksimal pasien yang bisa ditampung ke dalam variabel MAXN.

Baris ke-4, "self.q = [None] \* self.MAXN" untuk membuat daftar (array) kosong sebanyak kapasitas MAXN sebagai tempat duduk pasien.

Baris ke-5, "self.front_idx = -1" Ini untuk menandai bahwa posisi pasien terdepan belum ada (antrian masih kosong). dan pada baris ke-6 "self.rear_idx = -1" Ini untuk menandai bahwa posisi pasien terakhir juga belum ada.
"front_idx:" Digunakan untuk mencatat di posisi mana pasien yang paling depan berada (yang akan dilayani berikutnya).

"rear_idx:" Digunakan untuk mencatat di posisi mana pasien terakhir berada (tempat untuk menambahkan pasien baru).

"Nilai -1:" Digunakan sebagai penanda bahwa antrian tersebut masih kosong. Dalam pemrograman, indeks array dimulai dari 0, sehingga -1 berarti "tidak ada posisi".

Baris ke-8, "def is_empty(self):" adalah fungsi untuk mengecek apakah antrian kosong

Baris ke-9, "return self.front_idx == -1" ini artinya jika index front -1, berarti antrian kosong.

Baris ke-11, "def is_full(self):" ini untuk menngecek apakah array sudah penuh

Baris ke-14, "def enqueue(self, x):" ini adalah fungsi enqueue yaitu untuk menambahkan pasien ke antrian belakang

Baris ke-15, "if self.is_full():"  jika antrian/ruangan penuh maka,
Baris ke-16, " print("Tidak tersedia ruangan, ruangan sudah penuh")" menampilkan teks ini apabila kondisi pada baris ke-15 terpenuhi

Baris ke-18, "  if self.is_empty():" jika antrian/ruangan kosong maka,
Baris ke-19 dan ke-20, front dan real adalah 0 apabila kondisi pada baris 18 terpenuhi

Baris ke-22, self.rear_idx = (self.rear_idx + 1) % self.MAXN: Ini untuk menggeser posisi belakang ke urutan berikutnya secara melingkar jika antrian tidak kosong. Kondisi ini terjadi apabila 2 kondisi di atasnya yaitu pada baris ke-15 dan ke-16 tidak terpenuhi

Baris ke-23, "self.q[self.rear_idx] = x" Ini untuk memasukkan nama pasien ke dalam tempat duduk di posisi rear yang baru.

Baris ke-24, "print(f"Penambahan pasien baru bernama {x} berhasil")" menampilkan/mencetak teks bahwa nama pasien sudah ditambah ke dalam antrian/array

Baris ke-26, "def dequeue(self):" ini adalah fungsi enqueue yaitu untuk menghapus nama pasien yang dilayani atau menghapus nama yang berada didepan array

Baris ke-27, "if self.is_empty():" mengecek apakah antrian kosong

Baris ke-28, menampilkan teks ("Antrian kosong") apabila kondisi pada baris ke-27 terpenuhi

Baris ke-30, print(f"Pasien bernama {self.q[self.front_idx]}..."): Ini untuk menghapus nama pasien di posisi paling depan karena telah dilayani.

Baris ke-31, "if self.front_idx == self.rear_idx:" Ini untuk mengecek apakah pasien yang baru saja dilayani adalah orang terakhir di antrian tersebut.

Baris ke-32 dan ke-33: ketika kondisi pada baris ke-31 terpenuhi maka posisi front dan rear kembali ke -1 karena antrian menjadi kosong

I<img width="539" height="454" alt="Cuplikan layar 2026-05-13 135349" src="https://github.com/user-attachments/assets/7bea04e1-9012-42e6-b542-8f0c4576f6d0" />

Baris ke-35, self.front_idx = (self.front_idx + 1) % self.MAXN: Ini untuk menggeser posisi depan ke orang berikutnya secara melingkar setelah orang sebelumnya selesai.

Baris ke-37, "def peek(self):" ini adalah fungsi peek yaitu untuk melihat isi data array atau nama antrian bagian depan tanpa harus menghapusnya dari antrian/array

Baris ke-38 dan ke-39, jika antrian kosong akan menampilkan teks ("Antrian Kosong")

Baris ke-41, print(f"Antrian Pasien Terdepan: {self.q[self.front_idx]}"): Ini untuk melihat nama pasien yang ada di posisi front_idx tanpa menghapusnya.

Baris ke-43, "def display(self):" ini adalah fungsi display yaitu untuk menampilkan isi array atau daftar nama pasien dari awal sampai akhir (depan sampai belakang)

Baris ke-44 dan ke-45, jika antrian kosong akan menampilkan teks ("Antrian Kosong")

Baris ke-47, mencetak teks ("Daftar nama pasien di Rumah Sakit: ")

Baris ke-48, "i = self.front_idx:' Ini untuk menyiapkan variabel penghitung yang dimulai dari posisi pasien paling depan.

Baris ke-49, "while True:" Ini untuk memulai perulangan terus-menerus guna menyisir seluruh nama pasien yang ada.
Baris ke-50, "print(self.q[i], end=" ")" berfungsi untuk menampilkan nama pasien yang berada di posisi indeks i ke layar secara menyamping, bukan ke bawah.

Baris ke-51, "if i == self.rear_idx:" dan baris ke-52 "break:" Ini untuk menghentikan perulangan jika posisi penyisir sudah sampai ke pasien paling belakang.

Baris ke-53, i = (i + 1) % self.MAXN: Ini untuk menggeser ke posisi berikutnya secara melingkar agar semua pasien terdata.

Baris ke-54, "print()" untuk mencetak hasil fungsi display

Baris ke-57, "def main():" ini adalah fungsi utama

Baris ke-58, queue = QueueArray(): ini untuk membuat objek antrian baru dari cetakan yang sudah kita buat tadi.

Baris ke-59,"pilih = 0" Angka 0 diberikan sebagai nilai awal agar variabel pilih sudah terdefinisi sebelum program masuk ke dalam perulangan while.

Baris ke-60, while pilih != 5:: Ini untuk menjaga agar program tetap berjalan selama pengguna tidak memilih angka 5 (Keluar).

Baris ke-61 sampai dengan 66, adalah teks yang akan muncul pertama kali saat program dijalankan

<img width="455" height="437" alt="Cuplikan layar 2026-05-13 135404" src="https://github.com/user-attachments/assets/2e74ffe7-8886-4477-9e62-c2274ccbf07d" />

Baris ke-68, "pilih = int(input("Pilih: "))" Ini untuk menerima input angka pilihan menu dari pengguna.

Baris ke-69 dan baris ke-70, "except ValueError:" Ini untuk menangkap error, sehingga program tidak langsung mati.

Baris ke-78-87: Ini adalah logika percabangan untuk menjalankan fungsi (tambah, layani, lihat) sesuai dengan angka yang ditekan pengguna.


**OUTPUT**
<img width="514" height="397" alt="Cuplikan layar 2026-05-14 212314" src="https://github.com/user-attachments/assets/1b096567-89e7-4913-b600-9015fb5ae127" />
<img width="535" height="424" alt="Cuplikan layar 2026-05-14 212324" src="https://github.com/user-attachments/assets/55d77f4a-083c-4fe4-a2f6-247aa6011b50" />

Ketika program di jalankan akan memunculkan menu pilihan, lalu pengguna akan diminta untuk memasukkan pilihannnya sebagai inputan.

Jika pilih 1, maka pengguna di minta memasukkan nama pasien, lalu akan muncul teks bahwa penambahan nama pasien tersebut berhasil

Jika pilih 2, maka artinya pasien telah dilayani maka akan dihapus dari antrian atau array

jika pilih 3, maka akan menampilkan nama pasien yang mengantri paling depan tanpa dihapus

Jika pilih 4, maka akan menampilkan sisa antrian pasien yang belum dilayani

jila pilih 5, maka program akan selesai dan berhenti berjalan
kemudian program akan terus berulang sampai pengguna memasukkan pilihan 5

Link Youtube: https://youtu.be/jLz1S5LZoo4
