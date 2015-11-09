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
# from tornado.httpclient import AsyncHTTPClient
from tornado.options import define, options

settings = {'debug' : True}
define("debug",default=True,help="Debug Mode",type=bool)
define("port", default=8080, help="runS on given port", type=int)

from handlers import *

if __name__ == "__main__":
    # Use curl client for better performance
    # AsyncHTTPClient.configure('tornado.curl_httpclient.CurlAsyncHTTPClient')
    application = tornado.wsgi.WSGIApplication([
        # TODO: /(platform)/(game)/(streamer) three types of url
        (r"^/(?P<platform>[a-zA-Z0-9-]+)/$", PlatformHandler),
        (r"^/(?P<platform>[a-zA-Z0-9-]+)/(?P<game>[a-zA-Z0-9-]+)/$", GameHandler),
        (r"^/(?P<platform>[a-zA-Z0-9-]+)/(?P<game>[a-zA-Z0-9-]+)/(?P<streamer>[a-zA-Z0-9-]+)/$", StreamerHandler),
    ])
    http_server = httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
