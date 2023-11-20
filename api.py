import flask
from flask import jsonify, request
import pandas as pd
import os


blueprint = flask.Blueprint(
    'api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/add_data', methods=['POST'])
def add_data():  # ?password=29AF622358&id=43
    try:
        rdata = request.json
        data = {
            'sex': rdata.get('sex'),
            'cleaner': rdata.get('cleaner'),
            'residents': rdata.get('residents'),
            'grade': rdata.get('grade'),
            'room_type': rdata.get('room_type'),
            'school': rdata.get('school'),
            'GPA': float(rdata.get('GPA').replace(",", "."))
        }
        df0 = pd.read_csv('/home/stat57ya24/mysite/data.csv', delimiter=',')
        df = pd.DataFrame(data, index=[df0.shape[0] + 1])
        df.to_csv('/home/stat57ya24/mysite/data.csv', mode='a', index=False, header=False)
        return jsonify({'SUCCESS': 'Data appended successfully!'})
    except Exception as err:
        return jsonify({'ERROR': err.__class__.__name__})


@blueprint.route('/api/delete_data', methods=['DELETE', 'GET'])
def delete_data():  # ?password=29AF622358&id=43
    try:
        id = int(request.args.get('id'))
        df = pd.read_csv('mysite/data.csv', delimiter=',')
        df = df.drop([id])
        df.to_csv('/home/stat57ya24/mysite/data.csv')
        return jsonify({'SUCCESS': 'Data has been added!'})
    except Exception as err:
        return jsonify({'ERROR': err.__class__.__name__})


@blueprint.route('/api/clear_space', methods=['GET'])
def delete_data():  # ?password=29AF622358&id=43
    try:
        os.rmdir("graphs")
        return jsonify({'SUCCESS': 'Data has been added!'})
    except Exception:
        return jsonify({'ERROR': 'Error occurred when deleting files'})
