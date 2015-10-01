#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: memory.py 284 2015-01-29 00:10:44Z t1 $
# $Revision: 284 $
# $Date: 2015-01-29 09:10:44 +0900 (Thu, 29 Jan 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-01-29 09:10:44 +0900 (Thu, 29 Jan 2015) $

r"""memory -- DESCRIPTION

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


class DmiMemory(object):
    r"""SUMMARY
    """

    def __init__(self, dic):
        r"""

        @Arguments:
        - `dic`:
        """
        self._dic = dic

    @property
    def location(self, ):
        r"""SUMMARY

        location()

        @Return:
        """
        return self._dic['Location']

    @property
    def use(self, ):
        r"""SUMMARY

        use()

        @Return:
        """
        return self._dic['Use']

    @property
    def number_of_device(self, ):
        r"""SUMMARY

        number_of_device()

        @Return:
        """
        return self._dic['Number Of Devices']


    @property
    def maximum_capacity(self, ):
        r"""SUMMARY

        maximum_capacity()

        @Return:
        """
        return self._dic['Maximum Capacity']

    @property
    def error_correction_type(self, ):
        r"""SUMMARY

        error_correction_type()

        @Return:
        """
        return self._dic['Error Correction Type']

    @property
    def error_information_handle(self, ):
        r"""SUMMARY

        error_information_handle()

        @Return:
        """
        return self._dic['Error Information Handle']


class DmiMemoryDevice(object):
    r"""SUMMARY
    """

    def __init__(self, dic):
        r"""

        @Arguments:
        - `dic`:
        """
        self._dic = dic

    @property
    def form_factor(self, ):
        r"""SUMMARY

        form_factor()

        @Return:
        """
        return self._dic['Form Factor']

    @property
    def type_detail(self, ):
        r"""SUMMARY

        type_detail()

        @Return:
        """
        return self._dic['Type Detail']

    @property
    def size(self, ):
        r"""SUMMARY

        size()

        @Return:
        """
        return self._dic['Size']

    @property
    def speed(self, ):
        r"""SUMMARY

        speed()

        @Return:
        """
        return self._dic['Speed']

    @property
    def total_width(self, ):
        r"""SUMMARY

        total_width()

        @Return:
        """
        return self._dic['Total Width']

    @property
    def data_width(self, ):
        r"""SUMMARY

        data_width()

        @Return:
        """
        return self._dic['Data Width']

    @property
    def locator(self, ):
        r"""SUMMARY

        locator()

        @Return:
        """
        return self._dic['Locator']

    @property
    def bank_locator(self, ):
        r"""SUMMARY

        bank_locator()

        @Return:
        """
        return self._dic['Bank Locator']

    @property
    def manufacturer(self, ):
        r"""SUMMARY

        manufacturer()

        @Return:
        """
        return self._dic['Manufacturer']

    @property
    def serial_number(self, ):
        r"""SUMMARY

        serial_number()

        @Return:
        """
        return self._dic['Serial Number']

    @property
    def array_handle(self, ):
        r"""SUMMARY

        array_handle()

        @Return:
        """
        return self._dic['Array Handle']

    @property
    def set(self, ):
        r"""SUMMARY

        set()

        @Return:
        """
        return self._dic['Set']

    @property
    def error_information_handle(self, ):
        r"""SUMMARY

        error_information_handle()

        @Return:
        """
        return self._dic['Error Information Handle']

    @property
    def type(self, ):
        r"""SUMMARY

        type()

        @Return:
        """
        return self._dic['Type']


def getmemory():
    r"""SUMMARY

    getmemory()

    @Return:
    """
    for dic in parse.DmiParse(dmidecode.memory()):
        if 'Location' in dic:
            yield DmiMemory(dic)
        else:
            yield DmiMemoryDevice(dic)


def _test():
    r"""Test function."""
    return _os.EX_OK

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# memory.py ends here
