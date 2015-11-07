# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 lao605
# Licensed under The MIT License (MIT)
# http://opensource.org/licenses/MIT
#

# If new platform is coming, add following setting to USST
# "platform": {
#         "hostname": "http://www.douyu.com",  # hostname of the platform
#         "strategy": CustomizedStrategy,  # your customized scrapping strategy
#         "games": {
#             # name of the game to be used in the url
#             "heartstone": {
#                 "subdir": "/directory/game/How",
#                 "subscription": {
#                     # The key is English nickname to be used in the url
#                     "qiuri": "/qiuri",
#                 },
#             },
#             "warcraft": {
#                 "subdir": "/directory/game/WOW",
#                 "subscription": {
#                     "swifty": "/swifty",
#                 },
#             },
#         },
#     },

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
                "subdir": "/directory/game/How",
                "subscription": {
                    # The key is English nickname to be use in the url
                    "qiuri": "http://www.douyutv.com/qiuri",
                },
            },
            "warcraft": {
                "subdir": "/directory/game/WOW",
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
                "subdir": "/cate/hearthstone",
                "subscription": {

                },
            },
            "lol": {
                "subdir": "/cate/lol",
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
                "subdir": "/games/how",
                "subscription": {

                },
            },
            "warcraft": {
                "subdir": "/games/wow",
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
                "subdir": "/channels/belle",
                "subscription": {

                },
            },
            "cf": {
                "subdir": "/channels/cf",
                "subscription": {

                },
            },
        },
    },
}
