# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 lao605
# Licensed under The MIT License (MIT)
# http://opensource.org/licenses/MIT
#

from strategies import (DouyuStrategy,
                        PandaStrategy,
                        ZhanqiStrategy,
                        LongzhuStrategy)


USST = {
    "douyu": {
        "hostname": "http://www.douyutv.com",
        "strategy": DouyuStrategy,
        "games": {
            "heartstone": {
                "game_url": "http://www.douyutv.com/directory/game/How",
                "subscription": {
                    # The key is English nickname to be use in the url
                    "qiuri": "http://www.douyutv.com/qiuri",
                },
            },
            "warcraft": {
                "game_url": "http://www.douyutv.com/directory/game/WOW",
                "subscription": {
                    "btk": "http://www.douyutv.com/BTK",
                },
            },
        },
    },
    "panda": {
        "hostname": "http://www.panda.tv",
        "strategy": PandaStrategy,
        "games": {
            "heartstone": {
                "game_url": "/cate/hearthstone",
                "subscription": {

                },
            },
            "lol": {
                "game_url": "/cate/lol",
                "subscription": {

                },
            },
        },
    },
    "zhanqi": {
        "hostname": "http://www.zhanqi.tv",
        "strategy": ZhanqiStrategy,
        "games": {
            "heartstone": {
                "game_url": "/games/how",
                "subscription": {

                },
            },
            "warcraft": {
                "game_url": "/games/wow",
                "subscription": {

                },
            },
        },
    },
    "longzhu": {
        "hostname": "http://longzhu.com",
        "strategy": LongzhuStrategy,
        "games": {
            "beauty": {
                "game_url": "/channels/belle",
                "subscription": {

                },
            },
            "cf": {
                "game_url": "/channels/cf",
                "subscription": {

                },
            },
        },
    },
}

