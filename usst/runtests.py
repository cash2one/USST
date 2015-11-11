# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 lao605
# Licensed under The MIT License (MIT)
# http://opensource.org/licenses/MIT
#

'''
Test for test runner and AllSubHandler
'''

import unittest
import os


def all():
    return unittest.defaultTestLoader.discover(os.path.dirname(__file__))


if __name__ == '__main__':
    import tornado.testing
    tornado.testing.main()
