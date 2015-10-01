#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: devices.py 96 2013-12-23 13:08:21Z t1 $
# $Revision: 96 $
# $Date: 2013-12-23 22:08:21 +0900 (Mon, 23 Dec 2013) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2013-12-23 22:08:21 +0900 (Mon, 23 Dec 2013) $

r"""device -- /proc/bus/input/device

"""

import sys as _sys
import os as _os
from collections import namedtuple
from itertools import groupby
from t1.dictutil import dict_to_namedtuple


# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__revision__ = '$Revision: 96 $'
__version__ = '0.1.0'

KEYBOARD = '120013'


class ParseDevices(object):
    r"""
    """
    _path = '/proc/bus/input/devices'

    def __init__(self, ):
        r"""
        """
        self._map = {}
        try:
            self.file = open(self._path, 'r')
        except IOError:
            print('Failed open')
            # TODO: (Atami) [2013/12/21]
        self.elems = [list(group) for k, group in
                      groupby(self.file.readlines(), lambda x: x == '\n')
                      if not k]
        self._trim()

    def __iter__(self, ):
        r"""SUMMARY

        __iter__()

        @Return:
        """
        for elem in self.elems:
            dic = {}
            for string in elem:
                if string[0] == 'I':
                    dic = self._parse_I(string, dic)
                elif string[0] in ('N', 'P', 'U'):
                    dic = self._parse_NPU(string, dic)
                elif string[0] == 'S':
                    dic = self._parse_S(string, dic)
                elif string[0] == 'H':
                    dic = self._parse_H(string, dic)
                elif string[0] == 'B':
                    dic = self._parse_B(string, dic)
            yield dict_to_namedtuple('Device', dic)

    def _trim(self, ):
        r"""SUMMARY

        _trim()

        @Return:
        """
        for i in xrange(len(self.elems)):
            for j in xrange(len(self.elems[i])):
                self.elems[i][j] = self.elems[i][j].replace('"', '')
                #trim endswith '\n'
                if self.elems[i][j].endswith(('\n')):
                    self.elems[i][j] = self.elems[i][j][0:-1]

    def _parse_I(self, string, dic):
        r"""SUMMARY

        _parse_I(string)

        @Arguments:
        - `string`:

        @Return:
        """
        string = string[3:]
        for elem in string.split(' '):
            key, value = elem.split('=')
            dic[key] = value
        return dic

    def _parse_NPU(self, string, dic):
        r"""SUMMARY

        _parse_N(string)

        @Arguments:
        - `string`:

        @Return:
        """
        string = string[3:]
        dic[string[:4]] = string[5:]
        return dic

    def _parse_S(self, string, dic):
        r"""SUMMARY

        _parse_S(string)

        @Arguments:
        - `string`:

        @Return:
        """
        string = string[3:]
        dic[string[:5]] = string[6:]
        return dic

    def _parse_H(self, string, dic):
        r"""SUMMARY

        _parse_H(string)

        @Arguments:
        - `string`:

        @Return:
        """
        string = string[3:]
        dic[string[:8]] = string[9:]
        return dic

    def _parse_B(self, string, dic):
        r"""SUMMARY

        _parse_B(string)

        @Arguments:
        - `string`:

        @Return:
        """
        string = string[3:]
        key, value = string.split('=')
        if 1 == len(value):
            value = value[0]
        if 'KEY' == key:
            value = value.split(' ')
        dic[key] = value
        return dic

    def __del__(self, ):
        r"""SUMMARY

        __del__()

        @Return:
        """
        self.file.close()


def get_devices_info():
    r"""SUMMARY

    get_devices_info()

    @Return:
    """
    return list(ParseDevices())


def _test():
    r"""Test function."""
    return _os.EX_OK

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# device.py ends here
