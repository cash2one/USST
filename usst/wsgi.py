# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 lao605
# Licensed under The MIT License (MIT)
# http://opensource.org/licenses/MIT
#

import tornado.autoreload
import tornado.wsgi
from usst.core.settings import default_settings
from usst.core.handlers import (AllSubHandler,
                                PlatformHandler,
                                GameHandler,
                                StreamerHandler)


def application(setting):
    return tornado.wsgi.WSGIApplication([
        (r"^/$", AllSubHandler, dict(setting=setting)),
        (r"^/(?P<platform>[a-zA-Z0-9-]+)/$", PlatformHandler, dict(setting=setting)),
        (r"^/(?P<platform>[a-zA-Z0-9-]+)/(?P<game>[a-zA-Z0-9-]+)/$", GameHandler, dict(setting=setting)),
        (r"^/(?P<platform>[a-zA-Z0-9-]+)/(?P<game>[a-zA-Z0-9-]+)/(?P<streamer>[a-zA-Z0-9-]+)/$", StreamerHandler, dict(setting=setting)),
    ])


# Converts a tornado.web.Application instance into a WSGI application.
def wsgi_application(setting):
    return tornado.wsgi.WSGIAdapter(application(setting))

default_wsgi_application = wsgi_application(default_settings)
