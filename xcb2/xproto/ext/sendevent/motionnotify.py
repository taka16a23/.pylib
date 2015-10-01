#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""motionnotify -- a parts of xcb2

"""
from struct import pack as _pack
from cStringIO import StringIO as _StringIO

from xcb.xproto import EventMask
from xcb2.xproto.ext.sendevent.eventcode import EventCode
from xcb2.xproto.ext.sendevent.abstract import EventAbstract
from xcb2.xproto.ext.abstract import CoreSubMethodAbstract


class ButtonMotion(EventAbstract):
    r"""SUMMARY
    """
    mask = EventMask.ButtonMotion
    code = EventCode.MotionNotify

    _mask = _pack('I', EventMask.ButtonMotion)
    _code = _pack('B', EventCode.MotionNotify)


class Button1Motion(EventAbstract):
    r"""SUMMARY
    """
    mask = EventMask.Button1Motion
    code = EventCode.MotionNotify

    _mask = _pack('I', EventMask.Button1Motion)
    _code = _pack('B', EventCode.MotionNotify)


class Button2Motion(EventAbstract):
    r"""SUMMARY
    """
    mask = EventMask.Button2Motion
    code = EventCode.MotionNotify

    _mask = _pack('I', EventMask.Button2Motion)
    _code = _pack('B', EventCode.MotionNotify)


class Button3Motion(EventAbstract):
    r"""SUMMARY
    """
    mask = EventMask.Button3Motion
    code = EventCode.MotionNotify

    _mask = _pack('I', EventMask.Button3Motion)
    _code = _pack('B', EventCode.MotionNotify)


class Button4Motion(EventAbstract):
    r"""SUMMARY
    """
    mask = EventMask.Button4Motion
    code = EventCode.MotionNotify

    _mask = _pack('I', EventMask.Button4Motion)
    _code = _pack('B', EventCode.MotionNotify)


class Button5Motion(EventAbstract):
    r"""SUMMARY
    """
    mask = EventMask.Button5Motion
    code = EventCode.MotionNotify

    _mask = _pack('I', EventMask.Button5Motion)
    _code = _pack('B', EventCode.MotionNotify)


class MotionNotify(CoreSubMethodAbstract):
    r"""SUMMARY
    """
    code = EventCode.MotionNotify
    _code = _pack('B', EventCode.MotionNotify)

    def __init__(self, parent):
        r"""SUMMARY

        __init__(parent)

        @Arguments:
        - `parent`:

        @Return:
        """
        CoreSubMethodAbstract.__init__(self, parent)
        self.ButtonMotion = ButtonMotion(parent)
        self.Button1Motion = Button1Motion(parent)
        self.Button2Motion = Button2Motion(parent)
        self.Button3Motion = Button3Motion(parent)
        self.Button4Motion = Button4Motion(parent)
        self.Button5Motion = Button5Motion(parent)

    def _getbinary(self, propagate, destination, event_mask, detail,
                   sequence_number, time, root, window, child, root_x, root_y,
                   event_x, event_y, state, samescreen):
        r"""SUMMARY

        _getbinary(propagate, destination, event_mask, detail, sequence_number, time, root, window, child, root_x, root_y, event_x, event_y, state, samescreen)

        @Arguments:
        - `propagate`:
        - `destination`:
        - `event_mask`:
        - `detail`:
        - `sequence_number`:
        - `time`:
        - `root`:
        - `window`:
        - `child`:
        - `root_x`:
        - `root_y`:
        - `event_x`:
        - `event_y`:
        - `state`:
        - `samescreen`:

        @Return:
        """
        buf = _StringIO()
        buf.write(_pack('=xB2xII', propagate, destination, event_mask))
        buf.write(self._code)
        buf.write(_pack('B', detail))
        buf.write(_pack('H', sequence_number))
        buf.write(_pack('4I5HBx', time, root, window, child, root_x, root_y,
                        event_x, event_y, state, samescreen))
        return buf.getvalue()

    def __call__(self, propagate, destination, event_mask, detail,
                   sequence_number, time, root, window, child, root_x, root_y,
                   event_x, event_y, state, samescreen):
        r"""SUMMARY

        __call__()

        @Return:
        """
        return self._parent.request(self._getbinary(
            propagate, destination, event_mask, detail, sequence_number,
            time, root, window, child, root_x, root_y, event_x, event_y,
            state, samescreen))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# motionnotify.py ends here
