# -*- coding: utf-8 -*-
"""----------------------------------------------------------------------------
Author:
    Huang Quanyong (wo1fSea)
    quanyongh@foxmail.com
Date:
    2017/10/5
Description:
    queue.py
----------------------------------------------------------------------------"""

from .redis_object import RedisObject, DEFAULT_PACKER

QUEUE_MAX_LENGTH = -1


class Queue(RedisObject):
    def __init__(self, key, packer=DEFAULT_PACKER, max_len=QUEUE_MAX_LENGTH):
        super(Queue, self).__init__(key, packer)
        self.max_len = max_len

    def put(self, item):
        item = self.pack(item)
        self.redis.lpush(self.key, item)
        if self.max_len > 0:
            self.redis.ltrim(self.key, 0, self.max_len)

    def get(self):
        item = self.redis.rpop(self.key)
        item = self.unpack(item) if item else item
        return item

    def bget(self, timeout=0):
        b_items = self.redis.brpop(self.key, timeout)
        if not b_items:
            return None

        b_item = b_items[1]
        item = self.unpack(b_item) if b_item else b_item
        return item

    def clear(self):
        self.redis.delete(self.key)
