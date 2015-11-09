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
import json

# temporary
from settings import USST


class StreamerHandler(RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(StreamerHandler, self).__init__(application, request, **kwargs)

    async def get(self, platform, game, streamer):
        self.write("StreamerHandler %s, %s, %s"%(platform, game, streamer))
        self.finish()
        # TODO: This fetches information of a streamer of a games of a platform.
        '''
        1. Check streamer
        '''


class GameHandler(StreamerHandler):
    def __init__(self, application, request, **kwargs):
        super(GameHandler, self).__init__(application, request, **kwargs)

    async def get(self, platform, game):
        self.write("GameHandler %s, %s"%(platform, game))
        self.finish()
        # TODO: This fetches all information of all streamer of a games of a platform.
        '''
        1. Check game
        2. Call StreamerHandler
        '''


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
    streamer_coroutines = list(map(streamer_call, [platform]*len(streamers), [game]*len(streamers), streamers))
    result = []
    for streamer_coroutine in streamer_coroutines:
        # response: (streamer, url, online)
        response = await streamer_coroutine
        result.append(response)
    # return: {game: [(streamer1, url, online), (streamer2, url, online), ...]}
    return {game: result}

async def platform_call(platform):
    games = USST[platform]["games"].keys()
    game_coroutines = list(map(game_call, [platform]*len(games), games))
    result = {}
    for game_coroutine in game_coroutines:
        # response: {game: [(streamer, url, online), (streamer2, url, online), ...]}
        response = await game_coroutine
        for game in response.keys():
            result[game] = response[game]
    # result: {game1: [...], game2:[...], ...}
    return result
