import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('data.csv', sep=',')
param = 'GPA'
plt.figure(figsize=(8, 6))
sns.set(style="whitegrid")
df['sex'].value_counts().plot(kind='pie', autopct='%1.1f%%', legend=False)
plt.ylabel('')
plt.savefig(f'static/assets/img/graph_pie_sex.png')
plt.show()

