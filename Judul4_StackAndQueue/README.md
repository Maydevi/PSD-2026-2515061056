## **Queue Array**

Program ini berfungsi sebagai sistem manajemen antrian pasien di sebuah rumah sakit secara digital. Melalui antarmuka menu sederhana, pengguna dapat menambahkan nama pasien baru ke dalam daftar, menghapus pasien yang telah selesai dilayani, serta melihat siapa pasien yang berada di urutan paling depan tanpa menghapusnya. Program ini memastikan proses pelayanan berjalan tertib sesuai urutan kedatangan, sehingga meminimalisir kesalahan dalam pemanggilan pasien.

Struktur data yang diterapkan dalam kode ini adalah Circular Queue (Antrian Melingkar) berbasis Array. Algoritma ini menggunakan prinsip FIFO (First-In, First-Out), di mana pasien yang pertama kali mendaftar akan menjadi yang pertama dilayani. Penggunaan logika circular (menggunakan operator modulo %) bertujuan untuk mengoptimalkan penggunaan memori; ketika posisi akhir array tercapai, indeks akan kembali berputar ke posisi awal selama masih ada ruang kosong, sehingga mencegah terjadinya pemborosan memori yang sering terjadi pada antrian linear statis.

Pada Baris ke-1,"class QueueArray:" Ini adalah deklarasi sebuah kelas bernama QueueArray. Kelas ini dirancang untuk membungkus semua logika dan data yang berkaitan dengan antrian (seperti menambah, menghapus, dan mengecek isi antrian) ke dalam satu unit.

Pada Baris ke-2, "def **init**(self, max_size=100):"

"**init**" ini adalah metode khusus yang otomatis dijalankan saat Anda membuat objek baru (misalnya antrian = QueueArray()).

"self:" Parameter ini merujuk pada objek itu sendiri agar variabel di dalamnya bisa diakses oleh metode lain dalam kelas yang sama.

"max_size=100:" Ini adalah parameter dengan nilai default. Jika Anda tidak menentukan ukuran saat membuat objek, maka kapasitas maksimal antrian secara otomatis diset menjadi 100.

Pada Baris ke-3, "self.MAXN = max_size" Baris ini menyimpan angka kapasitas maksimal ke dalam variabel milik objek (self.MAXN). Gunanya adalah untuk membatasi jumlah pasien agar tidak melebihi kapasitas memori yang sudah disiapkan.

Pada Baris ke-4, "self.q = [None] \* self.MAXN" Program membuat sebuah list (array) di Python, Ukurannya sebesar self.MAXN, Semua elemen diisi dengan None sebagai tempat penampung kosong.

Pada Baris ke-5 dan ke-6, "self.front_idx = -1" dan "self.rear_idx = -1" "front_idx:" Digunakan untuk mencatat di posisi mana pasien yang paling depan berada (yang akan dilayani berikutnya).

"rear_idx:" Digunakan untuk mencatat di posisi mana pasien terakhir berada (tempat untuk menambahkan pasien baru).

"Nilai -1:" Digunakan sebagai penanda bahwa antrian tersebut masih kosong. Dalam pemrograman, indeks array dimulai dari 0, sehingga -1 berarti "tidak ada posisi".

Pada Baris ke-8, "def is_empty(self):" adalah fungsi untuk mengecek apakah array kosong

Pada Baris ke-9, "return self.front_idx == -1" ini artinya jika index front -1, berarti tidak ada data.
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-
Pada Baris ke-

