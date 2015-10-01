#!/usr/bin/env python
# -*- coding: utf-8 -*-
r""" utils -- google chrome urils


"""


import sys as _sys
from reutil import RegexpPattern


def trim_url(url):
    """Triming urls by regexp.

    @Arguments:
    - `urls`: list of urls

    @Return: list of trimed urls
    """
    result = RegexpPattern.get_compile('http_url').search(url)
    if result:
        return result.group()
    return None


def _test():
    r"""Test function."""
    return 0

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# utils.py ends here
