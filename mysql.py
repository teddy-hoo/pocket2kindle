# coding: utf-8

from flaskext.mysql import MySQL


class MySQLClient(object):

    _cursor = None
    _app = None

    @classmethod
    def set_app(cls, app):
        cls._app = app

    @classmethod
    def cursor(cls):
        if cls._cursor:
            return cls._cursor
        mysql = MySQL()
        mysql.init_app(cls._app)
        cls._cursor = mysql.get_db().cursor()
        return cls._cursor

    @classmethod
    def execute(cls, statement):
        pass
