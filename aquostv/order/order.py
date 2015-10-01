#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class Order:
    """Abstract class Order
    """
    __metaclass__ = ABCMeta

    # Operations
    @abstractmethod
    def get_orderline(self):
        raise NotImplementedError()

    @abstractmethod
    def receive(self, string):
        raise NotImplementedError()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# order.py ends here
