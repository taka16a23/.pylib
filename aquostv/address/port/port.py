#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: port.py 227 2014-09-13 08:15:46Z t1 $
# $Revision: 227 $
# $Date: 2014-09-13 17:15:46 +0900 (Sat, 13 Sep 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-09-13 17:15:46 +0900 (Sat, 13 Sep 2014) $

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
