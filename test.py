import pandas as pd
from models import Person
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('data.csv', sep=',')
param = 'GPA'
for main in ['sex', 'cleaner', 'grade', 'residents', 'room_type', 'school']:
        sns.set(style="whitegrid")
        plt.figure(figsize=(8, 6))
        sns.set_palette("Set3")
        tips = sns.load_dataset("tips")
        sns.set(style="whitegrid")
        sns.boxplot(x=main, y=param, data=df)
        plt.savefig(f'static/assets/img/graph_box_{main}')

