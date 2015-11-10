# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 lao605
# Licensed under The MIT License (MIT)
# http://opensource.org/licenses/MIT
#

from usst.strategy_helper import Strategy
from tornado.httpclient import AsyncHTTPClient
from bs4 import BeautifulSoup


class PandaStrategy(Strategy):
    async def parse(self):
        http_client = AsyncHTTPClient()
        response = await http_client.fetch(self.game_url)
        soup = BeautifulSoup(response.body, 'html.parser')
        streamers_blocks = soup.select(".video-list-item")

        for streamers_block in streamers_blocks:
            url_suffix = streamers_block.select(".video-list-item-inner")[0].get("href")
            url = "http://www.panda.tv" + url_suffix
            if url == self.streamer_url:
                return (self.streamer, self.streamer_url, "Online")
        return (self.streamer, self.streamer_url, "Offline")

    def __init__(self, game_url, streamer, streamer_url):
        super(PandaStrategy, self).__init__(game_url, streamer, streamer_url)
