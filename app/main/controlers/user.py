from app.main import api
from app.main.helpers.enum import Messages, Responses
from app.main.helpers.utility import res
from app.main.models import User
from flask import request

@api.route('/signup', methods=['POST'])
def register_user():
    json_dict = request.json
    print(json_dict)
    user = User()
    user.update_from_dict(json_dict, ['id'])
    existing_user = User.get_user_by_email(json_dict['email'])
    if existing_user:
       return Responses.OBJECT_EXIST()
    error = user.update()
    if len(error) > 0:
        return Responses.OPERATION_FAILED()
    return res(user.as_dict())

@api.route('/login', methods=['POST'])
def request_token():
    """
    request_token takes in email and password, returns the authentication token 

    Returns:
        [type]: [description]
    """
    if request.json is None:
        return Responses.OPERATION_FAILED()
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    user = User.authenticate(email, password)

    if user:
        token = user.token
        return res({'token':token})
    return Responses.AUTHENTICATION_FAILED()
