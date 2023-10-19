import flask
from flask import jsonify, request
import pandas as pd
import os


blueprint = flask.Blueprint(
    'api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/add_data', methods=['POST', 'GET'])
def add_data():  # ?password=29AF622358&id=43
    print(request.get_json())
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
    except Exception:
        return jsonify({'ERROR': 'Error occurred when adding data'})


@blueprint.route('/api/delete_data', methods=['DELETE', 'GET'])
def delete_data():  # ?password=29AF622358&id=43
    try:
        id = int(request.args.get('id'))
        df = pd.read_csv('data.csv', delimiter=',')
        df = df.drop([id])
        df.to_csv('data.csv')
        return jsonify({'SUCCESS': 'Data has been added!'})
    except Exception:
        return jsonify({'ERROR': 'Error occurred when deleting data'})


@blueprint.route('/api/clear_space', methods=['GET'])
def delete_data():  # ?password=29AF622358&id=43
    try:
        os.rmdir("graphs")
        return jsonify({'SUCCESS': 'Data has been added!'})
    except Exception:
        return jsonify({'ERROR': 'Error occurred when deleting files'})
