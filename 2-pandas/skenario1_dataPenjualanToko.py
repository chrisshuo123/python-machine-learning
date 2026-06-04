import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set seed untuk reproduktibilitas
np.random.seed(42)

# Membuat data simulasi
n_rows = 100

data = {
    'tanggal': [datetime(2024, 1, 1) + timedelta(days=i) for i in range(n_rows)],
    'produk': np.random.choice(['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headset'], n_rows),
    'kategori': np.random.choice(['Elektronik', 'Aksesoris', 'Periferal'], n_rows),
    'harga': np.random.randint(100000, 5000000, n_rows),
    'jumlah_terjual': np.random.randint(1, 50, n_rows),
    'rating': np.round(np.random.uniform(3.0, 5.0, n_rows), 1),
    'diskon_persen': np.random.choice([0, 5, 10, 15, 20], n_rows),
    'status': np.random.choice(['Selesai', 'Diproses', 'Dikirim', 'Dibatalkan'], n_rows, p=[0.6, 0.2, 0.15, 0.05])
}

df = pd.DataFrame(data)

# Menambahkan kolom total_penjualan
df['total_penjualan'] = df['harga'] * df['jumlah_terjual'] * (1 - df['diskon_persen']/100)

# Menyimpan ke CSV
df.to_csv('2-pandas\data\dataSkenario1.csv', index=False)
print("File data.csv telah dibuat!")
print("\n5 baris pertama:")
print(df.head())
print(f"\nShape dataset: {df.shape}")
print(f"\nInfo dataset:")
print(df.info())