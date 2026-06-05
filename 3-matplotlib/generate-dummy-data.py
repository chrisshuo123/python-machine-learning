import pandas as pd
import numpy as np

def generate_dummy_data(n_samples=1000, random_seed=42):
    """Generate dummy data for visualization practice"""
    np.random.seed(random_seed)

    data ={
        'column1': np.random.normal(100, 20, n_samples),        # For histplot
        'column2': np.random.uniform(0, 200, n_samples),        # For boxplot
        'column3': np.random.poisson(15, n_samples),            # Count data
        'column4': np.random.exponential(25, n_samples),        # Skewed data
        'category': np.random.choice(['Cat1', 'Cat2', 'Cat3'], n_samples),
        'value': np.random.randint(1, 1000, n_samples)
    }

    df = pd.DataFrame(data)
    df.to_csv('3-matplotlib\data\dummy-data.csv', index=False)
    print(f"Dummy data saved to '3-matplotlib\data\dummy-data.csv' with {n_samples} rows")
    return df

# Generate and save
df = generate_dummy_data()
print("\nFirst 5 rows:")
print(df.head())