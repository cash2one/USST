# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 lao605
# Licensed under The MIT License (MIT)
# http://opensource.org/licenses/MIT
#

import json
import os
from . import __PLATFORM__
from .strategy import ZhanqiStrategy

setting_path = os.path.join(os.path.dirname(__file__), "setting.json")

with open(setting_path, "r") as f:
    setting = json.load(f)
    setting[__PLATFORM__]["strategy"] = ZhanqiStrategy
