#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: parameter.py 227 2014-09-13 08:15:46Z t1 $
# $Revision: 227 $
# $Date: 2014-09-13 17:15:46 +0900 (Sat, 13 Sep 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-09-13 17:15:46 +0900 (Sat, 13 Sep 2014) $


class ParameterLengthError(StandardError):
    r"""ParameterLenghtError

    ParameterLenghtError is a StandardError.
    Responsibility:
    """
    def __init__(self, parameter, length):
        r"""

        @Arguments:
        - `parameter`:
        - `length`:
        """
        StandardError.__init__(self, )
        self._parameter = parameter
        self._length = length

    def __str__(self):
        return '"{0._parameter}" length than {0._length}'.format(self)


class Parameter(object):
    """Class Parameter
    """
    # Attributes:
    _length = 4
    _fill = ' '

    def __init__(self, parameter):
        r"""

        @Arguments:
        - `parameter`:
        """
        self._parameter = ''.ljust(self._length, self._fill)
        self.set(parameter)

    # Operations
    def _get_trimed(self):
        """function _get_trimed

        returns string
        """
        return self._parameter.replace(' ', '')

    def get(self):
        """function get

        returns
        """
        return self._parameter

    def set(self, param):
        """function set

        param:

        returns
        """
        parameter = str(param).replace(' ', '').ljust(self._length, self._fill)
        if self._length < len(parameter):
            raise ParameterLengthError(param, self._length)
        self._parameter = parameter

    def __int__(self):
        """function __int__

        returns int
        """
        return int(self._get_trimed())

    def __long__(self):
        """function __long__

        returns long
        """
        return long(int(self))

    def __add__(self, other):
        """function __add__

        other:

        returns Parameter
        """
        return self.__class__(int(self) + int(other))

    def __sub__(self, other):
        """function __sub__

        other:

        returns Parameter
        """
        return self.__class__(int(self) - int(other))

    def __str__(self):
        """function __str__

        returns string
        """
        return self._parameter

    def __cmp__(self, other):
        """function __cmp__

        other:

        returns
        """
        if isinstance(other, (self.__class__, str)):
            return cmp(self._parameter, str(other))
        return cmp(self._parameter, other)

    def __div__(self, other):
        """function __div__

        other:

        returns
        """
        return self.__class__(int(self) / int(other))

    def __hash__(self):
        """function __hash__

        returns
        """
        return hash(self._parameter)

    def __repr__(self):
        """function __repr__

        returns string
        """
        return '{0.__class__.__name__}("{0._parameter}")'.format(self)

    def __getitem__(self, key):
        """function __getitem__

        key: int

        returns string
        """
        return self._parameter[key]

    def __setitem__(self, key, val):
        """function __setitem__

        key: int
        val: string

        returns void
        """
        value = str(val)
        if not 1 == len(value):
            raise ValueError('{} must 1 length'.format(val))
        lis = list(self._parameter)
        lis[key] = value
        self.set(''.join(lis))

    def __eq__(self, other):
        """function __eq__

        other:

        returns bool
        """
        return self._parameter == str(other)

    def __ne__(self, other):
        """function __ne__

        other:

        returns bool
        """
        return self._parameter != str(other)

    def __lt__(self, other):
        """function __lt__

        other:

        returns bool
        """
        return int(self) < int(other)

    def __le__(self, other):
        """function __le__

        other:

        returns bool
        """
        return int(self) <= int(other)

    def __gt__(self, other):
        """function __gt__

        other:

        returns bool
        """
        return int(self) > int(other)

    def __ge__(self, other):
        """function __ge__

        other:

        returns bool
        """
        return int(self) >= int(other)

    def __pos__(self):
        """function __pos__

        returns Parameter
        """
        return self.__class__(abs(int(self)))

    def __neg__(self):
        """function __neg__

        returns Parameter
        """
        return self.__class__(-int(self))

    def __iadd__(self, other):
        """function __iadd__

        other:

        returns
        """
        self.set(int(self) + int(other))
        return self

    def __isub__(self, other):
        """function __isub__

        other:

        returns
        """
        self.set(int(self) - int(other))
        return self

    def __delitem__(self, key):
        """function __delitem__

        key: int

        returns
        """
        lis = list(self._parameter)
        lis[key] = self._fill
        self.set(''.join(lis))

    def __iter__(self):
        """function __iter__

        returns
        """
        return iter(self._parameter)

    def __setslice__(self, i, j, seq):
        """function __setslice__

        i: int
        j: int
        seq:

        returns
        """
        param = list(self._parameter)
        param[i:j] = seq
        if self._length < len(param):
            raise ParameterLengthError(seq, self._length)
        self.set(''.join(param))

    def __getslice__(self, i, j):
        """function __getslice__

        i: int
        j: int

        returns
        """
        return self._parameter[i:j]

    def __len__(self):
        return len(self._parameter)


# class RangeParameter(Parameter):
#     r"""RangeParameter

#     RangeParameter is a Parameter.
#     Responsibility:
#     """
#     def __init__(self, parameter, min_, max_):
#         r"""

#         @Arguments:
#         - `parameter`:
#         - `min_`:
#         - `max_`:
#         """
#         Parameter.__init__(self, parameter)
#         self._min = min_
#         self._max = max_



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# parameter.py ends here
