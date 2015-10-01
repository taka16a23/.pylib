#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""keypress -- a parts of xcb2

"""
from struct import pack as _pack

from xcb.xproto import EventMask
from xcb2.xproto.ext.sendevent.eventcode import EventCode
from xcb2.xproto.ext.sendevent.abstract import EventAbstract


class KeyPress(EventAbstract):
    r"""SUMMARY
    """
    mask = EventMask.KeyPress
    code = EventCode.KeyPress
    _mask = _pack('I', EventMask.KeyPress)
    _code = _pack('B', EventCode.KeyPress)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# keypress.py ends here
