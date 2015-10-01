#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""reply -- DESCRIPTION

"""
from xcb import Reply, List
from struct import unpack_from as _unpack_from

import wxcb.xobj.atomname as _atomname
import wxcb.xobj.atom
from wxcb.xobj.keysym import Keysym


class WrapReplyAbstract(object):
    r"""WrapReplyAbstract

    WrapReplyAbstract is a object.
    Responsibility:
    """
    def __init__(self, rawreply):
        r"""

        @Arguments:
        - `rawreply`:
        """
        self._rawreply = rawreply


class GetAtomNameReply(Reply):
    def __init__(self, parent, offset=0):
        Reply.__init__(self, parent, offset)
        _unpacked = _unpack_from('xx2x4xH22x', parent, offset)
        self.name_len = _unpacked[0]
        offset += 32
        self.name = _atomname.AtomName(
            str(List(parent, offset, self.name_len, 'b', 1).buf()))


class InternAtomReply(Reply):
    def __init__(self, parent, offset=0):
        Reply.__init__(self, parent, offset)
        _unpacked = _unpack_from('xx2x4xI', parent, offset)
        self.atom = wxcb.xobj.atom.Atom(_unpacked[0])


class GetKeyboardMappingReply(Reply):
    def __init__(self, parent, offset=0):
        Reply.__init__(self, parent, offset)
        (self.keysyms_per_keycode,) = _unpack_from('xB2x4x24x', parent, offset)
        offset += 32
        self.keysyms = [
            Keysym(x) for x in List(parent, offset, self.length, 'I', 4)]





# For Emacs
# Local Variables:
# coding: utf-8
# End:
# reply.py ends here
