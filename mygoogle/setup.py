#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: setup.py 87 2013-11-30 07:34:05Z t1 $
# $Revision: 87 $
# $Date: 2013-11-30 16:34:05 +0900 (Sat, 30 Nov 2013) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2013-11-30 16:34:05 +0900 (Sat, 30 Nov 2013) $

r"""setup -- setup.py

"""

import sys as _sys
import os as _os


__revision__ = '$Revision: 87 $'
__version__ = '0.1.0'

from distutils.core import setup
from Cython.Build import cythonize

setup(name = 'chrome app', ext_modules = cythonize("*.pyx"))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# setup.py ends here
