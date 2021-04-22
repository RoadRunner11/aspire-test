from app.main import api
from app.main.helpers.utility import res
from app.main.service import HTTPConnector
from flask import jsonify
from app.main.helpers.enum import Messages, Responses
from app.main.models import FavouriteQuotes, FavouriteCharacter
from app.main.decorators.auth import token_required
import os

access_token = os.environ.get("ACCESS_TOKEN", "xxxxxx")
base_url = 'https://the-one-api.dev/v2'
headers = {'Authorization': 'Bearer %s' % access_token}

@api.route('/characters/<string:char_id>/favourites', methods=['POST'])
@token_required
def favourite_characters(current_user, char_id):
    
    item = FavouriteCharacter.query.filter_by(_id = char_id).first()
    if item:
        return Responses.FAVOURITE_CHARACTER_EXISTS()
    conn = HTTPConnector('%s/character/%s' % (base_url, char_id), None, headers, 'GET')
    resp = conn.trigger_request()
    if resp.status_code == 200:
        result = resp.json()['docs'][0]
        result.update({'user_id': current_user.id})
        print(result)
        item = FavouriteCharacter()
        error = item.update(result)
        if len(error) == 0:
            return Responses.SUCCESS()
    # print(chars.text)
    return Responses.OPERATION_FAILED()

@api.route('/characters/<string:char_id>/quotes/<string:quo_id>/favourites', methods=['POST'])
@token_required
def favourite_quotes(current_user, char_id, quo_id):
    item = FavouriteQuotes.query.filter_by(_id = quo_id).first()
    if item:
        return Responses.FAVOURITE_CHARACTER_EXISTS()
    quote_conn = HTTPConnector('%s/quote/%s' % (base_url, quo_id), None, headers, 'GET')
    quote_resp = quote_conn.trigger_request()
    if quote_resp.status_code == 200:
        if quote_resp.json()['docs']:
            quote_result = quote_resp.json()['docs'][0]
            if quote_result['character'] != char_id:
                return res({'message': 'character id does not match with the provided one'})
            quote_result.update({'user_id': current_user.id})
            quote_item = FavouriteQuotes()
            quote_error = quote_item.update(quote_result)
            print(quote_result)
            if len(quote_error) == 0:
                char_item = FavouriteCharacter.query.filter_by(_id = char_id).first()
                if not char_item:
                    char_conn = HTTPConnector('%s/character/%s' % (base_url, char_id), None, headers, 'GET')
                    char_resp = conn.trigger_request()
                    if char_resp.status_code == 200:
                        char_result = char_resp.json()['docs'][0]
                        char_result.update({'user_id': current_user.id})
                        char_item = FavouriteCharacter()
                        char_error = char_item.update(char_result)
                        if len(char_error) == 0:
                            return Responses.SUCCESS()
                return Responses.SUCCESS()
        else:
            return Responses.NOT_EXIST()

    # print(chars.text)
    return Responses.OPERATION_FAILED()

@api.route('/favourites', methods=['GET'])
@token_required
def favourites(current_user):
    chars = FavouriteCharacter.get_characters_from_user(current_user.id)
    quotes = FavouriteQuotes.get_quotes_from_user(current_user.id)
    response = {
        'characters': [item.as_dict() for item in chars],
        'quotes': [item.as_dict() for item in quotes]
    }
    # print(chars.text)
    return res(response)