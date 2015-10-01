#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""port -- DESCRIPTION

"""
from abc import ABCMeta, abstractmethod


class Port:
    """Abstract class Port
    """
    __metaclass__ = ABCMeta
    # Attributes:

    # Operations
    @abstractmethod
    def get(self):
        """function get

        returns
        """
        raise NotImplementedError()

    @abstractmethod
    def set(self):
        """function set

        returns
        """
        raise NotImplementedError()

    @abstractmethod
    def __int__(self):
        """function __int__

        returns
        """
        raise NotImplementedError()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# port.py ends here
