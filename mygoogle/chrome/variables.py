#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""variables -- DESCRIPTION

"""
import sys as _sys
import os as _os
from ref.CMD import xfce4


if _os.name in ('posix', 'java'):
    BOOKMARK_BASE_PATH = '~/.config/google-chrome/Default/Bookmarks'
    BOOKMARK_PATH = _os.path.expanduser(BOOKMARK_BASE_PATH)

elif 'nt' == _os.name:
    BOOKMARK_BASE_PATH = ('Local Settings/Application Data/Google'
                          '/Chrome/User Data/Default/Bookmarks')
    BOOKMARK_PATH = _os.path.join(_os.environ['userprofile'],
                                  BOOKMARK_BASE_PATH)

else:
    BOOKMARK_PATH = ''
    # raise NotImplementedError('not supported {.name} environment'.format(_os))


DEFAULT_OPTS = [
    '--disable-geolocation',
                '--password-store=basic',
                '--disable-logging',
                '--disable-java',
                '--disable-application-cache',
                '--media-cache-size=100000000',
                '--disk-cache-size=100000000',
                '--disable-ipv6',
                '--disk-cache-dir="/tmp/chrome"',
                '--omnibox-popup-count=1',
                ]


def get_chrome_launcher():
    r"""SUMMARY

    get_chrome_launcher()

    @Return:
    """
    for file_ in xfce4.iter_desktops():
        with open(file_, 'r') as fobj:
            for line in fobj:
                if 'Exec' in line and 'google-chrome' in line:
                    return line
    return None


def get_launcher_options():
    r"""SUMMARY

    get_launcher_options()

    @Return:
    """
    line = get_chrome_launcher()
    if not line:
        return None
    trimed = line.replace('\n', '')
    return [x for x in trimed.split(' ') if x.startswith(('--'))]


# DEFAULT_OPTS = get_launcher_options() or DEFAULT_OPTS
DEFAULT_OPTS = DEFAULT_OPTS

def _test():
    r"""Test function."""
    return _os.EX_OK

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# variables.py ends here
