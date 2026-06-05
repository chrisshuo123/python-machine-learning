import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create simple DataFrame
np.random.seed(42)
df = pd.DataFrame({
    'column1': np.random.randint(20, 100, 500),     # 500 random integers between 20-100
    'column2': np.random.randn(500) * 10 + 50,      # 500 values with mean=50, std=10
    'column3': np.random.exponential(30, 500)       # 500 exponential values
})

# Your visualization
sns.set(style="darkgrid")
sns.histplot(data=df, x="column1", bins=20, kde=True, color='coral')
plt.title("Histogram of column1", fontsize=14)
plt.xlabel("Column1 Values", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.show()