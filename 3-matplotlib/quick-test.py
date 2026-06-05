import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# One-liner to create and plot
df = pd.DataFrame({'column1': np.random.randn(500) * 10 + 50})
sns.set(style="darkgrid")
sns.histplot(data=df, x="column1", bins=25, kde=True)
plt.show()