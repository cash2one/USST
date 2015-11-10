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

## How To Run

1. `make install`
2. `python -m usst.wsgi` or other methods to run wsgi app (see `examples`)
3. access it in browser

## TODO

1. <del>Write the scrapping process of different platforms<del>
2. <del>Finish all handlers<del>
3. <del>Set up the url<del>
4. <del>Make it runnable<del>
5. <del>Apply flake8<del>
6. Write tests (currently learning how to design test cases)
7. Write manage script
8. Add Travis CI
9. <del>Make setup easy<del>
10. Write client tool to control settings.py
11. Browser plugins to control settings.py
12. Add exception handling
13. Add logging
14. Add UI interface
15. <del>Use json conf file to replace settings.py<del> and add to system

## Contributing

Contribution is always welcome. If you have anything, please let me know in the issue to email me. Thanks.
