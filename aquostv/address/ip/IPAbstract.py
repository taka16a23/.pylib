#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""IPAbstract -- DESCRIPTION

"""
from abc import ABCMeta, abstractmethod


class IPAbstract:
    """Abstract class IPAbstract
    """
    __metaclass__ = ABCMeta
    # Attributes:

    # Operations
    @abstractmethod
    def get(self):
        raise NotImplementedError()

    @abstractmethod
    def set(self):
        raise NotImplementedError()

    @abstractmethod
    def __str__(self):
        raise NotImplementedError()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# IPAbstract.py ends here
