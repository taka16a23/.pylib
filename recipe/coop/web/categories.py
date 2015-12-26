#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""categories -- DESCRIPTION

"""
from dotavoider import dotavoid
from collections import namedtuple

# from recipe.coop.goods import Sales
from recipe.coop.web.webpage import ProductListPage
from recipe.coop.web.thread_request import thread_request


Sales = namedtuple('Sales', ('code', 'jancode', 'name', 'maker', 'country',
                             'explain', 'price', 'totalprice', 'order_no',
                             'standard', 'calorie'))


class Categories(object):
    r"""Categories

    Categories is a object.
    Responsibility:
    """
    def __init__(self, ):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        self._categories = {
            u'生鮮食品':
            ProductListPage(
                'https://shop.nanairo.coop/front/bb/shiga/product/'
                'productlist?&cc=0101000000&ps=1000&pn=1&si=0&dt=c&dm=1'),
            u'牛乳卵':
            ProductListPage(
                'https://shop.nanairo.coop/front/bb/shiga/product/'
                'productlist?&cc=0102000000&ps=300&pn=1&si=0&dt=c&dm=1'),
            u'冷凍':
            ProductListPage(
                'https://shop.nanairo.coop/front/bb/shiga/product/'
                'productlist?cc=0103000000&ps=1000&pn=1&si=0&dt=c&dm=1'),
            u'デイリー':
            ProductListPage(
                'https://shop.nanairo.coop/front/bb/shiga/product/'
                'productlist?cc=0104000000&ps=1000&pn=1&si=0&dt=c&dm=1'),
            u'パン_シリアル':
            ProductListPage(
                'https://shop.nanairo.coop/front/bb/shiga/product/'
                'productlist?&cc=0105000000&ps=1000&pn=1&si=0&dt=c&dm=1'),
            u'米_餅':
            ProductListPage(
                'https://shop.nanairo.coop/front/bb/shiga/product/'
                'productlist?cc=0106000000&ps=1000&pn=1&si=0&dt=c&dm=1'),
            u'加工食品_調味料':
            ProductListPage(
                'https://shop.nanairo.coop/front/bb/shiga/product/'
                'productlist?&cc=0107000000&ps=1000&pn=1&si=0&dt=c&dm=1'),}
        self._requested = False

    @property
    def categories(self, ):
        r"""SUMMARY

        categories()

        @Return:

        @Error:
        """
        if not self._requested:
            thread_request(self._categories.values())
            self._requested = True
        return self._categories

    def current_period(self, ):
        r"""SUMMARY

        current_period()

        @Return:

        @Error:
        """
        return self.categories.get(u'米_餅').period()

    # def iter_goods(self, categories):
    #     r"""SUMMARY

    #     iter_goods(categories)

    #     @Arguments:
    #     - `categories`:

    #     @Return:

    #     @Error:
    #     """
    #     pl_page = self.categories.get(categories, None)
    #     # if pl_page is None:
    #     #     return iter(())
    #     # period = self.c = {}
    #     pd_list, append =
    #     for pdp in pl_page.list_product_detail():
    #         dic[pdp] = pdp.detail_url()
    #     # remove None Value
    #     for k, v in dic.items():
    #         if v is None:
    #             del dic[k]
    #     thread_request(dic.values()) # request detail page
    #     # ProductDetailPage, GoodsDetailPage
    #     for pdp, gdp in dic.iteritems():
    #         yield Sales(code=gdp.goodscode(),
    #                     # period=period,
    #                     jancode=gdp.jancode(),
    #                     name=pdp.title(),
    #                     maker=gdp.maker(),
    #                     country=gdp.gensankoku(),
    #                     explain=gdp.setsumei(),
    #                     price=gdp.price(),
    #                     totalprice=gdp.taxprice(),
    #                     order_no=pdp.order_no(),
    #                     standard=pdp.standard(),
    #            rie(),)
    #         del pdp, gdp

    def iter_goods(self, categories):
        r"""SUMMARY

        iter_goods(categories)

        @Arguments:
        - `categories`:

        @Return:

        @Error:
        """
        pl_page = self.categories.get(categories, None)
        # if pl_page is None:
        #     return iter(())
        # period = self.current_period()
        dic = {}
        pdp_list, append = dotavoid([], 'append')
        for pdp in pl_page.iter_product_detail():
            append(pdp)
            if len(pdp_list) <= 20:
                continue
            thread_request(pdp_list)
            dic = {}
            for p in pdp_list:
                page = p.detail_url()
                if page is None:
                    continue
                dic[p] = page
            pdp_list[:] = []
            thread_request(dic.values()) # request detail page
            # ProductDetailPage, GoodsDetailPage
            for pdp, gdp in dic.iteritems():
                yield Sales(code=gdp.goodscode(),
                            # period=period,
                            jancode=gdp.jancode(),
                            name=pdp.title(),
                            maker=gdp.maker(),
                            country=gdp.gensankoku(),
                            explain=gdp.setsumei(),
                            price=pdp.price(),
                            totalprice=pdp.taxprice(),
                            order_no=pdp.order_no(),
                            standard=pdp.standard(),
                            calorie=gdp.calorie(),)
            dic.clear()
        if pdp_list:
            thread_request(pdp_list)
            dic = {}
            for p in pdp_list:
                page = p.detail_url()
                if page is None:
                    continue
                dic[p] = page
            pdp_list[:] = []
            thread_request(dic.values()) # request detail page
            # ProductDetailPage, GoodsDetailPage
            for pdp, gdp in dic.iteritems():
                yield Sales(code=gdp.goodscode(),
                            # period=period,
                            jancode=gdp.jancode(),
                            name=pdp.title(),
                            maker=gdp.maker(),
                            country=gdp.gensankoku(),
                            explain=gdp.setsumei(),
                            price=pdp.price(),
                            totalprice=pdp.taxprice(),
                            order_no=pdp.order_no(),
                            standard=pdp.standard(),
                            calorie=gdp.calorie(),)

    def list_categories(self, ):
        r"""SUMMARY

        list_categories()

        @Return:

        @Error:
        """
        return self.categories.keys()

    def clear_caches(self, ):
        r"""SUMMARY

        clear_caches()

        @Return:

        @Error:
        """
        dir_ = self.categories.get(u'米_餅').cache_dir
        for f in dir_.listdir():
            f.remove()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# categories.py ends here
