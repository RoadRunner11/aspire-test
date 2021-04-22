from app.main import api
from app.main.helpers.utility import res
from app.main.service import HTTPConnector
from flask import jsonify
from app.main.models import FavouriteQuotes, FavouriteCharacter
from app.main.decorators.auth import token_required
import os

access_token = os.environ.get("ACCESS_TOKEN", "xxxxxx")
base_url = 'https://the-one-api.dev/v2'
headers = {'Authorization': 'Bearer %s' % access_token}

@api.route('/characters/<string:char_id>/favourites', methods=['POST'])
def favourite_characters(char_id):
    
    item = FavouriteCharacter.query.get(_id = char_id)
    if item:
        return Responses.FAVOURITE_CHARACTER_EXISTS()
    conn = HTTPConnector('%s/character/%s' % (base_url, char_id), None, headers, 'GET')
    chars = conn.trigger_request()
    result = chars.json()['docs'][0]
    item = FavouriteCharacter()
    error = item.update(result)
    if len(error) > 0:
        return Responses.OPERATION_FAILED()
    # print(chars.text)
    return Responses.SUCCESS()

@api.route('/characters/<string:char_id>/quotes/<string:quo_id>/favourites', methods=['POST'])
def favourite_quotes(char_id, quo_id):
    conn = HTTPConnector('%s/character/%s/quote/%s' % (base_url, char_id, quo_id), None, headers, 'GET')
    chars = conn.trigger_request()
    # print(chars.text)
    return res(chars.text)

@api.route('/favourites', methods=['GET'])
@token_required
def favourites(current_user):

    chars = FavouriteCharacter.query.get(user_id=current_user.id)
    quotes = FavouriteQuotes.query.get(user_id=current_user.id)
    response = {
        'characters': chars.as_dict(),
        'quotes': quotes.as_dict()
    }
    # print(chars.text)
    return res(response)