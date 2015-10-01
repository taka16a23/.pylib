#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""period -- DESCRIPTION

"""


class Period(object):
    r"""Period

    Period is a object.
    Responsibility:
    """
    def __init__(self, start, end):
        r"""

        @Arguments:
        - `start`:
        - `end`:
        """
        sdate, edate = start, end
        if edate < sdate:
            sdate, edate = edate, sdate
        self._start = sdate
        self._end = edate

    def is_within(self, date):
        r"""SUMMARY

        is_within(date)

        @Arguments:
        - `date`:

        @Return:

        @Error:
        """
        return self._start <= date <= self._end

    def get_start(self, ):
        r"""SUMMARY

        get_start()

        @Return:

        @Error:
        """
        return self._start

    def set_start(self, start):
        r"""SUMMARY

        set_start(start)

        @Arguments:
        - `start`:

        @Return:

        @Error:
        """
        self._start = start

    start = property(get_start, set_start)

    def get_end(self, ):
        r"""SUMMARY

        get_end()

        @Return:

        @Error:
        """
        return self._end

    def set_end(self, end):
        r"""SUMMARY

        set_end(end)

        @Arguments:
        - `end`:

        @Return:

        @Error:
        """
        self._end = end

    end = property(get_end, set_end)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# period.py ends here
