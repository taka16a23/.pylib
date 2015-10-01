#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""error -- DESCRIPTION

"""
from struct import unpack_from as _unpack_from

from xcb import xcb


__all__ = ['ErrorBase', 'RequestError', 'BadRequest', 'ValueError', 'BadValue',
           'WindowError', 'BadWindow', 'PixmapError', 'BadPixmap', 'AtomError',
           'BadAtom', 'CursorError', 'BadCursor', 'FontError', 'BadFont',
           'MatchError', 'BadMatch', 'DrawableError', 'BadDrawable',
           'AccessError', 'BadAccess', 'AllocError', 'BadAlloc',
           'ColormapError', 'BadColormap', 'GContextError', 'BadGContext',
           'IDChoiceError', 'BadIDChoice', 'NameError', 'BadName',
           'LengthError', 'BadLength', 'ImplementationError',
           'BadImplementation', '_ERRORS']


class ErrorBase(xcb.Error):
    def __init__(self, parent, offset=0):
        xcb.Error.__init__(self, parent, offset)
        _unpacked = _unpack_from('xx2xIHBx', parent, offset)
        self.bad_value =    _unpacked[0]
        self.minor_opcode = _unpacked[1]
        self.major_opcode = _unpacked[2]


class RequestError(ErrorBase):
    """
    """


class BadRequest(xcb.ProtocolException):
    pass


class ValueError(ErrorBase):
    """
    """


class BadValue(xcb.ProtocolException):
    pass


class WindowError(ErrorBase):
    """
    """


class BadWindow(xcb.ProtocolException):
    pass


class PixmapError(ErrorBase):
    r"""SUMMARY
    """


class BadPixmap(xcb.ProtocolException):
    pass


class AtomError(ErrorBase):
    """
    """


class BadAtom(xcb.ProtocolException):
    pass


class CursorError(ErrorBase):
    """
    """

class BadCursor(xcb.ProtocolException):
    pass


class FontError(ErrorBase):
    """
    """


class BadFont(xcb.ProtocolException):
    pass


class MatchError(ErrorBase):
    """
    """


class BadMatch(xcb.ProtocolException):
    pass


class DrawableError(ErrorBase):
    """
    """


class BadDrawable(xcb.ProtocolException):
    pass


class AccessError(ErrorBase):
    """
    """


class BadAccess(xcb.ProtocolException):
    pass


class AllocError(ErrorBase):
    """
    """


class BadAlloc(xcb.ProtocolException):
    pass


class ColormapError(ErrorBase):
    """
    """


class BadColormap(xcb.ProtocolException):
    pass


class GContextError(ErrorBase):
    """
    """


class BadGContext(xcb.ProtocolException):
    pass


class IDChoiceError(ErrorBase):
    """
    """


class BadIDChoice(xcb.ProtocolException):
    pass


class NameError(ErrorBase):
    """
    """


class BadName(xcb.ProtocolException):
    pass


class LengthError(ErrorBase):
    """
    """


class BadLength(xcb.ProtocolException):
    pass


class ImplementationError(ErrorBase):
    """
    """


class BadImplementation(xcb.ProtocolException):
    pass


_ERRORS = {
    1 : (RequestError, BadRequest),
    2 : (ValueError, BadValue),
    3 : (WindowError, BadWindow),
    4 : (PixmapError, BadPixmap),
    5 : (AtomError, BadAtom),
    6 : (CursorError, BadCursor),
    7 : (FontError, BadFont),
    8 : (MatchError, BadMatch),
    9 : (DrawableError, BadDrawable),
    10 : (AccessError, BadAccess),
    11 : (AllocError, BadAlloc),
    12 : (ColormapError, BadColormap),
    13 : (GContextError, BadGContext),
    14 : (IDChoiceError, BadIDChoice),
    15 : (NameError, BadName),
    16 : (LengthError, BadLength),
    17 : (ImplementationError, BadImplementation),
    }



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# error.py ends here
