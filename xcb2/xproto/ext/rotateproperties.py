#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: rotateproperties.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""rotateproperties -- a parts of xcb2

RotateProperties

window: WINDOW
delta: INT16
properties: LISTofATOM

Errors: Atom, Match, Window

If the property names in the list are viewed as being numbered starting from
zero, and there are N property names in the list, then the value associated with
property name I becomes the value associated with property name (I + delta) mod
N, for all I from zero to N - 1. The effect is to rotate the states by delta
places around the virtual ring of property names (right for positive delta, left
for negative delta).

If delta mod N is nonzero, a PropertyNotify event is generated for each property
in the order listed.

If an atom occurs more than once in the list or no property with that name is
defined for the window, a Match error is generated. If an Atom or Match error is
generated, no properties are changed.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['RotateProperties', 'RotatePropertiesChecked', ]


class RotatePropertiesAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xIHh'
    code = 114

    def _getbinary(self, window, atoms_len, delta, atoms):
        buf = _StringIO()
        buf.write(_pack(self.fmt, window, atoms_len, delta, atoms))
        return buf.getvalue()

    def __call__(self, window, atoms_len, delta, atoms):
        """Request RotateProperties X protocol.

        @Arguments:
        - `window`:
        - `atoms_len`:
        - `delta`:
        - `atoms`:

        @Return:
        VoidCookie

        @Error:
        BadAtom, BadMatch, BadWindow
        """
        return self.request(self._getbinary(window, atoms_len, delta, atoms))


class RotateProperties(RotatePropertiesAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(window, atoms_len, delta, atoms)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class RotatePropertiesChecked(RotatePropertiesAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(window, atoms_len, delta, atoms)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# rotateproperties.py ends here
