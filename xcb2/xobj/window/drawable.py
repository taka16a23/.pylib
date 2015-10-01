#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""drawable -- DESCRIPTION

"""
from xcb2.xobj.geometry import WindowGeometry
from xcb2.xobj.window.resource import Resource


class Drawable(Resource):
    r"""SUMMARY
    """
    def get_geometry(self):
        reply = self.connection.core.GetGeometry(self).reply()
        return WindowGeometry(self.connection, reply, self)

    def create_pixmap(self, width, height, depth):
        pass

    def create_gc(self, **keys):
        pass

    def copy_area(self, gc, src_drawable, src_x, src_y, width, height,
                  dst_x, dst_y):
        pass

    def copy_plane(self, gc, src_drawable, src_x, src_y, width, height,
                   dst_x, dst_y, bit_plane):
        pass

    def poly_point(self, gc, coord_mode, points):
        pass

    def point(self, gc, x, y):
        pass

    def poly_line(self, gc, coord_mode, points):
        pass

    def line(self, gc, x1, y1, x2, y2):
        pass

    def poly_segment(self, gc, segments):
        pass

    def poly_rectangle(self, gc, rectangles):
        pass

    def rectangle(self, gc, x, y, width, height):
        pass

    def poly_arc(self, gc, arcs):
        pass

    def arc(self, gc,  x, y, width, height, angle1, angle2):
        pass

    def fill_poly(self, gc, shape, coord_mode, points):
        pass

    def poly_fill_rectangle(self, gc, rectangles):
        pass

    def fill_rectangle(self, gc, x, y, width, height):
        pass

    def poly_fill_arc(self, gc, arcs):
        pass

    def fill_arc(self, gc,  x, y, width, height, angle1, angle2):
        pass

    def put_image(self, gc, x, y, width, height, format,
                  depth, left_pad, data):
        pass

    def put_pil_image(self, gc, x, y, image):
        pass

    def get_image(self, x, y, width, height, format, plane_mask):
        pass

    def draw_text(self, gc, x, y, text):
        pass

    def poly_text(self, gc, x, y, items):
        pass

    def poly_text_16(self, gc, x, y, items):
        pass

    def image_text(self, gc, x, y, string):
        pass

    def image_text_16(self, gc, x, y, string):
        pass

    def query_best_size(self, item_class, width, height):
        pass



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# drawable.py ends here
