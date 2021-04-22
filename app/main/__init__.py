
from flask import Blueprint
from flask import request
import flask
# from .main.controller.payment_controller import api as payment_ns

api = Blueprint('api', __name__)

from app import heartbeat
from app.main.controlers import external

@api.after_request
def after_request(response):
    """
    after_request contains actions after request
    
    Args:
        response ([type]): [description]
    
    Returns:
        [type]: [description]
    """    

    request_origin = request.environ.get('HTTP_ORIGIN', "http://localhost:5000")
    # print(request_origin)
    # print(flask.current_app.config['ALLOW_ORIGIN'])
    if request_origin in flask.current_app.config['ALLOW_ORIGIN']:
        # print("hello")
        header = response.headers
        header['Access-Control-Allow-Origin'] = request_origin
        header['Access-Control-Allow-Credentials'] = 'true'
        header['Access-Control-Allow-Headers'] = 'content-type'
        header['Access-Control-Allow-Methods']='GET, PUT, POST, DELETE, HEAD'
    
    return response
