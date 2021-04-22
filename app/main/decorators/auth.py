from app.main.models import User
from flask import abort, has_request_context
from app.main.helpers.enum import Messages, Roles, Responses
from app.main.helpers.utility import res
from functools import wraps
from flask import jsonify, request

def token_required(f):
   @wraps(f)
   def decorator(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization']

        if not token:
            return jsonify({'message': 'a valid token is missing'})

        try:
            current_user = User.query.filter_by(token=token).first()
        except:
            return jsonify({'message': 'token is invalid'})

        return f(current_user, *args, **kwargs)
   return decorator