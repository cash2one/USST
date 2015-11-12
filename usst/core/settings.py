# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 lao605
# Licensed under The MIT License (MIT)
# http://opensource.org/licenses/MIT
#

import os
import json

# TODO: auto_discover

from usst.apps.douyu.setting import setting as douyu_setting
from usst.apps.panda.setting import setting as panda_setting
from usst.apps.zhanqi.setting import setting as zhanqi_setting
from usst.apps.longzhu.setting import setting as longzhu_setting

default_settings = {}

default_settings.update(douyu_setting)
default_settings.update(panda_setting)
default_settings.update(zhanqi_setting)
default_settings.update(longzhu_setting)


def read_file(file_path):
    data = {}
    if os.path.isfile(file_path):
        with open(file_path, 'r') as config_file:
            data = json.load(config_file)
    return data

# TODO: load setting from $HOME/.usst/config.json to override default setting
