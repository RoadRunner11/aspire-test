from app import db
from .db_mixin import DBMixin

class User(db.Model, DBMixin):
    __tablename__ = 'user'
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255))

    def __init__(self, email=' ', password=' '):
        '''
        __init__ initiates the user as well as hashing the password by using bcrypt

        Args:
            email (string): [description]
            password (string): [description]
        '''
        self.email = email
        self.password = AC().bcrypt.generate_password_hash(password)
        self.update_salt()

    @classmethod
    def get_user_by_email(cls, email, page=None, per_page=None):
        filter_query = cls.email == email
        users = cls.get(filter_query, page, per_page)
        return users[0] if len(users) > 0 else None

    @staticmethod
    def generate_token_identity(email, salt=None):
        if not salt:
            user = User.get_user_by_email(email)
            salt = user.salt
            if not user:
                return None
        return email+"||token||"+salt

    @staticmethod
    def authenticate(email, password):
        """
        authenticate verifies user's password returns user object

        Args:
            email (string): [description]
            password (string): [description]

        Returns:
            User: user object
        """
        user = User.get_user_by_email(email)
        if user and AC().bcrypt.check_password_hash(user.password, password):
            return user
        return None
    
    @staticmethod
    def authorisation(email, permitted_roles):
        """
        authorisation verifies user's role without checking user's password

        Args:
            email (string): [description]
            permitted_roles ([string]): [description]

        Returns:
            boolean: does user have permission
        """
        if len(permitted_roles) <= 0:
            # allow all access as permitted roles are empty
            return True
        user = User.get_user_by_email(email)
        if user and user.role.name in permitted_roles:
            return True
        return False