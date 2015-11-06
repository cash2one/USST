# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 lao605
# Licensed under The MIT License (MIT)
# http://opensource.org/licenses/MIT
#

import tornado.web
import tornado.wsgi
from tornado import httpserver
from tornado.httpclient import AsyncHTTPClient

from tornado.options import define, options
define("port", default=8080, help="run on given port", type=int)

from handlers import *

if __name__ == "__main__":
    # use curl client for better performance
    AsyncHTTPClient.configure('tornado.curl_httpclient.CurlAsyncHTTPClient')
    application = tornado.wsgi.WSGIApplication([
        # TODO: /(paltform)/(game)/(streamer) three types of url
        (r"/", MainHandler),
        (r"/douyu", DouyuHandler),
    ])
    http_server = httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
