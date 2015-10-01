#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: buttonrelease.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

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
