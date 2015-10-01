#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: abstract.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

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
