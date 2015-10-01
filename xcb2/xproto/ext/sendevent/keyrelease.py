#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: keyrelease.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

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
