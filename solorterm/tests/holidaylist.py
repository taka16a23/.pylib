#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""holidaylist -- DESCRIPTION

"""
from datetime import date
from dotavoider import ListDotAvoider

import xlrd

def getholidaylist(name):
    r"""SUMMARY

    getholidaylist(name)

    @Arguments:
    - `name`:

    @Return:
    """
    xlsfile = '/root/.pylib/solorterm/tests/holidaylist.xls'
    book = xlrd.open_workbook(xlsfile)
    sh1 = book.sheet_by_index(1)
    lis, append = ListDotAvoider().append
    for i in range(2, sh1.nrows):
        d = xlrd.xldate_as_tuple(sh1.cell_value(rowx=i, colx=2), 0)
        day = date(d[0], d[1], d[2])
        hname = sh1.cell_value(rowx=i, colx=3).encode('utf-8')
        if name == hname:
            append(day)
    return lis



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# holidaylist.py ends here
