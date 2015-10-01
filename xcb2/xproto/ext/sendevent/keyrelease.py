#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""keyrelease -- a parts of xcb2

"""
from struct import pack as _pack

from xcb.xproto import EventMask
from xcb2.xproto.ext.sendevent.eventcode import EventCode
from xcb2.xproto.ext.sendevent.abstract import EventAbstract


class KeyRelease(EventAbstract):
    r"""SUMMARY
    """
    mask = EventMask.KeyRelease
    code = EventCode.KeyRelease
    _mask = _pack('I', EventMask.KeyRelease)
    _code = _pack('B', EventCode.KeyRelease)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# keyrelease.py ends here
