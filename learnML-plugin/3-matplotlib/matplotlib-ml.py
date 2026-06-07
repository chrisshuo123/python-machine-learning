import matplotlib.pyplot as plt
import seaborn as sns
 
sns.set(style="darkgrid")
sns.histplot(data="df", x="column1") # Pastikan Anda sudah mengimport dataframe
plt.show()