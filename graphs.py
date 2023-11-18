import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def pie_plot(data):
    return 'ok'


def hist_plot(data, col1, col2):
    sns.scatterplot(data=data, x=col1, y=col2)
    plt.show()


def box_plot(data):
    sns.set(style="whitegrid", palette="pastel")
    plt.figure(figsize=(20, 12))  # Adjust the figure size here
    box_plot = sns.boxplot(x="room_type", y="grade", data=data, hue="sex", dodge=True, linewidth=2.5)
    box_plot.set_title("Distribution of Grades by Room Type and Gender", fontsize=16)
    box_plot.set_xlabel("Room Type", fontsize=14)
    box_plot.set_ylabel("Grade", fontsize=14)
    box_plot.legend(title="Gender", title_fontsize='14', loc='upper right')
    plt.grid(True, linestyle="--", alpha=0.7)
    box_plot.set_xticklabels(["Ideal Clean", "Quite Clean", "Not Very Clean", "Dirty"], rotation=45, ha='right')
    plt.show()


def graph_plot(data):
    return 'ok'

