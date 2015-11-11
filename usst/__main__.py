#
# Copyright (c) 2015 lao605
# Licensed under The MIT License (MIT)
# http://opensource.org/licenses/MIT
#

import sys
import tornado.web
from tornado import httpserver
from tornado.options import define, options
from .wsgi import app


define("debug", default=True, help="Debug Mode", type=bool)
define("port", default=8000, help="Run on given port", type=int)

try:
    from tornado.httpclient import AsyncHTTPClient
    AsyncHTTPClient.configure('tornado.curl_httpclient.CurlAsyncHTTPClient')
except:
    pass


def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    # TODO: Do argument parsing

    tornado.options.parse_command_line()
    http_server = httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()