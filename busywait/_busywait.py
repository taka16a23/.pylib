#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""_busywait -- DESCRIPTION

"""
import time
from psutil import cpu_percent


class TimeOut(Exception):
    r"""TimeOut

    TimeOut is a Exception.
    Responsibility:
    """
    pass


class BusyWait(object):
    r"""BusyWait

    BusyWait is a object.
    Responsibility:
    """
    def __init__(self, percent, percpu=False):
        r"""

        @Arguments:
        - `percent`:
        """
        self._percent = percent
        self._percpu = percpu

    def get_percent(self, ):
        r"""SUMMARY

        get_percent()

        @Return:

        @Error:
        """
        return self._percent

    def set_percent(self, percent):
        r"""SUMMARY

        set_percent(percent)

        @Arguments:
        - `percent`:

        @Return:

        @Error:
        """
        self._percent = float(percent)

    def is_percpu(self, ):
        r"""SUMMARY

        is_percpu()

        @Return:

        @Error:
        """
        return self._percpu

    def set_percpu(self, boolean):
        r"""SUMMARY

        set_percpu(boolean)

        @Arguments:
        - `boolean`:

        @Return:

        @Error:
        """
        self._percpu = bool(boolean)

    def _isbusy(self, percent):
        r"""SUMMARY

        _isbusy(percent)

        @Arguments:
        - `percent`:

        @Return:

        @Error:
        """
        return self._percent < percent

    def isbusy(self, interval):
        r"""SUMMARY

        _isbusy(percent)

        @Arguments:
        - `percent`:

        @Return:

        @Error:
        """
        results = cpu_percent(interval=interval, percpu=self._percpu)
        if isinstance(results, (list, )):
            for percent in results:
                if not self._isbusy(percent):
                    return False
            return True
        # got float
        return self._isbusy(results)

    def wait(self, interval):
        r"""SUMMARY

        _wait(interval)

        @Arguments:
        - `interval`:

        @Return:

        @Error:
        """
        while self.isbusy(interval):
            pass

    def wait_timeout(self, interval, timeout):
        r"""SUMMARY

        _wait_timeout(timeout)

        @Arguments:
        - `timeout`:

        @Return:

        @Error:
        """
        if timeout < interval:
            interval = timeout
        start = time.time()
        while self.isbusy(interval):
            if timeout <= time.time() - start:
                raise TimeOut(timeout)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _busywait.py ends here
