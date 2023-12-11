import pandas as pd
import seaborn as sns
import os
import matplotlib.pyplot as plt


df = pd.read_csv('data.csv', sep=',')
df.columns = df.columns.str.replace(' ', '_')
df.columns = df.columns.str.lower()
sns.kdeplot(df, x='sex', fill=True)
current_directory = os.getcwd()
final_directory = os.path.join(current_directory, r'graphs')
try:
    os.rmdir("graphs")
    os.makedirs(final_directory)
    plt.savefig('graphs/target_2_4.png')
except Exception:
    plt.show()