#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: abstract.py 262 2014-12-27 06:39:26Z t1 $
# $Revision: 262 $
# $Date: 2014-12-27 15:39:26 +0900 (Sat, 27 Dec 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-12-27 15:39:26 +0900 (Sat, 27 Dec 2014) $

r"""abstract -- DESCRIPTION

"""
from abc import ABCMeta, abstractmethod


class MyPath(object):
    r"""MyPath

    MyPath is a object.
    Responsibility:
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def pave(self, ):
        pass

    @abstractmethod
    def isexists(self, ):
        pass

    @abstractmethod
    def get_path(self, ):
        pass

    @abstractmethod
    def __str__(self):
        pass



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# abstract.py ends here
