#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
$Revision: 380 $
$LastChangedRevision: 380 $
$LastChangedDate: 2012-08-07 21:43:00 +0900 (Tue, 07 Aug 2012) $

sleep_progress.py

Countdown progress
"""


__revision__ = "$Revision$"
__version__ = "0.1.0"


__all__ = [ 'sleep_progress' ]


import sys as _sys
import time as _time

def sleep_progress(sec, strformat='Waiting %d'):
    """sleeping progress

    Arguments:
    - `time`:
    """
    sec = int(sec)
    # if 0 == sec:
        # sys.exit("Do not set {0}".format(sec))

    for remaining in range(sec, -1, -1):
        _sys.stdout.write('\r')
        _sys.stdout.write(strformat % remaining)
        _sys.stdout.flush()
        _time.sleep(1)

    _sys.stdout.write("\n")
    _sys.stdout.flush()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
