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
from ..exchange import SYMBOL_BTC_USDT, SYMBOL_LTC_ETH, SYMBOL_OMG_ETH
from .utils_okex import *


class ExchangeOKEX(Exchange):
    _SYMBOL_MAP = {
        SYMBOL_BTC_USDT: "btc_usdt",
        SYMBOL_LTC_ETH: "ltc_eth",
        SYMBOL_OMG_ETH: "omg_eth"
    }

    def __init__(self, api_key="", secret_key=""):
        super(ExchangeOKEX, self).__init__()
        self.__url = 'www.okex.com'
        self.__apikey = api_key
        self.__secretkey = secret_key

    def get_kline(self, symbol, period, size):
        raise NotImplementedError()

    def get_ticker(self, symbol):
        symbol = self._convert_symbol(symbol)
        TICKER_RESOURCE = "/api/v1/ticker.do"
        params = ''
        if symbol:
            params = 'symbol=%(symbol)s' % {'symbol': symbol}
        return http_get(self.__url, TICKER_RESOURCE, params)

    def get_depth(self, symbol):
        symbol = self._convert_symbol(symbol)
        DEPTH_RESOURCE = "/api/v1/depth.do"
        params = ''
        if symbol:
            params = 'symbol=%(symbol)s' % {'symbol': symbol}
        data = http_get(self.__url, DEPTH_RESOURCE, params)
        return {"bids": data.get("bids", []), "asks": data.get("asks", [])}

    def get_trades(self, symbol):
        symbol = self._convert_symbol(symbol)
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
        symbol = self._convert_symbol(symbol)
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
        symbol = self._convert_symbol(symbol)
        CANCEL_ORDER_RESOURCE = "/api/v1/cancel_order.do"
        params = {
            'api_key': self.__apikey,
            'symbol': symbol,
            'order_id': order_id
        }
        params['sign'] = sign(params, self.__secretkey)
        return http_post(self.__url, CANCEL_ORDER_RESOURCE, params)

    def get_order_info(self, symbol, order_id):
        symbol = self._convert_symbol(symbol)
        ORDER_INFO_RESOURCE = "/api/v1/order_info.do"
        params = {
            'api_key': self.__apikey,
            'symbol': symbol,
            'order_id': order_id
        }
        params['sign'] = sign(params, self.__secretkey)
        return http_post(self.__url, ORDER_INFO_RESOURCE, params)
