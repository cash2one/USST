# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 lao605
# Licensed under The MIT License (MIT)
# http://opensource.org/licenses/MIT
#

from tornado.testing import AsyncHTTPTestCase
from usst.wsgi import application
from .setting import load_setting


class LongzhuTestCase(AsyncHTTPTestCase):
    def get_app(self):
        return application(load_setting("fixtures/longzhu_test.json"))

    def test_http_fetch(self):
        response = self.fetch("/longzhu/")

        self.assertEqual(response.code, 200)
