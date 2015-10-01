#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: goods.py 485 2015-09-29 03:10:26Z t1 $
# $Revision: 485 $
# $Date: 2015-09-29 12:10:26 +0900 (Tue, 29 Sep 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-09-29 12:10:26 +0900 (Tue, 29 Sep 2015) $

r"""goods -- DESCRIPTION

"""


class CoopGoods(object):
    r"""CoopGoods

    CoopGoods is a object.
    Responsibility:
    """
    __slots__ = ('code', 'jancode', 'name', 'maker', 'origin_country',
                 'explain', 'period', 'price', 'totalprice', 'order_no',
                 'standard', 'calorie')

    def __init__(self, code, jancode=None, name=None, maker=None,
                 origin_country=None, explain=None, period=None, price=None,
                 totalprice=None, order_no=None, standard=None, calorie=None):
        r"""

        @Arguments:
        - `code`:
        - `jancode`:
        - `name`:
        - `maker`:
        - `origin_country`:
        - `explain`:
        - `period`:
        - `price`:
        - `totalprice`:
        - `order_no`:
        - `standard`:
        - `calorie`:
        """
        self.code = code
        self.jancode = jancode
        self.name = name
        self.maker = maker
        self.origin_country = origin_country
        self.explain = explain
        self.period = period
        self.price = price
        self.totalprice = totalprice
        self.order_no = order_no
        self.standard = standard
        self.calorie = calorie



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# goods.py ends here
