#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""drawable -- DESCRIPTION

"""
from struct import pack as _pack
import wxcb.xobj.resource as _resource
import wxcb.conn


class Drawable(_resource.Resource):
    r"""Drawable

    Drawable is a _resource.Resource.
    Responsibility:
    """

    def pack(self, ):
        r"""SUMMARY

        pack()

        @Return:
        """
        return _pack('I', self.id)

    def getgeometry(self):
        return self.id.getgeometry(self.display)

    def createpixmap(self, depth, pid, width, height):
        return self.id.createpixmap(self.display, depth, pid, width, height)

    def creategc(self, cid, value_mask, value_list):
        return self.id.creategc(self.display, cid, value_mask, value_list)

    def copyarea(self, gc, dst_drawable, src_x, src_y, width, height,
                 dst_x, dst_y):
        return self.id.copyarea(
            self.display, gc, dst_drawable, src_x, src_y, width, height,
            dst_x, dst_y)

    def copyplane(self, gc, dst_drawable, src_x, src_y, width, height,
                   dst_x, dst_y, bit_plane):
        return self.id.copyplane(
            self.display, gc, dst_drawable, src_x, src_y, width, height,
            dst_x, dst_y)

    def polypoint(self, coordinate_mode, gc, points_len, points):
        return self.id.polypoint(
            self.display, coordinate_mode, gc, points_len, points)

    def polyline(self, coordinate_mode, gc, points_len, points):
        return self.id.polyline(
            self.display, coordinate_mode, gc, points_len, points)

    def polysegment(self, gc, segments_len, segments):
        return self.id.polysegment(self.display, gc, segments_len, segments)

    def polyrectangle(self, gc, rectangles_len, rectangles):
        return self.id.polyrectangle(
            self.display, gc, rectangles_len, rectangles)

    def polyarc(self, gc, arcs_len, arcs):
        return self.id.polyarc(self.display, gc, arcs_len, arcs)

    def fillpoly(self, gc, shape, coordinate_mode, points_len, points):
        return self.id.fillpoly(
            self.display, gc, shape, coordinate_mode, points_len, points)

    def polyfillrectangle(self, gc, rectangles_len, rectangles):
        return self.id.polyfillrectangle(
            self.display, gc, rectangles_len, rectangles)

    def polyfillarc(self, gc, arcs_len, arcs):
        return self.id.polyfillarc(self.display, gc, arcs_len, arcs)

    def putimage(self, format, gc, width, height, dst_x, dst_y, left_pad,
                  depth, data_len, data):
        return self.id.putimage(
            self.display, format, gc, width, height, dst_x, dst_y, left_pad,
            depth, data_len, data)

    def getimage(self, format, x, y, width, height, plane_mask):
        return self.id.getimage(
            self.display, format, x, y, width, height, plane_mask)

    def polytext8(self, gc, x, y, items_len, items):
        return self.id.polytext8(self.display, gc, x, y, items_len, items)

    def polytext16(self, gc, x, y, items_len, items):
        return self.id.polytext16(self.display, gc, x, y, items_len, items)

    def imagetext8(self, string_len, gc, x, y, string):
        return self.id.imagetext8(self.display, string_len, gc, x, y, string)

    def imagetext16(self, string_len, gc, x, y, string):
        return self.id.imagetext16(self.display, string_len, gc, x, y, string)

    def querybestsize(self, _class, width, height):
        return self.id.querybestsize(self.display, _class, width, height)




# For Emacs
# Local Variables:
# coding: utf-8
# End:
# drawable.py ends here
