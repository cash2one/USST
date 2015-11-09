# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 lao605
# Licensed under The MIT License (MIT)
# http://opensource.org/licenses/MIT
#

# TODO: Choose good scrapping tool: beautifulsoup, lxml, pyquery, etc..

from tornado.httpclient import AsyncHTTPClient
from bs4 import BeautifulSoup


class Strategy(object):
    '''
    Customized strategy should inherit this class and do following steps:

    1. Observe the webpage and get the pattern of `name of streamers` and `url of the streamer`.
    2. Override `parse` method to write the parsing process.
    '''
    async def parse(self):
        '''
        Will return a tuple of `(streamer, url, online)` with which StreamerHandler and check whether online

        Url will be set to None if the streamer is not online
        '''
        raise NotImplementedError('Strategy must implement `parse` method.')

    def __init__(self, game_url, streamer_url):
        self.game_url = game_url
        self.streamer_url = streamer_url


class DouyuStrategy(Strategy):
    async def parse(self):
        http_client = AsyncHTTPClient()
        response = await http_client.fetch(self.game_url)
        soup = BeautifulSoup(response.body, 'html.parser')
        streamers_blocks = soup.select("#item_data ul li")
        print("game_url", self.game_url, "streamer_url", self.streamer_url)

        for streamers_block in streamers_blocks:
            url_suffix = streamers_block.select(".list")[0].get("href")
            url = "http://www.douyutv.com" + url_suffix
            name = streamers_block.select(".nnt")[0].string
            if url == self.streamer_url:
                print("url", url, "streamer_url", self.streamer_url)
                # return: (streamer, url, online)
                return (name, self.streamer_url, "Online")
        return (name, self.streamer_url, "Offline")


    def __init__(self, game_url, streamer_url):
        # TODO: Replace with specific name_selector and url_selector for each platform
        super(DouyuStrategy, self).__init__(game_url, streamer_url)


class PandaStrategy(Strategy):
    async def parse(self):
        pass

    def __init__(self, game_url, streamer_url):
        # TODO: Replace with specific name_selector and url_selector for each platform
        super(PandaStrategy, self).__init__(game_url, streamer_url)


class ZhanqiStrategy(Strategy):
    async def parse(self):
        pass

    def __init__(self, game_url, streamer_url):
        # TODO: Replace with specific name_selector and url_selector for each platform
        super(ZhanqiStrategy, self).__init__(game_url, streamer_url)


class LongzhuStrategy(Strategy):
    async def parse(self):
        pass

    def __init__(self, game_url, streamer_url):
        # TODO: Replace with specific name_selector and url_selector for each platform
        super(LongzhuStrategy, self).__init__(game_url, streamer_url)