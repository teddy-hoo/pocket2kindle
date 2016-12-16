# encoding: utf-8

from mysql import MySQLClient
import time


SQL_CREATE_USER_BY_RANDOM_KEY = 'INSERT '
SQL_SELECT_USER_BY_RANDOM_KEY = 'S'


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
    def create_user_by_random_key(cls, random_key):
        created_time = int(time.time())
        statement = SQL_CREATE_USER_BY_RANDOM_KEY %(random_key, created_time)
        MySQLClient.execute(statement)

    @classmethod
    def get_user_by_random_key(cls, random_key):
        statement = SQL_SELECT_USER_BY_RANDOM_KEY % random_key
        return MySQLClient.execute(statement)
