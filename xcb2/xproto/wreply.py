#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: wreply.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""wrapreply -- DESCRIPTION

"""
import xcb2
from xcb2.abstract import ConnectionAbstract
from xcb2.xobj import (
    Window, WindowRootType, WindowList, AtomName, Atom, AtomPair)


class WrapReplyAbstract(ConnectionAbstract):
    r"""SUMMARY
    """

    def __init__(self, connection, raw):
        r"""

        @Arguments:
        - `raw`:
        - `connection`:
        """
        ConnectionAbstract.__init__(self, connection)
        self._raw = raw


class WrapGetAtomNameReply(WrapReplyAbstract):
    r"""SUMMARY
    """

    @property
    def name(self, ):
        r"""SUMMARY

        name()

        @Return:
        """
        name = AtomName(self.connection, str(self._raw.name.buf()))
        num = Atom(self.connection, int(self._raw.atom))
        return AtomPair(name, num)

    @property
    def name_len(self, ):
        r"""SUMMARY

        name_len()

        @Return:
        """
        return self._raw.name_len


class WrapInternAtomReply(WrapReplyAbstract):
    r"""SUMMARY
    """

    @property
    def atom(self, ):
        r"""SUMMARY

        atom()

        @Return:
        """
        name = AtomName(self.connection, self._raw.name)
        num = Atom(self.connection, self._raw.atom)
        return AtomPair(name, num)

class WrapQueryTreeReply(WrapReplyAbstract):
    r"""SUMMARY
    """

    @property
    def children(self, ):
        r"""SUMMARY

        children()

        @Return:
        """
        return WindowList(
            [Window(self.connection, x) for x in self._raw.children])

    @property
    def children_len(self, ):
        r"""SUMMARY

        children_len()

        @Return:
        """
        return self._raw.children_len

    @property
    def parent(self, ):
        r"""SUMMARY

        parent()

        @Return:
        """
        return Window(self.connection, self._raw.parent).get_net_wm_window_type()

    @property
    def root(self, ):
        r"""SUMMARY

        root()

        @Return:
        """
        return WindowRootType(Window(self.connection, self._raw.root))


class WrapSCREEN(WrapReplyAbstract):
    r"""SUMMARY
    """

    @property
    def root(self, ):
        r"""SUMMARY

        root()

        @Return:
        """
        return WindowRootType(Window(self.connection, self._raw.root))

    @property
    def default_colormap(self, ):
        r"""SUMMARY

        default_colormap()

        @Return:
        """
        return self._raw.default_colormap

    @property
    def white_pixel(self, ):
        r"""SUMMARY

        white_pixel()

        @Return:
        """
        return self._raw.white_pixel

    @property
    def black_pixel(self, ):
        r"""SUMMARY

        black_pixel()

        @Return:
        """
        return self._raw.black_pixel

    @property
    def current_input_masks(self, ):
        r"""SUMMARY

        current_input_masks()

        @Return:
        """
        return self._raw.current_input_masks

    @property
    def width_in_pixels(self, ):
        r"""SUMMARY

        width_in_pixels()

        @Return:
        """
        return self._raw.width_in_pixels

    @property
    def height_in_pixels(self, ):
        r"""SUMMARY

        height_in_pixels()

        @Return:
        """
        return self._raw.height_in_pixels

    @property
    def width_in_millimeters(self, ):
        r"""SUMMARY

        width_in_millimeters()

        @Return:
        """
        return self._raw.width_in_millimeters

    @property
    def height_in_millimeters(self, ):
        r"""SUMMARY

        height_in_millimeters()

        @Return:
        """
        return self._raw.height_in_millimeters

    @property
    def min_installed_maps(self, ):
        r"""SUMMARY

        min_installed_maps()

        @Return:
        """
        return self._raw.min_installed_maps

    @property
    def max_installed_maps(self, ):
        r"""SUMMARY

        max_installed_maps()

        @Return:
        """
        return self._raw.max_installed_maps

    @property
    def root_visual(self, ):
        r"""SUMMARY

        root_visual()

        @Return:
        """
        return self._raw.root_visual

    @property
    def backing_stores(self, ):
        r"""SUMMARY

        backing_stores()

        @Return:
        """
        return self._raw.backing_stores

    @property
    def save_unders(self, ):
        r"""SUMMARY

        save_unders()

        @Return:
        """
        return self._raw.save_unders

    @property
    def root_depth(self, ):
        r"""SUMMARY

        root_depth()

        @Return:
        """
        return self._raw.root_depth

    @property
    def allowed_depths_len(self, ):
        r"""SUMMARY

        allowed_depths_len()

        @Return:
        """
        return self._raw.allowed_depths_len

    @property
    def allowed_depths(self, ):
        r"""SUMMARY

        allowed_depths()

        @Return:
        """
        return self._raw.allowed_depths


class WrapSetup(WrapReplyAbstract):
    r"""SUMMARY
    """

    @property
    def status(self, ):
        r"""SUMMARY

        status()

        @Return:
        """
        return self._raw.status

    @property
    def protocol_major_version(self, ):
        r"""SUMMARY

        protocol_major_version()

        @Return:
        """
        return self._raw.protocol_major_version

    @property
    def protocol_minor_version(self, ):
        r"""SUMMARY

        protocol_minor_version()

        @Return:
        """
        return self._raw.protocol_minor_version

    @property
    def length(self, ):
        r"""SUMMARY

        length()

        @Return:
        """
        return self._raw.length

    @property
    def release_number(self, ):
        r"""SUMMARY

        release_number()

        @Return:
        """
        return self._raw.release_number

    @property
    def resorce_id_base(self, ):
        r"""SUMMARY

        resorce_id_base()

        @Return:
        """
        return self._raw.resorce_id_base

    @property
    def resorce_id_mask(self, ):
        r"""SUMMARY

        resorce_id_mask()

        @Return:
        """
        return self._raw.resorce_id_mask

    @property
    def motion_buffer_size(self, ):
        r"""SUMMARY

        motion_buffer_size()

        @Return:
        """
        return self._raw.motion_buffer_size

    @property
    def vendor_len(self, ):
        r"""SUMMARY

        vendor_len()

        @Return:
        """
        return self._raw.vendor_len

    @property
    def maximum_request_length(self, ):
        r"""SUMMARY

        maximum_request_length()

        @Return:
        """
        return self._raw.maximum_request_length

    @property
    def roots_len(self, ):
        r"""SUMMARY

        roots_len()

        @Return:
        """
        return self._raw.roots_len

    @property
    def pixmap_formats_len(self, ):
        r"""SUMMARY

        pixmap_formats_len()

        @Return:
        """
        return self._raw.pixmap_formats_len

    @property
    def image_byte_order(self, ):
        r"""SUMMARY

        image_byte_order()

        @Return:
        """
        return self._raw.image_byte_order

    @property
    def bitmap_format_scanline_unit(self, ):
        r"""SUMMARY

        bitmap_format_scanline_unit()

        @Return:
        """
        return self._raw.bitmap_format_scanline_unit

    @property
    def bitmap_format_scanline_pad(self, ):
        r"""SUMMARY

        bitmap_format_scanline_pad()

        @Return:
        """
        return self._raw.bitmap_format_scanline_pad

    @property
    def min_keycode(self, ):
        r"""SUMMARY

        min_keycode()

        @Return:
        """
        return self._raw.min_keycode

    @property
    def max_keycode(self, ):
        r"""SUMMARY

        max_keycode()

        @Return:
        """
        return self._raw.max_keycode

    @property
    def vendor(self, ):
        r"""SUMMARY

        vendor()

        @Return:
        """
        return self._raw.vendor

    @property
    def pixmap_formats(self, ):
        r"""SUMMARY

        pixmap_formats()

        @Return:
        """
        return self._raw.pixmap_formats

    @property
    def roots(self, ):
        r"""SUMMARY

        roots()

        @Return:
        """
        return [WrapSCREEN(self.connection, x) for x in self._raw.roots]


class WrapGetGeometryReply(WrapReplyAbstract):
    r"""SUMMARY
    """

    @property
    def depth(self, ):
        r"""SUMMARY

        depth()

        @Return:
        """
        return self._raw.depth

    @property
    def root(self, ):
        r"""SUMMARY

        root()

        @Return:
        """
        return Window(self.connection, self._raw.root).get_net_wm_window_type()

    @property
    def x(self, ):
        r"""SUMMARY

        x()

        @Return:
        """
        return self._raw.x

    @property
    def y(self, ):
        r"""SUMMARY

        y()

        @Return:
        """
        return self._raw.y

    @property
    def width(self, ):
        r"""SUMMARY

        width()

        @Return:
        """
        return self._raw.width

    @property
    def height(self, ):
        r"""SUMMARY

        height()

        @Return:
        """
        return self._raw.height

    @property
    def border_width(self, ):
        r"""SUMMARY

        border_width()

        @Return:
        """
        return self._raw.border_width


class WrapListPropertyReply(WrapReplyAbstract):
    r"""SUMMARY
    """

    @property
    def atoms_len(self, ):
        r"""SUMMARY

        atoms_len()

        @Return:
        """
        return self._raw.atoms_len

    @property
    def atoms(self, ):
        r"""SUMMARY

        atoms()

        @Return:
        """
        return [self.connection.core.atomidentify(x) for x in self._raw.atoms]


class WrapGetInputFocusReply(WrapReplyAbstract):
    r"""SUMMARY
    """

    @property
    def focus(self, ):
        r"""SUMMARY

        focus()

        @Return:
        """
        return Window(self.connection, self._raw.focus).get_net_wm_window_type()

    @property
    def revert_to(self, ):
        r"""SUMMARY

        revert_to()

        @Return:
        """
        return self._raw.focus


class WrapGetKeyboardMappingReply(WrapReplyAbstract):
    r"""WrapGetKeyboardMappingReply

    WrapGetKeyboardMappingReply is a WrapReplyAbstract.
    Responsibility:
    """
    @property
    def keysyms(self, ):
        r"""SUMMARY

        keysyms()

        @Return:

        @Error:
        """
        import xcb2.xobj.key
        keysym = xcb2.xobj.key.keysym.Keysym
        return [keysym(sym) for sym in self._raw.keysyms]

    @property
    def keysyms_per_keycode(self, ):
        r"""SUMMARY

        keysyms_per_keycode()

        @Return:

        @Error:
        """
        return self._raw.keysyms_per_keycode



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# wrapreply.py ends here
