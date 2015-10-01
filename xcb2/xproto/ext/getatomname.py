#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""getatomname -- a parts of xcb2

GetAtomName

atom: ATOM

name: STRING8
Errors: Atom

This request returns the name for the given atom.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request
from xcb2.xobj import GlobalCacheAtoms
from xcb2.xproto.wcookie import WrapGetAtomNameCookie
from xcb2.xproto import GetAtomNameCookie, GetAtomNameReply
from xcb2.xproto.ext.abstract import CoreMethodAbstract, CoreSubMethodAbstract


__all__ = ['GetAtomName', 'GetAtomNameUnchecked', ]


class UseCache(CoreSubMethodAbstract):
    r"""SUMMARY
    """
    _head = _pack('=xx2x')
    fmt = 'I'

    def _getcache(self, atom):
        r"""SUMMARY

        _getcache(name)

        @Arguments:
        - `name`:

        @Return:
        """
        return GlobalCacheAtoms.getatom(atom, self._connection.display)

    def _addcache(self, atom):
        r"""SUMMARY

        _addcache(atom)

        @Arguments:
        - `atom`:

        @Return:
        """
        GlobalCacheAtoms.add(atom, self._connection.display)

    def _getbinary(self, atom):
        r"""SUMMARY

        _getbinary(atom)

        @Arguments:
        - `atom`:

        @Return:
        """
        buf = _StringIO()
        buf.write(self._head)
        buf.write(_pack(self.fmt, atom))
        return buf.getvalue()

    def _request(self, atom):
        r"""SUMMARY

        _request(atom)

        @Arguments:
        - `atom`:

        @Return:
        """
        cookie = self._parent.request(self._getbinary(atom))
        cookie.atom = atom
        return WrapGetAtomNameCookie(self._connection, cookie)

    def __call__(self, atom):
        cache = self._getcache(atom)
        if not cache is None:
            return cache
        name = self._request(atom).reply().name
        self._addcache(name)
        return name


class GetAtomNameAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """
    _head = _pack('=xx2x')
    fmt = 'I'
    code = 17

    def __init__(self, parent):
        r"""SUMMARY

        __init__(parent)

        @Arguments:
        - `parent`:

        @Return:
        """
        CoreMethodAbstract.__init__(self, parent)
        self.usecache = UseCache(self)

    def _getbinary(self, atom):
        buf = _StringIO()
        buf.write(self._head)
        buf.write(_pack(self.fmt, atom))
        return buf.getvalue()

    def __call__(self, atom):
        """Request GetAtomName X protocol.

        @Arguments:
        - `atom`: (int)

        @Return:
        WrapGetAtomNameCookie

        @Error:
        BadAtom
        """
        cookie = self.request(self._getbinary(atom))
        cookie.atom = atom
        return WrapGetAtomNameCookie(self._connection, cookie)


class GetAtomName(GetAtomNameAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(atom)

        @Arguments:
        - `atom`:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, True),
            GetAtomNameCookie(), GetAtomNameReply)


class GetAtomNameUnchecked(GetAtomNameAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(atom)

        @Arguments:
        - `atom`:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, False),
            GetAtomNameCookie(), GetAtomNameReply)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# getatomname.py ends here
