#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""observable -- DESCRIPTION

"""


class Observable(object):
    r"""Observable

    Observable is a object.
    Responsibility:
    """
    def __init__(self, ):
        r"""
        """
        self._observers = []

    def add_observer(self, observer):
        r"""SUMMARY

        add_observer(observer)

        @Arguments:
        - `observer`:

        @Return:

        @Error:
        """
        self._observers.append(observer)

    def remove_observer(self, observer):
        r"""SUMMARY

        remove_observer(observer)

        @Arguments:
        - `observer`:

        @Return:

        @Error:
        """
        self._observers.remove(observer)

    def has_observer(self, observer):
        r"""SUMMARY

        has_observer(observer)

        @Arguments:
        - `observer`:

        @Return:

        @Error:
        """
        return observer in self._observers

    def count_observer(self, ):
        r"""SUMMARY

        count_observer()

        @Return:

        @Error:
        """
        return len(self._observers)

    def clear_observer(self, ):
        r"""SUMMARY

        clear_observer()

        @Return:

        @Error:
        """
        del self._observers[:]




# For Emacs
# Local Variables:
# coding: utf-8
# End:
# observable.py ends here
