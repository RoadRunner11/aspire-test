from app import db, bcrypt
from .db_mixin import DBMixin
import secrets

class User(db.Model, DBMixin):
    __tablename__ = 'user'
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255))
    token = db.Column(db.String(255))

    new_item_must_have_column=['email','password', 'username']
    not_updatable_columns = ['id']

    def __init__(self, email=' ', password=' '):
        '''
        __init__ initiates the user as well as hashing the password by using bcrypt

        Args:
            email (string): [description]
            password (string): [description]
        '''
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.generate_user_token()

    @classmethod
    def get_user_by_email(cls, email, page=None, per_page=None):
        filter_query = cls.email == email
        users = cls.get(filter_query, page, per_page)
        return users[0] if len(users) > 0 else None

    def generate_user_token(self):
        token = secrets.token_urlsafe(16)
        self.token = token
    
    # def update_salt(self):
    #     """
    #     update_salt refresh salt
    #     """
    #     self.salt = str(os.urandom(30)).replace('\\', '')
    
    def update_from_dict(self, obj_dict, not_updatable_columns=[]):
        """
        update_from_dict updates self by using dict

        Args:
            obj_dict (dict):
            not_updatable_columns (list, optional): columns that won't be updated

        Returns:
            [type]: [description]
        """
        not_updatable_columns = not_updatable_columns if len(
            not_updatable_columns) > 0 else self.not_updatable_columns
        flag = False
        if obj_dict:
            for key in obj_dict:
                if hasattr(self, key):
                    if key in not_updatable_columns:
                        continue
                    if key == 'password':
                        setattr(self, key, bcrypt.generate_password_hash(
                            obj_dict[key]))
                        # self.update_salt()
                    else:
                        setattr(self, key, obj_dict[key])
                    flag = True
        return flag

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
        if user and bcrypt.check_password_hash(user.password, password):
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