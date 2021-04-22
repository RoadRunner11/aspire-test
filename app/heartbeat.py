from app.main import api

@api.route('/beat')
def heartbeat():
    return "I am still alive"

@api.route('/')
def home():
    return 'Hello'