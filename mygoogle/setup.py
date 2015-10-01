#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""setup -- setup.py

"""

import sys as _sys
import os as _os


__version__ = '0.1.0'

from distutils.core import setup
from Cython.Build import cythonize

setup(name = 'chrome app', ext_modules = cythonize("*.pyx"))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# setup.py ends here
