#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""keyname -- DESCRIPTION

"""


class Keyname(object):
    r"""Keyname

    Keyname is a object.
    Responsibility:
    """
    def __init__(self, name):
        r"""

        @Arguments:
        - `name`:
        """
        self._name = None
        self.set(name)

    def set(self, name):
        r"""SUMMARY

        set_name(name)

        @Arguments:
        - `name`:

        @Return:

        @Error:
        """
        self._name = str(name)

    def get(self, ):
        r"""SUMMARY

        get_name()

        @Return:

        @Error:
        """
        return self._name

    name = property(get, set)

    def __repr__(self):
        return '{0.__class__.__name__}("{0._name}")'.format(self)

    def __str__(self):
        return self._name

    def __cast(self, value):
        r"""SUMMARY

        __cast(value)

        @Arguments:
        - `value`:

        @Return:

        @Error:
        """
        if isinstance(value, (self.__class__, )):
            return str(value)
        return value

    def __cmp__(self, other):
        """
        self < other return -1
        self > other return 1
        self == other return 0
        """
        return cmp(self._name, self.__cast(other))

    def __eq__(self, other):
        return self._name == self.__cast(other)

    def __ne__(self, other):
        return not self == other

    def __hash__(self, ):
        return hash(self._name)


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# keyname.py ends here
