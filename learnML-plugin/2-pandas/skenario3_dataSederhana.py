import pandas as pd
import numpy as np

np.random.seed(42)

data = {
    'id': range(1, 51),
    'nama': [f'Item_{i}' for i in range(1, 51)],
    'nilai': np.random.randint(50, 100, 50),
    'kategori': np.random.choice(['A', 'B', 'C', 'D'], 50),
    'status': np.random.choice(['Active', 'Inactive'], 50, p=[0.7, 0.3])
}

df = pd.DataFrame(data)
df.to_csv('learnML-plugin\2-pandas\data\dataSkenario3.csv', index=False)
print("File data.csv (data sederhana) telah dibuat!")
print(df.head())