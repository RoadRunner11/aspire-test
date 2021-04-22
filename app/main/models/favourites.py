from app import db
from .db_mixin import DBMixin

class FavouriteCharacter(db.Model, DBMixin):
    __tablename__ = 'favourite_character'
    _id = db.Column(db.String(120), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  
    height = db.Column(db.String(255))
    race = db.Column(db.String(255))
    gender = db.Column(db.String(255))
    birth = db.Column(db.String(255))
    spouse = db.Column(db.String(255))
    death = db.Column(db.String(255))
    real = db.Column(db.String(255))
    hair = db.Column(db.String(255))
    name = db.Column(db.String(255))
    wikiurl = db.Column(db.String(255))

    user = db.relationship('User')

    not_updatable_columns = ['id']
    output_column = ['_id', 'height', 'race', 'gender', 'birth', 'spouse', 'death', 'real',
                    'hair', 'name', 'wikiurl']

    @classmethod
    def get_characters_from_user(cls, user_id):
        return FavouriteCharacter.query.filter_by(user_id = user_id).all()

class FavouriteQuotes(db.Model, DBMixin):
    __tablename__ = 'favourite_quotes'
    _id = db.Column(db.String(120), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 
    character = db.Column(db.String(255))
    dialog = db.Column(db.String(255))
    movie = db.Column(db.String(100))
    user = db.relationship('User')

    not_updatable_columns = ['id']
    output_column = ['_id', 'character', 'dialog', 'movie']
    
    @classmethod
    def get_quotes_from_user(cls, user_id):
        return FavouriteQuotes.query.filter_by(user_id = user_id).all()

