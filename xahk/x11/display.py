#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""display -- DESCRIPTION

"""
import os

import xcb, xcb.xproto
from xahk.utils.singleton import SingletonMeta


class Display(object):
    r"""Display

    Display is a object.
    Responsibility:

    d=Display(':0.0')
    d2=Display(':0.0')
    d3=Display('')
    d4=Display()
    """
    __metaclass__ = SingletonMeta

    name = os.environ.get('DISPLAY', '')

    @staticmethod
    def get_default_name():
        r"""SUMMARY

        get_default_name()

        @Return:

        @Error:
        """
        return Display.name

    @staticmethod
    def set_default_name(name):
        r"""SUMMARY

        set_default_name(name)

        @Arguments:
        - `name`:

        @Return:

        @Error:
        """
        Display.name = name

    def __init__(self, ):
        r"""

        @Arguments:
        - `name`:
        """
        self._connection = xcb.connect(self.name)
        self.core = self._connection.core

    def disconnect(self, ):
        r"""SUMMARY

        disconnect()

        @Return:

        @Error:
        """
        self._connection.disconnect()

    def get_display_name(self, ):
        r"""SUMMARY

        get_display_name()

        @Return:

        @Error:
        """
        return self.name

    def flush(self, ):
        r"""SUMMARY

        flush()

        @Return:

        @Error:
        """
        self._connection.flush()

    def __str__(self):
        return self._connection

    def __repr__(self):
        return '<{0.__class__.__name__} object at {1}>'.format(self, id(self))

    def generate_id(self, ):
        r"""SUMMARY

        generate_id()

        @Return:

        @Error:
        """
        return self._connection.generate_id()

    def get_file_descriptor(self, ):
        r"""SUMMARY

        get_file_descriptor()

        @Return:

        @Error:
        """
        return self._connection.get_file_descriptor()

    def get_maximum_request_length(self, ):
        r"""SUMMARY

        get_maximum_request_length()

        @Return:

        @Error:
        """
        return self._connection.get_maximum_request_length()

    def get_setup(self, ):
        r"""SUMMARY

        get_setup()

        @Return:

        @Error:
        """
        return self._connection.get_setup()

    def has_error(self, ):
        r"""SUMMARY

        has_error()

        @Return:

        @Error:
        """
        return self._connection.has_error()

    def poll_for_event(self, ):
        r"""SUMMARY

        poll_for_event()

        @Return:

        @Error:
        """
        try:
            return self._connection.poll_for_event()
        except xcb.xproto.BadLength:
            return None

    @property
    def pref_screen(self, ):
        r"""SUMMARY

        pref_screen()

        @Return:

        @Error:
        """
        return self._connection.pref_screen

    def prefetch_maximum_request_length(self, ):
        r"""SUMMARY

        prefetch_maximum_request_length()

        @Return:

        @Error:
        """
        return self._connection.prefetch_maximum_request_length()

    def wait_for_event(self, ):
        r"""SUMMARY

        wait_for_event()

        @Return:

        @Error:
        """
        return self._connection.wait_for_event()

    def __call__(self, *args, **kwargs):
        return self._connection(*args, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# display.py ends here
