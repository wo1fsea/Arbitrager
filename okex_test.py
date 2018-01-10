# -*- coding: utf-8 -*-
# author: 半熟的韭菜

from websocket import create_connection
import gzip
import json
import time

if __name__ == '__main__':
    while (1):
        try:
            ws = create_connection("wss://real.okex.com:10441/websocket")
            break
        except:
            print('connect ws error,retry...')
            time.sleep(5)

    # 订阅 KLine 数据
    # tradeStr = """{"sub": "market.ethusdt.kline.1min","id": "id10"}"""

    # 请求 KLine 数据
    # tradeStr="""{"req": "market.ethusdt.kline.1min","id": "id10", "from": 1513391453, "to": 1513392453}"""

    # 订阅 Market Depth 数据
    # tradeStr="""{"sub": "market.ethusdt.depth.step5", "id": "id10"}"""

    # 请求 Market Depth 数据
    # tradeStr="""{"req": "market.ethusdt.depth.step5", "id": "id10"}"""

    # 订阅 Trade Detail 数据
    tradeStr = """{'event':'addChannel','channel':'ok_sub_spot_btc_usdt_depth_5'}"""

    # 请求 Trade Detail 数据
    # tradeStr="""{"req": "market.ethusdt.trade.detail", "id": "id10"}"""

    # 请求 Market Detail 数据
    # tradeStr="""{"req": "market.ethusdt.detail", "id": "id12"}"""

    ws.send(tradeStr)
    while (1):
        compressData = ws.recv()
        # ws.send(""""{'event': 'ping'}""")
        # result = gzip.decompress(compressData).decode('utf-8')
        result = json.loads(compressData)
        if isinstance(result, list):
            for r in result:
                asks = r.get("data", {}).get("asks")
                bids = r.get("data", {}).get("bids")
                if asks:
                    print("a", sorted(asks, key=lambda x: x[0])[0][0], "b", sorted(bids, key=lambda x: x[0], reverse=True)[0][0])
        # if result[:7] == '{"ping"':
        #     ts = result[8:21]
        #     pong = '{"pong":' + ts + '}'
        #     ws.send(pong)
        #     ws.send(tradeStr)
        # else:
        #     print(result)
