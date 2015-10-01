#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""setpointermapping -- a parts of xcb2

"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack
from array import array as _array

from xcb2 import Request
from xcb2.xproto.ext.abstract import CoreMethodAbstract
from xcb2.xproto import SetPointerMappingCookie, SetPointerMappingReply


__all__ = ['SetPointerMapping', 'SetPointerMappingUnchecked', ]


class SetPointerMappingAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xB2x'
    code = 116

    def _getbinary(self, map_len, map):
        buf = _StringIO()
        buf.write(_pack(self.fmt, map_len))
        buf.write(str(buffer(_array('B', map))))
        return buf.getvalue()

    def __call__(self, map_len, map):
        return self.request(self._getbinary(map_len, map))


class SetPointerMapping(SetPointerMappingAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(map_len, map)

        @Arguments:
        - [yas] elisp error!:
        - [yas] elisp error!:
        - [yas] elisp error!:
        - [yas] elisp error!:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, True),
            SetPointerMappingCookie(), SetPointerMappingReply)


class SetPointerMappingUnchecked(SetPointerMappingAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(map_len, map)

        @Arguments:
        - [yas] elisp error!:
        - [yas] elisp error!:
        - [yas] elisp error!:
        - [yas] elisp error!:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, False),
            SetPointerMappingCookie(), SetPointerMappingReply)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# setpointermapping.py ends here
