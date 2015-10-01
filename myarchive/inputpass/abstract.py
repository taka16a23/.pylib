#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""abstract -- DESCRIPTION

"""
from abc import ABCMeta, abstractmethod



class InputPass(object):
    r"""InputPass

    InputPass is a object.
    Responsibility:
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def input(self, ):
        pass

    @abstractmethod
    def set_prompt(self, msg):
        pass



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# abstract.py ends here
