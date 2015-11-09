# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 lao605
# Licensed under The MIT License (MIT)
# http://opensource.org/licenses/MIT
#

import tornado.autoreload
import tornado.web
import tornado.wsgi
from tornado import httpserver
from tornado.options import define, options
from handlers import *


settings = {'debug' : True}
define("debug",default=True,help="Debug Mode",type=bool)
define("port", default=8080, help="runS on given port", type=int)

# Using curl client provides better performance
# from tornado.httpclient import AsyncHTTPClient
# AsyncHTTPClient.configure('tornado.curl_httpclient.CurlAsyncHTTPClient')
application = tornado.wsgi.WSGIApplication([
        # TODO: /(platform)/(game)/(streamer) three types of url
        (r"^/$", AllSubHandler),
        (r"^/(?P<platform>[a-zA-Z0-9-]+)/$", PlatformHandler),
        (r"^/(?P<platform>[a-zA-Z0-9-]+)/(?P<game>[a-zA-Z0-9-]+)/$", GameHandler),
        (r"^/(?P<platform>[a-zA-Z0-9-]+)/(?P<game>[a-zA-Z0-9-]+)/(?P<streamer>[a-zA-Z0-9-]+)/$", StreamerHandler),
    ])

if __name__ == "__main__":
    http_server = httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
