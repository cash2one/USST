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
                "game_url": "http://www.panda.tv/cate/hearthstone",
                "subscription": {
                    "wangshifu": "http://www.panda.tv/room/10029",
                },
            },
            "lol": {
                "game_url": "http://www.panda.tv/cate/lol",
                "subscription": {
                    "GPS": "http://www.panda.tv/room/10583",
                },
            },
        },
    },
    "zhanqi": {
        "hostname": "http://www.zhanqi.tv",
        "strategy": ZhanqiStrategy,
        "games": {
            "heartstone": {
                "game_url": "http://www.zhanqi.tv/games/how",
                "subscription": {
                    "sleepySM": "http://www.zhanqi.tv/shaman",
                },
            },
            "dnf": {
                "game_url": "http://www.zhanqi.tv/games/dnf",
                "subscription": {
                    "Rain__Y": "http://www.zhanqi.tv/rain_y",
                },
            },
        },
    },
    "longzhu": {
        "hostname": "http://longzhu.com",
        "strategy": LongzhuStrategy,
        "games": {
            "lol": {
                "game_url": "http://longzhu.com/channels/lol",
                "subscription": {
                    "haiwang": "http://star.longzhu.com/haiwang?from=challcontent",
                },
            },
            "cf": {
                "game_url": "http://longzhu.com/channels/cf",
                "subscription": {
                    "jueji": "http://star.longzhu.com/102404?from=challcontent",
                },
            },
        },
    },
}
