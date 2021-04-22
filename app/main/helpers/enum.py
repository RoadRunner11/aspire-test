from app.main.helpers.utility import res


class Messages:
    AUTHENTICATION_FAILED = 'Authentication failed, please try again'
    AUTHORISATION_FAILED = 'You do not have the required permission'
    NOT_ENOUGH_INFO = 'Information you provided is not accurate'
    NOT_EXIST = 'Record not found'
    OBJECT_EXIST = 'Object exists'
    SUCCESS = 'Operation Success'
    OPERATION_FAILED = 'Operation Failed'
    FAVOURITE_QUOTE_EXISTS = 'Quote name already in favourite'
    FAVOURITE_CHARACTER_EXISTS = 'Character name already in favourite'
    NEEDED_FIELD_EMPTY = 'One or more needed values empty'
    EMAIL_EXIST = 'Email already in use'
    EMAIL_EMPTY = 'Email can not be empty'
    TOKEN_EXPIRED = 'Token has expired'
    UNCONFIRMED_USER = 'Unconfirmed User'
    BLACKLISTED = 'User Blacklisted and account disabled'


class Roles:
    MEMBER = 'member'
    ADMIN = 'admin'


class Responses:
    @staticmethod
    def NOT_EXIST():
        return res('', Messages.NOT_EXIST, 404)

    @staticmethod
    def SUCCESS():
        return res(Messages.SUCCESS)

    @staticmethod
    def OBJECT_EXIST(err=Messages.OBJECT_EXIST):
        return res('', err, 409)

    @staticmethod
    def OPERATION_FAILED(err=Messages.OPERATION_FAILED):
        return res('', err, 400)

    @staticmethod
    def AUTHENTICATION_FAILED():
       return res('', Messages.AUTHENTICATION_FAILED, 401)
    
    @staticmethod
    def AUTHORISATION_FAILED():
        return res('', Messages.AUTHORISATION_FAILED, 403)

    @staticmethod
    def NEEDED_FIELD_EMPTY():
        return res('', Messages.NEEDED_FIELD_EMPTY, 400)

    @staticmethod
    def FAVOURITE_CHARACTER_EXISTS():
        return res('', Messages.FAVOURITE_CHARACTER_EXISTS, 400)

    @staticmethod
    def FAVOURITE_QUOTE_EXISTS():
        return res('', Messages.FAVOURITE_QUOTE_EXISTS, 400)

    @staticmethod
    def TOKEN_EXPIRED():
        return res('', Messages.TOKEN_EXPIRED, 400)   
    
    @staticmethod
    def BLACKLISTED():
        return res('', Messages.BLACKLISTED, 400)
