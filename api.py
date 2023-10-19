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
    if request.args.get('password') == '29AF622358':
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
            df = pd.DataFrame(data)
            df.to_csv('data.csv', mode='a')
            return jsonify({'SUCCESS': 'Data appended successfully!'})
        except Exception:
            return jsonify({'ERROR': 'Error occurred when adding data'})
    return jsonify({'ERROR': 'Wrong or invalid password'})


@blueprint.route('/api/delete_data', methods=['DELETE', 'GET'])
def delete_data():  # ?password=29AF622358&id=43
    if request.args.get('password') == '29AF622358':
        try:
            id = int(request.args.get('id'))
            df = pd.read_csv('data.csv', delimiter=',')
            df = df.drop([id])
            df.to_csv('data.csv')
            return jsonify({'SUCCESS': 'Data has been added!'})
        except Exception:
            return jsonify({'ERROR': 'Error occurred when deleting data'})
    return jsonify({'ERROR': 'Wrong or invalid password'})


@blueprint.route('/api/clear_space', methods=['GET'])
def delete_data():  # ?password=29AF622358&id=43
    if request.args.get('password') == '29AF622358':
        try:
            os.rmdir("graphs")
            return jsonify({'SUCCESS': 'Data has been added!'})
        except Exception:
            return jsonify({'ERROR': 'Error occurred when deleting files'})
    return jsonify({'ERROR': 'Wrong or invalid password'})
