from re import L
from typing import Union
from flask import jsonify


def simple_json_data_response(message: str='Request has been completed successfully',
                              code: int= 0, *,
                              body: Union[list, dict] = []) -> jsonify:
    """Простой json-ответ на get-запрос

    Args:
        message (str, optional): Сообщение ответа. Defaults to 'Request has been completed successfully'.
        code (int, optional): Код ответа веб-сервиса. Defaults to 0.
        body (Union[list, dict], optional): Тело данных запроса, результат обработки данных. Defaults to [].

    Returns:
        jsonify: jsonify-ответ на основании аргументов данных
    """
    return jsonify({
        'answer': message,
        'code' : code,
        'result' : body
    })
    
    
def simple_json_status_response(status: str='Success!',
                                code: int= 0) -> jsonify:
    """Просто json-ответ о статусе выполненного запроса

    Args:
        status (str, optional): Описание статуса запроса. Defaults to 'Success!'.
        code (int, optional): Код ответа веб-сервиса. Defaults to 0.

    Returns:
        jsonify: jsonify-ответ на основании аргументов данных
    """
    return jsonify({
        'status': status,
        'code': code
    })