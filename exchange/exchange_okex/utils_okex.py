# -*- coding: utf-8 -*-
"""----------------------------------------------------------------------------
Author:
    Huang Quanyong (wo1fSea)
    quanyongh@foxmail.com
Date:
    2018/1/11
Description:
    exchange_okex.py
----------------------------------------------------------------------------"""

import http.client
import urllib
import json
import hashlib
import time


def sign(params, secretKey):
    sign = ''
    for key in sorted(params.keys()):
        sign += key + '=' + str(params[key]) + '&'
    data = sign + 'secret_key=' + secretKey
    return hashlib.md5(data.encode("utf8")).hexdigest().upper()


def http_get(url, resource, params=''):
    conn = http.client.HTTPSConnection(url, timeout=10)
    conn.request("GET", resource + '?' + params)
    response = conn.getresponse()
    data = response.read().decode('utf-8')
    return json.loads(data)


def http_post(url, resource, params):
    headers = {
        "Content-type": "application/x-www-form-urlencoded",
    }
    conn = http.client.HTTPSConnection(url, timeout=10)
    temp_params = urllib.parse.urlencode(params)
    conn.request("POST", resource, temp_params, headers)
    response = conn.getresponse()
    data = response.read().decode('utf-8')
    params.clear()
    conn.close()
    return data
