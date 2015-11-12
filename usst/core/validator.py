# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 lao605
# Licensed under The MIT License (MIT)
# http://opensource.org/licenses/MIT
#


class Validator(object):
    def __init__(self, setting):
        self.setting = setting

    def check_platform(self, platform):
        return platform in self.setting

    def check_game(self, platform, game):
        if self.check_platform(platform):
            return game in self.setting[platform]["games"]
        else:
            return False

    def check_streamer(self, platform, game, streamer):
        if self.check_game(platform, game):
            return streamer in self.setting[platform]["games"][game]["subscription"]
        else:
            return False
