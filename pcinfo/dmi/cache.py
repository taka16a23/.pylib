#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: cache.py 284 2015-01-29 00:10:44Z t1 $
# $Revision: 284 $
# $Date: 2015-01-29 09:10:44 +0900 (Thu, 29 Jan 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-01-29 09:10:44 +0900 (Thu, 29 Jan 2015) $

r"""cache -- DESCRIPTION

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

class CacheConfiguration(object):
    r"""SUMMARY
    """

    def __init__(self, dic):
        r"""

        @Arguments:
        - `dic`:
        """
        self._dic = dic

    @property
    def enabled(self, ):
        r"""SUMMARY

        enabled()

        @Return:
        """
        return self._dic['Enabled']

    @property
    def level(self, ):
        r"""SUMMARY

        level()

        @Return:
        """
        return self._dic['Level']

    @property
    def socketed(self, ):
        r"""SUMMARY

        socketed()

        @Return:
        """
        return self._dic['Socketed']


class DmiCache(object):
    r"""SUMMARY
    """

    def __init__(self, dic):
        r"""

        @Arguments:
        - `dic`:
        """
        self._dic = dic

    @property
    def associativity(self, ):
        r"""SUMMARY

        associativity()

        @Return:
        """
        return self._dic['Associativity']

    @property
    def configuration(self, ):
        r"""SUMMARY

        configuration()

        @Return:
        """
        return CacheConfiguration(self._dic['Configuration'])

    @property
    def error_correction_type(self, ):
        r"""SUMMARY

        ()

        @Return:
        """
        return self._dic['Error Correction Type']

    @property
    def installed_sram_type(self, ):
        r"""SUMMARY

        ()

        @Return:
        """
        return self._dic['Installed SRAM Type']

    @property
    def installed_size(self, ):
        r"""SUMMARY

        ()

        @Return:
        """
        return self._dic['Installed Size']

    @property
    def location(self, ):
        r"""SUMMARY

        ()

        @Return:
        """
        return self._dic['Location']

    @property
    def maximum_size(self, ):
        r"""SUMMARY

        ()

        @Return:
        """
        return self._dic['Maximum Size']

    @property
    def operational_mode(self, ):
        r"""SUMMARY

        ()

        @Return:
        """
        return self._dic['Operational Mode']

    @property
    def socket_designation(self, ):
        r"""SUMMARY

        ()

        @Return:
        """
        return self._dic['Socket Designation']

    @property
    def speed(self, ):
        r"""SUMMARY

        ()

        @Return:
        """
        return self._dic['Speed']

    @property
    def supported_sram_type(self, ):
        r"""SUMMARY

        ()

        @Return:
        """
        return self._dic['Supported SRAM Type']

    @property
    def system_type(self, ):
        r"""SUMMARY

        ()

        @Return:
        """
        return self._dic['System Type']


def getcache():
    r"""SUMMARY

    getcache()

    @Return:
    """
    for dic in parse.DmiParse(dmidecode.cache()):
        yield DmiCache(dic)





def _test():
    r"""Test function."""
    return _os.EX_OK

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# cache.py ends here
