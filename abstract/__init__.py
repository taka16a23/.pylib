#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py


"""
from abstract import abcs
from abstract import singleton
from abstract.abcs import *
from abstract.singleton import *


__version__ = "0.1.0"

__all__ = ['IterABC', 'BoolABC', 'WithABC', 'FileAdaptorABC', 'Singleton',
           'SingletonMeta', 'SelectABC']


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
