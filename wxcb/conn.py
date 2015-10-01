#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: conn.py 280 2015-01-29 00:05:31Z t1 $
# $Revision: 280 $
# $Date: 2015-01-29 09:05:31 +0900 (Thu, 29 Jan 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-01-29 09:05:31 +0900 (Thu, 29 Jan 2015) $

r"""xconnection -- DESCRIPTION

"""
from xcb.xcb import connect as baseconnect

import wxcb.xobj.window as _window
import wxcb.xobj.keycode as _keycode


class WrapSCREEN(object):
    r"""WrapSCREEN

    WrapSCREEN is a object.
    Responsibility:
    """
    def __init__(self, rawreply, display):
        r"""

        @Arguments:
        - `rawreply`:
        - `display`:
        """
        self._rawreply = rawreply
        self.display = display

    @property
    def root(self, ):
        r"""SUMMARY

        root()

        @Return:

        @Error:
        """
        return _window.Window(self._rawreply.root, self.display)

    @property
    def default_colormap(self, ):
        r"""SUMMARY

        default_colormap()

        @Return:

        @Error:
        """
        return self._rawreply.default_colormap

    @property
    def white_pixel(self, ):
        r"""SUMMARY

        white_pixel()

        @Return:
        """
        return self._rawreply.white_pixel

    @property
    def black_pixel(self, ):
        r"""SUMMARY

        black_pixel()

        @Return:
        """
        return self._rawreply.black_pixel

    @property
    def current_input_masks(self, ):
        r"""SUMMARY

        current_input_masks()

        @Return:
        """
        return self._rawreply.current_input_masks

    @property
    def width_in_pixels(self, ):
        r"""SUMMARY

        width_in_pixels()

        @Return:
        """
        return self._rawreply.width_in_pixels

    @property
    def height_in_pixels(self, ):
        r"""SUMMARY

        height_in_pixels()

        @Return:
        """
        return self._rawreply.height_in_pixels

    @property
    def width_in_millimeters(self, ):
        r"""SUMMARY

        width_in_millimeters()

        @Return:
        """
        return self._rawreply.width_in_millimeters

    @property
    def height_in_millimeters(self, ):
        r"""SUMMARY

        height_in_millimeters()

        @Return:
        """
        return self._rawreply.height_in_millimeters

    @property
    def min_installed_maps(self, ):
        r"""SUMMARY

        min_installed_maps()

        @Return:
        """
        return self._rawreply.min_installed_maps

    @property
    def max_installed_maps(self, ):
        r"""SUMMARY

        max_installed_maps()

        @Return:
        """
        return self._rawreply.max_installed_maps

    @property
    def root_visual(self, ):
        r"""SUMMARY

        root_visual()

        @Return:
        """
        return self._rawreply.root_visual

    @property
    def backing_stores(self, ):
        r"""SUMMARY

        backing_stores()

        @Return:
        """
        return self._rawreply.backing_stores

    @property
    def save_unders(self, ):
        r"""SUMMARY

        save_unders()

        @Return:
        """
        return self._rawreply.save_unders

    @property
    def root_depth(self, ):
        r"""SUMMARY

        root_depth()

        @Return:
        """
        return self._rawreply.root_depth

    @property
    def allowed_depths_len(self, ):
        r"""SUMMARY

        allowed_depths_len()

        @Return:
        """
        return self._rawreply.allowed_depths_len

    @property
    def allowed_depths(self, ):
        r"""SUMMARY

        allowed_depths()

        @Return:
        """
        return self._rawreply.allowed_depths


