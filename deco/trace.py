#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id: trace.py 97 2014-01-04 08:46:02Z t1 $
# $Revision: 97 $
# $Date: 2014-01-04 17:46:02 +0900 (Sat, 04 Jan 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-01-04 17:46:02 +0900 (Sat, 04 Jan 2014) $
r""" trace -- trace decorator

$Revision: 97 $

"""

import sys as _sys
import os as _os
import linecache

from decorator import decorator as _decorator


# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__revision__ = '$Revision: 97 $'
__version__ = '0.1.0'


@_decorator
def trace(f, *args, **kw):
    r"""SUMMARY

    @Arguments:
    - `f`:
    - `* args`:
    - `** kw`:

    @Return:
    """
    print('calling {} with args {}, {}'.format(f.__name__, args, kw))

def print_trace(f):
    r"""SUMMARY

    @Arguments:
    - `f`:

    @Return:
    """
    def wrapped(*args, **kw):
        r"""SUMMARY

        wrapped(*args,**kw)

        @Arguments:
        - `*args`:
        - `**kw`:

        @Return:
        """
        print('-> {} ({})'.format(f, *args))
    return wrapped



def line(f):
    def globaltrace(frame, why, arg):
        if why == "call":
            return localtrace
        return None

    def localtrace(frame, why, arg):
        if why == "line":
            # record the file name and line number of every trace
            filename = frame.f_code.co_filename
            lineno = frame.f_lineno

            bname = _os.path.basename(filename)
            print "{}({}): {}".format(  bname,
                                        lineno,
                                        linecache.getline(filename, lineno)),
        return localtrace

    def _f(*args, **kwds):
        _sys.settrace(globaltrace)
        result = f(*args, **kwds)
        _sys.settrace(None)
        return result

    return _f

def _test():
    r"""Test function."""
    return 0

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# trace.py ends here
