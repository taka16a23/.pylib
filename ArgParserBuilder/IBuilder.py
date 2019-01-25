#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""IBuilder -- DESCRIPTION

"""
from abc import ABCMeta, abstractmethod


class IBuilder(object):
    """IBuilder

    IBuilder is a object.
    Responsibility:
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def build(self, parser):
        pass



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# IBuilder.py ends here
