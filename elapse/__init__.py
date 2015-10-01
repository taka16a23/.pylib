#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: __init__.py 299 2015-01-29 00:31:32Z t1 $
# $Revision: 299 $
# $Date: 2015-01-29 09:31:32 +0900 (Thu, 29 Jan 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-01-29 09:31:32 +0900 (Thu, 29 Jan 2015) $

r"""Name: __init__.py


"""
import time


__revision__ = "$Revision: 299 $"
__version__ = "0.1.0"

__all__ = [ ]


class TimeMeasure(object):
    r"""TimeMeasure

    TimeMeasure is a object.
    Responsibility:
    """
    def __init__(self, start, end):
        r"""

        @Arguments:
        - `start`:
        - `end`:
        """
        self._start = start
        self._end = end

    def __repr__(self, ):
        r"""SUMMARY

        __repr__()

        @Return:

        @Error:
        """
        return ('{0.__class__.__name__}(start={0._start}, end={0._end})'
                .format(self))

    def getstart(self, ):
        r"""SUMMARY

        getstart()

        @Return:

        @Error:
        """
        return self._start

    def setstart(self, time_):
        r"""SUMMARY

        setstart(time_)

        @Arguments:
        - `time_`:

        @Return:

        @Error:
        """
        self._start = time_

    def getend(self, ):
        r"""SUMMARY

        getend()

        @Return:

        @Error:
        """
        return self._end

    def setend(self, time_):
        r"""SUMMARY

        setend(time_)

        @Arguments:
        - `time_`:

        @Return:

        @Error:
        """
        self._end = time_

    def calc_epoch(self, ):
        r"""SUMMARY

        calc_epoch()

        @Return:

        @Error:
        """
        return self._end - self._start


class Timer(object):
    r"""Timer

    Timer is a object.
    Responsibility:
    """
    def __init__(self, time_):
        r"""

        @Arguments:
        - `time`:
        """
        self._time = time_

    @classmethod
    def now(self, ):
        r"""SUMMARY

        now()

        @Return:

        @Error:
        """
        return Timer(time.time())

    def elapsed(self, time_=None):
        r"""SUMMARY

        elapsed(time_=None)

        @Arguments:
        - `time_`:

        @Return:

        @Error:
        """
        time_ = time_ or time.time()
        return TimeMeasure(self._time, time_)

    def setepoch(self, time_):
        r"""SUMMARY

        setepoch(time_)

        @Arguments:
        - `time_`:

        @Return:

        @Error:
        """
        self._time = time_

    def getepoch(self, ):
        r"""SUMMARY

        getepoch()

        @Return:

        @Error:
        """
        return self._time



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
