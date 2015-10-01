#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: atom.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""atom -- DESCRIPTION

"""
from struct import pack as _pack
from xcb2.abstract import ConnectionAbstract


class Atom(ConnectionAbstract):
    r"""SUMMARY
    """
    format = 'I'

    def __init__(self, connection, atom):
        r"""

        @Arguments:
        - `connection`:
        - `atom`:
        """
        ConnectionAbstract.__init__(self, connection)
        self.atom = atom

    def pack(self, ):
        r"""SUMMARY

        pack()

        @Return:
        """
        return _pack(self.format, self.atom)

    def getname(self, ):
        r"""SUMMARY

        getname()

        @Return:
        """
        return self.connection.core.GetAtomNameUnchecked(self.atom)

    def gettype(self, ):
        r"""SUMMARY

        gettype()

        @Return:
        """
        return self.getname().reply().name.gettype()

    def gettypeatom(self, ):
        r"""SUMMARY

        gettypeatom()

        @Return:
        """
        return self.getname().reply().name.gettypeatom()

    def getformat(self, ):
        r"""SUMMARY

        getformat()

        @Return:
        """
        return self.getname().reply().name.getformat()

    def getproperty(self, delete, window, long_offset, long_length):
        r"""SUMMARY

        getproperty(delete, window, long_offset, long_length)

        @Arguments:
        - `delete`:
        - `window`:
        - `long_offset`:
        - `long_length`:

        @Return:
        """
        return self.connection.core.GetPropertyUnchecked(
            delete, window, self.atom, self.gettypeatom(),
            long_offset, long_length)

    def changeproperty(self, mode, window, data_len, data):
        r"""SUMMARY

        changeproperty(mode, window, data_len, data)

        @Arguments:
        - `mode`:
        - `window`:
        - `data_len`:
        - `data`:

        @Return:
        """
        types = self.gettypeatom()
        return self.connection.core.ChangePropertyChecked(
            mode, window, self.atom, types, types.getformat(), data_len, data)

    def deleteproperty(self, window):
        r"""SUMMARY

        deleteproperty(window)

        @Arguments:
        - `window`:

        @Return:
        """
        return self.connection.core.DeletePropertyChecked(
            window, self.atom)

    def convertselection(self, requestor, selection, target, time):
        r"""SUMMARY

        convertselection(requestor, selection, target, time)

        @Arguments:
        - `requestor`:
        - `selection`:
        - `target`:
        - `time`:

        @Return:
        """
        return self.connection.core.ConvertSelectionChecked(
            requestor, selection, target, self.atom, time)

    def __cmp__(self, other):
        if isinstance(other, self.__class__):
            return cmp(self.atom, other.atom)
        return cmp(self.atom, other)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.atom == other.atom
        return self.atom == other

    def __ne__(self, other):
        return not (self == other)

    def __int__(self, ):
        return self.atom

    def __long__(self, ):
        return self.atom.__long__()

    def __hash__(self, ):
        return hash(self.atom)

    def __repr__(self, ):
        return repr(self.atom)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# atom.py ends here
