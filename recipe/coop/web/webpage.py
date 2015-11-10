#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""webpage -- DESCRIPTION

from recipe.coop.webpage import ProductListParse


urls = ['https://shop.nanairo.coop/front/bb/shiga/product/'
        'productlist?&cc=0101000000&ps=1000&pn=1&si=0&dt=c&dm=1',
        'https://shop.nanairo.coop/front/bb/shiga/product/'
        'productlist?&cc=0102000000&ps=300&pn=1&si=0&dt=c&dm=1',
        'https://shop.nanairo.coop/front/bb/shiga/product/'
        'productlist?cc=0103000000&ps=1000&pn=1&si=0&dt=c&dm=1',
        'https://shop.nanairo.coop/front/bb/shiga/product/'
        'productlist?cc=0104000000&ps=1000&pn=1&si=0&dt=c&dm=1',
        'https://shop.nanairo.coop/front/bb/shiga/product/'
        'productlist?&cc=0105000000&ps=1000&pn=1&si=0&dt=c&dm=1',
        'https://shop.nanairo.coop/front/bb/shiga/product/'
        'productlist?cc=0106000000&ps=1000&pn=1&si=0&dt=c&dm=1',
        'https://shop.nanairo.coop/front/bb/shiga/product/'
        'productlist?&cc=0107000000&ps=1000&pn=1&si=0&dt=c&dm=1',
        ]

products = [ProductListPage(u) for u in urls]

def tes():
    for p in products:
        p.start()
    for p in products:
        p.join()

