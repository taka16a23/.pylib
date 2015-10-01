#!/usr/bin/env python
# -*- coding: utf-8 -*-
r""" blocking -- blocking decorator


"""

import sys as _sys
import threading as _threading

from decorator import decorator as _decorator


# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__version__ = '0.1.0'


def blocking(not_avail):
    def blocking(f, *args, **kw):
        if not hasattr(f, "thread"): # no thread running
            def set_result(): f.result = f(*args, **kw)
            f.thread = _threading.Thread(None, set_result)
            f.thread.start()
            return not_avail
        elif f.thread.isAlive():
            return not_avail
        else: # the thread is ended, return the stored result
            del f.thread
            return f.result
    return _decorator(blocking)


def _test():
    r"""Test function."""
    return 0

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# blocking.py ends here
