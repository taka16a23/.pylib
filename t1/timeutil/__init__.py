#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: __init__.py 124 2014-03-28 13:52:56Z t1 $
# $Revision: 124 $
# $Date: 2014-03-28 22:52:56 +0900 (Fri, 28 Mar 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-03-28 22:52:56 +0900 (Fri, 28 Mar 2014) $

r"""Name: __init__.py


"""
import time

__revision__ = "$Revision: 124 $"
__version__ = "0.1.0"

__all__ = [ '' ]


class CheckElapse(object):
    r"""
    """

    def __init__(self, interval=None):
        r"""

        @Arguments:
        - `interval`: (int) second of interval. If None, default 60.
        """
        self.maxelapse = interval or 60 # default 1 min
        self.lasttime = None

    def update_lasttime(self, ):
        r"""SUMMARY

        update_lasttime()

        @Return:
        """
        self.lasttime = time.time()

    def iselapsed(self, ):
        r"""SUMMARY

        iselapsed()

        @Return:
        """
        if self.lasttime is None:
            return True
        return (self.lasttime - time.time()) >= self.maxelapse

    def __nonzero__(self, ):
        return self.iselapsed()


class EpochTime(object):
    r"""SUMMARY
    """

    def __init__(self, time):
        r"""

        @Arguments:
        - `time`:
        """
        self._time = time

    def gmtime(self, ):
        r"""SUMMARY

        gmtime()

        @Return:
        """
        return time.gmtime(self._time)

    def strftime(self, format_):
        r"""SUMMARY

        strftime(format_)

        @Arguments:
        - `format_`:

        @Return:
        """
        return time.strftime(format_, self.gmtime())





# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
