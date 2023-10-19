from flask import request, Response, jsonify
import json
from http import HTTPStatus
from models import Forms
from flask import Flask
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)


@app.post('/view_graphs')
def show_graphs():
    df = pd.read_csv('data.csv', sep=',')
    sns.kdeplot(df, x='sex', fill=True)
    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, r'graphs')
    try:
        os.rmdir("graphs")
        os.makedirs(final_directory)
        plt.savefig('graphs/target_2_4.png')
    except Exception:
        return jsonify({'ERROR': 'Error occurred when deleting files'})
    return 'graphs/target_2_4.png'


@app.post('/view_data')
def show_data():
    df = pd.read_csv('data.csv', sep=',')
    return jsonify({'DF': df.values.tolist()})




