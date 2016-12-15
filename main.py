# encoding: utf-8

from pocket.pocket import (
    pocket_url,
    get_request_token,
)

from flask import Flask, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return '<a href="/go/pocket">go to pocket</a>'


@app.route('/go/pocket')
def go_pocket():
    request_token = get_request_token()
    redirect(pocket_url(request_token))


@app.route("/home")
def home():
    return "Hello World!"

if __name__ == "__main__":
    app.run(port=80)
