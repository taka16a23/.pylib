#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: reply.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""reply -- DESCRIPTION

"""
from xcb import xcb
import cStringIO
from struct import pack, unpack_from
from array import array


class DIRECTFORMAT(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.red_shift, self.red_mask, self.green_shift, self.green_mask, self.blue_shift, self.blue_mask, self.alpha_shift, self.alpha_mask,) = unpack_from('HHHHHHHH', parent, offset)


class PICTFORMINFO(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.id, self.type, self.depth,) = unpack_from('IBB2x', parent, offset)
        offset += 8
        self.direct = DIRECTFORMAT(parent, offset, 16)
        offset += 16
        offset += xcb.type_pad(4, offset)
        (self.colormap,) = unpack_from('I', parent, offset)


class PICTVISUAL(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.visual, self.format,) = unpack_from('II', parent, offset)


class PICTDEPTH(xcb.Struct):
    def __init__(self, parent, offset):
        xcb.Struct.__init__(self, parent, offset)
        base = offset
        (self.depth, self.num_visuals,) = unpack_from('BxH4x', parent, offset)
        offset += 8
        self.visuals = xcb.List(parent, offset, self.num_visuals, PICTVISUAL, 8)
        offset += len(self.visuals.buf())
        xcb._resize_obj(self, offset - base)


class PICTSCREEN(xcb.Struct):
    def __init__(self, parent, offset):
        xcb.Struct.__init__(self, parent, offset)
        base = offset
        (self.num_depths, self.fallback,) = unpack_from('II', parent, offset)
        offset += 8
        self.depths = xcb.List(parent, offset, self.num_depths, PICTDEPTH, -1)
        offset += len(self.depths.buf())
        xcb._resize_obj(self, offset - base)


class INDEXVALUE(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.pixel, self.red, self.green, self.blue, self.alpha,) = unpack_from('IHHHH', parent, offset)


class COLOR(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.red, self.green, self.blue, self.alpha,) = unpack_from('HHHH', parent, offset)


class POINTFIX(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.x, self.y,) = unpack_from('ii', parent, offset)


class LINEFIX(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        self.p1 = POINTFIX(parent, offset, 8)
        offset += 8
        offset += xcb.type_pad(8, offset)
        self.p2 = POINTFIX(parent, offset, 8)


class TRIANGLE(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        self.p1 = POINTFIX(parent, offset, 8)
        offset += 8
        offset += xcb.type_pad(8, offset)
        self.p2 = POINTFIX(parent, offset, 8)
        offset += 8
        offset += xcb.type_pad(8, offset)
        self.p3 = POINTFIX(parent, offset, 8)


class TRAPEZOID(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.top, self.bottom,) = unpack_from('ii', parent, offset)
        offset += 8
        self.left = LINEFIX(parent, offset, 16)
        offset += 16
        offset += xcb.type_pad(16, offset)
        self.right = LINEFIX(parent, offset, 16)


class GLYPHINFO(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.width, self.height, self.x, self.y, self.x_off, self.y_off,) = unpack_from('HHhhhh', parent, offset)


class QueryVersionCookie(xcb.Cookie):
    pass


class QueryVersionReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.major_version, self.minor_version,) = unpack_from('xx2x4xII16x', parent, offset)


class QueryPictFormatsReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.num_formats, self.num_screens, self.num_depths, self.num_visuals, self.num_subpixel,) = unpack_from('xx2x4xIIIII4x', parent, offset)
        offset += 32
        self.formats = xcb.List(parent, offset, self.num_formats, PICTFORMINFO, 28)
        offset += len(self.formats.buf())
        offset += xcb.type_pad(4, offset)
        self.screens = xcb.List(parent, offset, self.num_screens, PICTSCREEN, -1)
        offset += len(self.screens.buf())
        offset += xcb.type_pad(4, offset)
        self.subpixels = xcb.List(parent, offset, self.num_subpixel, 'I', 4)


class QueryPictIndexValuesReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.num_values,) = unpack_from('xx2x4xI20x', parent, offset)
        offset += 32
        self.values = xcb.List(parent, offset, self.num_values, INDEXVALUE, 12)


class TRANSFORM(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.matrix11, self.matrix12, self.matrix13, self.matrix21, self.matrix22, self.matrix23, self.matrix31, self.matrix32, self.matrix33,) = unpack_from('iiiiiiiii', parent, offset)


class QueryFiltersReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.num_aliases, self.num_filters,) = unpack_from('xx2x4xII16x', parent, offset)
        offset += 32
        self.aliases = xcb.List(parent, offset, self.num_aliases, 'H', 2)
        offset += len(self.aliases.buf())
        offset += xcb.type_pad(4, offset)
        self.filters = xcb.List(parent, offset, self.num_filters, STR, -1)


class ANIMCURSORELT(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.cursor, self.delay,) = unpack_from('II', parent, offset)


class SPANFIX(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        (self.l, self.r, self.y,) = unpack_from('iii', parent, offset)


class TRAP(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        self.top = SPANFIX(parent, offset, 12)
        offset += 12
        offset += xcb.type_pad(12, offset)
        self.bot = SPANFIX(parent, offset, 12)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# reply.py ends here
