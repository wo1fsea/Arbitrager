# -*- coding: utf-8 -*-
"""----------------------------------------------------------------------------
Author:
    Huang Quanyong (wo1fSea)
    quanyongh@foxmail.com
Date:
    2017/10/29
Description:
    redis_object.py
----------------------------------------------------------------------------"""

import time
from . import db_connection

import msgpack
import _pickle as pickle

_delta_time = None


class Packer(object):
    def pack(self, obj):
        raise NotImplementedError()

    def unpack(self, packed):
        raise NotImplementedError()


class NoPacker(object):
    def pack(self, obj):
        return obj

    def unpack(self, packed):
        return packed


class MsgPacker(Packer):
    def pack(self, obj):
        return msgpack.packb(obj)

    def unpack(self, packed):
        return msgpack.unpackb(packed, encoding='utf-8')


class PicklePacker(Packer):
    def pack(self, obj):
        return pickle.dumps(obj)

    def unpack(self, packed):
        return pickle.loads(packed)


DEFAULT_PACKER = PicklePacker


class RedisObject(object):
    Redis_Type = "none"

    def __init__(self, key, packer=DEFAULT_PACKER):
        self._key = key
        self._packer = packer()
        self.redis = db_connection.get_redis()

    def get_type(self):
        return self.redis.type(self._key).decode()

    def set_expire(self, milliseconds):
        self.redis.pexpire(self._key, milliseconds)

    @property
    def exists(self):
        return self.redis.exists(self._key)

    @property
    def time(self):
        global _delta_time
        if _delta_time is None:
            local_time = time.time()
            redis_time = float("%d.%d" % self.redis.time())
            _delta_time = redis_time - local_time
        return _delta_time + time.time()

    @property
    def key(self):
        return self._key

    def pack(self, obj):
        return self._packer.pack(obj)

    def unpack(self, packed):
        return self._packer.unpack(packed)
