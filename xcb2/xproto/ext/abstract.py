#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""abstract -- a parts of xcb2

"""
from abc import ABCMeta, abstractmethod
from cStringIO import StringIO as _StringIO


class CoreMethodAbstract(object):
    r"""SUMMARY
    """
    __metaclass__ = ABCMeta

    def __init__(self, connection):
        r"""

        @Arguments:
        - `connection`:
        """
        self._connection = connection
        self._buf = _StringIO()

    @abstractmethod
    def request(self, binary):
        raise NotImplementedError()


class CoreSubMethodAbstract(object):
    r"""SUMMARY
    """

    def __init__(self, parent):
        r"""

        @Arguments:
        - `parent`:
        """
        self._parent = parent
        self._connection = parent._connection



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# abstract.py ends here
