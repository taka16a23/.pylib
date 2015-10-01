#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: clientmessage.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""clientmessage -- a parts of xcb2

"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack
from array import array as _array
from enum import IntEnum as _IntEnum

from xcb2.xobj import AtomReplyTypes
from xcb.xproto import Time
from xcb2.xproto.ext.sendevent.eventcode import EventCode
from xcb2.xproto.ext.abstract import CoreSubMethodAbstract


class ClientMessageAbstract(CoreSubMethodAbstract):
    r"""SUMMARY
    """
    # KLUDGE: (Atami) [2014/05/23]
    # 0xffffff EventMask
    mask = 0xffffff
    code = EventCode.ClientMessage
    _mask = _pack('I', 0xffffff)
    _code = _pack('B', EventCode.ClientMessage)

    atomname = ''
    _format = ''

    def __init__(self, parent):
        r"""

        @Arguments:
        - `parent`:
        """
        CoreSubMethodAbstract.__init__(self, parent)
        self._atom = self._connection.core.InternAtom.usecache(
            self.atomname).pack()

    def _get_head_buf(self, window, propagate, sequence_number):
        r"""SUMMARY

        _get_head_buf(window, propagate, sequence_number)

        @Arguments:
        - `window`:
        - `propagate`:
        - `sequence_number`:

        @Return:
        """
        buf = _StringIO()
        buf.write(_pack('=xB2xI', propagate, window))
        buf.write(self._mask)
        buf.write(self._code)
        buf.write(self._format)
        buf.write(_pack('H', sequence_number))
        buf.write(_pack('I', window))
        buf.write(self._atom)
        return buf


class DeleteWindow(ClientMessageAbstract):
    r"""SUMMARY
    """
    atomname = 'WM_PROTOCOLS'
    _format = _pack('B', AtomReplyTypes.get_types('WM_PROTOCOLS').length)

    _dataatomname = 'WM_DELETE_WINDOW'
    _currenttime = _pack('I', Time.CurrentTime)
    _zerofill = _pack('3I', 0, 0, 0)

    def __init__(self, parent):
        r"""

        @Arguments:
        - `parent`:
        """
        ClientMessageAbstract.__init__(self, parent)
        self._dataatom = self._connection.core.InternAtom.usecache(
            self._dataatomname).pack()

    def _getbinary(self, window, time, propagate, sequence_number):
        r"""SUMMARY

        _getbinary(window, time, propagate, sequence_number)

        @Arguments:
        - `window`:
        - `time`:
        - `propagate`:
        - `sequence_number`:

        @Return:
        """
        buf = self._get_head_buf(window, propagate, sequence_number)
        buf.write(self._dataatom)
        if time is None:
            buf.write(self._currenttime)
        else:
            buf.write(_pack('I', time))
        buf.write(self._zerofill)
        return buf.getvalue()

    def __call__(self, window, time=None, propagate=False, sequence_number=0):
        r"""SUMMARY

        __call__(window, time=None, propagate=False, sequence_number=0)

        @Arguments:
        - `window`:
        - `time`:
        - `propagate`:
        - `sequence_number`:

        @Return:
        """
        return self._parent.request(
            self._getbinary(window, time, propagate, sequence_number))


class CloseWindow(ClientMessageAbstract):
    r"""SUMMARY
    """
    atomname = '_NET_CLOSE_WINDOW'
    _format = _pack('B', AtomReplyTypes.get_types('_NET_CLOSE_WINDOW').length)

    _zerofill = _pack('4I', 0, 0, 0, 0)
    _currenttime = _pack('I', Time.CurrentTime)

    def _getbinary(self, window, time, propagate, sequence_number):
        r"""SUMMARY

        _getbinary(window, time, propagate, sequence_number)

        @Arguments:
        - `window`:
        - `time`:
        - `propagate`:
        - `sequence_number`:

        @Return:
        """
        buf = self._get_head_buf(window, propagate, sequence_number)
        if time:
            buf.write(_pack('I', time))
        else:
            buf.write(self._currenttime)
        buf.write(self._zerofill)
        return buf.getvalue()

    def __call__(self, window, time=None, propagate=False, sequence_number=0):
        r"""SUMMARY

        __call__(time=None)

        @Arguments:
        - `time`:

        @Return:
        """
        return self._parent.request(
            self._getbinary(window, time, propagate, sequence_number))


class WindowStateMode(_IntEnum):
    r"""SUMMARY
    """
    Unset  = 0
    Set    = 1
    Toggle = 2


