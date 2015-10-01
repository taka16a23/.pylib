#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: keypress.py 342 2015-07-24 05:07:32Z t1 $
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
