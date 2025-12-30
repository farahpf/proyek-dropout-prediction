import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# 1. LOAD DATASET
# GANTI 'data.csv' dengan nama file dataset kamu yang asli (misal: 'data.csv' atau 'student_data.csv')
try:
    df = pd.read_csv('data.csv', delimiter=';') # Coba delimiter titik koma
except:
    df = pd.read_csv('data.csv') # Coba delimiter koma biasa

print("Dataset berhasil diload!")

# 2. DATA CLEANING (Sama seperti di Notebook)
# Hapus status Enrolled agar konsisten
df = df[df['Status'] != 'Enrolled']

# Mapping Target
status_mapping = {'Dropout': 1, 'Graduate': 0}
df['Status_Encoded'] = df['Status'].map(status_mapping)

# 3. FITUR SELECTION (Hanya 7 Fitur Streamlit)
selected_features = [
    'Tuition_fees_up_to_date',
    'Scholarship_holder',
    'Curricular_units_1st_sem_grade',
    'Curricular_units_2nd_sem_grade',
    'Age_at_enrollment',
    'Debtor',
    'Gender'
]

X = df[selected_features]
y = df['Status_Encoded']

# 4. LATIH MODEL
print("Sedang melatih model...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# 5. SIMPAN MODEL
joblib.dump(model, 'model.pkl')
print("✅ SUKSES! File 'model.pkl' berhasil diperbarui agar kompatibel dengan Streamlit.")