#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: functions.py 467 2015-08-17 16:32:37Z t1 $
# $Revision: 467 $
# $Date: 2015-08-18 01:32:37 +0900 (Tue, 18 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-18 01:32:37 +0900 (Tue, 18 Aug 2015) $

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
