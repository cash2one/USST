# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 lao605
# Licensed under The MIT License (MIT)
# http://opensource.org/licenses/MIT
#

'''
Handlers call Worker class coroutines.
'''

import json

from tornado.web import RequestHandler
from usst.core.validator import Validator
from usst.core.worker import Worker


# handlers independent of setting
class BaseHandler(RequestHandler):
    def initialize(self, setting):
        self.setting = setting
        self.validator = Validator(self.setting)
        self.worker = Worker(self.setting)


class StreamerHandler(BaseHandler):
    async def get(self, platform, game, streamer):
        '''
        1. Check streamer
        '''
        self.validator.check_streamer(platform, game, streamer)
        response = await self.worker.streamer_call(platform, game, streamer)
        self.write(json.dumps(response))
        self.finish()


class GameHandler(BaseHandler):
    async def get(self, platform, game):
        '''
        1. Check game
        2. Call StreamerHandler
        '''
        self.validator.check_game(platform, game)
        response = await self.worker.game_call(platform, game)
        self.write(json.dumps(response))
        self.finish()


class PlatformHandler(BaseHandler):
    async def get(self, platform):
        '''
        1. Check platform
        2. Call GameHandlers
        '''
        self.validator.check_platform(platform)
        response = await self.worker.platform_call(platform)
        self.write(json.dumps(response))
        self.finish()


class AllSubHandler(BaseHandler):
    async def get(self):
        '''
        Delegate request to Handlers of different platforms.
        '''
        response = await self.worker.allSub_call()
        self.write(json.dumps(response))
        self.finish()
