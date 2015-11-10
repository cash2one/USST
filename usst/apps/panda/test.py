# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 lao605
# Licensed under The MIT License (MIT)
# http://opensource.org/licenses/MIT
#

from tornado.testing import AsyncHTTPTestCase
from usst.wsgi import app


class DouyuTestCase(AsyncHTTPTestCase):
    def setUp(self):
        self.USST

    def get_app(self):
        return app

    def test_http_fetch(self):
        self.fetch("/douyu/")
