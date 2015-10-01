#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""display -- DESCRIPTION

"""
import os

import xcb, xcb.xproto


class display_multiton(object):
    r"""multiton_display

    multiton_display is a object.
    Responsibility:
    """
    __instances = {}

    def __call__(self, cls):
        def getinstance(display_name='', *args, **kwargs):
            dispname = display_name or os.environ.get('DISPLAY', '')
            if dispname not in display_multiton.__instances:
                display_multiton.__instances[dispname] = cls(
                    dispname, *args, **kwargs)
            return display_multiton.__instances[dispname]
        return getinstance

    @staticmethod
    def instances():
        r"""SUMMARY

        instances()

        @Return:

        @Error:
        """
        return display_multiton.__instances

    @staticmethod
    def get_instances(klass):
        r"""SUMMARY

        get_instances(cls)

        @Arguments:
        - `cls`:

        @Return:

        @Error:
        """
        return display_multiton.instances().get(klass, None)

    @classmethod
    def delete(cls, display_name):
        r"""SUMMARY

        delete()

        @Return:

        @Error:
        """
        del display_multiton.__instances[display_name]


@display_multiton()
class Display(object):
    r"""Display

    Display is a object.
    Responsibility:

    d=Display(':0.0')
    d2=Display(':0.0')
    d3=Display('')
    d4=Display()
    """

    def __init__(self, name=''):
        r"""

        @Arguments:
        - `name`:
        """
        self._display_name = name
        self._connection = xcb.connect(self._display_name)
        self.core = self._connection.core

    def __del__(self):
        """
        INTERNAL COMMENT
        Do not imprement `raise'!!
        """
        display_multiton.delete(self._display_name)

    def disconnect(self, ):
        r"""SUMMARY

        disconnect()

        @Return:

        @Error:
        """
        self.__del__()

    def get_display_name(self, ):
        r"""SUMMARY

        get_display_name()

        @Return:

        @Error:
        """
        return self._display_name

    def flush(self, ):
        r"""SUMMARY

        flush()

        @Return:

        @Error:
        """
        self._connection.flush()

    def __str__(self):
        return self._connection

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
        return self._connection.poll_for_event()

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
