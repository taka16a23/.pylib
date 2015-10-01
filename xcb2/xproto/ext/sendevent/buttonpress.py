#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""keypress -- a parts of xcb2

"""
from struct import pack as _pack

from xcb.xproto import EventMask
from xcb2.xproto.ext.sendevent.eventcode import EventCode
from xcb2.xproto.ext.sendevent.abstract import EventAbstract


class ButtonPress(EventAbstract):
    r"""SUMMARY
    """
    mask = EventMask.ButtonPress
    code = EventCode.ButtonPress
    _mask = _pack('I', EventMask.ButtonPress)
    _code = _pack('B', EventCode.ButtonPress)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# keypress.py ends here