class WrapSetup(object):
    r"""WrapSetup

    WrapSetup is a object.
    Responsibility:
    """
    def __init__(self, rawreply, display):
        r"""

        @Arguments:
        - `rawreply`:
        - `display`:
        """
        self._rawreply = rawreply
        self.display = display

    @property
    def status(self, ):
        r"""SUMMARY

        status()

        @Return:
        """
        return self._rawreply.status

    @property
    def protocol_major_version(self, ):
        r"""SUMMARY

        protocol_major_version()

        @Return:
        """
        return self._rawreply.protocol_major_version

    @property
    def protocol_minor_version(self, ):
        r"""SUMMARY

        protocol_minor_version()

        @Return:
        """
        return self._rawreply.protocol_minor_version

    @property
    def length(self, ):
        r"""SUMMARY

        length()

        @Return:
        """
        return self._rawreply.length

    @property
    def release_number(self, ):
        r"""SUMMARY

        release_number()

        @Return:
        """
        return self._rawreply.release_number

    @property
    def resorce_id_base(self, ):
        r"""SUMMARY

        resorce_id_base()

        @Return:
        """
        return self._rawreply.resorce_id_base

    @property
    def resorce_id_mask(self, ):
        r"""SUMMARY

        resorce_id_mask()

        @Return:
        """
        return self._rawreply.resorce_id_mask

    @property
    def motion_buffer_size(self, ):
        r"""SUMMARY

        motion_buffer_size()

        @Return:
        """
        return self._rawreply.motion_buffer_size

    @property
    def vendor_len(self, ):
        r"""SUMMARY

        vendor_len()

        @Return:
        """
        return self._rawreply.vendor_len

    @property
    def maximum_request_length(self, ):
        r"""SUMMARY

        maximum_request_length()

        @Return:
        """
        return self._rawreply.maximum_request_length

    @property
    def roots_len(self, ):
        r"""SUMMARY

        roots_len()

        @Return:
        """
        return self._rawreply.roots_len

    @property
    def pixmap_formats_len(self, ):
        r"""SUMMARY

        pixmap_formats_len()

        @Return:
        """
        return self._rawreply.pixmap_formats_len

    @property
    def image_byte_order(self, ):
        r"""SUMMARY

        image_byte_order()

        @Return:
        """
        return self._rawreply.image_byte_order

    @property
    def bitmap_format_scanline_unit(self, ):
        r"""SUMMARY

        bitmap_format_scanline_unit()

        @Return:
        """
        return self._rawreply.bitmap_format_scanline_unit

    @property
    def bitmap_format_scanline_pad(self, ):
        r"""SUMMARY

        bitmap_format_scanline_pad()

        @Return:
        """
        return self._rawreply.bitmap_format_scanline_pad

    @property
    def min_keycode(self, ):
        r"""SUMMARY

        min_keycode()

        @Return:
        """
        return _keycode.Keycode(self._rawreply.min_keycode)

    @property
    def max_keycode(self, ):
        r"""SUMMARY

        max_keycode()

        @Return:
        """
        return _keycode.Keycode(self._rawreply.max_keycode)

    @property
    def vendor(self, ):
        r"""SUMMARY

        vendor()

        @Return:
        """
        return self._rawreply.vendor

    @property
    def pixmap_formats(self, ):
        r"""SUMMARY

        pixmap_formats()

        @Return:
        """
        return self._rawreply.pixmap_formats

    @property
    def roots(self, ):
        r"""SUMMARY

        roots()

        @Return:
        """
        return [WrapSCREEN(x, self.display) for x in self._rawreply.roots]


class SingletonConnectionMeta(type):
    r"""Singleton Connection by display name."""

    instances = {}

    def __call__(cls, *args, **kwargs):
        if len(args):
            display = args[0]
        else:
            display = kwargs.get('display', '')
        key = str(display)
        if not key in cls.instances:
            cls.instances[key] = (
                super(SingletonConnectionMeta, cls).__call__(*args, **kwargs))
        return cls.instances[key]


class Connection(object):
    r"""Connection

    Connection is a object.
    Responsibility:
    """
    __metaclass__ = SingletonConnectionMeta

    def __init__(self, *args, **kwargs):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        if len(args):
            self.display = args[0]
        else:
            self.display = kwargs.get('display', '')
        self.rawconn = baseconnect(str(self.display))

    @staticmethod
    def get_instance(*args, **kwargs):
        r"""SUMMARY

        get_instance(*args, **kwargs)

        @Arguments:
        - `args`:
        - `kwargs`:

        @Return:

        @Error:
        """
        return Connection(*args, **kwargs)

    @property
    def core(self, ):
        r"""SUMMARY

        core()

        @Return:

        @Error:
        """
        return self.rawconn.core

    def flush(self, ):
        r"""SUMMARY

        flush()

        @Return:

        @Error:
        """
        self.rawconn.flush()

    def disconnect(self, ):
        r"""SUMMARY

        disconnect()

        @Return:

        @Error:
        """
        self.rawconn.disconnect()
        if self.display in self.__metaclass__.instances:
            del self.__metaclass__.instances[self.display]

    def generate_id(self, ):
        r"""SUMMARY

        generate_id()

        @Return:

        @Error:
        """
        return self.rawconn.generate_id()

    def get_file_descriptor(self, ):
        r"""SUMMARY

        get_file_descriptor()

        @Return:

        @Error:
        """
        return self.rawconn.get_file_descriptor()

    def get_maximum_request_length(self, ):
        r"""SUMMARY

        get_maximum_request_length()

        @Return:
        """
        return self.rawconn.get_maximum_request_length()

    def get_setup(self, ):
        r"""SUMMARY

        get_setup()

        @Return:

        @Error:
        """
        return WrapSetup(self.rawconn.get_setup(), self.display)

    def has_error(self, ):
        r"""SUMMARY

        has_error()

        @Return:
        """
        return self.rawconn.has_error()

    def poll_for_event(self, ):
        r"""SUMMARY

        poll_for_event()

        @Return:
        """
        return self.rawconn.poll_for_event()

    @property
    def pref_screen(self, ):
        r"""SUMMARY

        pref_screen()

        @Return:
        """
        return self.rawconn.pref_screen

    def prefetch_maximum_request_length(self, ):
        r"""SUMMARY

        prefetch_maximum_request_length()

        @Return:
        """
        return self.rawconn.prefetch_maximum_request_length()

    def wait_for_event(self, ):
        r"""SUMMARY

        wait_for_event()

        @Return:
        """
        return self.rawconn.wait_for_event()

    def __call__(self, *args, **kwargs):
        return self.rawconn(*args, **kwargs)


def connect(*args, **kwargs):
    r"""SUMMARY

    connection(*args, **kwargs)

    @Arguments:
    - `*args`:
    - `**kwargs`:

    @Return:
    """
    return Connection.get_instance(*args, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# xconnection.py ends here
