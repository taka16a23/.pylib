#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: receiver.py 290 2015-01-29 00:19:07Z t1 $
# $Revision: 290 $
# $Date: 2015-01-29 09:19:07 +0900 (Thu, 29 Jan 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-01-29 09:19:07 +0900 (Thu, 29 Jan 2015) $

r"""receiver -- DESCRIPTION

"""
from abc import ABCMeta, abstractmethod
from collections import deque


class Receiver(object):
    r"""Receiver

    Receiver is a object.
    Responsibility:
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def append(self, obj):
        pass

    @abstractmethod
    def pop(self, obj):
        pass


class DequeReceiver(deque, Receiver):
    r"""DequeReceiver

    DequeReceiver is a deque, Receiver.
    Responsibility:
    """
    def __repr__(self):
        return deque.__repr__(self).replace('deque', self.__class__.__name__, 1)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# receiver.py ends here
