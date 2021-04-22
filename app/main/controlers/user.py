from app.main import api

@api.route('/signup', methods=['POST'])
def signup():
    conn = HTTPConnector('%s/character' % base_url, None, headers, 'GET')
    chars = conn.trigger_request()
    # print(chars.text)
    return chars.text

@api.route('/login', methods=['POST'])
def login():
    conn = HTTPConnector('%s/character' % base_url, None, headers, 'GET')
    chars = conn.trigger_request()
    # print(chars.text)
    return chars.text