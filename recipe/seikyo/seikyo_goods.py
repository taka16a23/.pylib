#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
## parse goods

# parse product detail page urls from product list
# open product detail page
# parse goods detail page url from product detail
# open goods detail page
# parge goods detail (jancode, name, price, price with tax, Country of Origin,
#                      order number, maker, Calorie, explain, additional explain                      quantity)

# get outputable xls sheet from date
# output to xls sheet

"""
import argparse
import sys
import requests
from time import localtime
import grequests
from lxml import html
from pathhandler import PathHandler
from collections import deque
from urlparse import urlparse, parse_qs
import xlwt, xlrd
from xlutils.copy import copy as xlcopy
import datetime
import cPickle
from collections import OrderedDict



PRODUCT_LIST_URL = 'https://shop.nanairo.coop/front/bb/shiga/product/productlist?&pn={}&si=0&dm=1&amp;rc=0&ps=60&spc=&cps=0&trial=0'

CACHE_PATH = PathHandler('/mnt/data/MYTEMP').join('seikyo_web_cache')
PRODUCT_LIST_CACHE_PATH = CACHE_PATH.join('productlists')
PRODUCT_DETAIL_CACHE_PATH = CACHE_PATH.join('productdetails')
GOODS_DETAIL_CACHE_PATH = CACHE_PATH.join('goodsdetails')
SEIKYO_ARCHIVE_PATH = PathHandler('/data/archive/ref/seikyo/')
GOODS_DATABASE_PATH = SEIKYO_ARCHIVE_PATH.join('goods')


BASE_URL = 'https://shop.nanairo.coop'

PRODUCT_LIST_URLS = {
    u'生鮮食品':
    'https://shop.nanairo.coop/front/bb/shiga/product/'
    'productlist?&cc=0101000000&ps=1000&pn=1&si=0&dt=c&dm=1',
    u'牛乳卵':
    'https://shop.nanairo.coop/front/bb/shiga/product/'
    'productlist?&cc=0102000000&ps=300&pn=1&si=0&dt=c&dm=1',
    u'冷凍':
    'https://shop.nanairo.coop/front/bb/shiga/product/'
    'productlist?cc=0103000000&ps=1000&pn=1&si=0&dt=c&dm=1',
    u'デイリー':
    'https://shop.nanairo.coop/front/bb/shiga/product/'
    'productlist?cc=0104000000&ps=1000&pn=1&si=0&dt=c&dm=1',
    u'パン_シリアル':
    'https://shop.nanairo.coop/front/bb/shiga/product/'
    'productlist?&cc=0105000000&ps=1000&pn=1&si=0&dt=c&dm=1',
    u'米_餅':
    'https://shop.nanairo.coop/front/bb/shiga/product/'
    'productlist?cc=0106000000&ps=1000&pn=1&si=0&dt=c&dm=1',
    u'加工食品_調味料':
    'https://shop.nanairo.coop/front/bb/shiga/product/'
    'productlist?&cc=0107000000&ps=1000&pn=1&si=0&dt=c&dm=1',}


def async_requests(urls):
    r"""SUMMARY

    async_requests(urls)

    @Arguments:
    - `urls`:

    @Return:

    @Error:
    """
    return grequests.map((grequests.get(u, verify=False) for u in urls))


class CacheFileRequests(object):
    r"""CacheFileRequests

    CacheFileRequest is a object.
    Responsibility:
    """
    def __init__(self, directory):
        r"""

        @Arguments:
        - `directory`:
        """
        self._directory = PathHandler(directory)
        if self._directory.isfile():
            # TODO: (Atami) [2015/08/13]
            raise StandardError()

    def clear_caches(self, ):
        r"""SUMMARY

        clear_caches()

        @Return:

        @Error:
        """
        for path in self._directory.listdir(r'\.pickled$'):
            path.remove()

    def remove_cachedir(self, ):
        r"""SUMMARY

        remove_cachedir()

        @Return:

        @Error:
        """
        self._directory.remove()

    def get_cache_path(self, url):
        r"""SUMMARY

        get_cache_path(url)

        @Arguments:
        - `url`:

        @Return:

        @Error:
        """
        cache_name = u'{}.pickled'.format(url.replace('/', '|'))
        return self._directory.join(cache_name)

    def get_cache(self, url):
        r"""SUMMARY

        get_cache()

        @Return:

        @Error:
        """
        path = self.get_cache_path(url)
        if not path.exists():
            return None
        with path.open('rb') as fobj:
            return cPickle.load(fobj)

    def cache_file(self, url, obj):
        r"""SUMMARY

        cache_file(url, obj)

        @Arguments:
        - `url`:
        - `obj`:

        @Return:

        @Error:
        """
        path = self.get_cache_path(url)
        directory = path.get_dirname()
        if not directory.exists():
            directory.mkdir(777, parents=True)
        with path.open('wb') as fobj:
            cPickle.dump(obj, fobj, cPickle.HIGHEST_PROTOCOL)

    def grequests_get(self, urls, params=None, **kwargs):
        r"""SUMMARY

        grequests_get(urls)

        @Arguments:
        - `urls`:

        @Return:

        @Error:
        """
        ordered = OrderedDict.fromkeys(urls)
        remains = []
        for url in urls:
            ordered[url] = self.get_cache(url)
        remains = [x for x, value in ordered.items() if value is None]
        resps = grequests.map(
            (grequests.get(u, params=params, **kwargs) for u in remains))
        for url, resp in zip(remains, resps):
            ordered[url] = resp
            self.cache_file(url, resp)
        return ordered


def list_productlist_cache_path():
    r"""*SUMMARY

    iter_productlist_cache_path()

    @Return:

    @Error:
    """
    if not PRODUCT_LIST_CACHE_PATH.exists():
        PRODUCT_LIST_CACHE_PATH.mkdir(777, parents=True)

    all_pathes, pathes, urls = [], [], []

    for category, url in PRODUCT_LIST_URLS.items():
        path = PRODUCT_LIST_CACHE_PATH.join(u'{}.html'.format(category))
        all_pathes.append(path)
        if path.exists() and path.get_size() == 0:
            path.remove()
        if path.exists(): # already cached
            continue
        pathes.append(path)
        urls.append(url)
    print('requesting {}'.format(urls))
    if urls:
        resp = async_requests(urls)
        for r, p in zip(resp, pathes):
            with p.open('w') as fobj:
                fobj.write(r.text)
    return all_pathes


def iter_productlist_tree():
    r"""SUMMARY

    iter_productlist_tree()

    @Return:

    @Error:
    """
    for path in list_productlist_cache_path():
        with path.open('r') as fobj:
            yield html.fromstring(fobj.read())


def iter_productdetail_urls():
    r"""SUMMARY

    iter_productdetail_urls()

    @Return:

    @Error:
    """
    for tree in iter_productlist_tree():
        table = tree.xpath("//*[@class='product-list-table']")[0]
        order_nos = table.xpath("//*[@class='order-no-box']")
        product_urls = table.xpath("//*[@class='product-name force-wrap']")
        for no, url in zip(order_nos, product_urls):
            yield no.text_content(), BASE_URL + url.xpath('a')[0].attrib['href']


def iter_productdetail_tree():
    r"""SUMMARY

    iter_productdetail_tree()

    @Return:

    @Error:
    """
    if not PRODUCT_DETAIL_CACHE_PATH.exists():
        PRODUCT_DETAIL_CACHE_PATH.mkdir(777, parents=True)

    all_pathes, ress, pathes = [], [], []
    no_urls = deque(iter_productdetail_urls())
    print(len(no_urls))
    while len(no_urls):
        no, url = no_urls.popleft()
        path = PRODUCT_DETAIL_CACHE_PATH.join('{}.html'.format(no))
        all_pathes.append((no, path))
        if path.exists() and path.get_size() == 0:
            path.remove()
        if path.exists():
            continue
        pathes.append(path)
        ress.append(grequests.get(url, verify=False))
        if 20 <= len(ress) or len(no_urls) == 0:
            print('takings {}'.format(url))
            resp = grequests.map(ress)
            for p, r in zip(pathes, resp):
                if r is None:
                    continue
                with p.open('w') as fobj:
                    print(u'writing {}'.format(p))
                    fobj.write(r.text)
            ress, pathes = [], []
    return all_pathes


def iter_goodsdetail_tree():
    r"""SUMMARY

    iter_goodsdetai_tree()

    @Return:

    @Error:
    """
    for no, path in iter_productdetail_tree():
        with path.open('r') as fobj:
            yield no, html.fromstring(fobj.read())


def iter_goodsdetail_urls():
    r"""SUMMARY

    iter_goodsdetail_urls()

    @Return:

    @Error:
    """
    nos, titles, urls, standards = [], [], [], []
    for no, tree in iter_goodsdetail_tree():
        nos.append(no)
        table = tree.xpath("//*[@class='product-detail']")[0]
        standards.append(
            table.xpath("//*[@class='standard']")[0].text_content())
        titles.append(table.xpath("//*[@class='title']")[0].text_content())
        arrow2 = table.xpath("//*[@class='list-arrow2']")[0]
        lis = arrow2.getchildren()
        if not lis:
            urls.append(None)
            continue
        elt_a = lis[0].getchildren()
        if not elt_a:
            urls.append(None)
            continue
        atag = elt_a[0]
        if not u'商品情報検索' in atag.text_content():
            urls.append(None)
            continue
        urls.append(atag.attrib['href'])
    return nos, titles, urls, standards


def parse_goodscode(url):
    r"""SUMMARY

    parse_goodscode(url)

    @Arguments:
    - `url`:

    @Return:

    @Error:
    """
    query = urlparse(url).query
    return parse_qs(query).get('GoodsCode', ['0'])[0]


def parse_ids(path):
    r"""*SUMMARY

    parse_ids(path)

    @Arguments:
    - `path`:

    @Return:

    @Error:
    """
    fobj = path.open('rb')
    tree = html.fromstring(fobj.read().decode('utf-8'))
    fobj.close()
    try:
        jancode = tree.xpath('//*[@id="lblJAN"]')[0].text_content()
    except IndexError:
        jancode = ''
    try:
        price = tree.xpath(
            '//*[@id="lblHontaiKakaku"]')[0].text_content().replace(u'￥', u'')
    except IndexError:
        price = ''
    try:
        taxprice = tree.xpath(
            '//*[@id="lblKakaku"]')[0].text_content().replace(u'￥', u'')
    except IndexError:
        taxprice = ''
    try:
        calorie = tree.xpath('//*[@id="lblCaroly"]')[0].text_content()
    except IndexError:
        calorie = ''
    try:
        maker = tree.xpath('//*[@id="lblMaker"]')[0].text_content()
    except IndexError:
        maker = ''
    try:
        gensankoku = tree.xpath(
            '//*[@id="lblGensankokuKakouchi"]')[0].text_content()
    except IndexError:
        gensankoku = ''
    try:
        setsumei = tree.xpath(
            '//*[@id="lblSyohinSetsumei"]')[0].text_content()
    except IndexError:
        setsumei = ''
    return jancode, price, taxprice, calorie, maker, gensankoku, setsumei


def iter_goodsdetail_path():
    r"""SUMMARY

    iter_goodsdetail_path()

    @Return:

    @Error:
    """
    if not GOODS_DETAIL_CACHE_PATH.exists():
        GOODS_DETAIL_CACHE_PATH.mkdir(777, parents=True)

    all_pathes, ress, pathes, goodscodes = [], [], [], []
    nos, titles, urls, standards = iter_goodsdetail_urls()
    durls = deque(urls)
    dnos = deque(nos)
    header = {'User-Agent': 'Chrome/26.0.1410.63 Safari/537.31'}
    print(len(durls))
    while len(durls):
        url = durls.popleft()
        no = dnos.popleft()
        if url is None:
            goodscodes.append('0')
            all_pathes.append(None)
            continue
        goodscodes.append(parse_goodscode(url))
        path = GOODS_DETAIL_CACHE_PATH.join(u'{}.html'.format(no))
        all_pathes.append(path)
        if path.exists() and path.get_size() == 0:
            path.remove()
        if path.exists():
            continue
        pathes.append(path)
        ress.append(grequests.get(url, headers=header, verify=False))
        if 20 <= len(ress) or len(durls) == 0:
            print('takings {}'.format(url))
            resp = grequests.map(ress)
            for p, r in zip(pathes, resp):
                with p.open('wb') as fobj:
                    print(u'writing {}'.format(p))
                    fobj.write(r.text.encode('utf-8'))
            ress, pathes = [], []
    return nos, goodscodes, titles, all_pathes, standards


class GoodsDetail(object):
    r"""GoodsDetail

    GoodsDetail is a object.
    Responsibility:
    """
    def __init__(self, **kwargs):
        r"""

        @Arguments:
        - `kwargs`:
        """
        self._details = kwargs.copy()

    def get_jancode(self, ):
        r"""SUMMARY

        get_jancode()

        @Return:

        @Error:
        """
        return self._details.get('jancode', '0000000000000')

    def set_jancode(self, jancode):
        r"""SUMMARY

        set_jancode(jancode)

        @Arguments:
        - `jancode`:

        @Return:

        @Error:
        """
        self._details['jancode'] = jancode

    jancode = property(get_jancode, set_jancode)

    def get_name(self, ):
        r"""SUMMARY

        get_name()

        @Return:

        @Error:
        """
        return self._details.get('name', '')

    def set_name(self, name):
        r"""SUMMARY

        set_name(name)

        @Arguments:
        - `name`:

        @Return:

        @Error:
        """
        self._details['name'] = name

    name = property(get_name, set_name)

    def get_price(self, ):
        r"""SUMMARY

        get_price()

        @Return:

        @Error:
        """
        return self._details.get('price', '')

    def set_price(self, price):
        r"""SUMMARY

        set_price(price)

        @Arguments:
        - `price`:

        @Return:

        @Error:
        """
        self._details['price'] = price

    price = property(get_price, set_price)

    def get_price_with_tax(self, ):
        r"""SUMMARY

        get_price_with_tax()

        @Return:

        @Error:
        """
        return self._details.get('price_with_tax', '')

    def set_price_with_tax(self, price):
        r"""SUMMARY

        set_price_with_tax()

        @Return:

        @Error:
        """
        self._details['price_with_tax'] = price

    price_with_tax = property(get_price_with_tax, set_price_with_tax)

    def get_country_of_origin(self, ):
        r"""SUMMARY

        get_country_of_origin()

        @Return:

        @Error:
        """
        return self._details.get('origin', '')

    def set_country_of_origin(self, origin):
        r"""SUMMARY

        set_country_of_origin(origin)

        @Arguments:
        - `origin`:

        @Return:

        @Error:
        """
        self._details['origin'] = origin

    origin = property(get_country_of_origin, set_country_of_origin)

    def get_maker(self, ):
        r"""SUMMARY

        get_maker()

        @Return:

        @Error:
        """
        return self._details.get('maker', '')

    def set_maker(self, maker):
        r"""SUMMARY

        set_maker(maker)

        @Arguments:
        - `maker`:

        @Return:

        @Error:
        """
        self._details['maker'] = maker

    maker = property(get_maker, set_maker)

    def get_calorie(self, ):
        r"""SUMMARY

        get_calorie()

        @Return:

        @Error:
        """
        return self._details.get('calorie', '')

    def set_calorie(self, calorie):
        r"""SUMMARY

        set_calorie(calorie)

        @Arguments:
        - `calorie`:

        @Return:

        @Error:
        """
        self._details['calorie'] = calorie

    calorie = property(get_calorie, set_calorie)

    def get_order_no(self, ):
        r"""SUMMARY

        get_order_no()

        @Return:

        @Error:
        """
        return self._details.get('orderno', '')

    def set_order_no(self, orderno):
        r"""SUMMARY

        set_order_no(orderno)

        @Arguments:
        - `orderno`:

        @Return:

        @Error:
        """
        self._details['orderno'] = orderno

    order_no = property(get_order_no, set_order_no)

    def get_explain(self, ):
        r"""SUMMARY

        get_explain()

        @Return:

        @Error:
        """
        return self._details.get('explain')

    def set_explain(self, explain):
        r"""SUMMARY

        set_explain(explain)

        @Arguments:
        - `explain`:

        @Return:

        @Error:
        """
        self._details['explain'] = explain

    explain = property(get_explain, set_explain)

    def get_standard(self, ):
        r"""SUMMARY

        get_standard()

        @Return:

        @Error:
        """
        return self._details.get('standard', '')

    def set_standard(self, standard):
        r"""SUMMARY

        set_standard(standard)

        @Arguments:
        - `standard`:

        @Return:

        @Error:
        """
        self._details['standard'] = standard

    standard = property(get_standard, set_standard)

    def get_goodscode(self, ):
        r"""SUMMARY

        get_goodscode()

        @Return:

        @Error:
        """
        return self._details.get('goodscode', '')

    def set_goodscode(self, goodscode):
        r"""SUMMARY

        set_goodscode(goodscode)

        @Arguments:
        - `goodscode`:

        @Return:

        @Error:
        """
        self._details['goodscode'] = goodscode

    goodscode = property(get_goodscode, set_goodscode)

    def __repr__(self):
        return repr(self._details)


def iter_goodsdetail():
    r"""SUMMARY

    iter_goodsdetail()

    @Return:

    @Error:
    """
    nos, goodscodes, titles, allpaths, standards = iter_goodsdetail_path()
    for no, goodscode, title, path, standard in zip(
            nos, goodscodes, titles, allpaths, standards):
        jancode, price, taxprice, calorie, maker, gensankoku = ('', ) * 6
        if not path is None:
            jancode, price, taxprice, calorie, maker, gensankoku, setsumei = parse_ids(path)
        yield GoodsDetail(jancode=jancode, price=price, name=title,
                          price_with_tax=taxprice, origin=gensankoku,
                          maker=maker, calorie=calorie, orderno=no,
                          explain=setsumei, goodscode=goodscode,
                          standard=standard)


def get_xls_name(year, month):
    r"""SUMMARY

    get_xls_name(year, times)

    @Arguments:
    - `year`:
    - `times`:

    @Return:

    @Error:
    """
    return GOODS_DATABASE_PATH.join(u'{}{}'.format(year, month))


def get_date_orders():
    r"""SUMMARY

    get_date_orders()

    @Return:

    @Error:
    """
    year = datetime.datetime.now().year
    rep = requests.get(
        'https://shop.nanairo.coop/front/bb/shiga/top/top', verify=False)
    tree = html.fromstring(rep.text)
    string = tree.xpath("//*[@class='date-order']")[0].text_content()
    mstring, tail = string.split(u'月')
    month = int(mstring)
    times = int(tail.split(u'回')[0])
    return year, month, times


def clear_row(row):
    r"""SUMMARY

    clear_row(row)

    @Arguments:
    - `row`:

    @Return:

    @Error:
    """
    for column in xrange(0, row.get_max_col() + 1):
        row.set_cell_blank(column)


def clear_sheet(sheet):
    r"""SUMMARY

    clear_sheet(sheet)

    @Arguments:
    - `sheet`:

    @Return:

    @Error:
    """
    for row in sheet.rows.values():
        clear_row(row)


HEADING = ['JAN Code', 'Goods Code', 'Order No.', 'Name', 'Price',
           'Total Price', 'Country of Origin', 'Maker', 'Calorie', 'Standard',
           'Explain']


def tes():
    r"""SUMMARY

    tes()

    @Return:

    @Error:
    """
    year, month, times = get_date_orders()
    path = PathHandler(GOODS_DATABASE_PATH.join(u'{}_{}.xls'.format(year, month)))
    if not path.exists():
        wbook = xlwt.Workbook()
        sheet = wbook.add_sheet(unicode(times), cell_overwrite_ok=True)
    else:
        rbook = xlrd.open_workbook(path, formatting_info=True)
        wbook = xlcopy(rbook)
        if unicode(times) in rbook.sheet_names():
            index = rbook.sheet_names().index(unicode(times))
            sheet = wbook.get_sheet(index)
            clear_sheet(sheet)
        else:
            sheet = wbook.add_sheet(unicode(times), cell_overwrite_ok=True)
    row = sheet.row(0)
    for column, string in enumerate(HEADING, start=0):
        row.write(column, string)
    for rown, detail in enumerate(iter_goodsdetail(), start=1):
        sheet.write(rown, 0, detail.jancode)
        sheet.write(rown, 1, detail.goodscode)
        sheet.write(rown, 2, detail.order_no)
        sheet.write(rown, 3, detail.name)
        sheet.write(rown, 4, detail.price)
        sheet.write(rown, 5, detail.price_with_tax)
        sheet.write(rown, 6, detail.origin)
        sheet.write(rown, 7, detail.maker)
        sheet.write(rown, 8, detail.calorie)
        sheet.write(rown, 9, detail.standard)
        sheet.write(rown, 10, detail.explain)
    wbook.save(path)


def _predef_options():
    parser = argparse.ArgumentParser(description=""" """)

    parser.add_argument('--debug',
            dest='debug',
            action='store_true',
            default=False,
            required=False,
            # (yas/expand-link "argparse_other_options" t)
            help='A lot of messages.')

    # (yas/expand-link "argparse_add_argument" t)
    return parser


def _main():
    parser = _predef_options()
    opts = parser.parse_args()
    # parser.print_usage()
    # maintenance from 03:00 to 6:00
    now = localtime()
    if 3 <= now.tm_hour <= 6:
        print('DEBUG-1-seikyo_goods.py')
        return 1
    # if now.tm_min <= 30:
    #     print('DEBUG-2-seikyo_goods.py')
    #     return 1
    # execute
    tes()
    if not opts.debug:
        CACHE_PATH.remove()
    return 0

if __name__ == '__main__':
    sys.exit(_main())
