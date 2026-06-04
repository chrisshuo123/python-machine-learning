import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

n_rows = 200

data = {
    'karyawan_id': [f'EMP{str(i).zfill(4)}' for i in range(1, n_rows+1)],
    'nama': [f'Karyawan_{i}' for i in range(1, n_rows+1)],
    'departemen': np.random.choice(['HR', 'IT', 'Finance', 'Marketing', 'Operations'], n_rows),
    'jabatan': np.random.choice(['Staff', 'Senior Staff', 'Supervisor', 'Manager', 'Director'], n_rows),
    'gaji_pokok': np.random.randint(5000000, 25000000, n_rows),
    'tunjangan': np.random.randint(500000, 5000000, n_rows),
    'jam_lembur': np.random.randint(0, 40, n_rows),
    'rating_kinerja': np.round(np.random.uniform(1.0, 5.0, n_rows), 1),
    'tahun_masuk': np.random.choice(range(2015, 2025), n_rows),
    'status_keaktifan': np.random.choice(['Aktif', 'Cuti', 'Resign'], n_rows, p=[0.85, 0.1, 0.05])
}

df = pd.DataFrame(data)

# Menambahkan kolom total_gaji
df['total_gaji'] = df['gaji_pokok'] + df['tunjangan'] + (df['jam_lembur'] * 50000)

df.to_csv('2-pandas\data\dataSkenario2.csv', index=False)
print("File data.csv (data karyawan) telah dibuat!")
print(df.head())