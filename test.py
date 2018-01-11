# -*- coding: utf-8 -*-
"""----------------------------------------------------------------------------
Author:
    Huang Quanyong (wo1fSea)
    quanyongh@foxmail.com
Date:
    2018/1/12
Description:
    test.py
----------------------------------------------------------------------------"""

from exchange.exchange_huobi.exchange_huobi import ExchangeHuobi
from exchange.exchange_okex.exchange_okex import ExchangeOKEX


okex = ExchangeOKEX("")
huobi = ExchangeHuobi("")
print(huobi.get_depth("btcusdt"))
print(okex.get_depth("btc_usdt"))
