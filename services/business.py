from flask_sqlalchemy import SQLAlchemy
from flask import jsonify


from models import db, User
from .serializers import ListSerializer
from .base.responses import simple_json_data_response, \
                            simple_json_status_response


def get_all_users() -> jsonify:
    """Получить все данные о пользователях

    Returns:
        jsonify: jsonify-ответ с полученными данными
    """
    result = User.query.all()
    return simple_json_data_response(body=ListSerializer(result).data)


def add_new_user_in_db(*, user_data: dict, db: SQLAlchemy) -> None:
    """Добавляет пользователя в базу данных

    Args:
        user_data (dict): Данные о пользователе, представленные в словаре
        db (SQLAlchemy): Объект базы данных
    """ 
    user = User(**user_data)
    db.session.add(user)
    db.session.commit()
    
    
def get_user_by_id(id: int) -> jsonify:
    """Получить данные о пользователе по идентификатору

    Args:
        id (int): Идентификатор пользователя

    Returns:
        jsonify: Ответ на запрос
    """
    user = User.query.filter_by(id=id).first()
    return simple_json_data_response(body=user.serialize)