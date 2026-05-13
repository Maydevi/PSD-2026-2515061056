## **Queue Array**

Program ini berfungsi sebagai sistem manajemen antrian pasien di sebuah rumah sakit secara digital. Melalui antarmuka menu sederhana, pengguna dapat menambahkan nama pasien baru ke dalam daftar, menghapus pasien yang telah selesai dilayani, serta melihat siapa pasien yang berada di urutan paling depan tanpa menghapusnya. Program ini memastikan proses pelayanan berjalan tertib sesuai urutan kedatangan, sehingga meminimalisir kesalahan dalam pemanggilan pasien.

Struktur data yang diterapkan dalam kode ini adalah Circular Queue (Antrian Melingkar) berbasis Array. Algoritma ini menggunakan prinsip FIFO (First-In, First-Out), di mana pasien yang pertama kali mendaftar akan menjadi yang pertama dilayani. Penggunaan logika circular (menggunakan operator modulo %) bertujuan untuk mengoptimalkan penggunaan memori; ketika posisi akhir array tercapai, indeks akan kembali berputar ke posisi awal selama masih ada ruang kosong, sehingga mencegah terjadinya pemborosan memori yang sering terjadi pada antrian linear statis.

Baris ke-1,"class QueueArray:" Ini adalah deklarasi sebuah kelas bernama QueueArray. Kelas ini dirancang untuk membungkus semua logika dan data yang berkaitan dengan antrian (seperti menambah, menghapus, dan mengecek isi antrian) ke dalam satu unit.

Baris ke-2, "def **init**(self, max_size=100):"

"**init**" ini adalah metode khusus yang otomatis dijalankan saat Anda membuat objek baru (misalnya antrian = QueueArray()).

"self:" Parameter ini merujuk pada objek itu sendiri agar variabel di dalamnya bisa diakses oleh metode lain dalam kelas yang sama.

"max_size=100:" Ini adalah parameter dengan nilai default. Jika Anda tidak menentukan ukuran saat membuat objek, maka kapasitas maksimal antrian secara otomatis diset menjadi 100.

Baris ke-3, "self.MAXN = max_size" ini untuk menyimpan angka batas maksimal pasien yang bisa ditampung ke dalam variabel MAXN.

Baris ke-4, "self.q = [None] \* self.MAXN" Puntuk membuat daftar (array) kosong sebanyak kapasitas MAXN sebagai tempat duduk pasien.

Baris ke-5, "self.front_idx = -1" Ini untuk menandai bahwa posisi pasien terdepan belum ada (antrian masih kosong). dan pada baris ke-6 "self.rear_idx = -1" Ini untuk menandai bahwa posisi pasien terakhir juga belum ada.
"front_idx:" Digunakan untuk mencatat di posisi mana pasien yang paling depan berada (yang akan dilayani berikutnya).

"rear_idx:" Digunakan untuk mencatat di posisi mana pasien terakhir berada (tempat untuk menambahkan pasien baru).

"Nilai -1:" Digunakan sebagai penanda bahwa antrian tersebut masih kosong. Dalam pemrograman, indeks array dimulai dari 0, sehingga -1 berarti "tidak ada posisi".

Baris ke-8, "def is_empty(self):" adalah fungsi untuk mengecek apakah antrian kosong

Baris ke-9, "return self.front_idx == -1" ini artinya jika index front -1, berarti antrian kosong.

Baris ke-11, "def is_full(self):" ini untuk menngecek apakah array sudah penuh

Baris ke-12, "return (self.rear_idx + 1) % self.MAXN == self.front_idx" ini untuk mengecek jika posisi berikutnya setelah rear adalah front, maka tandanya ruangan sudah penuh (melingkar).

Baris ke-16, "if self.is_full():" Ini untuk mengecek kondisi apakah antrian sudah penuh sebelum memasukkan pasien baru.

Baris ke-17 sampai baris ke 18, Ini untuk menampilkan pesan penolakan dan menghentikan fungsi jika ruangan memang sudah penuh.

Baris ke-Baris ke-20, if self.is_empty():: Ini untuk mengecek apakah pasien yang masuk ini adalah pasien pertama di antrian yang kosong.

Baris ke-21-22: Ini untuk mengatur posisi depan (front) dan belakang (rear) ke angka 0 karena baru ada satu orang.

Baris ke-24, self.rear_idx = (self.rear_idx + 1) % self.MAXN: Ini untuk menggeser posisi belakang ke urutan berikutnya secara melingkar jika antrian tidak kosong.

Baris ke-25, self.q[self.rear_idx] = x: Ini untuk memasukkan nama pasien ke dalam tempat duduk di posisi rear yang baru.

Baris ke-29, if self.is_empty():: Ini untuk memastikan tidak ada proses pelayanan jika memang tidak ada pasien di antrian.

Baris ke-32, print(f"Pasien bernama {self.q[self.front_idx]}..."): Ini untuk mengambil nama pasien di posisi paling depan untuk segera dilayani.

Baris ke-33, if self.front_idx == self.rear_idx:: Ini untuk mengecek apakah pasien yang baru saja dilayani adalah orang terakhir di antrian tersebut.

Baris ke-34-35: Ini untuk mereset posisi front dan rear kembali ke -1 karena antrian menjadi kosong total.

Baris ke-37, self.front_idx = (self.front_idx + 1) % self.MAXN: Ini untuk menggeser posisi depan ke orang berikutnya secara melingkar setelah orang sebelumnya selesai.

Baris ke-43, print(f"Antrian Pasien Terdepan: {self.q[self.front_idx]}"): Ini untuk mengintip siapa nama pasien yang ada di posisi front_idx tanpa menghapusnya.

Baris ke-51, i = self.front_idx: Ini untuk menyiapkan variabel penghitung yang dimulai dari posisi pasien paling depan.

Baris ke-52, while True:: Ini untuk memulai perulangan terus-menerus guna menyisir seluruh nama pasien yang ada.

Baris ke-54, if i == self.rear_idx: break: Ini untuk menghentikan perulangan jika posisi penyisir sudah sampai ke pasien paling belakang.

Baris ke-56, i = (i + 1) % self.MAXN: Ini untuk menggeser penyisir ke posisi berikutnya secara melingkar agar semua pasien terdata.

Baris ke-62, queue = QueueArray(): Ini untuk membuat objek antrian baru dari cetakan yang sudah kita buat tadi.

Baris ke-64, while pilih != 5:: Ini untuk menjaga agar program tetap berjalan selama pengguna tidak memilih angka 5 (Keluar).

Baris ke-71, pilih = int(input("Pilih: ")): Ini untuk menerima input angka pilihan menu dari pengguna.

Baris ke-72-74, except ValueError:: Ini untuk menangkap error jika pengguna iseng memasukkan huruf, sehingga program tidak langsung mati.

Baris ke-76-88: Ini adalah logika percabangan untuk menjalankan fungsi (tambah, layani, lihat) sesuai dengan angka yang ditekan pengguna.
