import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('data.csv', sep=',')
param = 'GPA'
for elem in ['school']:
    plt.figure(figsize=(8, 6))
    sns.set(style="whitegrid", font_scale=0.6)
    sns.violinplot(x=elem, y='GPA', data=df)
    plt.savefig(f'static/assets/img/graph_violin_{elem}.png')
    plt.show()
