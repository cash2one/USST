# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 lao605
# Licensed under The MIT License (MIT)
# http://opensource.org/licenses/MIT
#

import json
from settings import USST
from tornado.web import RequestHandler
from helpers import (check_game,
                     check_platform,
                     check_streamer)


class StreamerHandler(RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(StreamerHandler, self).__init__(application, request, **kwargs)

    async def get(self, platform, game, streamer):
        # TODO: This fetches information of a streamer of a games of a platform.
        '''
        1. Check streamer
        '''
        check_streamer(platform, game, streamer)
        response = await streamer_call(platform, game, streamer)
        self.write(json.dumps(response))
        self.finish()


class GameHandler(StreamerHandler):
    def __init__(self, application, request, **kwargs):
        super(GameHandler, self).__init__(application, request, **kwargs)

    async def get(self, platform, game):
        # TODO: This fetches all information of all streamer of a games of a platform.
        '''
        1. Check game
        2. Call StreamerHandler
        '''
        check_game(platform, game)
        response = await game_call(platform, game)
        self.write(json.dumps(response))
        self.finish()

class PlatformHandler(GameHandler):
    def __init__(self, application, request, **kwargs):
        super(PlatformHandler, self).__init__(application, request, **kwargs)

    async def get(self, platform):
        # TODO: This fetches all information of all streamers of all games of a platform.
        '''
        1. Check platform
        2. Call GameHandlers
        '''
        check_platform(platform)
        response = await platform_call(platform)
        self.write(json.dumps(response))
        self.finish()


class AllSubHandler(PlatformHandler):
    def __init__(self, application, request, **kwargs):
        super(PlatformHandler, self).__init__(application, request, **kwargs)

    async def get(self):
        '''
        Delegate request to Handlers of different platforms.
        '''
        response = await allSub_call()
        self.write(json.dumps(response))
        self.finish()


async def streamer_call(platform, game, streamer):
    # strategy is platform agnostic.
    strategy = USST[platform]["strategy"]
    streamer_url = USST[platform]["games"][game]["subscription"][streamer]
    game_url = USST[platform]["games"][game]["game_url"]
    # return: (streamer, url, online)
    response = await strategy(game_url, streamer, streamer_url).parse()
    return response

async def game_call(platform, game):
    streamers = USST[platform]["games"][game]["subscription"].keys()
    result = []
    for streamer in streamers:
        streamer_coroutine = streamer_call(platform, game, streamer)
        # response: (streamer, url, online)
        response = await streamer_coroutine
        result.append(response)
    # return: [(streamer1, url, online), (streamer2, url, online), ...]
    return result

async def platform_call(platform):
    games = USST[platform]["games"].keys()
    result = {}
    for game in games:
        game_coroutine = game_call(platform, game)
        # response: {game: [(streamer, url, online), (streamer2, url, online), ...]}
        response = await game_coroutine
        result[game] = response
    # result: {game1: [...], game2: [...], ...}
    return result

async def allSub_call():
    platforms = USST.keys()
    result = {}
    for platform in platforms:
        platform_coroutine = platform_call(platform)
        # response: {game1: [...], game2: [...], ...}
        response = await platform_coroutine
        result[platform] = response
    # result: {platform1: {game: [..], game2: [...], ...}, platform2: {game: [..], game2: [...], ...}, ...}
    return result