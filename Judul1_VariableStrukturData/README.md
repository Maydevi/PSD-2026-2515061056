# List1D
Program ini dibuat untuk memahami bagaimana array (kumpulan data berindeks) menyimpan data di dalam memori komputer. Program ini memiliki 5 pilihan menu: melihat alamat memori dari keseluruhan array, melihat alamat memori setiap kotak (indeks) dalam array, mengisi nilai ke semua kotak array, memeriksa isi suatu kotak berdasarkan nomor indeksnya, dan keluar dari program.

Struktur data yang digunakan adalah array sederhana dengan 5 kotak (indeks 0 sampai 4). Program ini mengajarkan dua cara dasar mengakses data: akses berurutan (sequential) yaitu mengisi atau melihat semua kotak satu per satu dari awal sampai akhir, dan akses langsung (direct indexing) yaitu langsung mengambil data dari kotak tertentu tanpa perlu memeriksa kotak lainnya. Fungsi `id()` digunakan untuk melihat alamat memori, sehingga pemula bisa melihat bahwa setiap kotak dalam array menyimpan alamat yang berbeda di memori komputer.


<img width="1144" height="692" alt="Cuplikan layar 2026-04-21 225244" src="https://github.com/user-attachments/assets/b62e65a5-fc89-4485-8553-621777a7f5b7" />

Pada baris 1-6, fungsi ini hanya mencetak opsi-opsi menu ke layar. Tidak mengembalikan nilai (return None).

Pada baris 9, fungsi main() membuat fungsi utama yang akan menjalankan seluruh program.

Pada baris 10, [0] * 5 artinya: buat sebuah list (array) yang berisi angka 0 sebanyak 5 kali.

Pada baris 11, selama running bernilai True, program terus berjalan.

Pada baris 12, memulai loop utama program (menu berulang), selama kondisi di sampingnya bernilai True, blok kode di dalamnya akan diulang terus.

Pada baris 13, memanggil fungsi menu() yang sudah kita buat di atas, sehingga pilihan menu muncul di layar.

Pada baris 14-18, menerima input dari user dan mengubahnya menjadi integer. Jika input bukan angka (misal huruf), maka terjadi ValueError, program mencetak pesan error lalu continue (kembali ke awal loop tanpa menjalankan kode di bawahnya).

Pada baris 19, jika pilihan user adalah 1, maka jalankan blok kode di bawahnya

Pada baris 20, id(a) adalah fungsi untuk melihat alamat memori tempat variabel a disimpan di komputer.
<img width="518" height="176" alt="Cuplikan layar 2026-04-21 234833" src="https://github.com/user-attachments/assets/51c7feb7-f6d8-4242-bc63-f2977c55798e" />

Pada baris 21-23,  program akan menampilkan alamat memori dari setiap kotak (indeks 0 sampai 4) dalam array a.
<img width="515" height="286" alt="Cuplikan layar 2026-04-21 235007" src="https://github.com/user-attachments/assets/1f13990c-41bd-4228-8d22-0c0a5174d015" />

<img width="914" height="653" alt="Cuplikan layar 2026-04-21 225304" src="https://github.com/user-attachments/assets/4771e3ae-3c32-4aec-a6d1-86beb663e48c" />

Pada baris 24-33,  menerima input dari user dan mengubahnya menjadi integer. Jika input bukan angka (misal huruf), maka terjadi ValueError, program mencetak pesan error lalu continue (kembali ke awal loop tanpa menjalankan kode di bawahnya).
<img width="554" height="342" alt="Cuplikan layar 2026-04-21 235343" src="https://github.com/user-attachments/assets/6799f659-9c45-424a-ae86-c62caa086b70" />


Pada baris 34-47, memeriksa nilai indeks satu per satu. Jika indeks antara 0-4, cetak nilai yang tersimpan di posisi tersebut. Jika di luar rentang, cetak pesan error.
<img width="509" height="212" alt="Cuplikan layar 2026-04-21 235425" src="https://github.com/user-attachments/assets/626bc24a-4072-4e2f-961a-341c9353ab1b" />


<img width="886" height="333" alt="Cuplikan layar 2026-04-21 225328" src="https://github.com/user-attachments/assets/50d92b8f-8d8e-444e-80ae-5dea24f77823" />

Pada baris 48-52, mengubah running menjadi False, sehingga loop while akan berhenti setelah iterasi ini. Lalu mencetak pesan selesai.
<img width="578" height="182" alt="Cuplikan layar 2026-04-21 235551" src="https://github.com/user-attachments/assets/dca10408-cf70-4bc9-a54d-d4ba2689cf64" />


Pada baris 55-56, memeriksa apakah file ini dijalankan langsung (bukan diimpor sebagai modul). Jika iya, maka fungsi main() dipanggil, sehingga program mulai berjalan.

