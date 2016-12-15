# encoding: utf-8

import requests

from config import (
    customer_key,
    request_token_url,
    redirect_uri,
    pocket_url,
)


def get_request_token():
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
        return response.content.split('=')[1]

    raise Exception('get token error!')


def redirect_to_pocket(request_token):
    url = pocket_url + '?'
    url += 'request_token=' + request_token
    url += 'redirect_uri=' + redirect_uri
    return url

if __name__ == '__main__':
    print get_request_token()
