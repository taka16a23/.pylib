#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""\
Name: __init__.py


"""


__version__ = "0.1.0"

__all__ = [ ]

# TODO: (Atami) [2013/09/04]
# class get elements from current directory files

import os as _os

if 'nt' == _os.name:
    from .nt_ref import *

elif 'posix' == _os.name:
    from .posix_ref import *



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
