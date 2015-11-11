# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 lao605
# Licensed under The MIT License (MIT)
# http://opensource.org/licenses/MIT
#

from tornado.testing import AsyncHTTPTestCase
from usst.wsgi import app
import json


class AllSubTestCase(AsyncHTTPTestCase):
    def get_app(self):
        return app

    def test_http_fetch(self):
        response = self.fetch("/")

        self.assertEqual(response.code, 200)
        self.assertGreaterEqual(len(json.loads(response.body.decode()).items()), 4)
