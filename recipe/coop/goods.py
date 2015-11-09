#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""goods -- DESCRIPTION

"""


class Goods(object):
    r"""Goods

    Goods is a object.
    Responsibility:
    """
    __slots__ = ('_code', '_jancode', '_name', '_maker', '_country', '_explain',)

    def __init__(self, code, jancode='', name='', maker='', country='', explain=''):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        self._code = code
        self._jancode = jancode
        self._name = name
        self._maker = maker
        self._country = country
        self._explain = explain

    def as_dict(self, ):
        r"""SUMMARY

        as_dict()

        @Return:

        @Error:
        """
        dic = {'code': self.code,
               'jancode': self.jancode,
               'name': self.name,
               'maker': self.maker,
               'country': self.country,
               'explain': self.explain,}
        return dic

    def get_code(self, ):
        r"""SUMMARY

        get_code()

        @Return:

        @Error:
        """
        return self._code

    def set_code(self, code):
        r"""SUMMARY

        set_code(code)

        @Arguments:
        - `code`:

        @Return:

        @Error:
        """
        self._code = code

    code = property(get_code, set_code)

    def get_jancode(self, ):
        r"""SUMMARY

        get_jancode()

        @Return:

        @Error:
        """
        if not self._jancode or self._jancode == '0000000000000':
            return None
        return self._jancode

    def set_jancode(self, jancode):
        r"""SUMMARY

        set_jancode(jancode)

        @Arguments:
        - `jancode`:

        @Return:

        @Error:
        """
        self._jancode = jancode

    jancode = property(get_jancode, set_jancode)

    def get_name(self, ):
        r"""SUMMARY

        get_name()

        @Return:

        @Error:
        """
        if not self._name:
            return None
        return self._name

    def set_name(self, name):
        r"""SUMMARY

        set_name(name)

        @Arguments:
        - `name`:

        @Return:

        @Error:
        """
        # self._name = name.replace("'", "")
        self._name = name

    name = property(get_name, set_name)

    def get_maker(self, ):
        r"""SUMMARY

        get_maker()

        @Return:

        @Error:
        """
        if not self._maker:
            return None
        return self._maker

    def set_maker(self, maker):
        r"""SUMMARY

        set_maker(maker)

        @Arguments:
        - `maker`:

        @Return:

        @Error:
        """
        self._maker = maker

    maker = property(get_maker, set_maker)

    def get_country(self, ):
        r"""SUMMARY

        get_country()

        @Return:

        @Error:
        """
        if not self._country:
            return None
        return self._country

    def set_country(self, country):
        r"""SUMMARY

        set_country(country)

        @Arguments:
        - `country`:

        @Return:

        @Error:
        """
        self._country = country

    country = property(get_country, set_country)

    def get_explain(self, ):
        r"""SUMMARY

        get_explain()

        @Return:

        @Error:
        """
        if not self._explain:
            return None
        return self._explain

    def set_explain(self, explain):
        r"""SUMMARY

        set_explain(explain)

        @Arguments:
        - `explain`:

        @Return:

        @Error:
        """
        self._explain = explain

    explain = property(get_explain, set_explain)


class Sales(object):
    r"""Sales

    Sales is a object.
    Responsibility:
    """
    __slots__ = ('_detail', '_goods', '_period', '_price', '_totalprice',
                 '_order_no', '_standard', '_calorie', )

    def __init__(self, goods, period, price='', totalprice='', order_no='',
                 standard='', calorie=''):
        r"""

        @Arguments:
        - `goods`:
        - `period`:
        - `price`:
        - `totalprice`:
        - `order_no`:
        - `standard`:
        - `calorie`:
        """
        self._goods = goods
        self._period = period
        self._price = price
        self._totalprice = totalprice
        self._order_no = order_no
        self._standard = standard
        self._calorie = calorie

    @classmethod
    def create(cls, code, period, jancode='', name='', maker='', country='',
               explain='', price='', totalprice='', order_no='', standard='',
               calorie=''):
        r"""SUMMARY

        create()

        @Return:

        @Error:
        """
        return cls(Goods(code, jancode, name, maker, country, explain),
                   period, price, totalprice, order_no, standard, calorie)

    def get_code(self, ):
        r"""SUMMARY

        get_code()

        @Return:

        @Error:
        """
        return self._goods.get_code()

    def set_code(self, code):
        r"""SUMMARY

        set_code(code)

        @Arguments:
        - `code`:

        @Return:

        @Error:
        """
        self._goods.set_code(code)

    code = property(get_code, set_code)

    def get_period(self, ):
        r"""SUMMARY

        get_period()

        @Return:

        @Error:
        """
        return self._period

    def set_period(self, period):
        r"""SUMMARY

        set_period(period)

        @Arguments:
        - `period`:

        @Return:

        @Error:
        """
        self._period = period

    period = property(get_period, set_period)

    def get_jancode(self, ):
        r"""SUMMARY

        get_jancode()

        @Return:

        @Error:
        """
        return self._goods.get_jancode()

    def set_jancode(self, jancode):
        r"""SUMMARY

        set_jancode(jancode)

        @Arguments:
        - `jancode`:

        @Return:

        @Error:
        """
        self._goods.set_jancode(jancode)

    jancode = property(get_jancode, set_jancode)

    def get_name(self, ):
        r"""SUMMARY

        get_name()

        @Return:

        @Error:
        """
        return self._goods.get_name()

    def set_name(self, name):
        r"""SUMMARY

        set_name(name)

        @Arguments:
        - `name`:

        @Return:

        @Error:
        """
        self._goods.set_name(name)

    name = property(get_name, set_name)

    def get_maker(self, ):
        r"""SUMMARY

        get_maker()

        @Return:

        @Error:
        """
        return self._goods.get_maker()

    def set_maker(self, maker):
        r"""SUMMARY

        set_maker(maker)

        @Arguments:
        - `maker`:

        @Return:

        @Error:
        """
        self._goods.set_maker(maker)

    maker = property(get_maker, set_maker)

    def get_country(self, ):
        r"""SUMMARY

        get_country()

        @Return:

        @Error:
        """
        return self._goods.get_country()

    def set_country(self, country):
        r"""SUMMARY

        set_country(country)

        @Arguments:
        - `country`:

        @Return:

        @Error:
        """
        self._goods.set_country(country)

    country = property(get_country, set_country)

    def get_explain(self, ):
        r"""SUMMARY

        get_explain()

        @Return:

        @Error:
        """
        return self._goods.get_explain()

    def set_explain(self, explain):
        r"""SUMMARY

        set_explain(explain)

        @Arguments:
        - `explain`:

        @Return:

        @Error:
        """
        self._goods.set_explain(explain)

    explain = property(get_explain, set_explain)

    def get_price(self, ):
        r"""SUMMARY

        get_price()

        @Return:

        @Error:
        """
        if isinstance(self._price, (int, long)):
            return self._price
        if not self._price:
            return None
        return self._price

    def set_price(self, price):
        r"""SUMMARY

        set_price(price)

        @Arguments:
        - `price`:

        @Return:

        @Error:
        """
        self._price = price

    price = property(get_price, set_price)

    def get_totalprice(self, ):
        r"""SUMMARY

        get_totalprice()

        @Return:

        @Error:
        """
        if isinstance(self._totalprice, (int, long)):
            return self._totalprice
        if not self._totalprice:
            return None
        return self._totalprice

    def set_totalprice(self, totalprice):
        r"""SUMMARY

        set_totalprice(totalprice)

        @Arguments:
        - `totalprice`:

        @Return:

        @Error:
        """
        self._totalprice = totalprice

    totalprice = property(get_totalprice, set_totalprice)

    def get_order_no(self, ):
        r"""SUMMARY

        get_order_no()

        @Return:

        @Error:
        """
        if not self._order_no:
            return None
        return self._order_no

    def set_order_no(self, order_no):
        r"""SUMMARY

        set_order_no(order_no)

        @Arguments:
        - `order_no`:

        @Return:

        @Error:
        """
        self._order_no = order_no

    order_no = property(get_order_no, set_order_no)

    def get_standard(self, ):
        r"""SUMMARY

        get_standard()

        @Return:

        @Error:
        """
        if not self._standard:
            return None
        return self._standard

    def set_standard(self, standard):
        r"""SUMMARY

        set_standard()

        @Return:

        @Error:
        """
        self._standard = standard

    standard = property(get_standard, set_standard)

    def get_calorie(self, ):
        r"""SUMMARY

        get_calorie()

        @Return:

        @Error:
        """
        if not self._calorie or u'カロリー表示無し' == self._calorie:
            return None
        return self._calorie

    def set_calorie(self, calorie):
        r"""SUMMARY

        set_calorie(calorie)

        @Arguments:
        - `calorie`:

        @Return:

        @Error:
        """
        self._calorie = calorie

    calorie = property(get_calorie, set_calorie)

    def as_dict(self, ):
        r"""SUMMARY

        as_dict()

        @Return:

        @Error:
        """
        dic = self._goods.as_dict()
        dic.update({'code': self.code,
                    'period': self.period,
                    'price': self.price,
                    'totalprice': self.totalprice,
                    'order_no': self.order_no,
                    'standard': self.standard,
                    'calorie': self.calorie,})
        return dic



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# goods.py ends here
