#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: changepointercontrol.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""changepointercontrol -- a parts of xcb2

ChangePointerControl

do-acceleration, do-threshold: BOOL
acceleration-numerator, acceleration-denominator: INT16
threshold: INT16

Errors: Value

This request defines how the pointer moves. The acceleration is a multiplier for
movement expressed as a fraction. For example, specifying 3/1 means the pointer
moves three times as fast as normal. The fraction can be rounded arbitrarily by
the server. Acceleration only takes effect if the pointer moves more than
threshold number of pixels at once and only applies to the amount beyond the
threshold. Setting a value to -1 restores the default. Other negative values
generate a Value error, as does a zero value for acceleration-denominator.
"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2 import Request, VoidCookie
from xcb2.xproto.ext.abstract import CoreMethodAbstract


__all__ = ['ChangePointerControl', 'ChangePointerControlChecked', ]


class ChangePointerControlAbstract(CoreMethodAbstract):
    r"""SUMMARY
    """

    fmt = '=xx2xhhhBB'
    code = 105

    def _getbinary(self,
            acceleration_numerator, acceleration_denominator, threshold,
            do_acceleration, do_threshold):
        buf = _StringIO()
        buf.write(_pack(self.fmt, acceleration_numerator,
                        acceleration_denominator, threshold,
                        do_acceleration, do_threshold))
        return buf.getvalue()

        raise NotImplementedError()

    def __call__(self, acceleration_numerator, acceleration_denominator,
                 threshold, do_acceleration, do_threshold):
        """Request ChangePointerControl X protocol.

        @Arguments:
        - `acceleration_numerator`:
        - `acceleration_denominator`:
        - `threshold`:
        - `do_acceleration`:
        - `do_threshold`:

        @Return:
        VoidCookie

        @Error:
        BadValue
        """
        return self.request(self._getbinary(
            acceleration_numerator, acceleration_denominator, threshold,
            do_acceleration, do_threshold))


class ChangePointerControl(ChangePointerControlAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(acceleration_numerator, acceleration_denominator,
        threshold, do_acceleration, do_threshold)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, False), VoidCookie())


class ChangePointerControlChecked(ChangePointerControlAbstract):
    r"""SUMMARY
    """

    def request(self, binary):
        r"""SUMMARY

        request(acceleration_numerator, acceleration_denominator,
        threshold, do_acceleration, do_threshold)

        @Arguments:

        @Return:
        """
        return self._connection.core.send_request(
            Request(binary, self.code, True, True), VoidCookie())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# changepointercontrol.py ends here
