#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: nation_webpage.py 349 2015-08-04 22:35:27Z t1 $
# $Revision: 349 $
# $Date: 2015-08-05 07:35:27 +0900 (Wed, 05 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-05 07:35:27 +0900 (Wed, 05 Aug 2015) $

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


__revision__ = '$Revision: 349 $'
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
