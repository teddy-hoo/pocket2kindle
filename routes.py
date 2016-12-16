# encoding: utf-8

from service.pocket import (
    redirect_to_pocket,
    get_request_token,
    get_access_token,
)
from app import app
from flask import (
    redirect,
    render_template,
    request,
    make_response,
)
from logic.user import User


@app.route('/')
def index():
    random_key = request.cookies.get('random_key', None)
    if User.is_authenticated(random_key):
        redirect('/home')
    random_key = User.new_user()
    resp = make_response(render_template('index.html'))
    resp.set_cookie('random_key', random_key)
    return resp


@app.route('/go/pocket')
def go_pocket():
    get_request_token()
    return redirect(redirect_to_pocket())


@app.route("/home")
def home():
    content = get_access_token()
    return content