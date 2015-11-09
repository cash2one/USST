# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 lao605
# Licensed under The MIT License (MIT)
# http://opensource.org/licenses/MIT
#

from settings import USST


def check_platform(platform):
    return platform in USST

def check_game(platform, game):
    if check_platform():
        return game in USST[platform]["games"]
    else:
        return False

def check_streamer(platform, game, streamer):
    # Maybe the most important part of the app.
    if check_game(platform, game):
        return streamer in USST[platform]["games"][game]["subscription"]
    else:
        return False