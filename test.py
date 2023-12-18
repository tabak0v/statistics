import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('data.csv', sep=',')
param = 'GPA'
for factor in ["school"]:
    plt.figure(figsize=(8, 6))
    sns.set(style="whitegrid")
    sns.set(font_scale=0.6)
    sns.violinplot(data=df, x=factor, y='GPA', cut=0)
    plt.ylabel('')
    plt.savefig(f'static/assets/img/graph_violin_{factor}.png')
    plt.show()


