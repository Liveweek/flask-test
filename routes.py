from flask import jsonify, Flask
from flask.globals import request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite3'


from models import User, db
from services.base.responses import simple_json_status_response
from services.business import *


@app.route('/user', methods=['GET', 'POST'])
def add_read_user():
    if request.method == 'GET':
        return get_all_users()
    else:
        add_new_user_in_db(user_data=request.args, db=db)
        return simple_json_status_response()
    

@app.route('/user/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def detail_user(id):
    #TODO: Добавить методы для обновления и удаления пользователей
    
    if request.method == 'GET':
        return get_user_by_id(id)
    elif request.method == 'PUT':
        pass
    else:
        pass