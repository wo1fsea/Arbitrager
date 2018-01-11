# -*- coding: utf-8 -*-
"""----------------------------------------------------------------------------
Author:
    Huang Quanyong (wo1fSea)
    quanyongh@foxmail.com
Date:
    2018/1/12
Description:
    exchange_okex.py
----------------------------------------------------------------------------"""

from ..exchange import Exchange
from .utils_huobi import *


class ExchangeHuobi(Exchange):
    def __init__(self, args):
        super(ExchangeHuobi, self).__init__()

    def get_kline(self, symbol, period, size):
        params = {'symbol': symbol,
                  'period': period,
                  'size': size}

        url = MARKET_URL + '/market/history/kline'
        return http_get_request(url, params)

    def get_ticker(self, symbol):
        params = {'symbol': symbol}

        url = MARKET_URL + '/market/detail/merged'
        return http_get_request(url, params)

    def get_depth(self, symbol):
        params = {'symbol': symbol,
                  'type': 'step0'}

        url = MARKET_URL + '/market/depth'
        return http_get_request(url, params)

    def get_trades(self, symbol):
        params = {'symbol': symbol}

        url = MARKET_URL + '/market/trade'
        return http_get_request(url, params)

    def get_accounts(self):
        path = "/v1/account/accounts"
        params = {}
        return api_key_get(params, path)

    def get_user_balance(self):
        accounts = self.get_accounts()
        acct_id = accounts['data'][0]['id']

        url = "/v1/account/accounts/{0}/balance".format(acct_id)
        params = {"account-id": acct_id}
        return api_key_get(params, url)

    def trade(self, symbol, trace_type, price, amount):
        accounts = self.get_accounts()
        acct_id = accounts['data'][0]['id']

        params = {"account-id": acct_id,
                  "amount": amount,
                  "symbol": symbol,
                  "type": trace_type,
                  # "source": source
                  }
        if price:
            params["price"] = price

        url = '/v1/order/orders/place'
        return api_key_post(params, url)

    def cancel_order(self, symbol, order_id):
        params = {}
        url = "/v1/order/orders/{0}/submitcancel".format(order_id)
        return api_key_post(params, url)

    def get_order_info(self, symbol, order_id):
        params = {}
        url = "/v1/order/orders/{0}".format(order_id)
        return api_key_get(params, url)
