#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: atom.py 306 2015-02-07 03:48:07Z t1 $
# $Revision: 306 $
# $Date: 2015-02-07 12:48:07 +0900 (Sat, 07 Feb 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-02-07 12:48:07 +0900 (Sat, 07 Feb 2015) $

r"""atom -- DESCRIPTION

"""
from struct import pack as _pack
from userint import UserInt as _UserInt

# from wxcb.conn import connect
from wxcb.protocol.xproto.requests import GetAtomName


class Atom(_UserInt):
    r"""Atom

    Atom is a UserInt.
    Responsibility:
    """
    def pack(self, ):
        r"""SUMMARY

        pack()

        @Return:

        @Error:
        """
        return _pack('I', self._value)

    def getname(self, display):
        r"""SUMMARY

        getname(display)

        @Arguments:
        - `display`:

        @Return:

        @Error:
        """
        # return connect(display).core.GetAtomName(self._value)
        return GetAtomName(self._value, display=display).request()

    def deleteproperty(self, display, window):
        r"""SUMMARY

        deleteproperty(display, window)

        @Arguments:
        - `display`:
        - `window`:

        @Return:

        @Error:
        """
        # return connect(display).core.DeleteProperty(window, self._value)

    def changeproperty(self, display, mode, window, type_, format_, data_len,
                       data):
        r"""SUMMARY

        changeproperty(display, mode, window, type_, format_, data_len, data)

        @Arguments:
        - `display`:
        - `mode`:
        - `window`:
        - `type_`:
        - `format_`:
        - `data_len`:
        - `data`:

        @Return:

        @Error:
        """
        # return connect(display).core.ChangeProperty(
            # mode, window, self._value, type_, format_, data_len, data)

    def convertselection(self, display, requestor, selection, target, time):
        r"""SUMMARY

        convertselection(display, requestor, selection, target, time)

        @Arguments:
        - `display`:
        - `requestor`:
        - `selection`:
        - `target`:
        - `time`:

        @Return:

        @Error:
        """
        # return connect(display).core.ConvertSelection(
            # requestor, selection, target, self._value, time)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# atom.py ends here
