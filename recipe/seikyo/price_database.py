#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: price_database.py 468 2015-08-19 05:49:01Z t1 $
# $Revision: 468 $
# $Date: 2015-08-19 14:49:01 +0900 (Wed, 19 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-19 14:49:01 +0900 (Wed, 19 Aug 2015) $

r"""price_database -- DESCRIPTION

"""
import xlrd, xlwt

from recipe.seikyo.seikyo_goods import SEIKYO_ARCHIVE_PATH
from recipe.seikyo.database import SeikyoDatabase



class PriceDatabase(object):
    r"""PriceDatabase

    PriceDatabase is a object.
    Responsibility:
    """
    prices_path = SEIKYO_ARCHIVE_PATH.join('prices.xls')
    startcol = 0

    def __init__(self, ):
        r"""
        """

    def update(self, ):
        r"""SUMMARY

        update()

        @Return:

        @Error:
        """
        wbook = xlwt.Workbook()
        sheet = wbook.add_sheet('prices', cell_overwrite_ok=True)
        row1 = sheet.row(0)
        row1.write(self.startcol, 'Name')
        row1.write(self.startcol + 1, 'GoodsCode')
        database = SeikyoDatabase()
        colsdic = {}
        for col, when in enumerate(database.list_when(),
                                   start=self.startcol + 2):
            colsdic['{0}{1:02d}{2}'.format(when[0], when[1], when[2])] = col
        for whenstr, colx in colsdic.iteritems():
            row1.write(colx, whenstr)
        right = xlwt.Alignment()
        right.horz = 3
        right_style = xlwt.XFStyle()
        right_style.alignment = right
        namedic = {}
        rowsdic = {}
        rowcount = 1
        for goods in database.iter_all_goods():
            if goods.goodscode == '0000000000':
                continue
            if not goods.goodscode in rowsdic:
                rowsdic[goods.goodscode] = rowcount
                rowcount += 1
            sheet.write(
                rowsdic[goods.goodscode], colsdic[goods.when], goods.price,
                right_style)
            if not goods.goodscode in namedic:
                namedic[goods.goodscode] = goods.name
        for goodscode, rowx in rowsdic.iteritems():
            sheet.write(rowx, 1, goodscode)
        for goodscode, name in namedic.iteritems():
            sheet.write(rowsdic[goodscode], 0, name)
        wbook.save(self.prices_path)

    def average(self, goodscode):
        r"""SUMMARY

        average(goodscode)

        @Arguments:
        - `goodscode`:

        @Return:

        @Error:
        """
        book = xlrd.open_workbook(self.prices_path)
        sheet = book.sheets()[0]
        goodscode_col = self.startcol + 1
        cells = []
        for nrow in xrange(sheet.nrows):
            collist = sheet.row(nrow)
            if len(collist) < goodscode_col + 1:
                continue
            if goodscode == collist[goodscode_col].value:
                cells = collist[goodscode_col + 1:]
                break
        if not cells:
            return 0
        ret = 0
        for cell in cells:
            ret += int(cell.value)
        return ret / len(cells)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# price_database.py ends here
