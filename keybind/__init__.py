#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py


"""
import sys
import predicate
from event import NoEventDevice, EventKeyABC, EventHandler, AutoKBDInputDevice
from keymap import KeyMapUpAbstract
import subprocess as _sbp


import wm


__version__ = "0.1.0"

__all__ = [ '' ]

def xfce_launch():
    r"""SUMMARY

    xfce_launch()

    @Return:
    """
    if wm.exists(klass='Xfrun4'):
        win = wm.getwin(klass='Xfrun4')
        if win:
            win.close()
    else:
        active_win = wm.active.ActiveWindow()
        if not 'Emacs' in active_win.klass:
            _sbp.Popen(['xfrun4'])

def nullfunc():
    r"""SUMMARY

    nullfunc()

    @Return:
    """
    pass


class Keybind(EventHandler, KeyMapUpAbstract, EventKeyABC):
    r"""
    """

    timemap = {'<\Control>': 0.2}
    funcmap = {'<\Control>': xfce_launch}

    def __init__(self, device=None):
        r"""

        @Arguments:
        - `device`:
        """
        self.str = ''
        self.lastupkey = ''
        self.lasttime = 0.0

        # set map for key up
        KeyMapUpAbstract.__init__(self)

        # parse device
        readlist = []
        if predicate.isstring(device):
            readlist.append(AutoKBDInputDevice(device))
        elif device is None:
            readlist.append(AutoKBDInputDevice())
        else:
            for dev in device:
                readlist.append(AutoKBDInputDevice(dev))
        EventHandler.__init__(self, rlist=readlist, wlist=(), xlist=())

    def run(self, ):
        r"""SUMMARY

        run()

        @Return:
        """
        try:
            self.handle_event()
        except KeyboardInterrupt:
            print('\n\nKeylogger Keyboard interrupted.')

    def keydown(self, event):
        r"""SUMMARY

        keydown(event)

        @Arguments:
        - `event`:

        @Return:
        """
        pass

    def key_event(self, event):
        r"""SUMMARY

        key_event(event)

        @Arguments:
        - `event`:

        @Return:
        """
        # key up
        if event.value == self._key_up:
            self.keyup(event)
        # # shift key
        # elif self._shift:
        #     self.keyshift(event)
        # # key hold
        # elif event.value == KeyLogger._key_hold:
        #     self.keyhold(event)
        # # down
        # elif event.value == KeyLogger._key_down:
        #     self.keydown(event)
        # # write out
        # if self.str:
        #     self.write()

    def keyup(self, event):
        r"""SUMMARY

        keyup(event)

        @Arguments:
        - `event`:

        @Return:
        """
        str_ = self.getupkey(event.code)
        thistime = event.timestamp()
        if self.lastupkey == str_:
            diff = thistime - self.lasttime
            if  diff <= self.timemap.get(str_, 0.0):
                self.samekey(event)
                self.funcmap.get(str_, nullfunc)()
        self.lastupkey = str_
        self.lasttime = thistime

    def samekey(self, event):
        r"""SUMMARY

        samekey()

        @Return:
        """
        self.funcmap.get(self.getupkey(event.code), nullfunc)()

    def keyshift(self, event):
        r"""SUMMARY

        keyshift(event)

        @Arguments:
        - `event`:

        @Return:
        """
        pass

    def keyhold(self, event):
        r"""SUMMARY

        keyhold(event)

        @Arguments:
        - `event`:

        @Return:
        """
        pass



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
