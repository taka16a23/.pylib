#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""coop_database -- DESCRIPTION

"""
from abc import ABCMeta, abstractmethod

import MySQLdb
from recipe.coop.tables import SalesTable
from recipe.coop.goods import Sales


class CoopDatabaseInterface(object):
    r"""CoopDatabaseInterface

    CoopDatabaseInterface is a object.
    Responsibility:
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def iter_sales(self, ): pass
    @abstractmethod
    def iter_codes(self, ): pass
    @abstractmethod
    def iter_periods(self, ): pass
    @abstractmethod
    def iter_names(self, ): pass
    @abstractmethod
    def iter_jancodes(self, ): pass
    @abstractmethod
    def iter_by_period(self, period): pass
    @abstractmethod
    def iter_by_code(self, code): pass
    @abstractmethod
    def iter_by_name(self, name): pass
    @abstractmethod
    def iter_by_jancode(self, jancode): pass
    @abstractmethod
    def get_sales(self, code, period): pass
    @abstractmethod
    def insert(self, **kwargs): pass
    @abstractmethod
    def delete(self, code, period): pass



# TODO: (Atami) [2015/10/29]
# refact create Sales
# convert dict in CoopDatabase
class CoopDatabase(CoopDatabaseInterface):
    r"""CoopDatabase

    CoopDatabase is a CoopDatabaseInterface.
    Responsibility:
    """
    host = 'localhost'
    db = 'coop'
    user = 'root'
    passwd = 'toor'
    charset = 'utf8'

    def __init__(self, ):
        r"""

        @Arguments:
        """
        self.connection = MySQLdb.connect(host=self.host, db=self.db,
                                          user=self.user, passwd=self.passwd,
                                          charset=self.charset)

        self.table = SalesTable(self.connection)
        self.__gen = None

    def iter_sales(self, ):
        r"""SUMMARY

        iter_sales()

        @Return:

        @Error:
        """
        return iter(self.table)

    def iter_codes(self, ):
        r"""SUMMARY

        iter_codes()

        @Return:

        @Error:
        """
        gen = iter(self.table.iter_codes())
        code = gen.next()
        while 1:
            if code == 'null':
                code = gen.next()
                continue
            yield code
            code = gen.next()

    def iter_periods(self, ):
        r"""SUMMARY

        iter_periods()

        @Return:

        @Error:
        """
        gen = iter(self.table.iter_periods())
        code = gen.next()
        while 1:
            if code == 'null':
                code = gen.next()
                continue
            yield code
            code = gen.next()

    def iter_jancodes(self, ):
        r"""SUMMARY

        iter_jancodes()

        @Return:

        @Error:
        """
        gen = iter(self.table.iter_jancodes())
        code = gen.next()
        while 1:
            if code == 'null':
                code = gen.next()
                continue
            yield code
            code = gen.next()

    def iter_names(self, ):
        r"""SUMMARY

        iter_names()

        @Return:

        @Error:
        """
        gen = iter(self.table.iter_names())
        code = gen.next()
        while 1:
            if code == 'null':
                code = gen.next()
                continue
            yield code
            code = gen.next()

    def iter_by_code(self, code):
        r"""SUMMARY

        iter_by_code(code)

        @Arguments:
        - `code`:

        @Return:

        @Error:
        """
        gen = self.table.iter_by_code(code)
        while 1:
            dic = gen.next()
            if 'entry_no' in dic:
                del dic['entry_no']
            yield Sales.create(**dic)

    def iter_by_period(self, period):
        r"""SUMMARY

        iter_by_period(period)

        @Arguments:
        - `period`:

        @Return:

        @Error:
        """
        gen = self.table.iter_by_period(period)
        while 1:
            dic = gen.next()
            if 'entry_no' in dic:
                del dic['entry_no']
            yield Sales.create(**dic)

    def iter_by_jancode(self, jancode):
        r"""SUMMARY

        iter_by_jancode(jancode)

        @Arguments:
        - `jancode`:

        @Return:

        @Error:
        """
        gen = self.table.iter_by_jancode(jancode)
        while 1:
            dic = gen.next()
            if 'entry_no' in dic:
                del dic['entry_no']
            yield Sales.create(**dic)

    def iter_by_name(self, name):
        r"""SUMMARY

        iter_by_name(name)

        @Arguments:
        - `name`:

        @Return:

        @Error:
        """
        gen = self.table.iter_by_name(name)
        while 1:
            dic = gen.next()
            if 'entry_no' in dic:
                del dic['entry_no']
            yield Sales.create(**dic)

    def iter_by_current_order_no(self, order_no):
        r"""SUMMARY

        iter_by_order_no(order_no)

        @Arguments:
        - `order_no`:

        @Return:

        @Error:
        """
        orderno = '{0:06d}'.format(int(order_no))
        periods = [int(i) for i in self.iter_periods()]
        periods.sort()
        period = periods[-1]
        result = None
        for sales in self.iter_by_period(period):
            if sales.order_no == orderno:
                result = sales
        if result is None:
            return iter(())
        return self.iter_by_code(result.code)

    def delete(self, code, period):
        r"""SUMMARY

        delete(code, period)

        @Arguments:
        - `code`:
        - `period`:

        @Return:

        @Error:
        """
        self.table.delete(code, period)

    def insert(self, sales):
        r"""SUMMARY

        insert(code, period, **kwargs)

        @Arguments:
        - `code`:
        - `period`:
        - `kwargs`:

        @Return:

        @Error:
        """
        self.table.insert(**sales.as_dict())

    def get_sales(self, code, period):
        r"""SUMMARY

        get_sales(code, period)

        @Arguments:
        - `code`:
        - `period`:

        @Return:

        @Error:
        """
        dic = self.table.get_sales(code, period)
        if 'entry_no' in dic:
            del dic['entry_no']
        return Sales.create(**dic)

    def __del__(self):
        # Do not imprement "raise"!!
        self.connection.close()

    def __iter__(self):
        self.__gen = self.iter_sales()
        return self

    def next(self, ):
        r"""SUMMARY

        next()

        @Return:

        @Error:
        """
        dic = self.__gen.next()
        if 'entry_no' in dic:
            del dic['entry_no']
        return Sales.create(**dic)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# coop_database.py ends here
