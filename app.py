import streamlit as st
import pandas as pd
import joblib
import numpy as np

# 1. Load Model
# Pastikan file model.pkl adalah hasil training ulang (7 fitur) dari notebook
model = joblib.load('model.pkl')

# Judul Halaman
st.title("🎓 Jaya Jaya Institut - Dropout Prediction System")
st.write("Sistem prediksi dini untuk mendeteksi mahasiswa yang berisiko Dropout.")

# Sidebar untuk Input User
st.sidebar.header("Masukkan Data Mahasiswa")

# --- INPUT FITUR UTAMA (7 FITUR) ---

tuition_fees = st.sidebar.selectbox("Status Pembayaran SPP (Tuition Fees)", ["Tepat Waktu", "Menunggak"])
tuition_value = 1 if tuition_fees == "Tepat Waktu" else 0

scholarship = st.sidebar.selectbox("Penerima Beasiswa?", ["Ya", "Tidak"])
scholarship_value = 1 if scholarship == "Ya" else 0

grade_1st = st.sidebar.number_input("Nilai Rata-rata Semester 1", min_value=0.0, max_value=20.0, value=12.0)
grade_2nd = st.sidebar.number_input("Nilai Rata-rata Semester 2", min_value=0.0, max_value=20.0, value=12.0)

age = st.sidebar.slider("Umur saat Mendaftar", 17, 50, 19)

debtor = st.sidebar.selectbox("Memiliki Hutang?", ["Tidak", "Ya"])
debtor_value = 1 if debtor == "Ya" else 0

gender = st.sidebar.selectbox("Gender", ["Wanita", "Pria"])
gender_value = 1 if gender == "Pria" else 0

# --- PREDIKSI ---
if st.sidebar.button("Prediksi Status"):

    # REVISI: Membuat DataFrame HANYA dengan 7 fitur yang sesuai dengan model baru
    # Urutan kolom harus sama persis dengan yang ada di Notebook saat training
    input_data = pd.DataFrame({
        'Tuition_fees_up_to_date': [tuition_value],
        'Scholarship_holder': [scholarship_value],
        'Curricular_units_1st_sem_grade': [grade_1st],
        'Curricular_units_2nd_sem_grade': [grade_2nd],
        'Age_at_enrollment': [age],
        'Debtor': [debtor_value],
        'Gender': [gender_value]
    })
    
    # Lakukan Prediksi
    # Karena input_data sudah pas 7 kolom, tidak akan ada error shape mismatch lagi
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0]

    st.subheader("Hasil Prediksi:")
    
    if prediction == 1: # Dropout
        st.error(f"⚠️ BERISIKO DROPOUT (Probabilitas: {probability[1]:.2%})")
        st.write("Saran: Mahasiswa ini memerlukan pendampingan akademik dan konseling finansial segera.")
    else: # Graduate
        st.success(f"✅ KEMUNGKINAN LULUS (Probabilitas: {probability[0]:.2%})")
        st.write("Saran: Pertahankan performa akademik.")
        
else:
    st.info("Silakan masukkan data di sidebar kiri dan klik tombol Prediksi.")