class _NET_WM_STATEAbstract(ClientMessageAbstract):
    r"""SUMMARY
    """

    atomname = '_NET_WM_STATE'
    _format = _pack('B', AtomReplyTypes.get_types('_NET_WM_STATE').length)

    _dataatomnames = ('', )
    _set = _pack('I', WindowStateMode.Set)
    _unset = _pack('I', WindowStateMode.Unset)
    _toggle = _pack('I', WindowStateMode.Toggle)

    def __init__(self, parent):
        r"""SUMMARY

        __init__(parent)

        @Arguments:
        - `parent`:

        @Return:
        """
        ClientMessageAbstract.__init__(self, parent)
        self.atoms = [self._connection.core.InternAtom.usecache(x)
                      for x in self._dataatomnames]
        data = self.atoms[:]
        for _ in range(4 - len(self.atoms)): # zerofill
            data.append(0)
        self._data = str(buffer(_array('I', data)))

    def _getbinary(self, window, propagate, sequence_number, mode):
        r"""SUMMARY

        _getbinary(window, propagate, sequence_number, mode)

        @Arguments:
        - `window`:
        - `propagate`:
        - `sequence_number`:
        - `mode`:

        @Return:
        """
        buf = self._get_head_buf(window, propagate, sequence_number)
        buf.write(mode)
        buf.write(self._data)
        return buf.getvalue()

    def _get_setbinary(self, window, propagate, sequence_number):
        r"""SUMMARY

        _get_setbinary(window, propagate, sequence_number)

        @Arguments:
        - `window`:
        - `propagate`:
        - `sequence_number`:

        @Return:
        """
        return self._getbinary(window, propagate, sequence_number, self._set)

    def _get_unsetbinary(self, window, propagate, sequence_number):
        r"""SUMMARY

        _get_setbinary(window, propagate, sequence_number)

        @Arguments:
        - `window`:
        - `propagate`:
        - `sequence_number`:

        @Return:
        """
        return self._getbinary(window, propagate, sequence_number, self._unset)

    def _get_togglebinary(self, window, propagate, sequence_number):
        r"""SUMMARY

        _get_setbinary(window, propagate, sequence_number)

        @Arguments:
        - `window`:
        - `propagate`:
        - `sequence_number`:

        @Return:
        """
        return self._getbinary(window, propagate, sequence_number, self._toggle)

    def set(self, window, propagate=False, sequence_number=0):
        r"""SUMMARY

        set()

        @Return:
        """
        return self._parent.request(
            self._get_setbinary(window, propagate, sequence_number))

    def unset(self, window, propagate=False, sequence_number=0):
        r"""SUMMARY

        unset()

        @Return:
        """
        return self._parent.request(
            self._get_unsetbinary(window, propagate, sequence_number))

    def toggle(self, window, propagate=False, sequence_number=0):
        r"""SUMMARY

        toggle()

        @Return:
        """
        return self._parent.request(
            self._get_togglebinary(window, propagate, sequence_number))


class FullScreen(_NET_WM_STATEAbstract):
    r"""SUMMARY
    """
    _dataatomnames = ('_NET_WM_STATE_FULLSCREEN', )


class Shade(_NET_WM_STATEAbstract):
    r"""SUMMARY
    """
    _dataatomnames = ('_NET_WM_STATE_SHADED', )


class Above(_NET_WM_STATEAbstract):
    r"""SUMMARY
    """
    _dataatomnames = ('_NET_WM_STATE_ABOVE', )


class Below(_NET_WM_STATEAbstract):
    r"""SUMMARY
    """
    _dataatomnames = ('_NET_WM_STATE_BELOW', )


class Hidden(_NET_WM_STATEAbstract):
    r"""SUMMARY
    """
    _dataatomnames = ('_NET_WM_STATE_HIDDEN', )


class Minimize(_NET_WM_STATEAbstract):
    r"""SUMMARY
    """
    _dataatomnames = ('_NET_WM_ACTION_MINIMIZE', )


class Maximize(_NET_WM_STATEAbstract):
    r"""SUMMARY
    """
    _dataatomnames = ('_NET_WM_STATE_MAXIMIZED_VERT',
                      '_NET_WM_STATE_MAXIMIZED_HORZ')


class ClientMessage(CoreSubMethodAbstract):
    r"""SUMMARY
    """
    # KLUDGE: (Atami) [2014/05/23]
    # 0xffffff EventMask
    mask = 0xffffff
    code = EventCode.ClientMessage
    _mask = _pack('I', 0xffffff)
    _code = _pack('B', EventCode.ClientMessage)

    def __init__(self, parent):
        r"""

        @Arguments:
        - `parent`:
        """
        CoreSubMethodAbstract.__init__(self, parent)
        self.fullscreen = FullScreen(parent)
        self.shade = Shade(parent)
        self.above = Above(parent)
        self.below = Below(parent)
        self.hidden = Hidden(parent)
        self.maximize = Maximize(parent)
        self.close = CloseWindow(parent)
        self.delete = DeleteWindow(parent)

    def _getbinary(self, propagate, destination, format, sequence_number,
                   window, atom, data):
        r"""SUMMARY

        _getbinary(propagate, destination, format, sequence_number, window,
        atom, data)

        @Arguments:
        - `propagate`:
        - `destination`:
        - `format`:
        - `sequence_number`:
        - `window`:
        - `atom`:
        - `data`:

        @Return:
        """
        buf = _StringIO()
        buf.write(_pack('=xB2xI', propagate, destination))
        buf.write(self._mask)
        buf.write(self._code)
        buf.write(_pack('B', format))
        buf.write(_pack('H', sequence_number))
        buf.write(_pack('2I', window, atom))
        buf.write(str(buffer(_array('b', data))))
        return buf.getvalue()

    def __call__(self, propagate, destination, format, sequence_number,
                 window, atom, data):
        r"""SUMMARY

        __call__(propagate, destination, format, sequence_number, window, atom, data)

        @Arguments:
        - `propagate`:
        - `destination`:
        - `format`:
        - `sequence_number`:
        - `window`:
        - `atom`:
        - `data`:

        @Return:
        """
        return self._parent.request(
            self._getbinary(propagate, destination, format, sequence_number,
                 window, atom, data))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# clientmessage.py ends here
