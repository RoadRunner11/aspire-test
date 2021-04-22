
from app.main import api
from app.main.helpers.utility import res
from app.main.service import HTTPConnector
from flask import jsonify
import os

access_token = os.environ.get("ACCESS_TOKEN", "xxxxxx")
base_url = 'https://the-one-api.dev/v2'
headers = {'Authorization': 'Bearer %s' % access_token}

@api.route('/characters', methods=['GET'])
def characters():
    conn = HTTPConnector('%s/character' % base_url, None, headers, 'GET')
    chars = conn.trigger_request()
    # print(chars.text)
    return chars.json()

@api.route('/characters/<string:char_id>/quotes', methods=['GET'])
def character_quotes(char_id):
    conn = HTTPConnector('%s/character/%s' % (base_url, char_id), None, headers, 'GET')
    quotes = conn.trigger_request()
    # print(type(quotes.text))
    return quotes.json()