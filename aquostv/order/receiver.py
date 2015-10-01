#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class Receiver:
    """Abstract class Receiver
    """
    __metaclass__ = ABCMeta

    # Operations
    @abstractmethod
    def set_received(self):
        raise NotImplementedError()

    @abstractmethod
    def get_received(self):
        raise NotImplementedError()

    @abstractmethod
    def issuccess(self):
        raise NotImplementedError()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# receiver.py ends here
