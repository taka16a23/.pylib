#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""functions -- DESCRIPTION

"""
import sys
import warnings
try:
    from progress_timer._wx import ProgressTimerWX
except ImportError:
    warnings.warn('Not exists wxPython package')
from progress_timer._cli import ProgressTimerCLI


if sys.stdout.isatty():
    progress = ProgressTimerCLI()
elif 'ProgressTimerWX' in globals():
    progress = ProgressTimerWX()




# For Emacs
# Local Variables:
# coding: utf-8
# End:
# functions.py ends here
