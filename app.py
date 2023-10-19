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
    except Exception as err:
        return jsonify({'ERROR': err.__class__.__name__})
    return 'graphs/target_2_4.png'


@app.post('/view_data')
def show_data():
    df = pd.read_csv('data.csv', sep=',')
    return jsonify({'DF': df.values.tolist()})


@app.route('/add_data', methods=['POST', 'GET'])
def add_data():  # ?password=29AF622358&id=43
    try:
        args = request.get_json()
        data = {
            'sex': args['sex'],
            'cleaner': args['cleaner'],
            'residents': args['residents'],
            'grade': args['grade'],
            'room_type': args['room_type'],
            'school': args['school'],
            'GPA': args['GPA']
        }
        df = pd.DataFrame(data)
        df.to_csv('data.csv', mode='a')
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
