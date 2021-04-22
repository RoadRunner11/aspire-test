
from app.main import api
from app.main.helpers.utility import res
from app.main.service import HTTPConnector
from app.main.helpers.enum import Responses
from flask import jsonify
import os

access_token = os.environ.get("ACCESS_TOKEN", "xxxxxx")
base_url = 'https://the-one-api.dev/v2'
headers = {'Authorization': 'Bearer %s' % access_token}

@api.route('/characters', methods=['GET'])
def characters():
    conn = HTTPConnector('%s/character' % base_url, None, headers, 'GET')
    resp = conn.trigger_request()
    if resp.status_code == 200:
        # print(chars.text)
        return resp.json()

    return Responses.OPERATION_FAILED()

@api.route('/characters/<string:char_id>/quotes', methods=['GET'])
def character_quotes(char_id):
    conn = HTTPConnector('%s/character/%s/quote' % (base_url, char_id), None, headers, 'GET')
    resp = conn.trigger_request()
    if resp.status_code == 200:
        # print(chars.text)
        return resp.json()

    return Responses.OPERATION_FAILED()