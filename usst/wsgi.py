# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 lao605
# Licensed under The MIT License (MIT)
# http://opensource.org/licenses/MIT
#

import tornado.autoreload
import tornado.wsgi

from usst.core.handlers import (AllSubHandler,
                                PlatformHandler,
                                GameHandler,
                                StreamerHandler)

# when run with wsgi server, import this application object
app = tornado.wsgi.WSGIApplication([
    (r"^/$", AllSubHandler),
    (r"^/(?P<platform>[a-zA-Z0-9-]+)/$", PlatformHandler),
    (r"^/(?P<platform>[a-zA-Z0-9-]+)/(?P<game>[a-zA-Z0-9-]+)/$", GameHandler),
    (r"^/(?P<platform>[a-zA-Z0-9-]+)/(?P<game>[a-zA-Z0-9-]+)/(?P<streamer>[a-zA-Z0-9-]+)/$", StreamerHandler),
])


def wsgi_application(environ, start_response):
    return app(environ, start_response)
