from flask import jsonify, render_template, request
from models import Person
from flask import Flask
import pandas as pd
import seaborn as sns
import api
import matplotlib.pyplot as plt
import os

app = Flask(__name__)
app.register_blueprint(api.blueprint)
if __name__ == "__main__":
    app.run(debug=True)


@app.route('/', methods=['POST', 'GET'])
def show_graphs():
    if request.method == 'POST':
        try:
            graph_type = request.form.get('graph')
            param = request.form.get('param')
            pic = f'/static/assets/img/graph_{graph_type}_{param}.png'
        except Exception as err:
            return jsonify({'ERROR': err.__class__.__name__})
        return render_template('index.html', pic=pic, chosen_graph=graph_type, chosen_param=param)
    return render_template('index.html', pic=f'/static/assets/img/example.png')


@app.route('/view_data', methods=['GET'])
def show_data():
    try:
        df = pd.read_csv('data.csv', sep=',')  # /home/stat57ya24/mysite/
        data = []
        for row in df.itertuples():
            person = Person(*row[1:])
            data.append(person)
        print(data)
        return render_template('table.html', data=data)
    except Exception as err:
        return jsonify({'ERROR': err.__class__.__name__})


@app.route('/contact', methods=['GET'])
def see_contacts():
    try:
        return render_template('qandcontact.html')
    except Exception as err:
        return jsonify({'ERROR': err.__class__.__name__})
