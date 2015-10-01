#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: atomtypes.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""atomtypes -- DESCRIPTION

"""
from struct import pack as _pack, unpack as _unpack
from abc import ABCMeta, abstractmethod

from dotavoider import ListDotAvoider
from xcb2.xobj.window import Window, WindowList


__all__ = ['WrapGetPropertyReply', 'AtomType0Reply', 'AtomType8Reply',
           'AtomType32Reply', 'AtomTypeSTRINGReply', 'AtomTypeUTF8STRINGReply',
           'AtomTypeUTF8STRINGLISTReply', 'AtomTypeWINDOWReply',
           'AtomTypeATOMReply', 'AtomTypeCARDINALReply', 'AtomTypeANYReply',
           'AtomTypeNONEReply', 'AtomReplyTypes']


class AtomFromat(int):
    r"""SUMMARY
    """

    def pack(self, ):
        r"""SUMMARY

        pack()

        @Return:
        """
        return _pack('B', self)


class WrapGetPropertyReply(object):
    r"""SUMMARY
    """
    __metaclass__ = ABCMeta

    name = ''
    length = None

    def __init__(self, connection, reply):
        r"""

        @Arguments:
        - `connection`:
        - `reply`:
        - `window`:
        - `property_`:
        """
        self.connection = connection
        self._reply = reply

    @abstractmethod
    def get_value(self, ):
        r"""SUMMARY

        get_value()

        @Return:
        """
        raise StandardError()

    @property
    def bytes_after(self, ):
        r"""SUMMARY

        bytes_after()

        @Return:
        """
        return self._reply.bytes_after

    @property
    def format(self, ):
        r"""SUMMARY

        format()

        @Return:
        """
        return self._reply.format

    @property
    def type(self, ):
        r"""SUMMARY

        type()

        @Return:
        """
        return self.connection.core.InternAtom.usecache(
            self._reply.type).reply()

    @property
    def value(self, ):
        r"""SUMMARY

        value()

        @Return:
        """
        return list(self._reply.value)

    @property
    def value_buf(self, ):
        r"""SUMMARY

        value_buf()

        @Return:
        """
        return self._reply.value.buf()

    @property
    def value_len(self, ):
        r"""SUMMARY

        value_len()

        @Return:
        """
        return self._reply.value_len

    def get_offset(self, ):
        r"""SUMMARY

        get_offset()

        @Return:
        """
        return self._reply.value_len / 4

    def get_bytes_after(self, ):
        r"""SUMMARY

        get_after_value()

        @Return:
        """
        if self.bytes_after == 0:
            return None
        return self.connection.core.GetProperty.getproperty(
            self._reply.property, self._reply.window, self.get_offset(),
            self.bytes_after / 4 + 1 # length
            ).reply()

    def get_full_value(self, ):
        r"""SUMMARY

        get_full_value()

        @Return:
        """
        value = self.get_value()
        after = self.get_bytes_after()
        if after is not None:
            value += after.get_value()
        return value


class AtomType0Reply(WrapGetPropertyReply):
    r"""SUMMARY
    """
    length = AtomFromat(0)

    def get_value(self, ):
        r"""SUMMARY

        get_value()

        @Return:
        """
        return self.value_buf


class AtomType8Reply(WrapGetPropertyReply):
    r"""SUMMARY
    """
    length = AtomFromat(8)

    def get_value(self, ):
        r"""SUMMARY

        get_value()

        @Return:
        """
        return str(self.value_buf)


class AtomType32Reply(WrapGetPropertyReply):
    r"""SUMMARY
    """
    length = AtomFromat(32)

    def get_offset(self, ):
        r"""SUMMARY

        get_offset()

        @Return:
        """
        return self._reply.value_len

    def get_value(self, ):
        r"""SUMMARY

        get_value()

        @Return:
        """
        return list(_unpack('I' * self.value_len, self.value_buf))


class AtomTypeSTRINGReply(AtomType8Reply):
    r"""SUMMARY
    """
    name = 'STRING'


class AtomTypeUTF8STRINGReply(AtomType8Reply):
    r"""SUMMARY
    """
    name = 'UTF8_STRING'


class AtomTypeUTF8STRINGLISTReply(AtomType8Reply):
    r"""SUMMARY
    """
    name = 'UTF8_STRING[]'

    def get_value(self, ):
        r"""SUMMARY

        get_result()

        @Return:
        """
        result, append = ListDotAvoider().append
        chr_ = ''
        for ord_ in self.value:
            if not ord_:
                append(chr_)
                chr_ = ''
            else:
                chr_ += chr(ord_)
        return result


class AtomTypeWINDOWReply(AtomType32Reply):
    r"""SUMMARY
    """
    name = 'WINDOW'

    def get_value(self, ):
        r"""SUMMARY

        get_value()

        @Return:
        """
        values = _unpack('I' * self.value_len, self.value_buf)
        return WindowList([Window(self.connection, x) for x in values])


class AtomTypeATOMReply(AtomType32Reply):
    r"""SUMMARY
    """
    name = 'ATOM'

    def get_value(self, ):
        r"""SUMMARY

        get_result()

        @Return:
        """
        values = _unpack('I' * self.value_len, self.value_buf)
        return [self.connection.core.atomidentify(x) for x in values]


class AtomTypeCARDINALReply(AtomType32Reply):
    r"""SUMMARY
    """
    name = 'CARDINAL'


class AtomTypeANYReply(AtomType32Reply):
    r"""SUMMARY
    """
    name = 'ANY'


class AtomTypeNONEReply(AtomType32Reply):
    r"""SUMMARY
    """

    def get_value(self, ):
        r"""SUMMARY

        get_value()

        @Return:
        """
        raise NotImplementedError()


BUILTIN_ATOMS = {
    'WM_NAME'             : AtomTypeSTRINGReply,
    'WM_LOCALE_NAME'      : AtomTypeSTRINGReply,
    # 'WM_HINTS'            : ('', ),
    'WM_ICON_NAME'        : AtomTypeSTRINGReply,
    'WM_CLASS'            : AtomTypeSTRINGReply,
    'WM_TRANSIENT_FOR'    : AtomTypeWINDOWReply,
    'WM_PROTOCOLS'        : AtomTypeATOMReply,
    'WM_COLORMAP_WINDOWS' : AtomTypeWINDOWReply,
    'WM_CLIENT_MACHINE'   : AtomTypeSTRINGReply,
    # 'WM_NORMAL_HINTS': ('WM_SIZE_HINTS', ),
    }

BASE_ATOMS = {
    'WM_STATE'                   : AtomTypeCARDINALReply,

    '_WIN_WORKSPACE'             : AtomTypeCARDINALReply,
    '_WIN_STATE'                 : AtomTypeCARDINALReply,
    '_NET_SUPPORTED'             : AtomTypeATOMReply,
    '_NET_CLIENT_LIST'           : AtomTypeWINDOWReply,
    '_NET_CLIENT_LIST_STACKING'  : AtomTypeWINDOWReply,
    '_NET_NUMBER_OF_DESKTOPS'    : AtomTypeCARDINALReply,
    '_NET_DESKTOP_GEOMETRY'      : AtomTypeCARDINALReply,
    '_NET_DESKTOP_VIEWPORT'      : AtomTypeCARDINALReply,
    '_NET_CURRENT_DESKTOP'       : AtomTypeCARDINALReply,
    '_NET_DESKTOP_NAMES'         : AtomTypeUTF8STRINGLISTReply,
    '_NET_ACTIVE_WINDOW'         : AtomTypeWINDOWReply,
    '_NET_WORKAREA'              : AtomTypeCARDINALReply,
    '_NET_SUPPORTING_WM_CHECK'   : AtomTypeWINDOWReply,
    '_NET_VIRTUAL_ROOTS'         : AtomTypeWINDOWReply,
    '_NET_DESKTOP_LAYOUT'        : AtomTypeCARDINALReply,
    '_NET_SHOWING_DESKTOP'       : AtomTypeCARDINALReply,

    '_NET_CLOSE_WINDOW'          : AtomTypeNONEReply,
    '_NET_MOVERESIZE_WINDOW'     : AtomTypeNONEReply,
    '_NET_WM_MORERESIZE'         : AtomTypeNONEReply,
    '_NET_RESTACK_WINDOW'        : AtomTypeNONEReply,
    '_NET_REQUEST_FRAME_EXTENTS' : AtomTypeCARDINALReply,

    '_NET_WM_NAME'               : AtomTypeUTF8STRINGReply,
    '_NET_WM_VISIBLE_NAME'       : AtomTypeUTF8STRINGReply,
    '_NET_WM_ICON_NAME'          : AtomTypeUTF8STRINGReply,
    '_NET_WM_VISIBLE_ICON_NAME'  : AtomTypeUTF8STRINGReply,
    '_NET_WM_DESKTOP'            : AtomTypeCARDINALReply,
    '_NET_WM_WINDOW_TYPE'        : AtomTypeATOMReply,
    '_NET_WM_STATE'              : AtomTypeATOMReply,
    '_NET_WM_ALLOWED_ACTIONS'    : AtomTypeATOMReply,
    '_NET_WM_STRUT'              : AtomTypeCARDINALReply,
    '_NET_WM_STRUT_PARTIAL'      : AtomTypeCARDINALReply,
    '_NET_WM_ICON_GEOMETRY'      : AtomTypeCARDINALReply,
    '_NET_WM_ICON'               : AtomTypeCARDINALReply,
    '_NET_WM_PID'                : AtomTypeCARDINALReply,
    '_NET_WM_HANDLED_ICONS'      : AtomTypeCARDINALReply,
    '_NET_WM_USER_TIME'          : AtomTypeCARDINALReply,
    '_NET_WM_USER_TIME_WINDOW'   : AtomTypeCARDINALReply,
    '_NET_FRAME_EXTENTS'         : AtomTypeCARDINALReply,

    '_OB_APP_TYPE'               : AtomTypeUTF8STRINGReply,
    }

WINDOW_TYPES = {
    '_NET_WM_WINDOW_TYPE_DESKTOP'       : AtomTypeATOMReply,
    '_NET_WM_WINDOW_TYPE_DOCK'          : AtomTypeATOMReply,
    '_NET_WM_WINDOW_TYPE_TOOLBAR'       : AtomTypeATOMReply,
    '_NET_WM_WINDOW_TYPE_MENU'          : AtomTypeATOMReply,
    '_NET_WM_WINDOW_TYPE_UTILITY'       : AtomTypeATOMReply,
    '_NET_WM_WINDOW_TYPE_SPLASH'        : AtomTypeATOMReply,
    '_NET_WM_WINDOW_TYPE_DIALOG'        : AtomTypeATOMReply,
    '_NET_WM_WINDOW_TYPE_DROPDOWN_MENU' : AtomTypeATOMReply,
    '_NET_WM_WINDOW_TYPE_POPUP_MENU'    : AtomTypeATOMReply,
    '_NET_WM_WINDOW_TYPE_TOOLTIP'       : AtomTypeATOMReply,
    '_NET_WM_WINDOW_TYPE_NOTIFICATION'  : AtomTypeATOMReply,
    '_NET_WM_WINDOW_TYPE_COMBO'         : AtomTypeATOMReply,
    '_NET_WM_WINDOW_TYPE_DND'           : AtomTypeATOMReply,
    '_NET_WM_WINDOW_TYPE_NORMAL'        : AtomTypeATOMReply,
    }

WINDOW_STATES = {
    '_NET_WM_STATE_MODAL'             : AtomTypeATOMReply,
    '_NET_WM_STATE_STICKY'            : AtomTypeATOMReply,
    '_NET_WM_STATE_MAXIMIZED_VERT'    : AtomTypeATOMReply,
    '_NET_WM_STATE_MAXIMIZED_HORZ'    : AtomTypeATOMReply,
    '_NET_WM_STATE_SHADED'            : AtomTypeATOMReply,
    '_NET_WM_STATE_SKIP_TASKBAR'      : AtomTypeATOMReply,
    '_NET_WM_STATE_SKIP_PAGER'        : AtomTypeATOMReply,
    '_NET_WM_STATE_HIDDEN'            : AtomTypeATOMReply,
    '_NET_WM_STATE_FULLSCREEN'        : AtomTypeATOMReply,
    '_NET_WM_STATE_ABOVE'             : AtomTypeATOMReply,
    '_NET_WM_STATE_BELOW'             : AtomTypeATOMReply,
    '_NET_WM_STATE_DEMANDS_ATTENTION' : AtomTypeATOMReply,
    }

WINDOW_ALLOWED_ACTIONS = {
    '_NET_WM_ACTION_MOVE'           : AtomTypeATOMReply,
    '_NET_WM_ACTION_RESIZE'         : AtomTypeATOMReply,
    '_NET_WM_ACTION_MINIMIZE'       : AtomTypeATOMReply,
    '_NET_WM_ACTION_SHADE'          : AtomTypeATOMReply,
    '_NET_WM_ACTION_STICK'          : AtomTypeATOMReply,
    '_NET_WM_ACTION_MAXIMIZE_HORZ'  : AtomTypeATOMReply,
    '_NET_WM_ACTION_MAXIMIZE_VERT'  : AtomTypeATOMReply,
    '_NET_WM_ACTION_FULLSCREEN'     : AtomTypeATOMReply,
    '_NET_WM_ACTION_CHANGE_DESKTOP' : AtomTypeATOMReply,
    '_NET_WM_ACTION_CLOSE'          : AtomTypeATOMReply,
    '_NET_WM_ACTION_ABOVE'          : AtomTypeATOMReply,
    '_NET_WM_ACTION_BELOW'          : AtomTypeATOMReply,
    }


ATOMTYPES = {}
ATOMTYPES.update(BUILTIN_ATOMS)
ATOMTYPES.update(BASE_ATOMS)
ATOMTYPES.update(WINDOW_TYPES)
ATOMTYPES.update(WINDOW_STATES)
ATOMTYPES.update(WINDOW_ALLOWED_ACTIONS)


class AtomReplyTypes(object):
    r"""
    """
    atomtypes = ATOMTYPES.copy()

    @staticmethod
    def get_types(name):
        r"""SUMMARY

        get_types_length()

        @Return:
        """
        return AtomReplyTypes.atomtypes.get(str(name), AtomType32Reply)

    @staticmethod
    def get_name(name):
        r"""SUMMARY

        get_types(default=0)

        @Arguments:
        - `default`:

        @Return:
        """
        return AtomReplyTypes.atomtypes.get(str(name)).name

    @staticmethod
    def get_length(name):
        r"""SUMMARY

        get_length()

        @Return:
        """
        return AtomReplyTypes.atomtypes.get(str(name)).length


del (ATOMTYPES, BUILTIN_ATOMS, BASE_ATOMS, WINDOW_TYPES, WINDOW_STATES,
     WINDOW_ALLOWED_ACTIONS)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# atomtypes.py ends here
