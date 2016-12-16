# encoding: utf-8

from pocket.pocket import (
    redirect_to_pocket,
    get_request_token,
    request_token,
    get_access_token,
)

from flask import Flask, redirect
app = Flask(__name__)


from flaskext.mysql import MySQL
mysql = MySQL()
mysql.init_app(app)
cursor = mysql.get_db().cursor()


@app.route('/')
def index():
    return '<a href="/go/pocket">go to pocket</a>'


@app.route('/go/pocket')
def go_pocket():
    get_request_token()
    return redirect(redirect_to_pocket())


@app.route("/home")
def home():
    content = get_access_token()
    return content

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
