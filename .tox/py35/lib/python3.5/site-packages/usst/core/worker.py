# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 lao605
# Licensed under The MIT License (MIT)
# http://opensource.org/licenses/MIT
#


class Worker(object):
    def __init__(self, setting):
        self.setting = setting

    async def streamer_call(self, platform, game, streamer):
        # TODO: refactor -- crawling once for streamers of a game is enough
        # strategy is platform agnostic.
        strategy = self.setting[platform]["strategy"]
        streamer_url = self.setting[platform]["games"][game]["subscription"][streamer]
        game_url = self.setting[platform]["games"][game]["game_url"]
        # return: (streamer, url, online)
        response = await strategy(game_url, streamer, streamer_url).parse()
        return response

    async def game_call(self, platform, game):
        streamers = self.setting[platform]["games"][game]["subscription"].keys()
        result = []
        for streamer in streamers:
            streamer_coroutine = self.streamer_call(platform, game, streamer)
            # response: (streamer, url, online)
            response = await streamer_coroutine
            result.append(response)
        # return: [(streamer1, url, online), (streamer2, url, online), ...]
        return result

    async def platform_call(self, platform):
        games = self.setting[platform]["games"].keys()
        result = {}
        for game in games:
            game_coroutine = self.game_call(platform, game)
            # response: [(streamer, url, online), (streamer2, url, online), ...]
            response = await game_coroutine
            result[game] = response
        # result: {game1: [...], game2: [...], ...}
        return result

    async def allSub_call(self):
        platforms = self.setting.keys()
        result = {}
        for platform in platforms:
            platform_coroutine = self.platform_call(platform)
            # response: {game1: [...], game2: [...], ...}
            response = await platform_coroutine
            result[platform] = response
        # result: {platform1: {game: [..], game2: [...], ...}, platform2: {game: [..], game2: [...], ...}, ...}
        return result
