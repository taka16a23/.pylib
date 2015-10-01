#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: xconnection.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""connection -- DESCRIPTION

"""
from xcb.xcb import connect as baseconnect
from xcb2.xproto.wrapcore import WrapCore
from xcb2.xproto.wreply import WrapSetup
from xcb2.xobj import Window


class SingletonConnectionMeta(type):
    r"""Singleton Connection by display name."""

    _instances = {}

    def __call__(cls, *args, **kwargs):
        key = kwargs.get('display', '')
        if cls not in cls._instances:
            cls._instances[cls] = {}
        if key not in cls._instances[cls]:
            cls._instances[cls][key] = (super(SingletonConnectionMeta, cls)
                                        .__call__(*args, **kwargs))
        return cls._instances[cls][key]


class Connection(object):
    r"""SUMMARY
    """
    __metaclass__ = SingletonConnectionMeta

    def __init__(self, *args, **kwargs):
        r"""

        @Arguments:
        - `*args`:
        - `**kwargs`:
        """
        if args:
            self.display = args[0]
        else:
            self.display = kwargs.get('display', '')
        self.rawconnection = baseconnect(*args, **kwargs)
        self.core = WrapCore(self)
        self.root = self.get_setup().roots[0].root
        # KLUDGE: (Atami) [2014/05/08]
        self.core.load()

    @staticmethod
    def get_instance(*args, **kwargs):
        r"""SUMMARY

        get_instance()

        @Return:
        """
        return Connection(*args, **kwargs)

    def flush(self, ):
        r"""SUMMARY

        flush()

        @Return:
        """
        self.rawconnection.flush()

    def disconnect(self, ):
        r"""SUMMARY

        disconnect()

        @Return:
        """
        self.rawconnection.disconnect()
        instances = SingletonConnectionMeta._instances
        if self.__class__ not in SingletonConnectionMeta._instances:
            return
        if self.display not in SingletonConnectionMeta._instances[self.__class__]:
            return
        del SingletonConnectionMeta._instances[self.__class__][self.display]

    def generate_id(self, ):
        r"""SUMMARY

        generate_id()

        @Return:
        """
        return self.rawconnection.generate_id()

    def get_file_descriptor(self, ):
        r"""SUMMARY

        get_file_descriptor()

        @Return:
        """
        return self.rawconnection.get_file_descriptor()

    def get_maximum_request_length(self, ):
        r"""SUMMARY

        get_maximum_request_length()

        @Return:
        """
        return self.rawconnection.get_maximum_request_length()

    def get_setup(self, ):
        r"""SUMMARY

        get_setup()

        @Return:
        """
        return WrapSetup(self, self.rawconnection.get_setup())

    def has_error(self, ):
        r"""SUMMARY

        has_error()

        @Return:
        """
        return self.rawconnection.has_error()

    def poll_for_event(self, ):
        r"""SUMMARY

        poll_for_event()

        @Return:
        """
        return self.rawconnection.poll_for_event()

    @property
    def pref_screen(self, ):
        r"""SUMMARY

        pref_screen()

        @Return:
        """
        return self.rawconnection.pref_screen

    def prefetch_maximum_request_length(self, ):
        r"""SUMMARY

        prefetch_maximum_request_length()

        @Return:
        """
        return self.rawconnection.prefetch_maximum_request_length()

    def wait_for_event(self, ):
        r"""SUMMARY

        wait_for_event()

        @Return:
        """
        return self.rawconnection.wait_for_event()

    def get_window(self, window):
        r"""SUMMARY

        get_window(window)

        @Arguments:
        - `window`:

        @Return:
        """
        return Window(self, window)

    def get_windowtype(self, window):
        r"""SUMMARY

        get_windowtype()

        @Return:
        """
        return self.get_window(window).get_net_wm_window_type()

    def __call__(self, *args, **kwargs):
        return self.rawconnection(*args, **kwargs)


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
# connection.py ends here
