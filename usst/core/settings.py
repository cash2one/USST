# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 lao605
# Licensed under The MIT License (MIT)
# http://opensource.org/licenses/MIT
#

# TODO: auto_discover

from usst.apps.douyu.setting import setting as douyu_setting
from usst.apps.panda.setting import setting as panda_setting
from usst.apps.zhanqi.setting import setting as zhanqi_setting
from usst.apps.longzhu.setting import setting as longzhu_setting

USST = {}

USST.update(douyu_setting)
USST.update(panda_setting)
USST.update(zhanqi_setting)
USST.update(longzhu_setting)

# TODO: load setting from $HOME/.usst/config.json to override default setting
