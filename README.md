# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Domain Proyek

**Jaya Jaya Institut** adalah salah satu institusi pendidikan perguruan tinggi yang telah berdiri sejak tahun 2000. Meskipun memiliki reputasi baik, institusi ini menghadapi masalah serius berupa tingginya angka mahasiswa yang tidak menyelesaikan pendidikan (*dropout*).

Tingginya angka *dropout* ini berdampak negatif pada reputasi institusi dan efisiensi sumber daya. Oleh karena itu, proyek ini bertujuan untuk membantu Jaya Jaya Institut mendeteksi mahasiswa yang berisiko *dropout* sedini mungkin agar dapat diberikan bimbingan khusus.

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan tinggi yang telah berdiri sejak tahun 2000. Hingga saat ini, institusi telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat masalah serius berupa tingginya angka mahasiswa yang tidak menyelesaikan pendidikan (*dropout*).

Tingginya angka *dropout* ini menjadi masalah besar karena merugikan reputasi institusi dan menyia-nyiakan potensi sumber daya. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan *dropout* sehingga dapat diberi bimbingan khusus.

### Permasalahan Bisnis
Permasalahan bisnis utama yang akan diselesaikan dalam proyek ini adalah:
1.  **Deteksi Dini:** Pihak institusi kesulitan mengidentifikasi mahasiswa yang berisiko *dropout* sejak awal semester.
2.  **Faktor Penyebab:** Belum diketahuinya secara pasti faktor dominan (akademik, finansial, atau demografi) yang paling mempengaruhi keputusan mahasiswa untuk berhenti kuliah.
3.  **Monitoring:** Belum adanya alat visualisasi data yang memudahkan manajemen memantau performa mahasiswa secara *real-time*.

### Cakupan Proyek
Cakupan proyek ini meliputi:
1.  **Analisis Data (EDA):** Menganalisis pola data historis mahasiswa untuk menemukan korelasi antara fitur (seperti status pembayaran SPP, nilai, umur) dengan status kelulusan.
2.  **Pembuatan Dashboard:** Membangun dashboard interaktif untuk memvisualisasikan data dan memantau KPI utama.
3.  **Machine Learning:** Mengembangkan model prediksi klasifikasi (Supervised Learning) untuk memprediksi apakah seorang mahasiswa akan *Graduate* atau *Dropout*.
4.  **Deployment:** Membuat prototype aplikasi berbasis web agar model prediksi dapat digunakan dengan mudah oleh staf akademik.

### Persiapan

Sumber data: [Jaya Jaya Institut Student Performance Dataset](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance)

Setup environment:
Untuk menjalankan proyek ini di lokal, pastikan Anda telah menginstal library yang dibutuhkan.

```bash
pip install pandas numpy scikit-learn matplotlib seaborn streamlit joblib
```

## Business Dashboard
Sebuah dashboard interaktif telah dibuat menggunakan Tableau Public untuk membantu manajemen memantau performa mahasiswa. Dashboard ini memvisualisasikan distribusi status mahasiswa, korelasi antara pembayaran SPP dengan tingkat dropout, serta analisis nilai akademik.

Link Dashboard: https://public.tableau.com/views/MonitoringPerformaMahasiswa/MonitoringPerformaMahasiswa?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link 


## Menjalankan Sistem Machine Learning
Prototype sistem prediksi dropout telah berhasil di-deploy menggunakan Streamlit Cloud. Sistem ini memungkinkan pengguna memasukkan data mahasiswa (seperti status SPP, nilai semester, beasiswa) dan mendapatkan prediksi risiko dropout secara instan.

Link Prototype: https://proyek-dropout-prediction-4tszb7w4ddrb8skhlux8tr.streamlit.app/ 

Cara menjalankan di lokal:
```Bash
streamlit run app.py
```

## Conclusion
Berdasarkan analisis mendalam menggunakan statistik deskriptif dan pemodelan Machine Learning, ditemukan pola karakteristik mahasiswa yang sangat kuat:

1.  **Faktor Finansial adalah Penentu Utama:**
    Mahasiswa yang status pembayaran SPP-nya menunggak (`Tuition_fees_up_to_date = 0`) memiliki probabilitas *dropout* di atas 80%. Ini adalah indikator risiko paling dominan dibandingkan faktor akademik sekalipun.

2.  **Karakteristik Mahasiswa Berisiko Tinggi:**
    * **Usia:** Mahasiswa yang mendaftar pada usia lebih tua (di atas rata-rata 25 tahun) cenderung lebih sulit menyelesaikan studi tepat waktu dibandingkan mahasiswa usia muda (fresh graduate SMA).
    * **Akademik Awal:** Nilai IPK Semester 1 & 2 yang rendah (< 10.0) merupakan sinyal kuat kegagalan studi di masa depan.
    * **Beasiswa:** Mahasiswa penerima beasiswa memiliki tingkat kelulusan yang jauh lebih tinggi, mengindikasikan bahwa bantuan finansial efektif menekan angka *dropout*.

3.  **Efektivitas Sistem Prediksi:**
    Model Random Forest yang dikembangkan dengan 7 fitur kunci (termasuk SPP, Nilai, Usia, dan Gender) berhasil memprediksi status mahasiswa dengan akurasi **92%**. Model ini telah diintegrasikan sepenuhnya ke dalam aplikasi berbasis web yang konsisten dan siap pakai.

### Rekomendasi Action Items
Untuk mencapai target penurunan angka *dropout*, manajemen Jaya Jaya Institut disarankan melakukan:
-   **Sistem Deteksi Tunggakan Otomatis:** Mengirim notifikasi personal kepada mahasiswa yang terlambat membayar SPP di minggu pertama jatuh tempo, dilanjutkan dengan tawaran konseling keuangan.
-   **Program Adaptasi Mahasiswa Dewasa:** Kampus perlu menyediakan program mentoring khusus bagi mahasiswa yang masuk di usia >25 tahun untuk membantu adaptasi lingkungan akademik.
-   **Intervensi Akademik Dini:** Mewajibkan bimbingan belajar tambahan bagi mahasiswa dengan IPK Semester 1 di bawah standar.