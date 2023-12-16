import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('data.csv', sep=',')
param = 'GPA'
plt.figure(figsize=(14, 10))
sns.set(style="whitegrid")
df['room_type'].value_counts().plot(kind='pie', autopct='%1.1f%%', legend=False, fontsize=36)
plt.ylabel('')
plt.savefig('output.png', transparent=True)
plt.show()


