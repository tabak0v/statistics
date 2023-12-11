import flask
from flask import jsonify, request
import pandas as pd
import os


blueprint = flask.Blueprint(
    'api',
    __name__,
    template_folder='templates'
)


def check_school(school):
    if school == "ГБОУ Школа №57":
        return 1
    elif school == "ГБОУ Школа №179":
        return 2
    elif school == "ГБОУ Лицей Вторая школа":
        return 3
    elif school == "Школа ЦПМ":
        return 4
    elif school == 'Школа "Летово"':
        return 5
    elif school == 'ГБОУ Школа №2007':
        return 6
    else:
        return 7


def check_room(room):
    if room == "Идеально чисто":
        return 1
    elif room == "Достаточно чисто":
        return 2
    elif room == "Не очень чисто":
        return 3
    else:
        return 4


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
        data = pd.read_csv('/home/stat57ya24/mysite/data.csv', delimiter=',')
        data["school"] = data["school"].apply(lambda x: check_school(x))
        data["sex"] = data["sex"].apply(lambda x: 'male' if x == "Мужской" else "female")
        data["room_type"] = data["room_type"].apply(lambda x: check_room(x))
        data["cleaner"] = data["cleaner"].apply(lambda x: "me" if x == "Сами убираете комнату" else "other")
        data["residents"] = data["residents"].apply(lambda x: "1" if x == "Живу в комнате один/одна" else "1+")
        data["grade"] = data["grade"].apply(lambda x: int(x[:-5]))
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
