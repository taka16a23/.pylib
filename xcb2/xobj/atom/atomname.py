#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""atomname -- DESCRIPTION

"""
from array import array as _array
from xcb2.abstract import ConnectionAbstract
from xcb2.xobj.atom.atomtypes import AtomReplyTypes


class AtomName(ConnectionAbstract):
    r"""SUMMARY
    """
    format = 'b'

    def __init__(self, connection, name):
        r"""

        @Arguments:
        - `connection`:
        - `name`:
        """
        ConnectionAbstract.__init__(self, connection)
        self.name = name

    def pack(self, ):
        r"""SUMMARY

        pack()

        @Return:
        """
        return str(buffer(_array('b', self.name)))

    def intern(self, only_if_exists):
        r"""SUMMARY

        intern(only_if_exists)

        @Arguments:
        - `only_if_exists`:

        @Return:
        """
        return self.connection.core.InternAtomUnchecked(
            only_if_exists, len(self), self.name)

    def gettype(self, ):
        r"""SUMMARY

        gettype()

        @Return:
        """
        return AtomReplyTypes.get_types(self.name)

    def gettypeatom(self, ):
        r"""SUMMARY

        gettypeatom()

        @Return:
        """
        return self.connection.core.InternAtom.usecache(self.gettype().name)

    def getformat(self, ):
        r"""SUMMARY

        getformat()

        @Return:
        """
        return self.gettype().length

    def getlength(self, ):
        r"""SUMMARY

        getlength()

        @Return:
        """
        return len(self.name)

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
        atom = self.intern(True).reply().atom
        return atom.getproperty(delete, window, long_offset, long_length)

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
        atom = self.intern(True).reply().atom
        return atom.changeproperty(mode, window, data_len, data)

    def deleteproperty(self, window):
        r"""SUMMARY

        deleteproperty(window)

        @Arguments:
        - `window`:

        @Return:
        """
        atom = self.intern(True).reply().atom
        return atom.deleteproperty(window)

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
        atom = self.intern(True).reply().atom
        return atom.convertselection(requestor, selection, target, time)

    def __iter__(self):
        for i in range(0, len(self)):
            yield self.name[i]
        raise StopIteration()

    def __cmp__(self, other):
        if isinstance(other, self.__class__):
            return cmp(self.name, other.name)
        return cmp(self.name, other)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.name == other.name
        return self.name == other

    def __ne__(self, other):
        return not (self == other)

    def __str__(self, ):
        return self.name

    def __len__(self, ):
        return self.getlength()

    def __getitem__(self, index):
        return self.name[index]

    def __hash__(self, ):
        return hash(self.name)

    def __repr__(self, ):
        return repr(self.name)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# atomname.py ends here
