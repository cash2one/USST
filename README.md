# Universal Streamer Subscribing Tool (USST)
======================

With new streaming platforms rising, panda.tv etc., streamers are distributed in different platforms, which cause audiences to switch between platforms in order to see what they want.
Such switching always cost plenty of time. This tool helps solving this problems by:

1. Allow users to get the information of all streamers he is interested with one request.
2. Extensible structure which allows quick adjustment to new platforms.

Currently, four platforms are supported: `douyu`, `panda`, `zhanqi`, `longzhu`.

## Compatibility

`>= Python 3.5.0`, the latest version, is needed to run the app. These is no downward compatibility because it uses the new keywords, `async` and `await`.

`>= Tornado 4.3`, the latest version, is needed to support the usage of `async` and `await` in Python 3.5.0.

## Current situation

The tool is still under construction, and it may takes a few weeks to finish it.

## TODO

1. Write the scrapping process of different platforms (douyu done; rest undone)
2. Set up the url (done, but still ugly)
3. Make it runnable (partly done)
4. Apply PEP8 coding style
5. Write tests
6. Write manage script
7. Add Travis CI
8. Make setup easy
9. Write client tool to control settings.py
10. Browser plugins to control settings.py
11. .......

## Contributing

Contribution is always welcome. If you have anything, please let me know in the issue to email me. Thanks.
