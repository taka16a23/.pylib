#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
