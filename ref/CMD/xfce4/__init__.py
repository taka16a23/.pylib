#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py


"""
import os as _os

__version__ = "0.1.0"

__all__ = [ '' ]

if 'nt' == _os.name:
    raise NotImplementedError('not supported {.name} environment'.format(_os))
elif 'posix' == _os.name:
    from ref.CMD.xfce4.posix_functions import *
else:
    raise NotImplementedError('not supported {.name} environment'.format(_os))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
