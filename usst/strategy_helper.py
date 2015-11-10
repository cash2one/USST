# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 lao605
# Licensed under The MIT License (MIT)
# http://opensource.org/licenses/MIT
#

'''
strategy refers to the actual process of users' scrapping information from pages of different platform.

For example:

strategy of douyu defines the process where you get the `urls` of streamers of a certain pages of douyu.

Most strategies are DouyuStrategy-alike.
'''


# TODO: Choose good scrapping tool: beautifulsoup, lxml, pyquery, etc..


class Strategy(object):
    '''
    Customized strategy should inherit this class and do following steps:

    1. Override `parse` method to write the parsing process.
    '''
    async def parse(self):
        '''
        Will return a tuple of `(streamer, url, online)` with which StreamerHandler and check whether online

        Url will be set to None if the streamer is not online
        '''
        raise NotImplementedError('Strategy must implement `parse` method.')

    def __init__(self, game_url, streamer, streamer_url):
        self.game_url = game_url
        self.streamer = streamer
        self.streamer_url = streamer_url
