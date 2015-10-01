#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""atompair -- DESCRIPTION

"""
import predicate


class AtomPair(object):
    r"""SUMMARY
    """
    __slots__ = ('name', 'atom')

    def __init__(self, name, atom):
        r"""

        @Arguments:
        - `name`:
        - `atom`:
        """
        self.name = name
        self.atom = atom

    def pack(self, ):
        r"""SUMMARY

        pack()

        @Return:
        """
        return self.packatom()

    def packatom(self, ):
        r"""SUMMARY

        packatom()

        @Return:
        """
        return self.atom.pack()

    def packname(self, ):
        r"""SUMMARY

        packname()

        @Return:
        """
        return self.name.pack()

    def get_namelen(self, ):
        r"""SUMMARY

        get_namelen()

        @Return:
        """
        return self.name.getlength()

    def gettype(self, ):
        r"""SUMMARY

        gettype()

        @Return:
        """
        return self.name.gettype()

    def gettypeatom(self, ):
        r"""SUMMARY

        gettypeatom()

        @Return:
        """
        return self.name.gettypeatom()

    def getformat(self, ):
        r"""SUMMARY

        getformat()

        @Return:
        """
        return self.name.getformat()

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
        return self.atom.getproperty(delete, window, long_offset, long_length)

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
        return self.atom.changeproperty(mode, window, data_len, data)

    def deleteproperty(self, window):
        r"""SUMMARY

        deleteproperty(window)

        @Arguments:
        - `window`:

        @Return:
        """
        return self.atom.deleteproperty(window)

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
        return self.atom.convertselection(requestor, selection, target, time)

    def __cmp__(self, other):
        if isinstance(other, self.__class__):
            return cmp(self.atom, other.atom)
        if predicate.isstring(other):
            return cmp(self.name, other)
        if predicate.isint(other):
            return cmp(self.atom, other)
        return 1

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.atom == other.atom
        if predicate.isint(other):
            return self.atom == other
        if predicate.isstring(other):
            return self.name == other
        return False

    def __ne__(self, other):
        return not (self == other)

    def __int__(self, ):
        return int(self.atom)

    def __long__(self, ):
        return long(self.atom)

    def __str__(self, ):
        return str(self.name)

    def __getitem__(self, key):
        return str(self)[key]

    def __len__(self, ):
        return self.name.getlength()

    def __hash__(self, ):
        return hash(self.atom)

    def __repr__(self, ):
        fmt = "{0.__class__.__name__}(name='{0.name}', atom={0.atom})".format
        return fmt(self)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# atompair.py ends here
