#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""windowproperty -- DESCRIPTION

"""
from xobj.window.window import Window
from xcb2.xobj.atom import AtomPair


class WindowProperty(object):
    r"""SUMMARY
    """

    def __init__(self, atom, window):
        r"""

        @Arguments:
        - `window`:
        """
        if not isinstance(window, Window):
            raise TypeError()
        if not isinstance(atom, AtomPair):
            raise TypeError()
        self._window = window
        self._atom = atom

    def get(self, delete, long_offset, long_length):
        r"""SUMMARY

        getproperty(delete, long_offset, long_length)

        @Arguments:
        - `delete`:
        - `long_offset`:
        - `long_length`:

        @Return:
        """
        return self._window.getproperty(
            delete, self._atom, self._atom.gettypeatom(), long_offset,
            long_length)

    def change(self, mode, data_len, data):
        r"""SUMMARY

        changeproperty(mode, data_len, data)

        @Arguments:
        - `mode`:
        - `data_len`:
        - `data`:

        @Return:
        """
        return self._window.changeproperty(
            mode, self._atom, self._atom.gettypeatom(), self._atom.getformat(),
            data_len, data)

    def delete(self, ):
        r"""SUMMARY

        delete()

        @Return:
        """
        return self._window.deleteproperty(self._atom)

    def convertselection(self, ):
        r"""SUMMARY

        convertselection(request)

        @Arguments:
        - `request`:

        @Return:
        """
        raise NotImplementedError()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# windowproperty.py ends here
