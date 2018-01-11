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
from .utils_okex import *


class ExchangeOKEX(Exchange):
    def __init__(self, args):
        super(ExchangeOKEX, self).__init__()
        self.__url = 'www.okex.com'
        self.__apikey = ''
        self.__secretkey = ''

    def get_kline(self, symbol, period, size):
        raise NotImplementedError()

    def get_ticker(self, symbol):
        TICKER_RESOURCE = "/api/v1/ticker.do"
        params = ''
        if symbol:
            params = 'symbol=%(symbol)s' % {'symbol': symbol}
        return http_get(self.__url, TICKER_RESOURCE, params)

    def get_depth(self, symbol):
        DEPTH_RESOURCE = "/api/v1/depth.do"
        params = ''
        if symbol:
            params = 'symbol=%(symbol)s' % {'symbol': symbol}
        return http_get(self.__url, DEPTH_RESOURCE, params)

    def get_trades(self, symbol):
        TRADES_RESOURCE = "/api/v1/trades.do"
        params = ''
        if symbol:
            params = 'symbol=%(symbol)s' % {'symbol': symbol}
        return http_get(self.__url, TRADES_RESOURCE, params)

    def get_user_balance(self):
        USERINFO_RESOURCE = "/api/v1/userinfo.do"
        params = {}
        params['api_key'] = self.__apikey
        params['sign'] = sign(params, self.__secretkey)
        return http_post(self.__url, USERINFO_RESOURCE, params)

    def trade(self, symbol, trace_type, price, amount):
        TRADE_RESOURCE = "/api/v1/trade.do"
        params = {
            'api_key': self.__apikey,
            'symbol': symbol,
            'type': trace_type
        }
        if price:
            params['price'] = price
        if amount:
            params['amount'] = amount

        params['sign'] = sign(params, self.__secretkey)
        return http_post(self.__url, TRADE_RESOURCE, params)

    def cancel_order(self, symbol, order_id):
        CANCEL_ORDER_RESOURCE = "/api/v1/cancel_order.do"
        params = {
            'api_key': self.__apikey,
            'symbol': symbol,
            'order_id': order_id
        }
        params['sign'] = sign(params, self.__secretkey)
        return http_post(self.__url, CANCEL_ORDER_RESOURCE, params)

    def get_order_info(self, symbol, order_id):
        ORDER_INFO_RESOURCE = "/api/v1/order_info.do"
        params = {
            'api_key': self.__apikey,
            'symbol': symbol,
            'order_id': order_id
        }
        params['sign'] = sign(params, self.__secretkey)
        return http_post(self.__url, ORDER_INFO_RESOURCE, params)
