from flask import request, Response
import json
from http import HTTPStatus
from __init__ import app, USERS
from models import Forms


@app.post('/forms/create')
def create_form():
    data = request.get_json()
    form_id = len(USERS)
    sex = data['sex']
    cleaner = data['cleaner']
    residents = data['residents']
    grade = data['grade']
    room_type = data['room_type']
    school = data['school']
    GPA = data['GPA']
    form = Forms(sex, cleaner, residents, grade, room_type, school, GPA)
    USERS.append(form)
    response = Response(
        json.dumps(
            {
                "form_id": form_id,
                "sex": form.sex,
                "cleaner": form.cleaner,
                "residents": form.residents,
                "grade": form.grade,
                "room_type": form.room_type
            }
        ),
        status=HTTPStatus.OK,
        mimetype="applicaction/json",
    )
    return response


@app.get('/form/<int:id>')
def get_form(form_id):
    form = USERS(form_id)
    response = Response(
        json.dumps(
            {
                "form_id": form_id,
                "sex": form.sex,
                "cleaner": form.cleaner,
                "residents": form.residents,
                "grade": form.grade,
                "room_type": form.room_type
            }
        ),
        status=HTTPStatus.OK,
        mimetype="applicaction/json",
    )
    return response
