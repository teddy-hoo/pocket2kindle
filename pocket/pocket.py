# encoding: utf-8

import requests

from config import (
    customer_key,
    request_token_url,
    redirect_uri,
    pocket_url,
    authorize_url,
)


request_token = None
access_token = None


def get_request_token():
    global request_token
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'charset': 'UTF-8',
        'X-Accept': 'application/x-www-form-urlencoded',
    }
    data = {
        'consumer_key': customer_key,
        'redirect_uri': redirect_uri,
    }
    response = requests.post(
        request_token_url,
        headers=headers,
        data=data,
    )

    if response.content:
        request_token = response.content.split('=')[1]

    raise Exception('get token error!')


def redirect_to_pocket():
    url = pocket_url + '?'
    url += 'request_token=' + str(request_token)
    url += 'redirect_uri=' + redirect_uri
    return url


def get_access_token():
    global access_token
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'charset': 'UTF-8',
        'X-Accept': 'application/x-www-form-urlencoded',
    }
    data = {
        'consumer_key': customer_key,
        'request_token': request_token,
    }

    response = requests.post(
        authorize_url,
        headers=headers,
        data=data,
    )

    print response.content
    return response.content
