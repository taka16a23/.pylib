#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
