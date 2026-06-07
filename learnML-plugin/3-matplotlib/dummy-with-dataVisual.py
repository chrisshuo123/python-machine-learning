import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set seed for reproducibility
np.random.seed(42)

# Create dummy dataset
n_samples = 1000

data = {
    'column1': np.random.normal(loc=100, scale=15, size=n_samples),     # Normal Distribution
    'column2': np.random.exponential(scale=50, size=n_samples),         # Exponential Distribution
    'column3': np.random.uniform(0, 100, n_samples),                    # Uniform Distribution
    'column4': np.random.poisson(lam=30, size=n_samples),               # Poisson Distribution
    'column5': np.random.binomial(n=100, p=0.5, size=n_samples),        # Binomial Distribution
    'category': np.random.choice(['A', 'B', 'C', 'D'], n_samples, p=[0.3, 0.4, 0.2, 0.1]),
    'group': np.random.choice(['Group1', 'Group2', 'Group3'], n_samples)
}

df = pd.DataFrame(data)

# Save to CSV (Opsional)
df.to_csv('3-matplotlib\data\data.csv', index=False)

print("Dataset created successfully!")
print(f"Shape: {df.shape}")
print("\nFirst 5 rows:")
print(df.head())
print("\nBasic Statistics:")
print(df.describe())

# Your histogram plot
sns.set(style="darkgrid")
sns.histplot(data=df, x="column1", bins=30, color='steelblue', alpha=0.7)
plt.title('Distribution of Column1 (Normal Distribution)', fontsize=14, fontweight='bold')
plt.xlabel('Values', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.show()



