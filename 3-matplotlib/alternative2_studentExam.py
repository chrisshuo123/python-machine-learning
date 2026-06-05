import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

# Create exam scores data
df = pd.DataFrame({
    'column1': np.random.normal(72, 12, 200),       # Exam scores (mean=75, std=12)
    'math_scores': np.random.normal(70, 15, 200),
    'science_scores': np.random.normal(80, 10, 200),
    'student_category': np.random.choice(['Freshman', 'Sophomore', 'Junior', 'Senior'], 200)
})

# Ensure scores are between 0-100
df['column1'] = np.clip(df['column1'], 0, 100)
df['math_scores'] = np.clip(df['math_scores'], 0, 100)
df['science_scores'] = np.clip(df['science_scores'], 0, 100)

print("Exam Scores Dataset:")
print(df.head())

# Your Histogram
sns.set(style="darkgrid")
sns.histplot(data=df, x="column1", bins=15, kde=True, color='green', edgecolor='black')
plt.axvline(df['column1'].mean(), color='red', linestyle='--', linewidth=2, label=f"Mean: {df['column1'].mean():.1f}")
plt.title("Distribution of Student Exam Scores", fontsize=14, fontweight='bold')
plt.xlabel("Scores", fontsize=12)
plt.ylabel("Number of Students", fontsize=12)
plt.legend()
plt.show()

# Additional useful info
print(f"\nStatistics for Column1:")
print(f"Mean: {df['column1'].mean():.2f}")
print(f"Median: {df['column1'].median():.2f}")
print(f"Std: {df['column1'].std():.2f}")
print(f"Min: {df['column1'].min():.2f}")
print(f"Max: {df['column1'].max():.2f}")