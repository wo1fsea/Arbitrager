# -*- coding: utf-8 -*-
"""----------------------------------------------------------------------------
Author:
    Huang Quanyong (wo1fSea)
    quanyongh@foxmail.com
Date:
    2017/10/5
Description:
    config_reader.py
----------------------------------------------------------------------------"""

import os
import shutil
import json

from utils.singleton import Singleton

CONFIG_PATH = "./config/"
DEFAULT_FILE = "default.json"
CONFIG_FILE = "config.json"


class ConfigReader(Singleton):
    def __init__(self):
        self.config_data = {}

        config_path = os.path.join(CONFIG_PATH, CONFIG_FILE)
        default_path = os.path.join(CONFIG_PATH, DEFAULT_FILE)
        if not os.path.exists(config_path):
            assert os.path.exists(default_path), "default config file: %s not exists" % default_path
            shutil.copyfile(default_path, config_path)

        with open(config_path) as fp:
            self.config_data = json.load(fp)

    def get_config(self, key):
        return self.config_data.get(key, None)



