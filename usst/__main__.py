#
# Copyright (c) 2015 lao605
# Licensed under The MIT License (MIT)
# http://opensource.org/licenses/MIT
#

'''
Launch script
'''

import tornado.web
import tornado.log
from tornado import httpserver
from tornado.options import define, options
from usst.core.settings import read_file
from usst.wsgi import application
from usst.core.settings import default_settings


logger = tornado.log.logging.getLogger()
tornado.log.access_log.setLevel(tornado.log.logging.DEBUG)
tornado.log.app_log.setLevel(tornado.log.logging.DEBUG)

# no logfile by default; writing log to file will harm performance
# tornado.options.options.__dict__['log_file_prefix'] = '/tmp/usst_access.log'

define("port", default=8000, help="Run on given port", type=int)
define("config", default="", type=str, help="Path to config file",
       callback=lambda path: read_file(path))

try:
    from tornado.httpclient import AsyncHTTPClient
    AsyncHTTPClient.configure('tornado.curl_httpclient.CurlAsyncHTTPClient')
except:
    pass


def main(args=None):
    logger.setLevel(tornado.log.logging.DEBUG)
    tornado.options.parse_command_line()
    setting = options.config if options.config else default_settings
    http_server = httpserver.HTTPServer(application(setting))
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("USST server is down.")
