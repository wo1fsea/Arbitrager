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

from exchange.exchange import SYMBOL_BTC_USDT, SYMBOL_LTC_ETH, SYMBOL_OMG_ETH
from exchange.exchange_huobi.exchange_huobi import ExchangeHuobi
from exchange.exchange_okex.exchange_okex import ExchangeOKEX

okex = ExchangeOKEX()
huobi = ExchangeHuobi()


def find_spread(asks, bids):
    if not asks or not bids:
        return None

    asks = sorted(asks, key=lambda x: x[0])
    bids = sorted(bids, key=lambda x: x[0], reverse=True)

    buy = asks[0][0]
    sell = bids[0][0]

    if buy < sell:# and (sell - buy) / sell > 0.003:
        return {"buy": buy, "sell": sell, "amount": min(asks[0][1], bids[0][1]) * sell, "profit %": (sell - buy) / sell * 100}
    else:
        return None


while True:
    try:
        huobi_depth = huobi.get_depth(SYMBOL_OMG_ETH)
        okex_depth = okex.get_depth(SYMBOL_OMG_ETH)
    except Exception as ex:
        print(ex)
        huobi_depth = {}
        okex_depth = {}

    spread0 = find_spread(huobi_depth.get("asks"), okex_depth.get("bids"))
    spread1 = find_spread(okex_depth.get("asks"), huobi_depth.get("bids"))

    if spread0:
        print("buy from huobi")
        print(spread0)

    if spread1:
        print("buy from okex")
        print(spread1)
