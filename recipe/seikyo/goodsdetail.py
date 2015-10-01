#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: goodsdetail.py 468 2015-08-19 05:49:01Z t1 $
# $Revision: 468 $
# $Date: 2015-08-19 14:49:01 +0900 (Wed, 19 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-19 14:49:01 +0900 (Wed, 19 Aug 2015) $

r"""goodsdetail -- DESCRIPTION

"""
from pprint import pformat


class SeikyoGoodsDetail(object):
    r"""SeikyoGoodsDetail

    SeikyoGoodsDetail is a object.
    Responsibility:
    """
    __slots__ = ('when', 'jancode', 'goodscode', 'orderno', 'name', 'price',
                 'totalprice', 'origin', 'maker', 'calorie', 'standard',
                 'explain')

    def __init__(self, when='', jancode='', goodscode='', orderno='', name='',
                 price='', totalprice='', origin='', maker='', calorie='',
                 standard='', explain=''):
        r"""

        @Arguments:
        - `when`:
        - `jancode`:
        - `goodscode`:
        - `orderno`:
        - `name`:
        - `price`:
        - `taxprice`:
        - `origin`:
        - `maker`:
        - `calorie`:
        - `explain`:
        - `standard`:
        """
        self.when = when
        self.jancode = jancode
        self.goodscode = goodscode
        self.orderno = orderno
        self.name = name
        self.price = price
        self.totalprice = totalprice
        self.origin = origin
        self.maker = maker
        self.calorie = calorie
        self.standard = standard
        self.explain = explain

    def as_dict(self, ):
        r"""SUMMARY

        as_dict()

        @Return:

        @Error:
        """
        dic = {}
        dic['when'] = self.when
        dic['jancode'] = self.jancode
        dic['goodscode'] = self.goodscode
        dic['orderno'] = self.orderno
        dic['name'] = self.name
        dic['price'] = self.price
        dic['totalprice'] = self.totalprice
        dic['origin'] = self.origin
        dic['maker'] = self.maker
        dic['calorie'] = self.calorie
        dic['standard'] = self.standard
        dic['explain'] = self.explain
        return dic

    def __repr__(self):
        return '{0.__class__.__name__}({1})'.format(
            self, pformat(self.as_dict()))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# goodsdetail.py ends here
