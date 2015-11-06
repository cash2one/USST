#
# Copyright (c) 2015
# Licensed under The MIT License (MIT)
# http://opensource.org/licenses/MIT
#

import tornado.web
import tornado.wsgi
from tornado import httpserver
from tornado.httpclient import AsyncHTTPClient
from tornado.httpclient import HTTPRequest
import tornado.gen


from tornado.options import define, options
define("port", default=8080, help="run on given port", type=int)

from bs4 import BeautifulSoup
import json

from settings import (DOUYU,
                      PANDA)


class MainHandler(tornado.web.RequestHandler):
    '''
    :description:

    This will start climbing streamers information from all four platforms.

    :return:

    A json response of all online streamers.
    '''
    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        http = AsyncHTTPClient()
        http.fetch
        self.finish()



class DouyuHandler(tornado.web.RequestHandler):
    '''
    :description:

    Douyu module.

    :return:

    A json response of all douyu online streamers.
    '''
    def __init__(self, application, request, **kwargs):
        # besic setup
        super(DouyuHandler, self).__init__(application, request, **kwargs)
        self.client = AsyncHTTPClient()
        self.streamer_names = {}

    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        request = HTTPRequest(DOUYU["hostname"] + DOUYU["modules"]["heartstone"]["subdir"], 'GET', follow_redirects=True)
        response = yield tornado.gen.Task(self.client.fetch, request)
        soup = BeautifulSoup(response.body, 'html.parser')
        streamers_blocks = soup.select("#item_data ul li")

        for streamers_block in streamers_blocks:
            url_suffix = streamers_block.select(".list")[0].get("href")
            url = DOUYU["hostname"] + url_suffix
            name = streamers_block.select(".nnt")[0].string
            self.streamer_names[name] = url

        self.write(json.dumps(self.streamer_names))
        self.finish()


class ZhanqiHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        self.finish()

class LongzhuHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        self.finish()


if __name__ == "__main__":
    # use curl client for better performance
    AsyncHTTPClient.configure('tornado.curl_httpclient.CurlAsyncHTTPClient')
    application = tornado.wsgi.WSGIApplication([
        (r"/", MainHandler),
        (r"/douyu", DouyuHandler),
    ])
    http_server = httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
