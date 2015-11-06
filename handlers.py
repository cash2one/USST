# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 lao605
# Licensed under The MIT License (MIT)
# http://opensource.org/licenses/MIT
#

from tornado.web import RequestHandler
from helpers import (check_game,
                     check_platform,
                     check_streamer)


class StreamerHandler(RequestHandler):
    def __init__(self, application, request, **kwargs):
        pass

    def get(self, platform, game, streamer):
        # TODO: This fetches information of a streamer of a games of a platform.
        '''
        1. Check streamer
        '''


class GameHandler(StreamerHandler):
    def __init__(self, application, request, **kwargs):
        super(GameHandler, self).__init__(application, request, **kwargs)

    def get(self, platform, game):
        # TODO: This fetches all information of all streamer of a games of a platform.
        '''
        1. Check game
        2. Call StreamerHandler
        '''


class PlatformHandler(GameHandler):
    def __init__(self, application, request, **kwargs):
        super(PlatformHandler, self).__init__(application, request, **kwargs)

    def get(self, platform):
        # TODO: This fetches all information of all streamers of all games of a platform.
        '''
        1. Check platform
        2. Call GameHandlers.
        '''
        pass

