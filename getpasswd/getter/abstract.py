#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""_getter -- DESCRIPTION

"""
from abc import ABCMeta, abstractmethod


class PassGetter(object):
    r"""PassGetter

    PassGetter is a object.
    Responsibility:
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def getpass(self, prompt='Password: '):
        pass





# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _getter.py ends here
