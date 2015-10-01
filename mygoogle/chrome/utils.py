#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id: utils.py 389 2015-08-06 15:46:41Z t1 $
# $Revision: 389 $
# $Date: 2015-08-07 00:46:41 +0900 (Fri, 07 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-07 00:46:41 +0900 (Fri, 07 Aug 2015) $
r""" utils -- google chrome urils

$Revision: 389 $

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
