#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: slot.py 284 2015-01-29 00:10:44Z t1 $
# $Revision: 284 $
# $Date: 2015-01-29 09:10:44 +0900 (Thu, 29 Jan 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-01-29 09:10:44 +0900 (Thu, 29 Jan 2015) $

r"""slot -- DESCRIPTION

"""

import sys as _sys
import os as _os

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__revision__ = '$Revision: 284 $'
__version__ = '0.1.0'


class DmiSlot(object):
    r"""SUMMARY
    """

    def __init__(self, dic):
        r"""

        @Arguments:
        - `dic`:
        """
        self._dic = dic

    @property
    def characteristics(self, ):
        r"""SUMMARY

        characteristics()

        @Return:
        """
        return self._dic['Characteristics']

    @property
    def current_usage(self, ):
        r"""SUMMARY

        current_usage()

        @Return:
        """
        return self._dic['Current Usage']

    @property
    def designation(self, ):
        r"""SUMMARY

        designation()

        @Return:
        """
        return self._dic['Designation']

    @property
    def slotid(self, ):
        r"""SUMMARY

        slotid()

        @Return:
        """
        return self._dic['SlotId']

    @property
    def slotlength(self, ):
        r"""SUMMARY

        slotlength()

        @Return:
        """
        return self._dic['SlotLength']

    @property
    def type_slotbuswidth(self, ):
        r"""SUMMARY

        type_slotbuswidth()

        @Return:
        """
        return self._dic['Type:SlotBusWidth']

    @property
    def type_slottype(self, ):
        r"""SUMMARY

        type_slottype()

        @Return:
        """
        return self._dic['Type:SlotType']


def getslot():
    r"""SUMMARY

    getslot()

    @Return:
    """
    for dic in parse.DmiParse(dmidecode.slot()):
        yield DmiSlot(dic)


def _test():
    r"""Test function."""
    return _os.EX_OK

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# slot.py ends here
