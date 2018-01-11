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

from Arbitrager.utils.singleton import Singleton


class Exchange(Singleton):
    def __init__(self):
        pass

    def get_kline(self, symbol, period, size):
        raise NotImplementedError()

    def get_ticker(self, symbol):
        raise NotImplementedError()

    def get_depth(self, symbol):
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
