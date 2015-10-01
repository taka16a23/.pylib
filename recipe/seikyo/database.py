#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""database -- DESCRIPTION

"""
import xlrd
from recipe.seikyo.seikyo_goods import GOODS_DATABASE_PATH
from recipe.seikyo.sheetreader import SeikyoGoodsSheetReader


class SeikyoDatabase(object):
    r"""SeikyoDatabase

    SeikyoDatabase is a object.
    Responsibility:
    """
    database_path = GOODS_DATABASE_PATH
    file_format = '{}_{}.xls'

    def iter_goods(self, year, month, times):
        r"""SUMMARY

        iter_goods(year, times)

        @Arguments:
        - `year`:
        - `times`:

        @Return:

        @Error:
        """
        require_path = self.database_path.join(
            self.file_format.format(year, month))
        if not require_path.exists():
            return iter([])
        book = xlrd.open_workbook(str(require_path))
        if not str(times) in book.sheet_names():
            return iter([])
        sheet = book.sheet_by_name(str(times))
        return iter(SeikyoGoodsSheetReader(sheet, year, month))

    def list_goods(self, year, month, times):
        r"""SUMMARY

        list_goods(year, times)

        @Arguments:
        - `year`:
        - `times`:

        @Return:

        @Error:
        """
        return list(self.iter_goods(year, month, times))

    def list_when(self, ):
        r"""SUMMARY

        list_when()

        @Return: list
        [(year, month, times), ]
        @Error:
        """
        whens = []
        for path in self.database_path.listdir():
            if not path.endswith(('xls', )):
                continue
            year, month = [
                int(x) for x in path.get_basename().splitext()[0].split('_')]
            book = xlrd.open_workbook(path)
            for times in book.sheet_names():
                whens.append((year, month, int(times)))
        return whens

    def iter_all_goods(self, ):
        r"""SUMMARY

        iter_all_goods()

        @Return:

        @Error:
        """
        for year, month, times in self.list_when():
            for goods in self.iter_goods(year, month, times):
                yield goods



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# database.py ends here
