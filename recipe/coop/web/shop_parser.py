#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""shop_parser -- DESCRIPTION

"""
from recipe.coop.web.categories import Categories


class ShopParser(object):
    r"""ShopParser

    ShopParser is a object.
    Responsibility:
    """
    def __init__(self, ):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        self._categories = Categories()

    def iter_goods(self, ):
        r"""SUMMARY

        iter_goods()

        @Return:

        @Error:
        """
        for categorie in self._categories.list_categories():
            for goods in self._categories.iter_goods(categorie):
                yield goods

    def current_period(self, ):
        r"""SUMMARY

        current_period()

        @Return:

        @Error:
        """
        return self._categories.current_period()

    def clear_caches(self, ):
        r"""SUMMARY

        clear_caches()

        @Return:

        @Error:
        """
        self._categories.clear_caches()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# shop_parser.py ends here
