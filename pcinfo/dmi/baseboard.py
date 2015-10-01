#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: baseboard.py 284 2015-01-29 00:10:44Z t1 $
# $Revision: 284 $
# $Date: 2015-01-29 09:10:44 +0900 (Thu, 29 Jan 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-01-29 09:10:44 +0900 (Thu, 29 Jan 2015) $

r"""baseboard -- DESCRIPTION

"""
import sys as _sys
import os as _os

import dmidecode
from pcinfo.dmi import parse

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__revision__ = '$Revision: 284 $'
__version__ = '0.1.0'


class DmiBaseBoard(object):
    r"""SUMMARY
    """

    def __init__(self, dic):
        r"""

        @Arguments:
        - `dic`:
        """
        self._dic = dic

    @property
    def manufacturer(self, ):
        r"""SUMMARY

        manufacturer()

        @Return:
        """
        return self._dic['Manufacturer']

    @property
    def product_name(self, ):
        r"""SUMMARY

        product_name()

        @Return:
        """
        return self._dic['Product Name']

    @property
    def serial_number(self, ):
        r"""SUMMARY

        serial_number()

        @Return:
        """
        return self._dic['Serial Number']

    @property
    def version(self, ):
        r"""SUMMARY

        version()

        @Return:
        """
        return self._dic['Version']


def getbaseboard():
    r"""SUMMARY

    getsystem()

    @Return:
    """
    for dic in parse.DmiParse(dmidecode.baseboard()):
        yield DmiBaseBoard(dic)


def _test():
    r"""Test function."""
    return _os.EX_OK

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# baseboard.py ends here
