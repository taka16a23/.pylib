#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: alloccolorcelles.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""alloccolorcelles -- DESCRIPTION

"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request
from xcb2.xproto.ext.abstract import CoreMethodAbstract
from xcb2.xproto import AllocColorCellsCookie, AllocColorCellsReply


__all__ = ['AllocColorCells', 'AllocColorCellsUnchecked', ]


class AllocColorCellsAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xB2xIHH'
    code = 86

    def _getbinary(self, contiguous, cmap, colors, planes):
        r"""SUMMARY

        _getbinary(contiguous, cmap, colors, planes)

        @Arguments:
        - `contiguous`:
        - `cmap`:
        - `colors`:
        - `planes`:

        @Return:
        """
        buf = _StringIO()
        buf.write(_pack(self.fmt, contiguous, cmap, colors, planes))
        return buf.getvalue()

    def __call__(self, contiguous, cmap, colors, planes):
        return self.request(self._getbinary(contiguous, cmap, colors, planes))


class AllocColorCells(AllocColorCellsAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(contiguous, cmap, colors, planes)

        @Arguments:
        - `contiguous`:
        - `cmap`:
        - `colors`:
        - `planes`:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, True),
            AllocColorCellsCookie(), AllocColorCellsReply)


class AllocColorCellsUnchecked(AllocColorCellsAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(contiguous, cmap, colors, planes)

        @Arguments:
        - `contiguous`:
        - `cmap`:
        - `colors`:
        - `planes`:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, False, False),
            AllocColorCellsCookie(), AllocColorCellsReply)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# alloccolorcelles.py ends here
