#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: atomname.py 280 2015-01-29 00:05:31Z t1 $
# $Revision: 280 $
# $Date: 2015-01-29 09:05:31 +0900 (Thu, 29 Jan 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-01-29 09:05:31 +0900 (Thu, 29 Jan 2015) $

r"""atomname -- DESCRIPTION

"""
from array import array as _array


class AtomName(object):
    r"""AtomName

    AtomName is a object.
    Responsibility:
    """
    def __init__(self, name):
        r"""

        @Arguments:
        - `name`:
        """
        self._name = None
        self.set(name)

    def get(self, ):
        r"""SUMMARY

        get()

        @Return:

        @Error:
        """
        return self._name

    def set(self, name):
        r"""SUMMARY

        set()

        @Return:

        @Error:
        """
        self._name = str(name)

    name = property(get, set)

    def pack(self, ):
        r"""SUMMARY

        pack()

        @Return:

        @Error:
        """
        return str(buffer(_array('b', self.name)))

    def get_length(self, ):
        r"""SUMMARY

        get_length()

        @Return:

        @Error:
        """
        return len(self.name)

    def __iter__(self):
        return iter(self.name)

    def __cmp__(self, other):
        """
        self < other return -1
        self > other return 1
        self == other return 0
        """
        if isinstance(other, (self.__class__, )):
            return cmp(self.name, other.get())
        return cmp(self.name, other)

    def __eq__(self, other):
        if isinstance(other, (self.__class__, )):
            return self.name == other.get()
        return self.name == other

    def __ne__(self, other):
        return not self == other

    def __str__(self, ):
        return self.name

    def __len__(self):
        return self.get_length()

    def __getitem__(self, index):
        return self.name[index]

    def __hash__(self, ):
        return hash(self.name)

    def __repr__(self, ):
        return '{0.__class__.__name__}("{0.name}")'.format(self)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# atomname.py ends here
