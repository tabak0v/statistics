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
app.register_blueprint(api.blueprint)
if __name__ == "__main__":
    app.run(debug=True)


@app.route('/view_graphs', methods=['POST', 'GET'])
def show_graphs():
    df = pd.read_csv('/home/stat57ya24/mysite/data.csv', sep=',')
    sns.kdeplot(df, x='sex', fill=True)
    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, r'graphs')
    try:
        os.rmdir("graphs")
        os.makedirs(final_directory)
        plt.savefig('graphs/target_2_4.png')
    except Exception as err:
        return jsonify({'ERROR': err.__class__.__name__})
    return 'graphs/target_2_4.png'


@app.route('/view_data', methods=['POST', 'GET'])
def show_data():
    df = pd.read_csv('/home/stat57ya24/mysite/data.csv', sep=',')
    return jsonify({'DF': df.values.tolist()})


@app.route('/clear_space', methods=['DELETE', 'GET'])
def delete_files():  # ?password=29AF622358&id=43
    try:
        os.rmdir("graphs")
        return jsonify({'SUCCESS': 'Data has been added!'})
    except Exception as err:
        return jsonify({'ERROR': err.__class__.__name__})
