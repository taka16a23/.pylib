#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import Sequence

import keysymdef


class Namesym(Sequence):
    """Class Namesym
    """
    # Attributes:
    __slots__ = ('_name', )

    def __init__(self, name):
        r"""

        @Arguments:
        - `name`:
        """
        self._name = str(name)
        if not isinstance(self._name, basestring):
            raise TypeError('name must be basestring type: {}'.format(name))

    # Operations
    def to_sym(self):
        """function to_sym

        returns Keysym
        """
        return keysymdef.Keysymdef.name_to_sym(self)

    def isdefined(self):
        """function ispredefined

        returns bool
        """
        return keysymdef.Keysymdef.isdefined(self)

    def __str__(self):
        """function __str__

        returns str
        """
        return self._name

    def __repr__(self):
        """function __repr__

        returns str
        """
        return '{0.__class__.__name__}("{0._name}")'.format(self)

    def __int__(self):
        """function __int__

        returns int
        """
        return int(self.to_sym())

    def __long__(self):
        """function __long__

        returns long
        """
        return long(self.to_sym())

    def __hash__(self):
        """function __hash__

        returns
        """
        return hash(self._name)

    def __cmp__(self, other):
        """function __cmp__

        other:

        returns
        """
        # if isinstance(other, self.__class__):
            # return cmp(self._name, str(other))
        return cmp(self._name, str(other))

    def __contains__(self, char):
        """function __contains__

        char:

        returns bool
        """
        return char in self._name

    def __len__(self):
        """function __len__

        returns
        """
        return len(self._name)

    def __getitem__(self, index):
        """function __getitem__

        index: int

        returns
        """
        return self._name[index]

    def __getslice__(self, start, end):
        """function __getslice__

        start:
        end:

        returns
        """
        return self._name[start, end]

    def __nonzero__(self):
        """function __nonzero__

        returns bool
        """
        return self.isdefined()

    def __lt__(self, other):
        return self.to_sym() < int(other)

    def __le__(self, other):
        return self.to_sym() <= int(other)

    def __gt__(self, other):
        return self.to_sym() > int(other)

    def __ge__(self, other):
        return self.to_sym() >= int(other)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# namesym.py ends here
