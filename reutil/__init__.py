#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py


"""
import re as _re

__version__ = "0.1.0"

__all__ = [ '' ]


class RegexpPattern(object):
    r"""RegexpPattern

    RegexpPattern is a object.
    Responsibility:
    """
    _cache = {}
    patterns = {
        # ip address like "192.168.1.1", "8.8.8.8"
        'ipv4': r'(([0-9]{1,3}\.){3}[0-9]{1,3})',
        # http, https url like "http://google.com"
        'http_url': r'(http|https)://[A-Za-z0-9.?.$,;:&=!*~@_()\-\#%+/]+',

        }

    @staticmethod
    def get_pattern(name):
        r"""SUMMARY

        get_pattern(name)

        @Arguments:
        - `name`:

        @Return:

        @Error:
        """
        return RegexpPattern.patterns.get(name, '')

    @staticmethod
    def get_compile(name):
        r"""SUMMARY

        get_compile(name)

        @Arguments:
        - `name`:

        @Return:

        @Error:
        """
        if not name in RegexpPattern._cache:
            pattern = RegexpPattern.get_pattern(name)
            if pattern == '':
                return None
            RegexpPattern._cache[name] = _re.compile(pattern)
        return RegexpPattern._cache[name]

    @staticmethod
    def list_names():
        r"""SUMMARY

        list_names()

        @Return:

        @Error:
        """
        return RegexpPattern.patterns.keys()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
