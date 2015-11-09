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

from usst.handlers import (AllSubHandler,
                           PlatformHandler,
                           GameHandler,
                           StreamerHandler)

define("debug", default=True, help="Debug Mode", type=bool)
define("port", default=8000, help="Run on given port", type=int)

try:
    from tornado.httpclient import AsyncHTTPClient
    AsyncHTTPClient.configure('tornado.curl_httpclient.CurlAsyncHTTPClient')
except:
    pass

# when run with wsgi server, import this application object
app = tornado.wsgi.WSGIApplication([
        (r"^/$", AllSubHandler),
        (r"^/(?P<platform>[a-zA-Z0-9-]+)/$", PlatformHandler),
        (r"^/(?P<platform>[a-zA-Z0-9-]+)/(?P<game>[a-zA-Z0-9-]+)/$", GameHandler),
        (r"^/(?P<platform>[a-zA-Z0-9-]+)/(?P<game>[a-zA-Z0-9-]+)/(?P<streamer>[a-zA-Z0-9-]+)/$", StreamerHandler),
])


def wsgi_application(environ, start_response):
    return app(environ, start_response)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
