# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 lao605
# Licensed under The MIT License (MIT)
# http://opensource.org/licenses/MIT
#

'''
independent of setting (setting as an input)
'''

import unittest
import os
from usst.core.validator import Validator
from usst.core.settings import read_file


class Test_validator(unittest.TestCase):
    def setUp(self):
        self.setting = read_file(os.path.join(os.path.dirname(__file__),
                                 "fixtures/validator_test.json"))
        self.validator = Validator(self.setting)

    def test_check_platform(self):
        self.assertTrue(self.validator.check_platform("douyu"))
        self.assertTrue(self.validator.check_platform("panda"))
        self.assertTrue(self.validator.check_platform("zhanqi"))
        self.assertTrue(self.validator.check_platform("longzhu"))

        self.assertFalse(self.validator.check_platform("XXXXXXXXX"))

    def test_check_game(self):
        self.assertTrue(self.validator.check_game("douyu", "heartstone"))
        self.assertTrue(self.validator.check_game("douyu", "warcraft"))
        self.assertTrue(self.validator.check_game("panda", "heartstone"))
        self.assertTrue(self.validator.check_game("panda", "lol"))
        self.assertTrue(self.validator.check_game("zhanqi", "heartstone"))
        self.assertTrue(self.validator.check_game("zhanqi", "warcraft"))
        self.assertTrue(self.validator.check_game("longzhu", "beauty"))
        self.assertTrue(self.validator.check_game("longzhu", "cf"))

        self.assertFalse(self.validator.check_game("douyu", "lol"))
        self.assertFalse(self.validator.check_game("panda", "hahaha"))
        self.assertFalse(self.validator.check_game("zhanqi", "laobi"))
        self.assertFalse(self.validator.check_game("longzhu", "zhansha"))

        self.assertFalse(self.validator.check_game("haha", "haha"))
        self.assertFalse(self.validator.check_game("qwerty", "asdfgh"))
        self.assertFalse(self.validator.check_game("haha", "heartstone"))
        self.assertFalse(self.validator.check_game("qwerty", "lol"))

    def test_check_streamer(self):
        self.assertTrue(self.validator.check_streamer("douyu", "heartstone", "qiuri"))
        self.assertTrue(self.validator.check_streamer("douyu", "warcraft", "btk"))

        self.assertFalse(self.validator.check_streamer("panda", "heartstone", "XXX"))
        self.assertFalse(self.validator.check_streamer("panda", "lol", "XXX"))

        self.assertFalse(self.validator.check_streamer("zhanqi", "heartstone", "XXX"))

# TODO: test other functions


if __name__ == "__main__":
    unittest.main()
