#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: _macaddr.py 369 2015-08-06 03:39:24Z t1 $
# $Revision: 369 $
# $Date: 2015-08-06 12:39:24 +0900 (Thu, 06 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-06 12:39:24 +0900 (Thu, 06 Aug 2015) $

r"""_macaddr -- DESCRIPTION

"""
import netaddr


class EUI(object):
    r"""EUI

    EUI is a object.
    Responsibility:
    """
    _formats = {'unix': netaddr.mac_unix,
                'bare': netaddr.mac_bare,
                'cisco': netaddr.mac_cisco,
                'pgsql': netaddr.mac_pgsql,
                'eui48': netaddr.mac_eui48,
                }

    def __init__(self, addr, fmt=None):
        r"""

        @Arguments:
        - `addr`:
        - `format_`:
        """
        self._eui = netaddr.EUI(addr)
        self._format_ = None
        if fmt is None:
            # guess format
            for fmt, dialect in self._formats.items():
                if self._eui.dialect == dialect:
                    self._format = fmt
                    break
        else:
            self.set_format(fmt)
        if self._format is None:
            raise StandardError('{} not supported format.'.format(fmt))

    def set_format(self, fmt):
        r"""SUMMARY

        set_format(fmt)

        @Arguments:
        - `fmt`:

        @Return:

        @Error:
        """
        dialect = self._formats.get(fmt, None)
        if dialect is None:
            raise StandardError('{} not supported format.'.format(fmt))
        self._eui.dialect = dialect
        self._format = fmt

    def get_format(self, ):
        r"""SUMMARY

        get_format()

        @Return:

        @Error:
        """
        return self._format

    def get_binary(self, ):
        r"""SUMMARY

        get_binary()

        @Return:

        @Error:
        """
        return self._eui.bin

    def organizations(self, ):
        r"""SUMMARY

        get_organization()

        @Return:

        @Error:
        """
        return [x['org'] for x in self._eui.oui.records if 'org' in x]

    def pack(self, ):
        r"""SUMMARY

        pack()

        @Return:

        @Error:
        """
        return self._eui.packed

    def list_address(self, ):
        r"""SUMMARY

        get_address()

        @Return:

        @Error:
        """
        return [x['address'] for x in self._eui.oui.records if 'address' in x]

    def organizations_ids(self, ):
        r"""SUMMARY

        organizations_ids()

        @Return:

        @Error:
        """
        return [x['idx'] for x in self._eui.oui.records if 'idx' in x]

    def get_oui(self, ):
        r"""SUMMARY

        get_oui()

        @Return:

        @Error:
        """
        return str(self._eui.oui)

    def __int__(self):
        return int(self._eui)

    def __long__(self):
        return long(self._eui)

    def __oct__(self):
        return oct(self._eui)

    def __hex__(self):
        return hex(self._eui)

    def __repr__(self):
        return '{0.__class__.__name__}({1})'.format(self, str(self))

    def __str__(self):
        return str(self._eui)

    def __gt__(self, other):
        return self._eui > other

    def __ge__(self, other):
        return self._eui >= other

    def __lt__(self, other):
        return self._eui < other

    def __le__(self, other):
        return self._eui <= other

    def __getitem__(self, key):
        return self._eui.words[key]

    def __setitem__(self, key, val):
        self._eui.__setitem__(key, val)

    def __hash__(self, ):
        return hash(self._eui)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _macaddr.py ends here
