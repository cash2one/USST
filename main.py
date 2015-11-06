#
# Copyright (c) 2015
# Licensed under The MIT License (MIT)
# http://opensource.org/licenses/MIT
#

import tornado.web
import tornado.wsgi
from wsgiref import handlers
from tornado import httpserver
from tornado.httpclient import AsyncHTTPClient
from tornado.httpclient import HTTPRequest
import tornado.gen

from tornado.options import define, options
define("port", default=8080, help="run on given port", type=int)

from bs4 import BeautifulSoup

from settings import (douyu_url,
                       panda_url,
                       zhanqi_url,
                       longzhu_url,
                       douyu_streamers,
                       panda_streamers,
                       zhanqi_streamers,
                       longzhu_streamers)


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
    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        # besic setup
        client = AsyncHTTPClient()
        streamer_names = []

        request = HTTPRequest(douyu_url, 'GET', follow_redirects=True)
        response = yield tornado.gen.task(client.fetch, request)
        soup = BeautifulSoup(response.body, 'html.parser')
        for nnt in soup.find_all('.nnt'):
            streamer_names.append(nnt.string)

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
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
