# README

## Deskripsi Proyek
Aplikasi ini adalah sistem pencarian berbasis teks menggunakan embeddings dan indeks FAISS. Proyek ini dirancang untuk mengelola data produk dan memberikan hasil pencarian yang relevan berdasarkan kategori yang diinputkan pengguna. Proyek ini mengimplementasikan konsep matriks dan vektor untuk melakukan pencarian dan peringkat hasil.

---

## A. Konsep Algoritma

### 1. Preprocessing Teks
Sebelum menerapkan model pembelajaran mesin, teks harus diproses terlebih dahulu agar dapat digunakan dalam model. Langkah-langkah preprocessing termasuk:
- **Tokenisasi:** Memecah teks menjadi kata-kata atau token.
- **Lowercasing:** Mengubah teks menjadi huruf kecil untuk menghindari variasi.
- **Pembersihan Teks:** Menghapus karakter khusus atau tanda baca yang tidak relevan.

Algoritma ini penting untuk memastikan bahwa teks diubah menjadi bentuk yang dapat dipahami oleh model.

### 2. Pembuatan Embedding dengan Model Pre-trained (e.g., Sentence-BERT)
Setelah preprocessing, langkah selanjutnya adalah menghasilkan embedding vektor untuk setiap potongan teks menggunakan model pre-trained seperti Sentence-BERT. Proses ini menghasilkan vektor dengan dimensi tinggi yang merepresentasikan makna semantik dari teks.

### 3. Pencarian k-Nearest Neighbors (k-NN)
Setelah teks diubah menjadi embedding, kita menggunakan k-NN untuk menemukan vektor terdekat. Langkah-langkah dalam k-NN adalah:
- **Perhitungan Jarak:** Menghitung jarak antara vektor query dengan vektor dalam dataset menggunakan rumus Euclidean Distance atau Cosine Similarity.
- **Peringkat Hasil:** Mengurutkan hasil pencarian berdasarkan jarak terpendek atau kesamaan tertinggi.

### 4. FAISS untuk Optimasi Pencarian
Jika dataset sangat besar, pencarian menggunakan k-NN bisa menjadi sangat lambat. Untuk mengatasi ini, kita menggunakan FAISS, yang mengoptimalkan pencarian dengan metode Inverted File Index (IVF) atau HNSW. FAISS memungkinkan pencarian lebih cepat dengan mengurangi jumlah perhitungan yang diperlukan untuk menemukan vektor terdekat.

---

## B. Alur Proses Pencarian

1. **Input Query:** Pengguna memasukkan query teks yang ingin dicari.
2. **Embeddings:** Query teks diproses untuk menghasilkan embedding vektor menggunakan model transformer (e.g., Sentence-BERT).
3. **Pencarian k-NN:** Menggunakan FAISS atau algoritma pencarian lainnya, kita mencari k vektor terdekat dalam dataset yang diwakili oleh query.
4. **Pengurutan dan Peringkat:** Hasil pencarian diurutkan berdasarkan jarak atau kesamaan (tergantung metrik yang dipilih).
5. **Output:** Hasil pencarian yang paling relevan ditampilkan kepada pengguna.
