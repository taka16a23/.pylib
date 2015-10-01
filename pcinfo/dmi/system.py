#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: system.py 284 2015-01-29 00:10:44Z t1 $
# $Revision: 284 $
# $Date: 2015-01-29 09:10:44 +0900 (Thu, 29 Jan 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-01-29 09:10:44 +0900 (Thu, 29 Jan 2015) $

r"""system -- DESCRIPTION

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


class DmiSystem(object):
    r"""SUMMARY
    """

    def __init__(self, dic):
        r"""

        @Arguments:
        - `values`:
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
    def sku_number(self, ):
        r"""SUMMARY

        sku_number()

        @Return:
        """
        return self._dic['SKU Number']

    @property
    def uuid(self, ):
        r"""SUMMARY

        uuid()

        @Return:
        """
        return self._dic['UUID']

    @property
    def version(self, ):
        r"""SUMMARY

        version()

        @Return:
        """
        return self._dic['Version']

    @property
    def wake_up(self, ):
        r"""SUMMARY

        wake_up()

        @Return:
        """
        return self._dic['Wake-Up Type']

    @property
    def family(self, ):
        r"""SUMMARY

        family()

        @Return:
        """
        return self._dic['Family']


class DmiSystemStatus(object):
    r"""SUMMARY
    """

    def __init__(self, dic):
        r"""

        @Arguments:
        - `dic`:
        """
        self._dic = dic

    @property
    def status(self, ):
        r"""SUMMARY

        status()

        @Return:
        """
        return self._dic['Status']


def getsystem():
    r"""SUMMARY

    getsystem()

    @Return:
    """
    for dic in parse.DmiParse(dmidecode.system()):
        if 'Status' in dic:
            yield DmiSystemStatus(dic)
        else:
            yield DmiSystem(dic)


def _test():
    r"""Test function."""
    return _os.EX_OK

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# system.py ends here
