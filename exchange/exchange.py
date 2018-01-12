# -*- coding: utf-8 -*-
"""----------------------------------------------------------------------------
Author:
    Huang Quanyong (wo1fSea)
    quanyongh@foxmail.com
Date:
    2018/1/12
Description:
    exchange.py
----------------------------------------------------------------------------"""

from utils.singleton import Singleton

SYMBOL_BTC_USDT = "SYMBOL_BTC_USDT"
SYMBOL_LTC_ETH = "SYMBOL_LTC_ETH"
SYMBOL_OMG_ETH = "SYMBOL_OMG_ETH"


class Exchange(Singleton):
    _SYMBOL_MAP = {
    }

    def __init__(self):
        pass

    def get_kline(self, symbol, period, size):
        raise NotImplementedError()

    def get_ticker(self, symbol):
        """
        {"bid": 0.0, "ask": 0.0, "low": 0.0, "high": 0.0, "last": 0.0, "vol": 0.0}
        :param symbol:
        :return: tick
        """
        raise NotImplementedError()

    def get_depth(self, symbol):
        """
        {"bids": [], "asks": []}
        :param symbol:
        :return:
        """
        raise NotImplementedError

    def get_trades(self, symbol):
        raise NotImplementedError()

    def get_user_balance(self):
        raise NotImplementedError()

    def trade(self, symbol, trace_type, price, amount):
        raise NotImplementedError()

    def cancel_order(self, symbol, order_id):
        raise NotImplementedError()

    def get_order_info(self, symbol, order_id):
        raise NotImplementedError()

    def _convert_symbol(self, symbol):
        return self._SYMBOL_MAP[symbol]