"""
from lxml import html
from threading import Thread
import requests
from urlparse import urlparse, parse_qs
from pathhandler import PathHandler
from dotavoider import dotavoid
from recipe.coop.web.thread_request import thread_request
from datetime import datetime


class WebPage(Thread):
    r"""WebPage

    WebPage is a Thread.
    Responsibility:
    """
    cache_dir = PathHandler('/root/homedata/MYTEMP/coopcache')

    def __init__(self, url):
        r"""

        @Arguments:
        - `text`:
        """
        super(WebPage, self).__init__()
        self.url = url
        self._html = None

    def _request(self, ):
        r"""SUMMARY

        _request()

        @Return:

        @Error:
        """
        if self.cache_dir.exists() and not self.cache_dir.isdir():
            raise StandardError('File exists error: {}'.format(self.cache_dir))
        if not self.cache_dir.exists():
            self.cache_dir.mkdir(777, parents=True)
        cache_path = self.cache_dir.join(self.url.replace('/', '|'))
        if cache_path in self.cache_dir.listdir():
            with cache_path.open('rb') as fobj:
                print('Read Caching {}'.format(self.url))
                self._html = html.fromstring(fobj.read().decode('utf-8'))
            return
        print('Requesting {}'.format(self.url))
        response = requests.get(self.url)
        # if not response.ok:
        #     self._html = html.fromstring('<html></html>') # empty
        #     return
        # self._html = html.fromstring(response.text)
        with cache_path.open('wb') as fobj:
            fobj.write(response.text.encode('utf-8'))

    def run(self, ):
        r"""SUMMARY

        run()

        @Return:

        @Error:
        """
        if not self.cache_dir.join(self.url.replace('/', '|')).exists():
            print('DEBUG-1-webpage.py')
            self._request()


class GoodsDetailPage(WebPage):
    r"""GoodsDetailPage

    GoodsDetailPage is a WebPage.
    Responsibility:
    """
    def __init__(self, url):
        r"""

        @Arguments:
        - `url`:
        """
        if not 'GoodsDetail' in url:
            raise ValueError('Invalid url: {}'.format(url))
        WebPage.__init__(self, url)

    def goodscode(self, ):
        r"""SUMMARY

        goodscode()

        @Return:

        @Error:
        """
        query = urlparse(self.url).query
        return parse_qs(query).get('GoodsCode', ['0'])[0]

    def _get_html(self, ):
        r"""SUMMARY

        _get_html()

        @Return:

        @Error:
        """
        if self._html is None:
            self._request()
        return self._html

    def jancode(self, ):
        r"""SUMMARY

        jancode()

        @Return:

        @Error:
        """
        codes = self._get_html().xpath('//*[@id="lblJAN"]')
        if not codes:
            return ''
        return codes[0].text_content()

    def price(self, ):
        r"""SUMMARY

        price()

        @Return:

        @Error:
        """
        prices = self._get_html().xpath('//*[@id="lblHontaiKakaku"]')
        if not prices:
            return ''
        return prices[0].text_content().replace(u'￥', u'')

    def taxprice(self, ):
        r"""SUMMARY

        taxprice()

        @Return:

        @Error:
        """
        prices = self._get_html().xpath('//*[@id="lblKakaku"]')
        if not prices:
            return ''
        return prices[0].text_content().replace(u'￥', u'')

    def calorie(self, ):
        r"""SUMMARY

        calorie()

        @Return:

        @Error:
        """
        calories = self._get_html().xpath('//*[@id="lblCaroly"]')
        if not calories:
            return ''
        return calories[0].text_content()

    def maker(self, ):
        r"""SUMMARY

        maker()

        @Return:

        @Error:
        """
        makers = self._get_html().xpath('//*[@id="lblMaker"]')
        if not makers:
            return ''
        return makers[0].text_content()

    def gensankoku(self, ):
        r"""SUMMARY

        gensankoku()

        @Return:

        @Error:
        """
        gensankokus = self._get_html().xpath('//*[@id="lblGensankokuKakouchi"]')
        if not gensankokus:
            return ''
        return gensankokus[0].text_content()

    def setsumei(self, ):
        r"""SUMMARY

        setsumei()

        @Return:

        @Error:
        """
        setsumeis = self._get_html().xpath('//*[@id="lblSyohinSetsumei"]')
        if not setsumeis:
            return ''
        return setsumeis[0].text_content()

    def __del__(self):
        # Do not imprement "raise"!!
        print('deleted GoodsDetailPage')


class ProductDetailPage(WebPage):
    r"""ProductDetailPage

    ProductDetailPage is a WebPage.
    Responsibility:
    """
    def __init__(self, url):
        r"""

        @Arguments:
        - `url`:
        """
        if not 'productdetail' in url:
            raise ValueError('invalid url {}'.format(url))
        WebPage.__init__(self, url)

    def _get_table(self, ):
        r"""SUMMARY

        _get_product_table()

        @Return:

        @Error:
        """
        if self._html is None:
            self._request()
        return self._html.xpath("//*[@class='product-detail']")

    def title(self, ):
        r"""SUMMARY

        title()

        @Return:

        @Error:
        """
        table = self._get_table()
        if not table:
            return ''
        titles = table[0].xpath("//*[@class='title']")
        if not titles:
            return ''
        return titles[0].text_content()

    def order_no(self, ):
        r"""SUMMARY

        order_no()

        @Return:

        @Error:
        """
        table = self._get_table()
        if not table:
            return ''
        ids = table[0].xpath("//*[@class='id']")
        if not ids:
            return ''
        # expect get '\n    \n    \n    \n      000005\n    '
        result = ids[0].text_content()
        for char in ('\n', ' ',  '\r'):
            result = result.replace(char, '')
        return result

    def standard(self, ):
        r"""SUMMARY

        standard()

        @Return:

        @Error:
        """
        table = self._get_table()
        if not table:
            return ''
        standards = table[0].xpath("//*[@class='standard']")
        if not standards:
            return ''
        return standards[0].text_content()

    def detail_url(self, ):
        r"""SUMMARY

        detail_url()

        @Return:

        @Error:
        """
        table = self._get_table()
        if not table:
            return None
        arrow2 = table[0].xpath("//*[@class='list-arrow2']")
        if not arrow2:
            return None
        lis = arrow2[0].getchildren()
        if not lis:
            return None
        elt_a = lis[0].getchildren()
        if not elt_a:
            return None
        if not u'商品情報検索' in elt_a[0].text_content():
            return None
        return GoodsDetailPage(elt_a[0].attrib['href'])

    def __del__(self):
        # Do not imprement "raise"!!
        print('deleted ProductDetailPage')

BASE_URL = 'https://shop.nanairo.coop'


class ProductListPage(WebPage):
    r"""ProductListParse

    ProductListPage is a object.
    Responsibility:

    https://shop.nanairo.coop/front/bb/shiga/product/productlist?
    """

    def __init__(self, url):
        r"""

        @Arguments:
        - `text`:
        """
        if not 'productlist' in url:
            raise ValueError('invalid url')
        super(ProductListPage, self).__init__(url)

    def period(self, ):
        r"""SUMMARY

        period()

        @Return:

        @Error:
        """
        if self._html is None:
            self._request()
        string = self._html.xpath("//*[@class='date-order']")[0].text_content()
        mstring, tail = string.split(u'月')
        month = int(mstring)
        times = int(tail.split(u'回')[0])
        year = datetime.now().year
        return '{0}{1:02d}{2}'.format(year, month, times)

    def _get_product_table(self, ):
        r"""SUMMARY

        _get_product_table()

        @Return:

        @Error:
        """
        if self._html is None:
            self._request()
        return self._html.xpath("//*[@class='product-list-table']")

    # def list_product_detail(self, ):
    #     r"""SUMMARY

    #     list_product_urls()

    #     @Return:

    #     @Error:
    #     """
    #     table = self._get_product_table()
    #     if not table:
    #         return []
    #     name_links = table[0].xpath("//*[@class='product-name force-wrap']")
    #     if not name_links:
    #         return []
    #     links, append = dotavoid([], 'append')
    #     for url in name_links:
    #         a_link = url.xpath('a')
    #         if not a_link:
    #             continue
    #         append(ProductDetailPage(BASE_URL + a_link[0].attrib['href']))
    #     thread_request(links)
    #     return links

    def iter_product_detail(self, ):
        r"""SUMMARY

        list_product_urls()

        @Return:

        @Error:
        """
        table = self._get_product_table()
        # if not table:
        #     return []
        name_links = table[0].xpath("//*[@class='product-name force-wrap']")
        # if not name_links:
        #     return []
        # links, append = dotavoid([], 'append')
        for url in name_links:
            a_link = url.xpath('a')
            if not a_link:
                continue
            yield ProductDetailPage(BASE_URL + a_link[0].attrib['href'])
        # start, stop = 0, 20
        # while links[start:stop]:
        #     thread_request(links[start:stop])
        #     for link in links[start:stop]:
        #         yield link



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# webpage.py ends here
