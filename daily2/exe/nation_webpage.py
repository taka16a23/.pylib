#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: nation_webpage.py

"""

import sys
import os
import argparse

import busywait
from mygoogle import chrome
from mygoogle.chrome.variables import DEFAULT_OPTS as CHROME_OPTS

# for debug
import cgitb
cgitb.enable(format='text')


__version__ = '0.0.1'


def _predef_options():
    parser = argparse.ArgumentParser(description="""""")
    parser.add_argument('--version',
                        dest='version',
                        action='version',
                        version=__version__,
                        help='Version Strings.')
    # (yas/expand-link "argparse_add_argument" t)
    return parser

def _main():
    r"""Main function."""
    parser = _predef_options()
    opts = parser.parse_args()
    # parser.print_usage()
    urls = chrome.get_urls('Nation')
    try:
        chrome.run(urls.pop(), CHROME_OPTS + ['--new-window'])
    except IndexError:
        pass
    bwait = busywait.BusyWait(30)
    while urls:
        try:
            bwait.wait_timeout(interval=1, timeout=15)
        except busywait.TimeOut:
            pass
        chrome.run(urls.pop(), CHROME_OPTS)
    return os.EX_OK

if __name__ == '__main__':
    sys.exit(_main())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# nation_webpage.py ends here
