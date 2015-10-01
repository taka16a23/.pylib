#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: period.py 460 2015-08-10 16:51:55Z t1 $
# $Revision: 460 $
# $Date: 2015-08-11 01:51:55 +0900 (Tue, 11 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-11 01:51:55 +0900 (Tue, 11 Aug 2015) $

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
