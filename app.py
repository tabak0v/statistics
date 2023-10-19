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


@app.route('/view_graphs', methods=['POST', 'GET'])
def show_graphs():
    df = pd.read_csv('data.csv', sep=',')
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
    df = pd.read_csv('data.csv', sep=',')
    return jsonify({'DF': df.values.tolist()})


@app.route('/add_data', methods=['POST'])
def add_data():  # ?password=29AF622358&id=43
    try:
        data = {
            'sex': request.args.get('sex'),
            'cleaner': request.args.get('cleaner'),
            'residents': request.args.get('residents'),
            'grade': request.args.get('grade'),
            'room_type': request.args.get('room_type'),
            'school': request.args.get('school'),
            'GPA': request.args.get('GPA')
        }
        df0 = pd.read_csv('data.csv', delimiter=',')
        df = pd.DataFrame(data, index=[df0.shape[0] + 1])
        df.to_csv('data.csv', mode='a', index=False, header=False)
        return jsonify({'SUCCESS': 'Data appended successfully!'})
    except Exception as err:
        return jsonify({'ERROR': err.__class__.__name__})


@app.route('/delete_data', methods=['DELETE', 'GET'])
def delete_data():  # ?password=29AF622358&id=43
    try:
        id = int(request.args.get('id'))
        df = pd.read_csv('data.csv', delimiter=',')
        df = df.drop([id])
        df.to_csv('data.csv')
        return jsonify({'SUCCESS': 'Data has been added!'})
    except Exception as err:
        return jsonify({'ERROR': err.__class__.__name__})


@app.route('/clear_space', methods=['DELETE', 'GET'])
def delete_files():  # ?password=29AF622358&id=43
    try:
        os.rmdir("graphs")
        return jsonify({'SUCCESS': 'Data has been added!'})
    except Exception as err:
        return jsonify({'ERROR': err.__class__.__name__})
