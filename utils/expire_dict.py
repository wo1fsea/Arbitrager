# -*- coding: utf-8 -*-
"""----------------------------------------------------------------------------
Author:
    Huang Quanyong (wo1fSea)
    quanyongh@foxmail.com
Date:
    2017/11/8
Description:
    expire_dict.py
----------------------------------------------------------------------------"""

import time
from collections import UserDict


class ExpireDict(UserDict):
    def __init__(self, expire_time):
        super(ExpireDict, self).__init__()
        self._expire_time = expire_time

    def _renew_data(self):
        cur_time = time.time()
        self.data = dict(filter(lambda x: x[1][1] > cur_time, self.data.items()))

    def __len__(self):
        self._renew_data()
        return len(self.data)

    def __getitem__(self, key):
        item, expire_time = self.data.get(key, (None, -1))

        if expire_time > time.time():
            return item
        elif expire_time != -1:
            del self.data[key]

        raise KeyError(key)

    def __setitem__(self, key, item):
        self.data[key] = (item, time.time() + self._expire_time)

    def __contains__(self, key):
        self._renew_data()
        return key in self.data

    def __repr__(self):
        self._renew_data()
        return repr(self.data)

    def copy(self):
        if self.__class__ is UserDict:
            return UserDict(self.data.copy())
        import copy
        data = self.data
        try:
            self.data = {}
            c = copy.copy(self)
        finally:
            self.data = data
        c.update(self)
        return c
