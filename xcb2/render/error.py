#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""error -- DESCRIPTION

"""
from xcb import xcb

__all__ = ['PictFormatError', 'BadPictFormat', 'PictureError', 'BadPicture',
           'PictOpError', 'BadPictOp', 'GlyphSetError', 'BadGlyphSet',
           'GlyphError', 'BadGlyph', '_ERRORS']


class PictFormatError(xcb.Error):
    def __init__(self, parent, offset=0):
        xcb.Error.__init__(self, parent, offset)


class BadPictFormat(xcb.ProtocolException):
    pass


class PictureError(xcb.Error):
    def __init__(self, parent, offset=0):
        xcb.Error.__init__(self, parent, offset)


class BadPicture(xcb.ProtocolException):
    pass


class PictOpError(xcb.Error):
    def __init__(self, parent, offset=0):
        xcb.Error.__init__(self, parent, offset)


class BadPictOp(xcb.ProtocolException):
    pass


class GlyphSetError(xcb.Error):
    def __init__(self, parent, offset=0):
        xcb.Error.__init__(self, parent, offset)


class BadGlyphSet(xcb.ProtocolException):
    pass


class GlyphError(xcb.Error):
    def __init__(self, parent, offset=0):
        xcb.Error.__init__(self, parent, offset)


class BadGlyph(xcb.ProtocolException):
    pass


_ERRORS = {
    0 : (PictFormatError, BadPictFormat),
    1 : (PictureError, BadPicture),
    2 : (PictOpError, BadPictOp),
    3 : (GlyphSetError, BadGlyphSet),
    4 : (GlyphError, BadGlyph),
}



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# error.py ends here
