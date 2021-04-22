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

    @classmethod
    def get_characters_from_user(cls, user_id):
        return FavouriteCharacter.query.filter_by(user_id = user_id).all()

class FavouriteQuotes(db.Model, DBMixin):
    __tablename__ = 'favourite_quotes'
    quote_id = db.Column(db.String(120), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 
    character_id = db.Column(db.Integer, db.ForeignKey('favourite_character.id'), nullable=False, default=1)  
    character = db.relationship('FavouriteCharacter')
    dialog = db.Column(db.String(255))
    user = db.relationship('User')
    
    @classmethod
    def get_quotes_from_user(cls, user_id):
        return FavouriteQuotes.query.filter_by(user_id = user_id).all()

