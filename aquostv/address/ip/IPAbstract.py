#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: IPAbstract.py 227 2014-09-13 08:15:46Z t1 $
# $Revision: 227 $
# $Date: 2014-09-13 17:15:46 +0900 (Sat, 13 Sep 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-09-13 17:15:46 +0900 (Sat, 13 Sep 2014) $

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
