#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py


"""
import os

__version__ = "0.1.0"

__all__ = [ '' ]

if os.path.exists('/proc/bus/input/devices'):
    from . import devices





# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
