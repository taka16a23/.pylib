#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: alloccolor.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""alloccolor -- a parts of xcb2

"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request
from xcb2.xproto.ext.abstract import CoreMethodAbstract
from xcb.xproto import AllocColorCookie, AllocColorReply


__all__ = [ 'AllocColor', 'AllocColorUnchecked', ]


class AllocColorAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xIHHH2x'
    code = 84

    def _getbinary(self, cmap, red, green, blue):
        r"""SUMMARY

        _getbinary(cmap, red, green, blue)

        @Arguments:
        - `cmap`:
        - `red`:
        - `green`:
        - `blue`:

        @Return:
        """
        buf = _StringIO()
        buf.write(_pack(self.fmt, cmap, red, green, blue))
        return buf.getvalue()

    def __call__(self, cmap, red, green, blue):
        return self.request(self._getbinary(cmap, red, green, blue))


class AllocColor(AllocColorAbstract):
    r"""SUMMARY
    """
    def request(self, binary):
        r"""SUMMARY

        request(cmap, red, green, blue)

        @Arguments:
        - `cmap`:
        - `red`:
        - `green`:
        - `blue`:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, True),
            AllocColorCookie(), AllocColorReply)


class AllocColorUnchecked(AllocColorAbstract):
    r"""SUMMARY
    """
    def request(self, binary):
        r"""SUMMARY

        request(cmap, red, green, blue)

        @Arguments:
        - `cmap`:
        - `red`:
        - `green`:
        - `blue`:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, False),
            AllocColorCookie(), AllocColorReply)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# alloccolor.py ends here
