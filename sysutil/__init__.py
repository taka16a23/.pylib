#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""\
Name: __init__.py


"""
import sys as _sys
import os as _os
from . import redirect

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')

__version__ = "0.1.0"

__all__ = [ '' ]

EXIT_SUCCESS = 0
EXIT_FAILURE = 1


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
