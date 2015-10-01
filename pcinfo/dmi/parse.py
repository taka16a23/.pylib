#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""parse -- DESCRIPTION

"""

import sys as _sys
import os as _os

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__version__ = '0.1.0'


class DmiParse(object):
    r"""SUMMARY
    """

    def __init__(self, dic):
        r"""

        @Arguments:
        - `dic`:
        """
        self._dic = dic

    def each(self, ):
        r"""SUMMARY

        each()

        @Return:
        """
        for value in self._dic.itervalues():
            yield value

    def iterdata(self, ):
        r"""SUMMARY

        iterdata()

        @Return:
        """
        for each in self.each():
            yield each['data']

    def __iter__(self, ):
        return iter(self.iterdata())

    def __repr__(self, ):
        return '{0.__class__.__name__}({0._dic})'.format(self)


def _test():
    r"""Test function."""
    return _os.EX_OK

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# parse.py ends here
