#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py


"""
import xcb2 as xcb
import cStringIO
from struct import pack, unpack_from
from array import array

from xcb2.render.define import *
from xcb2.render.reply import *
from xcb2.render.error import *


__all__ = [ ]

MAJOR_VERSION = 0
MINOR_VERSION = 11

key = xcb.ExtensionKey('RENDER')


class renderExtension(xcb.Extension):

    def QueryVersion(self, client_major_version, client_minor_version):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', client_major_version, client_minor_version))
        return self.send_request(xcb.Request(buf.getvalue(), 0, False, True),
                                 QueryVersionCookie(),
                                 QueryVersionReply)

    def QueryVersionUnchecked(self, client_major_version, client_minor_version):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', client_major_version, client_minor_version))
        return self.send_request(xcb.Request(buf.getvalue(), 0, False, False),
                                 QueryVersionCookie(),
                                 QueryVersionReply)

    def QueryPictFormats(self, ):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2x', ))
        return self.send_request(xcb.Request(buf.getvalue(), 1, False, True),
                                 QueryPictFormatsCookie(),
                                 QueryPictFormatsReply)

    def QueryPictFormatsUnchecked(self, ):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2x', ))
        return self.send_request(xcb.Request(buf.getvalue(), 1, False, False),
                                 QueryPictFormatsCookie(),
                                 QueryPictFormatsReply)

    def QueryPictIndexValues(self, format):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', format))
        return self.send_request(xcb.Request(buf.getvalue(), 2, False, True),
                                 QueryPictIndexValuesCookie(),
                                 QueryPictIndexValuesReply)

    def QueryPictIndexValuesUnchecked(self, format):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', format))
        return self.send_request(xcb.Request(buf.getvalue(), 2, False, False),
                                 QueryPictIndexValuesCookie(),
                                 QueryPictIndexValuesReply)

    def CreatePictureChecked(self, pid, drawable, format, value_mask, value_list):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIII', pid, drawable, format, value_mask))
        buf.write(str(buffer(array('I', value_list))))
        return self.send_request(xcb.Request(buf.getvalue(), 4, True, True),
                                 xcb.VoidCookie())

    def CreatePicture(self, pid, drawable, format, value_mask, value_list):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIII', pid, drawable, format, value_mask))
        buf.write(str(buffer(array('I', value_list))))
        return self.send_request(xcb.Request(buf.getvalue(), 4, True, False),
                                 xcb.VoidCookie())

    def ChangePictureChecked(self, picture, value_mask, value_list):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', picture, value_mask))
        buf.write(str(buffer(array('I', value_list))))
        return self.send_request(xcb.Request(buf.getvalue(), 5, True, True),
                                 xcb.VoidCookie())

    def ChangePicture(self, picture, value_mask, value_list):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', picture, value_mask))
        buf.write(str(buffer(array('I', value_list))))
        return self.send_request(xcb.Request(buf.getvalue(), 5, True, False),
                                 xcb.VoidCookie())

    def SetPictureClipRectanglesChecked(self, picture, clip_x_origin, clip_y_origin, rectangles_len, rectangles):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIhh', picture, clip_x_origin, clip_y_origin))
        for elt in xcb.Iterator(rectangles, 4, 'rectangles', True):
            buf.write(pack('=hhHH', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 6, True, True),
                                 xcb.VoidCookie())

    def SetPictureClipRectangles(self, picture, clip_x_origin, clip_y_origin, rectangles_len, rectangles):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIhh', picture, clip_x_origin, clip_y_origin))
        for elt in xcb.Iterator(rectangles, 4, 'rectangles', True):
            buf.write(pack('=hhHH', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 6, True, False),
                                 xcb.VoidCookie())

    def FreePictureChecked(self, picture):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', picture))
        return self.send_request(xcb.Request(buf.getvalue(), 7, True, True),
                                 xcb.VoidCookie())

    def FreePicture(self, picture):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', picture))
        return self.send_request(xcb.Request(buf.getvalue(), 7, True, False),
                                 xcb.VoidCookie())

    def CompositeChecked(self, op, src, mask, dst, src_x, src_y, mask_x, mask_y, dst_x, dst_y, width, height):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3xIIIhhhhhhHH', op, src, mask, dst, src_x, src_y, mask_x, mask_y, dst_x, dst_y, width, height))
        return self.send_request(xcb.Request(buf.getvalue(), 8, True, True),
                                 xcb.VoidCookie())

    def Composite(self, op, src, mask, dst, src_x, src_y, mask_x, mask_y, dst_x, dst_y, width, height):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3xIIIhhhhhhHH', op, src, mask, dst, src_x, src_y, mask_x, mask_y, dst_x, dst_y, width, height))
        return self.send_request(xcb.Request(buf.getvalue(), 8, True, False),
                                 xcb.VoidCookie())

    def TrapezoidsChecked(self, op, src, dst, mask_format, src_x, src_y, traps_len, traps):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3xIIIhh', op, src, dst, mask_format, src_x, src_y))
        for elt in xcb.Iterator(traps, 10, 'traps', True):
            buf.write(pack('=iiiiiiiiii', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 10, True, True),
                                 xcb.VoidCookie())

    def Trapezoids(self, op, src, dst, mask_format, src_x, src_y, traps_len, traps):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3xIIIhh', op, src, dst, mask_format, src_x, src_y))
        for elt in xcb.Iterator(traps, 10, 'traps', True):
            buf.write(pack('=iiiiiiiiii', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 10, True, False),
                                 xcb.VoidCookie())

    def TrianglesChecked(self, op, src, dst, mask_format, src_x, src_y, triangles_len, triangles):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3xIIIhh', op, src, dst, mask_format, src_x, src_y))
        for elt in xcb.Iterator(triangles, 6, 'triangles', True):
            buf.write(pack('=iiiiii', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 11, True, True),
                                 xcb.VoidCookie())

    def Triangles(self, op, src, dst, mask_format, src_x, src_y, triangles_len, triangles):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3xIIIhh', op, src, dst, mask_format, src_x, src_y))
        for elt in xcb.Iterator(triangles, 6, 'triangles', True):
            buf.write(pack('=iiiiii', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 11, True, False),
                                 xcb.VoidCookie())

    def TriStripChecked(self, op, src, dst, mask_format, src_x, src_y, points_len, points):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3xIIIhh', op, src, dst, mask_format, src_x, src_y))
        for elt in xcb.Iterator(points, 2, 'points', True):
            buf.write(pack('=ii', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 12, True, True),
                                 xcb.VoidCookie())

    def TriStrip(self, op, src, dst, mask_format, src_x, src_y, points_len, points):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3xIIIhh', op, src, dst, mask_format, src_x, src_y))
        for elt in xcb.Iterator(points, 2, 'points', True):
            buf.write(pack('=ii', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 12, True, False),
                                 xcb.VoidCookie())

    def TriFanChecked(self, op, src, dst, mask_format, src_x, src_y, points_len, points):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3xIIIhh', op, src, dst, mask_format, src_x, src_y))
        for elt in xcb.Iterator(points, 2, 'points', True):
            buf.write(pack('=ii', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 13, True, True),
                                 xcb.VoidCookie())

    def TriFan(self, op, src, dst, mask_format, src_x, src_y, points_len, points):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3xIIIhh', op, src, dst, mask_format, src_x, src_y))
        for elt in xcb.Iterator(points, 2, 'points', True):
            buf.write(pack('=ii', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 13, True, False),
                                 xcb.VoidCookie())

    def CreateGlyphSetChecked(self, gsid, format):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', gsid, format))
        return self.send_request(xcb.Request(buf.getvalue(), 17, True, True),
                                 xcb.VoidCookie())

    def CreateGlyphSet(self, gsid, format):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', gsid, format))
        return self.send_request(xcb.Request(buf.getvalue(), 17, True, False),
                                 xcb.VoidCookie())

    def ReferenceGlyphSetChecked(self, gsid, existing):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', gsid, existing))
        return self.send_request(xcb.Request(buf.getvalue(), 18, True, True),
                                 xcb.VoidCookie())

    def ReferenceGlyphSet(self, gsid, existing):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', gsid, existing))
        return self.send_request(xcb.Request(buf.getvalue(), 18, True, False),
                                 xcb.VoidCookie())

    def FreeGlyphSetChecked(self, glyphset):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', glyphset))
        return self.send_request(xcb.Request(buf.getvalue(), 19, True, True),
                                 xcb.VoidCookie())

    def FreeGlyphSet(self, glyphset):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', glyphset))
        return self.send_request(xcb.Request(buf.getvalue(), 19, True, False),
                                 xcb.VoidCookie())

    def AddGlyphsChecked(self, glyphset, glyphs_len, glyphids, glyphs, data_len, data):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', glyphset, glyphs_len))
        buf.write(str(buffer(array('I', glyphids))))
        for elt in xcb.Iterator(glyphs, 6, 'glyphs', True):
            buf.write(pack('=HHhhhh', *elt))
        buf.write(str(buffer(array('B', data))))
        return self.send_request(xcb.Request(buf.getvalue(), 20, True, True),
                                 xcb.VoidCookie())

    def AddGlyphs(self, glyphset, glyphs_len, glyphids, glyphs, data_len, data):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xII', glyphset, glyphs_len))
        buf.write(str(buffer(array('I', glyphids))))
        for elt in xcb.Iterator(glyphs, 6, 'glyphs', True):
            buf.write(pack('=HHhhhh', *elt))
        buf.write(str(buffer(array('B', data))))
        return self.send_request(xcb.Request(buf.getvalue(), 20, True, False),
                                 xcb.VoidCookie())

    def FreeGlyphsChecked(self, glyphset, glyphs_len, glyphs):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', glyphset))
        buf.write(str(buffer(array('I', glyphs))))
        return self.send_request(xcb.Request(buf.getvalue(), 22, True, True),
                                 xcb.VoidCookie())

    def FreeGlyphs(self, glyphset, glyphs_len, glyphs):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', glyphset))
        buf.write(str(buffer(array('I', glyphs))))
        return self.send_request(xcb.Request(buf.getvalue(), 22, True, False),
                                 xcb.VoidCookie())

    def CompositeGlyphs8Checked(self, op, src, dst, mask_format, glyphset, src_x, src_y, glyphcmds_len, glyphcmds):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3xIIIIhh', op, src, dst, mask_format, glyphset, src_x, src_y))
        buf.write(str(buffer(array('B', glyphcmds))))
        return self.send_request(xcb.Request(buf.getvalue(), 23, True, True),
                                 xcb.VoidCookie())

    def CompositeGlyphs8(self, op, src, dst, mask_format, glyphset, src_x, src_y, glyphcmds_len, glyphcmds):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3xIIIIhh', op, src, dst, mask_format, glyphset, src_x, src_y))
        buf.write(str(buffer(array('B', glyphcmds))))
        return self.send_request(xcb.Request(buf.getvalue(), 23, True, False),
                                 xcb.VoidCookie())

    def CompositeGlyphs16Checked(self, op, src, dst, mask_format, glyphset, src_x, src_y, glyphcmds_len, glyphcmds):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3xIIIIhh', op, src, dst, mask_format, glyphset, src_x, src_y))
        buf.write(str(buffer(array('B', glyphcmds))))
        return self.send_request(xcb.Request(buf.getvalue(), 24, True, True),
                                 xcb.VoidCookie())

    def CompositeGlyphs16(self, op, src, dst, mask_format, glyphset, src_x, src_y, glyphcmds_len, glyphcmds):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3xIIIIhh', op, src, dst, mask_format, glyphset, src_x, src_y))
        buf.write(str(buffer(array('B', glyphcmds))))
        return self.send_request(xcb.Request(buf.getvalue(), 24, True, False),
                                 xcb.VoidCookie())

    def CompositeGlyphs32Checked(self, op, src, dst, mask_format, glyphset, src_x, src_y, glyphcmds_len, glyphcmds):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3xIIIIhh', op, src, dst, mask_format, glyphset, src_x, src_y))
        buf.write(str(buffer(array('B', glyphcmds))))
        return self.send_request(xcb.Request(buf.getvalue(), 25, True, True),
                                 xcb.VoidCookie())

    def CompositeGlyphs32(self, op, src, dst, mask_format, glyphset, src_x, src_y, glyphcmds_len, glyphcmds):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3xIIIIhh', op, src, dst, mask_format, glyphset, src_x, src_y))
        buf.write(str(buffer(array('B', glyphcmds))))
        return self.send_request(xcb.Request(buf.getvalue(), 25, True, False),
                                 xcb.VoidCookie())

    def FillRectanglesChecked(self, op, dst, color, rects_len, rects):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3xI', op, dst))
        for elt in xcb.Iterator(color, 4, 'color', False):
            buf.write(pack('=HHHH', *elt))
        for elt in xcb.Iterator(rects, 4, 'rects', True):
            buf.write(pack('=hhHH', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 26, True, True),
                                 xcb.VoidCookie())

    def FillRectangles(self, op, dst, color, rects_len, rects):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xB3xI', op, dst))
        for elt in xcb.Iterator(color, 4, 'color', False):
            buf.write(pack('=HHHH', *elt))
        for elt in xcb.Iterator(rects, 4, 'rects', True):
            buf.write(pack('=hhHH', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 26, True, False),
                                 xcb.VoidCookie())

    def CreateCursorChecked(self, cid, source, x, y):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIHH', cid, source, x, y))
        return self.send_request(xcb.Request(buf.getvalue(), 27, True, True),
                                 xcb.VoidCookie())

    def CreateCursor(self, cid, source, x, y):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIIHH', cid, source, x, y))
        return self.send_request(xcb.Request(buf.getvalue(), 27, True, False),
                                 xcb.VoidCookie())

    def SetPictureTransformChecked(self, picture, transform):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', picture))
        for elt in xcb.Iterator(transform, 9, 'transform', False):
            buf.write(pack('=iiiiiiiii', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 28, True, True),
                                 xcb.VoidCookie())

    def SetPictureTransform(self, picture, transform):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', picture))
        for elt in xcb.Iterator(transform, 9, 'transform', False):
            buf.write(pack('=iiiiiiiii', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 28, True, False),
                                 xcb.VoidCookie())

    def QueryFilters(self, drawable):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', drawable))
        return self.send_request(xcb.Request(buf.getvalue(), 29, False, True),
                                 QueryFiltersCookie(),
                                 QueryFiltersReply)

    def QueryFiltersUnchecked(self, drawable):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', drawable))
        return self.send_request(xcb.Request(buf.getvalue(), 29, False, False),
                                 QueryFiltersCookie(),
                                 QueryFiltersReply)

    def SetPictureFilterChecked(self, picture, filter_len, filter, values_len, values):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIH2x', picture, filter_len))
        buf.write(str(buffer(array('b', filter))))
        buf.write(str(buffer(array('i', values))))
        return self.send_request(xcb.Request(buf.getvalue(), 30, True, True),
                                 xcb.VoidCookie())

    def SetPictureFilter(self, picture, filter_len, filter, values_len, values):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIH2x', picture, filter_len))
        buf.write(str(buffer(array('b', filter))))
        buf.write(str(buffer(array('i', values))))
        return self.send_request(xcb.Request(buf.getvalue(), 30, True, False),
                                 xcb.VoidCookie())

    def CreateAnimCursorChecked(self, cid, cursors_len, cursors):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', cid))
        for elt in xcb.Iterator(cursors, 2, 'cursors', True):
            buf.write(pack('=II', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 31, True, True),
                                 xcb.VoidCookie())

    def CreateAnimCursor(self, cid, cursors_len, cursors):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', cid))
        for elt in xcb.Iterator(cursors, 2, 'cursors', True):
            buf.write(pack('=II', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 31, True, False),
                                 xcb.VoidCookie())

    def AddTrapsChecked(self, picture, x_off, y_off, traps_len, traps):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIhh', picture, x_off, y_off))
        for elt in xcb.Iterator(traps, 6, 'traps', True):
            buf.write(pack('=iiiiii', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 32, True, True),
                                 xcb.VoidCookie())

    def AddTraps(self, picture, x_off, y_off, traps_len, traps):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xIhh', picture, x_off, y_off))
        for elt in xcb.Iterator(traps, 6, 'traps', True):
            buf.write(pack('=iiiiii', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 32, True, False),
                                 xcb.VoidCookie())

    def CreateSolidFillChecked(self, picture, color):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', picture))
        for elt in xcb.Iterator(color, 4, 'color', False):
            buf.write(pack('=HHHH', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 33, True, True),
                                 xcb.VoidCookie())

    def CreateSolidFill(self, picture, color):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', picture))
        for elt in xcb.Iterator(color, 4, 'color', False):
            buf.write(pack('=HHHH', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 33, True, False),
                                 xcb.VoidCookie())

    def CreateLinearGradientChecked(self, picture, p1, p2, num_stops, stops, colors):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', picture))
        for elt in xcb.Iterator(p1, 2, 'p1', False):
            buf.write(pack('=ii', *elt))
        for elt in xcb.Iterator(p2, 2, 'p2', False):
            buf.write(pack('=ii', *elt))
        buf.write(pack('=I', num_stops))
        buf.write(str(buffer(array('i', stops))))
        for elt in xcb.Iterator(colors, 4, 'colors', True):
            buf.write(pack('=HHHH', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 34, True, True),
                                 xcb.VoidCookie())

    def CreateLinearGradient(self, picture, p1, p2, num_stops, stops, colors):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', picture))
        for elt in xcb.Iterator(p1, 2, 'p1', False):
            buf.write(pack('=ii', *elt))
        for elt in xcb.Iterator(p2, 2, 'p2', False):
            buf.write(pack('=ii', *elt))
        buf.write(pack('=I', num_stops))
        buf.write(str(buffer(array('i', stops))))
        for elt in xcb.Iterator(colors, 4, 'colors', True):
            buf.write(pack('=HHHH', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 34, True, False),
                                 xcb.VoidCookie())

    def CreateRadialGradientChecked(self, picture, inner, outer, inner_radius, outer_radius, num_stops, stops, colors):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', picture))
        for elt in xcb.Iterator(inner, 2, 'inner', False):
            buf.write(pack('=ii', *elt))
        for elt in xcb.Iterator(outer, 2, 'outer', False):
            buf.write(pack('=ii', *elt))
        buf.write(pack('=iiI', inner_radius, outer_radius, num_stops))
        buf.write(str(buffer(array('i', stops))))
        for elt in xcb.Iterator(colors, 4, 'colors', True):
            buf.write(pack('=HHHH', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 35, True, True),
                                 xcb.VoidCookie())

    def CreateRadialGradient(self, picture, inner, outer, inner_radius, outer_radius, num_stops, stops, colors):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', picture))
        for elt in xcb.Iterator(inner, 2, 'inner', False):
            buf.write(pack('=ii', *elt))
        for elt in xcb.Iterator(outer, 2, 'outer', False):
            buf.write(pack('=ii', *elt))
        buf.write(pack('=iiI', inner_radius, outer_radius, num_stops))
        buf.write(str(buffer(array('i', stops))))
        for elt in xcb.Iterator(colors, 4, 'colors', True):
            buf.write(pack('=HHHH', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 35, True, False),
                                 xcb.VoidCookie())

    def CreateConicalGradientChecked(self, picture, center, angle, num_stops, stops, colors):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', picture))
        for elt in xcb.Iterator(center, 2, 'center', False):
            buf.write(pack('=ii', *elt))
        buf.write(pack('=iI', angle, num_stops))
        buf.write(str(buffer(array('i', stops))))
        for elt in xcb.Iterator(colors, 4, 'colors', True):
            buf.write(pack('=HHHH', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 36, True, True),
                                 xcb.VoidCookie())

    def CreateConicalGradient(self, picture, center, angle, num_stops, stops, colors):
        buf = cStringIO.StringIO()
        buf.write(pack('=xx2xI', picture))
        for elt in xcb.Iterator(center, 2, 'center', False):
            buf.write(pack('=ii', *elt))
        buf.write(pack('=iI', angle, num_stops))
        buf.write(str(buffer(array('i', stops))))
        for elt in xcb.Iterator(colors, 4, 'colors', True):
            buf.write(pack('=HHHH', *elt))
        return self.send_request(xcb.Request(buf.getvalue(), 36, True, False),
                                 xcb.VoidCookie())


_events = {
}


xcb._add_ext(key, renderExtension, _events, _ERRORS)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
