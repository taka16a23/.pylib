#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""

sleep_progress.py

Countdown progress
"""


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
