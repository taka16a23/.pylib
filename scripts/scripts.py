#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""scripts -- DESCRIPTION

"""
from abc import ABCMeta, abstractmethod


class Script(object):
    """
    """
    __metaclass__ = ABCMeta

    def __init__(self, receiver=None):
        self.receiver = receiver

    @abstractmethod
    def execute(self, shell):
        pass


class GetExitStatus(Script):
    r"""GetExitStatus

    GetExitStatus is a Script.
    Responsibility:
    def execute(self, shell):
        pass



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# scripts.py ends here
