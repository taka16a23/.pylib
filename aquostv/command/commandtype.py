#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""commandtype -- DESCRIPTION

"""


class CommandType(object):
    r"""CommandType

    CommandType is a object.
    Responsibility:
    """
    _length = 4

    def __init__(self, cmdtype):
        r"""

        @Arguments:
        - `cmdtype`:
        """
        self._check_length(cmdtype)
        self._cmdtype = cmdtype

    def get(self, ):
        r"""SUMMARY

        get()

        @Return:

        @Error:
        """
        return self._cmdtype

    def set(self, cmdtype):
        r"""SUMMARY

        set(cmdtype)

        @Arguments:
        - `cmdtype`:

        @Return:

        @Error:
        """
        self._check_length(cmdtype)
        self._cmdtype = cmdtype

    def _check_length(self, string):
        r"""SUMMARY

        _check_length(string)

        @Arguments:
        - `string`:

        @Return:

        @Error:
        """
        if self._length != len(string):
            raise ValueError(string)

    def __hash__(self):
        return hash(self._cmdtype)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._cmdtype == other.get()
        return self._cmdtype == other

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return self._cmdtype != other.get()
        return self._cmdtype != other

    def __add__(self, other):
        return self._cmdtype + str(other)

    def __str__(self):
        return self._cmdtype

    def __repr__(self):
        return '{0.__class__.__name__}("{0._cmdtype}")'.format(self)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# commandtype.py ends here
