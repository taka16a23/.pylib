#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: _beep.py 341 2015-07-24 05:04:33Z t1 $
# $Revision: 341 $
# $Date: 2015-07-24 14:04:33 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:04:33 +0900 (Fri, 24 Jul 2015) $

r"""_beep -- DESCRIPTION

"""
import os
from excepthook._print import PrintExceptionHook


class BeepExceptionHook(PrintExceptionHook):
    r"""BeepExceptionHook

    BeepExceptionHook is a PrintExceptionHook.
    Responsibility:
    """
    def __init__(self, hz, msec, repeat=1, delay=100):
        r"""

        @Arguments:
        - `hz`:
        - `msec`:
        """
        super(BeepExceptionHook, self).__init__()
        self._hz = hz
        self._msec = msec
        self._repeat = repeat
        self._delay = delay

    def on_except(self, excls, value, trcbck):
        r"""SUMMARY

        on_except(excls, value, trcbck)

        @Arguments:
        - `excls`:
        - `value`:
        - `trcbck`:

        @Return:

        @Error:
        """
        super(BeepExceptionHook, self).on_except(excls, value, trcbck)
        os.system('modprobe pcspkr')
        os.system('/usr/bin/beep'
                  ' -f {0._hz} -l {0._msec} -r {0._repeat} -d {0._delay}'
                  .format(self))
        os.system('rmmod pcspkr')



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _beep.py ends here
