#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""setmodifiermapping -- a parts of xcb2

"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack
from array import array as _array

from xcb2 import Request
from xcb2.xproto.ext.abstract import CoreMethodAbstract
from xcb2.xproto import SetModifierMappingCookie, SetModifierMappingReply


__all__ = ['SetModifierMapping', 'SetModifierMappingUnchecked', ]


class SetModifierMappingAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xB2x'
    code = 118

    def _getbinary(self, keycodes_per_modifier, keycodes):
        buf = _StringIO()
        buf.write(_pack(self.fmt, keycodes_per_modifier))
        buf.write(str(buffer(_array('B', keycodes))))
        return buf.getvalue()

    def __call__(self, keycodes_per_modifier, keycodes):
        return self.request(self._getbinary(keycodes_per_modifier, keycodes))


class SetModifierMapping(SetModifierMappingAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(keycodes_per_modifier, keycodes)

        @Arguments:
        - [yas] elisp error!:
        - [yas] elisp error!:
        - [yas] elisp error!:
        - [yas] elisp error!:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, True),
            SetModifierMappingCookie(), SetModifierMappingReply)


class SetModifierMappingUnchecked(SetModifierMappingAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(keycodes_per_modifier, keycodes)

        @Arguments:
        - [yas] elisp error!:
        - [yas] elisp error!:
        - [yas] elisp error!:
        - [yas] elisp error!:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, False),
            SetModifierMappingCookie(), SetModifierMappingReply)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# setmodifiermapping.py ends here
