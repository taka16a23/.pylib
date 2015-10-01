#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: internatom.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""internatom -- a parts of xcb2

InternAtom

name: STRING8
only-if-exists: BOOL

atom: ATOM or None

Errors: Alloc, Value

This request returns the atom for the given name. If only-if-exists is False,
then the atom is created if it does not exist. The string should use the ISO
Latin-1 encoding. Uppercase and lowercase matter.

The lifetime of an atom is not tied to the interning client. Atoms remain
defined until server reset (see section 10).
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack
from array import array as _array

from xcb2 import Request
from xcb2.xobj import GlobalCacheAtoms
from xcb2.xproto import InternAtomCookie, InternAtomReply
from xcb2.xproto.ext.abstract import CoreMethodAbstract, CoreSubMethodAbstract
from xcb2.xproto.wcookie import WrapInternAtomCookie


__all__ = ['InternAtom', 'InternAtomUnchecked', ]


class UseCache(CoreSubMethodAbstract):
    r"""SUMMARY
    """

    def __init__(self, parent):
        r"""

        @Arguments:
        - `parent`:
        """
        CoreSubMethodAbstract.__init__(self, parent)
        self._only_if_exists = _pack('=xB2x', True)

    def set_only_if_exists(self, bool_):
        r"""SUMMARY

        set_only_if_exists(bool_)

        @Arguments:
        - `bool_`:

        @Return:
        """
        if not isinstance(bool_, bool):
            # TODO: (Atami) [2014/05/27]
            raise StandardError()
        self._only_if_exists = _pack('=xB2x', bool_)

    def _getcache(self, name):
        r"""SUMMARY

        _getcache(name)

        @Arguments:
        - `name`:

        @Return:
        """
        return GlobalCacheAtoms.getatom(name, self._connection.display)

    def _addcache(self, atom):
        r"""SUMMARY

        _addcache(atom)

        @Arguments:
        - `atom`:

        @Return:
        """
        GlobalCacheAtoms.add(atom, self._connection.display)

    def _getbinary(self, name):
        r"""SUMMARY

        _getbinary(name)

        @Arguments:
        - `name`:

        @Return:
        """
        buf = _StringIO()
        buf.write(self._only_if_exists)
        buf.write(_pack('H2x', len(name)))
        buf.write(str(buffer(_array('b', name))))
        return buf.getvalue()

    def _request(self, name):
        r"""SUMMARY

        request(binary)

        @Arguments:
        - `binary`:

        @Return:
        """
        cookie = self._parent.request(self._getbinary(name))
        cookie.name = name
        return WrapInternAtomCookie(self._connection, cookie)

    def __call__(self, name):
        cache = self._getcache(name)
        if not cache is None:
            return cache
        atom = self._request(name).reply().atom
        self._addcache(atom)
        return atom


class InternAtomAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xB2xH2x'
    code = 16

    def __init__(self, parent):
        r"""SUMMARY

        __init__(parent)

        @Arguments:
        - `parent`:

        @Return:
        """
        CoreMethodAbstract.__init__(self, parent)
        self.usecache = UseCache(self)

    def _getbinary(self, only_if_exists, name_len, name):
        buf = _StringIO()
        buf.write(_pack(self.fmt, only_if_exists, name_len))
        buf.write(str(buffer(_array('b', name))))
        return buf.getvalue()

    def __call__(self, only_if_exists, name_len, name):
        """Request InternAtom X protocol.

        @Arguments:
        - `only_if_exists`: (bool)
        - `name_len`:
        - `name`:

        @Return:
        WrapInternAtomCookie

        @Error:
        BadAlloc, BadValue
        """
        cookie = self.request(self._getbinary(only_if_exists, name_len, name))
        cookie.name = name
        return WrapInternAtomCookie(self._connection.display, cookie)


class InternAtom(InternAtomAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(only_if_exists, name_len, name)

        @Arguments:
        - `only_if_exists`:
        - `name_len`:
        - `name`:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, True),
            InternAtomCookie(), InternAtomReply)


class InternAtomUnchecked(InternAtomAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(only_if_exists, name_len, name)

        @Arguments:
        - `only_if_exists`:
        - `name_len`:
        - `name`:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, False),
            InternAtomCookie(), InternAtomReply)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# internatom.py ends here
