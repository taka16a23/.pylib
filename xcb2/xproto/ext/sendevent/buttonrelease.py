#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""keypress -- a parts of xcb2

"""
from struct import pack as _pack

from xcb.xproto import EventMask
from xcb2.xproto.ext.sendevent.eventcode import EventCode
from xcb2.xproto.ext.sendevent.abstract import EventAbstract


class ButtonRelease(EventAbstract):
    r"""SUMMARY
    """
    mask = EventMask.ButtonRelease
    code = EventCode.ButtonRelease
    _mask = _pack('I', EventMask.ButtonRelease)
    _code = _pack('B', EventCode.ButtonRelease)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# keypress.py ends here
