#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: connector.py 284 2015-01-29 00:10:44Z t1 $
# $Revision: 284 $
# $Date: 2015-01-29 09:10:44 +0900 (Thu, 29 Jan 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-01-29 09:10:44 +0900 (Thu, 29 Jan 2015) $

r"""connector -- DESCRIPTION

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


class DmiConnector(object):
    r"""SUMMARY
    """

    def __init__(self, dic):
        r"""

        @Arguments:
        - `dic`:
        """
        self._dic = dic

    @property
    def port_type(self, ):
        r"""SUMMARY

        port_type()

        @Return:
        """
        return self._dic['Port Type']

    @property
    def internal_reference(self, ):
        r"""SUMMARY

        internal_reference()

        @Return:
        """
        return self._dic['Internal Reference Designator']

    @property
    def internal_connector_type(self, ):
        r"""SUMMARY

        internal_connector_type()

        @Return:
        """
        return self._dic['Internal Connector Type']

    @property
    def external_reference_designator(self, ):
        r"""SUMMARY

        external_reference_designator()

        @Return:
        """
        return self._dic['External Reference Designator']

    @property
    def external_connector_type(self, ):
        r"""SUMMARY

        external_connector_type()

        @Return:
        """
        return self._dic['External Connector Type']


def getconnector():
    r"""SUMMARY

    getchassis()

    @Return:
    """
    for dic in parse.DmiParse(dmidecode.connector()):
        yield DmiConnector(dic)


def _test():
    r"""Test function."""
    return _os.EX_OK

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# connector.py ends here
