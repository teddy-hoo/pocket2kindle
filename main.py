# encoding: utf-8

from pocket.pocket import (
    pocket_url,
    get_request_token,
    request_token,
    get_access_token,
)

from flask import Flask, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return '<a href="/go/pocket">go to pocket</a>'


@app.route('/go/pocket')
def go_pocket():
    get_request_token()
    redirect(pocket_url(request_token))


@app.route("/home")
def home():
    content = get_request_token()
    return content

if __name__ == "__main__":
    app.run(port=80)
