# encoding: utf-8

import uuid
from model.user import User as UserModel


SQL_CREATE_USER_BY_UUID = 'INSERT '


class User(object):
    """
    schema
    id int
    created_time int
    updated_time int
    authenticate_time int
    uuid int unique
    access_token string
    user_name string
    """

    @classmethod
    def new_user(cls):
        random_key = uuid.uuid1()
        UserModel.create_user_by_random_key(random_key)
        return random_key

    @classmethod
    def is_authenticated(cls, random_key):
        user = UserModel.get_user_by_random_key(random_key)
        return True if user else False
