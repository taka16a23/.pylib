#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""chassis -- DESCRIPTION

"""

import sys as _sys
import os as _os

import dmidecode
from pcinfo.dmi import parse

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__version__ = '0.1.0'


class DmiChassiss(object):
    r"""SUMMARY
    """

    def __init__(self, dic):
        r"""

        @Arguments:
        - `dic`:
        """
        self._dic = dic

    @property
    def asset_tag(self, ):
        r"""SUMMARY

        ()

        @Return:
        """
        return self._dic['Asset Tag']

    @property
    def boot_up_state(self, ):
        r"""SUMMARY

        ()

        @Return:
        """
        return self._dic['Boot-Up State']

    @property
    def lock(self, ):
        r"""SUMMARY

        ()

        @Return:
        """
        return self._dic['Lock']

    @property
    def manufacturer(self, ):
        r"""SUMMARY

        ()

        @Return:
        """
        return self._dic['Manufacturer']

    @property
    def power_supply_state(self, ):
        r"""SUMMARY

        ()

        @Return:
        """
        return self._dic['Power Supply State']

    @property
    def security_status(self, ):
        r"""SUMMARY

        ()

        @Return:
        """
        return self._dic['Security Status']

    @property
    def serial_number(self, ):
        r"""SUMMARY

        ()

        @Return:
        """
        return self._dic['Serial Number']

    @property
    def thermal_state(self, ):
        r"""SUMMARY

        ()

        @Return:
        """
        return self._dic['Thermal State']

    @property
    def type(self, ):
        r"""SUMMARY

        ()

        @Return:
        """
        return self._dic['Type']

    @property
    def version(self, ):
        r"""SUMMARY

        ()

        @Return:
        """
        return self._dic['Version']


def getchassis():
    r"""SUMMARY

    getchassis()

    @Return:
    """
    for dic in parse.DmiParse(dmidecode.chassis()):
        yield DmiChassiss(dic)


def _test():
    r"""Test function."""
    return _os.EX_OK

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# chassis.py ends here
