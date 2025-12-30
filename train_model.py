import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# 1. Load Data
print("Sedang melatih ulang model agar kompatibel...")
try:
    df = pd.read_csv('data.csv', delimiter=';')
except FileNotFoundError:
    print("Error: File data.csv tidak ditemukan di folder ini.")
    exit()

# 2. Cleaning & Preprocessing 
df_clean = df[df['Status'] != 'Enrolled'].copy()

# Encoding Target: Dropout = 1, Graduate = 0
status_mapping = {'Dropout': 1, 'Graduate': 0}
df_clean['Status_Encoded'] = df_clean['Status'].map(status_mapping)

# Pisahkan Fitur (X) dan Target (y)
X = df_clean.drop(columns=['Status', 'Status_Encoded'])
y = df_clean['Status_Encoded']

# 3. Training Model Full 
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# 4. Simpan Model Baru
joblib.dump(model, 'model.pkl')
print("SUKSES! Model baru (model.pkl) berhasil disimpan.")