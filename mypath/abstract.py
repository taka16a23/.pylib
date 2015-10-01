#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
