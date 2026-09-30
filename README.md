# Pertemuan 05 Perulangan Python

Nama: Bunga Nusa Peertiwi
NIM: 2225250166
Kelas: 3F

## Tujuan
Menggunakan for dan while untuk menyelesaikan masalah iteratif[cite: 1].

## Cara Menjalankan
python kuis/kuis2_deret_aritmetika.py

## Algoritma Kuis 2
1. Menerima input suku pertama (a) dan beda (d) sebagai float, serta banyak suku (n) sebagai integer[cite: 1].
2. Melakukan validasi input n menggunakan while; jika n <= 0, program meminta input ulang sampai n positif[cite: 1].
3. Menyiapkan variabel total = 0.0 sebagai akumulator[cite: 1].
4. Menggunakan perulangan for dari 0 sampai n-1 untuk menghitung suku ke-i dengan rumus a + (i * d)[cite: 1].
5. Menambahkan nilai suku ke variabel total dan menampilkan nilai suku tersebut[cite: 1].
6. Menampilkan jumlah akhir seluruh suku dengan format dua angka di belakang koma[cite: 1].

## Hasil Pengujian

| Input | Keluaran yang Diharapkan | Keluaran Aktual | Status |
| --- | --- | --- | --- |
| a = 2, d = 3, n = 5 | Suku: 2, 5, 8, 11, 14; Jumlah: 40.00 | Suku: 2.00, 5.00, 8.00, 11.00, 14.00; Jumlah: 40.00 | Success |
| a = 10, d = -2, n = 4 | Suku: 10, 8, 6, 4; Jumlah: 28.00 | Suku: 10.00, 8.00, 6.00, 4.00; Jumlah: 28.00 | Success |
| a = 1.5, d = 0.5, n = 3 | Suku: 1.5, 2.0, 2.5; Jumlah: 6.00 | Suku: 1.50, 2.00, 2.50; Jumlah: 6.00 | Success |
| n = -2 | Menolak input dan meminta n ulang | Tampil "n harus bilangan bulat positif." lalu meminta input ulang | Success |

## Refleksi
Salah satu kesalahan perulangan yang sering terjadi adalah menempatkan inisialisasi akumulator (total = 0) di dalam badan perulangan[cite: 1]. Hal ini menyebabkan nilai total terus di-reset menjadi 0 pada setiap iterasi[cite: 1]. Cara memperbaikinya adalah dengan meletakkan total = 0 di luar perulangan (sebelum loop dimulai) agar nilainya dapat terus bertambah[cite: 1].