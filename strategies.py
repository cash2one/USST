# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 lao605
# Licensed under The MIT License (MIT)
# http://opensource.org/licenses/MIT
#

# TODO: Choose good scrapping tool: beautifulsoup, lxml, pyquery, etc..


class Strategy(object):
    '''
    Customized strategy should inherit this class and do following steps:

    1. Observe the webpage and get the pattern of `name of streamers` and `url of the streamer`.
    2. Override `parse` method to write the parsing process.
    '''
    def parse(self):
        "Will return a dict of `streamer:url` with which StreamerHandler and check whether online"
        raise NotImplementedError('Strategy must implement `parse` method.')

    def __call__(self, url, name_selector=None, url_selector=None):
        self.url = url
        self.name_selector = name_selector
        self.url_selector = url_selector
        self.parse()


class DouyuStrategy(Strategy):
    def parse(self):
        pass

    def __call__(self, url):
        # TODO: Replace with specific name_selector and url_selector for each platform
        super(DouyuStrategy, self).__call__(url, ".nnt", ".list")


class PandaStrategy(Strategy):
    def parse(self):
        pass

    def __call__(self, url):
        # TODO: Replace with specific name_selector and url_selector for each platform
        super(DouyuStrategy, self).__call__(url, ".nnt", ".list")


class ZhanqiStrategy(Strategy):
    def parse(self):
        pass

    def __call__(self, url):
        # TODO: Replace with specific name_selector and url_selector for each platform
        super(DouyuStrategy, self).__call__(url, ".nnt", ".list")


class LongzhuStrategy(Strategy):
    def parse(self):
        pass

    def __call__(self, url):
        # TODO: Replace with specific name_selector and url_selector for each platform
        super(DouyuStrategy, self).__call__(url, ".nnt", ".list")