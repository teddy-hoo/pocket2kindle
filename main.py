# encoding: utf-8


from app import app
from mysql import MySQLClient
MySQLClient.set_app(app)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
