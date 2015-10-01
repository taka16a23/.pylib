#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""sheetreader -- DESCRIPTION

"""
from recipe.seikyo.goodsdetail import SeikyoGoodsDetail



class SeikyoGoodsSheetReader(object):
    r"""SeikyoGoodsSheetReader

    SeikyoGoodsSheetReader is a object.
    Responsibility:
    """
    def __init__(self, sheet, year, month):
        r"""

        @Arguments:
        - `sheet`:
        """
        self.year = year
        self.month = month
        self._sheet = sheet
        self._index = 1

    def get_goodsdetail(self, rowx):
        r"""SUMMARY

        get_goodsdetail(rowx)

        @Arguments:
        - `rowx`:

        @Return:

        @Error:
        """
        goods = SeikyoGoodsDetail()
        cells = self._sheet.row(rowx)
        if not cells or len(cells) != 11:
            return goods
        goods.when = '{0}{1:02d}{2}'.format(
            self.year, self.month, int(self._sheet.name))
        # goods.jancode = '{0:013d}'.format(long(cells[0].value))
        goods.jancode = cells[0].value
        goods.goodscode = '{0:010d}'.format(int(cells[1].value))
        goods.orderno = '{0:06d}'.format(int(cells[2].value))
        goods.name = cells[3].value
        goods.price = cells[4].value
        goods.totalprice = cells[5].value
        goods.origin = cells[6].value
        goods.maker = cells[7].value
        goods.calorie = cells[8].value
        goods.standard = cells[9].value
        goods.explain = cells[10].value
        return goods

    def __iter__(self):
        self._index = 1
        return self

    def next(self, ):
        if self._sheet.nrows <= self._index:
            raise StopIteration
        goods = self.get_goodsdetail(self._index)
        self._index += 1
        return goods



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# sheetreader.py ends here
