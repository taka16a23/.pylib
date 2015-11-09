#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""goods_detail -- DESCRIPTION

"""
from MySQLdb.cursors import DictCursor
from recipe.coop.error import AlreadyExistsError


class GoodsTable(object):
    r"""GoodsTable

    GoodsTable is a object.
    Responsibility:
    """
    table = 't_goods'
    code = 'c_goods_code'
    jancode = 'c_goods_jancode'
    name = 'c_goods_name'
    maker = 'c_goods_maker'
    country = 'c_goods_country'
    explain = 'c_goods_explain'

    key_dic = {code: 'code',
               jancode: 'jancode',
               name: 'name',
               maker: 'maker',
               country: 'country',
               explain: 'explain',
    }

    _value_fmt = (u"('{0[code]}','{0[jancode]}','{0[name]}',"
                  "'{0[maker]}','{0[country]}','{0[explain]}')")

    # if not has values will set null
    _defaults = ['jancode', 'name', 'maker', 'country', 'explain']

    def __init__(self, connection):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        self.connection = connection
        self.cursor = connection.cursor(DictCursor)

    def key_convert(self, dic):
        r"""SUMMARY

        key_convert(dic)

        @Arguments:
        - `dic`:

        @Return:

        @Error:
        """
        for k, v in self.key_dic.items():
            if k in dic:
                dic[v] = dic[k]
                del dic[k]
        return dic

    def _execute(self, query):
        r"""SUMMARY

        _execute(query)

        @Arguments:
        - `query`:

        @Return:

        @Error:
        """
        print(repr(query))
        self.cursor.execute(query)

    def get(self, code):
        r"""SUMMARY

        get(code)

        @Arguments:
        - `code`:

        @Return:

        @Error:
        """
        query = "SELECT * FROM {0.table} WHERE {0.code}='{1}'"
        self._execute(query.format(self, code))
        return self.cursor.fetchall()

    def has_entry(self, code):
        r"""SUMMARY

        has_entry(code)

        @Arguments:
        - `code`:

        @Return:

        @Error:
        """
        return bool(self.get(code))

    def _make_values_fmt(self, *diclist):
        r"""SUMMARY

        _value()

        @Return:

        @Error:
        """
        def type_check(dic):
            if not isinstance(dic['code'], (basestring, )):
                raise TypeError("'code' type is not str. got ({})"
                                .format(type(dic['code'])))
            if len(dic['code']) != 10:
                raise ValueError('code length error got({})'
                                 .format(len(dic['code'])))
            if not isinstance(dic['jancode'], (basestring, )):
                raise TypeError("'jancode' type is not str. got({})"
                                .format(type(dic['jancode'])))
            if not (dic['jancode'] == 'null' or len(dic['jancode']) == 13):
                raise ValueError('jancode value error got({})'
                                 .format(dic['jancode']))
        text_keys = ('name', 'maker', 'country', 'explain')
        for dic in diclist:
            # convert None to 'null'
            for k, v in dic.items():
                if v is None:
                    dic[k] = 'null'
                # escape ' => to ''
                if k in text_keys and v is not None and "'" in v:
                    dic[k] = v.replace("'", "''")
            # set 'null' to default key
            for key in self._defaults:
                if not key in dic:
                    dic[key] = 'null'
            type_check(dic)
        return u','.join([self._value_fmt.format(dic) for dic in diclist])

    def insert(self, **kwargs):
        r"""SUMMARY

        insert(detail)

        @Arguments:
        - `kwargs`:
        'code', jancode', 'name', 'maker', 'country', 'explain'
        @Return:

        @Error:

        """
        query = u"INSERT INTO {0.table} VALUES".format(self)
        query += self._make_values_fmt(kwargs)
        self._execute(query)
        self.connection.commit()

    def insert_many(self, *diclist):
        r"""SUMMARY

        insert_many(dictlist)

        @Arguments:
        - `dictlist`:

        @Return:

        @Error:
        """
        query_fmt = u"INSERT INTO {0.table} VALUES" + self._make_values_fmt(
            *diclist)
        query = query_fmt.format(self)
        self._execute(query)
        self.connection.commit()

    def delete(self, code):
        r"""SUMMARY

        delete(code)

        @Arguments:
        - `code`:

        @Return:

        @Error:
        """
        query = "DELETE from {0.table} WHERE {0.code} = '{1}'"
        self._execute(query.format(self, code))
        self.connection.commit()

    def update(self, **kwargs):
        r"""SUMMARY

        update()

        @Return:

        @Error:
        """
        if self.has_entry(kwargs[self.key_dic[self.code]]):
            self.delete(kwargs[self.key_dic[self.code]])
        self.insert(**kwargs)

    def close(self, ):
        r"""SUMMARY

        close()

        @Return:

        @Error:
        """
        self.cursor.close()

    def __iter__(self):
        """Iterate all entrys."""
        self._execute('SELECT * from {0.table}'.format(self))
        return self

    def next(self, ):
        # for remove None
        entry = self.cursor.fetchone()
        if entry is None:
            raise StopIteration
        return entry

    def __del__(self):
        # Do not imprement "raise"!!
        self.cursor.close()


class SalesTable(object):
    r"""SalesTable

    SalesTable is a object.
    Responsibility:
    """
    table = 't_sales'

    entry_no = 'c_sales_entry_no'
    code = 'c_sales_code'
    period = 'c_sales_period'
    price = 'c_sales_price'
    totalprice = 'c_sales_totalprice'
    order_no = 'c_sales_order_no'
    standard = 'c_sales_standard'
    calorie = 'c_sales_calorie'
    key_dic = {entry_no: 'entry_no',
               code: 'code',
               period: 'period',
               price: 'price',
               totalprice: 'totalprice',
               order_no: 'order_no',
               standard: 'standard',
               calorie: 'calorie',
    }

    _value_fmt = (u"('{0[code]}','{0[period]}',{0[price]},{0[totalprice]},"
                  "'{0[order_no]}','{0[standard]}','{0[calorie]}')")
    _defaults = ['code', 'price', 'totalprice', 'order_no',
                 'standard', 'calorie']

    def __init__(self, connection):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        self.goods = GoodsTable(connection)

    def key_convert(self, dic):
        r"""SUMMARY

        key_convert(dic)

        @Arguments:
        - `dic`:

        @Return:

        @Error:
        """
        self.goods.key_convert(dic)
        for k, v in self.key_dic.items():
            if k in dic:
                dic[v] = dic[k]
                del dic[k]
        for k,  v in dic.items():
            if v == 'null':
                dic[k] = None
        return dic

    @property
    def connection(self, ):
        r"""SUMMARY

        connection()

        @Return:

        @Error:
        """
        return self.goods.connection

    @property
    def cursor(self, ):
        r"""SUMMARY

        cursor()

        @Return:

        @Error:
        """
        return self.goods.cursor

    def _execute(self, query):
        r"""SUMMARY

        _execute(query)

        @Arguments:
        - `query`:

        @Return:

        @Error:
        """
        print(repr(query))
        self.cursor.execute(query)

    def get_entry(self, entry_no):
        r"""SUMMARY

        get_entry(code, period)

        @Arguments:
        - `code`:
        - `period`:

        @Return:

        @Error:
        """
        query = "SELECT * FROM "
        query += "{0.table} LEFT OUTER JOIN "
        query += "{1.table} ON "
        query += "{0.table}.{0.code}={1.table}.{1.code} "
        query += "WHERE {0.table}.{0.entry_no}={2}"
        query = query.format(self, self.goods, entry_no)
        self._execute(query)
        return [self.key_convert(d) for d in self.cursor.fetchall()]

    def get_sales(self, code, period):
        r"""SUMMARY

        get_sales(code, period)

        @Arguments:
        - `code`:
        - `period`:

        @Return:

        @Error:
        """
        query = "SELECT * FROM "
        query += "{0.table} LEFT OUTER JOIN "
        query += "{1.table} ON {0.table}.{0.code}={1.table}.{1.code} "
        query += "WHERE {0.table}.{0.code}='{2}' AND {0.table}.{0.period}='{3}'"
        query = query.format(self, self.goods, code, period)
        self._execute(query)
        return [self.key_convert(d) for d in self.cursor.fetchall()]

    def has_entry(self, entry_no):
        r"""SUMMARY

        has_entry(code, period)

        @Arguments:
        - `code`:
        - `period`:

        @Return:

        @Error:
        """
        return bool(self.get_entry(entry_no))

    def has_sales(self, code, period):
        r"""SUMMARY

        has_sales(code, period)

        @Arguments:
        - `code`:
        - `period`:

        @Return:

        @Error:
        """
        return bool(self.get_sales(code, period))

    def iter_codes(self, ):
        r"""SUMMARY

        iter_code()

        @Return:

        @Error:
        """
        query = "SELECT DISTINCT {0.code} FROM {0.table} ORDER BY {0.code}"
        query = query.format(self)
        self._execute(query)
        while 1:
            yield self.next().values()[0]

    def iter_periods(self, ):
        r"""SUMMARY

        iter_periods()

        @Return:

        @Error:
        """
        query = "SELECT DISTINCT {0.period} FROM {0.table} ORDER BY {0.period}"
        query = query.format(self)
        self._execute(query)
        while 1:
            yield self.next().values()[0]

    def iter_jancodes(self, ):
        r"""SUMMARY

        iter_jancodes()

        @Return:

        @Error:
        """
        query = "SELECT DISTINCT {1.jancode} FROM {0.table} "
        query += "LEFT OUTER JOIN "
        query += "{1.table} ON {0.table}.{0.code}={1.table}.{1.code} "
        query += "ORDER BY {1.jancode}"
        query = query.format(self, self.goods)
        self._execute(query)
        while 1:
            yield self.next().values()[0]

    def iter_names(self, ):
        r"""SUMMARY

        iter_names()

        @Return:

        @Error:
        """
        query = "SELECT DISTINCT {1.name} FROM {0.table} "
        query += "LEFT OUTER JOIN "
        query += "{1.table} ON {0.table}.{0.code}={1.table}.{1.code} "
        query += "ORDER BY {1.name}"
        query = query.format(self, self.goods)
        self._execute(query)
        while 1:
            yield self.next().values()[0]

    def iter_by_code(self, code):
        r"""SUMMARY

        iter_by_code(code)

        @Arguments:
        - `code`:

        @Return:

        @Error:
        """
        query = "SELECT * FROM "
        query += "{0.table} "
        query += "LEFT OUTER JOIN "
        query += "{1.table} ON {0.table}.{0.code}={1.table}.{1.code} "
        query += "WHERE {0.table}.{0.code}='{2}'"
        query = query.format(self, self.goods, code)
        self._execute(query)
        while 1:
            yield self.next()

    def iter_by_period(self, period):
        r"""SUMMARY

        iter_by_period(period)

        @Arguments:
        - `period`:

        @Return:

        @Error:
        """
        query = "SELECT * FROM "
        query += u"{0.table} "
        query += "LEFT OUTER JOIN "
        query += "{1.table} ON {0.table}.{0.code}={1.table}.{1.code} "
        query += "WHERE {0.table}.{0.period}='{2}'"
        query = query.format(self, self.goods, period)
        self._execute(query)
        while 1:
            yield self.next()

    def iter_by_jancode(self, jancode):
        r"""SUMMARY

        iter_by_jancode(jancode)

        @Arguments:
        - `period`:

        @Return:

        @Error:
        """
        query = "SELECT * FROM "
        query += u"{0.table} "
        query += "LEFT OUTER JOIN "
        query += "{1.table} ON {0.table}.{0.code}={1.table}.{1.code} "
        query += "WHERE {1.table}.{1.jancode}='{2}'"
        query = query.format(self, self.goods, jancode)
        self._execute(query)
        while 1:
            yield self.next()

    def iter_by_name(self, name):
        r"""SUMMARY

        iter_by_name(name)

        @Arguments:
        - `period`:

        @Return:

        @Error:
        """
        query = "SELECT * FROM "
        query += u"{0.table} "
        query += "LEFT OUTER JOIN "
        query += "{1.table} ON {0.table}.{0.code}={1.table}.{1.code} "
        query += "WHERE {1.table}.{1.name}='{2}'"
        query = query.format(self, self.goods, name)
        self._execute(query)
        while 1:
            yield self.next()

    def _make_values_fmt(self, *diclist):
        r"""SUMMARY

        _value()

        @Return:

        @Error:
        """
        def type_check(dic):
            if not isinstance(dic['code'], (basestring, )):
                raise TypeError("'code' type is not str. got ({})"
                                .format(type(dic['code'])))
            if len(dic['code']) != 10:
                raise ValueError('code length error got({})'
                                 .format(len(dic['code'])))
        text_keys = ('standard', 'calorie')
        for dic in diclist:
            # convert None to 'null'
            for k, v in dic.items():
                if v is None:
                    dic[k] = 'null'
                # escape ' => ''
                if k in text_keys and v is not None and "'" in v:
                    dic[k] = v.replace("'", "''")
            # set 'null' to default key
            for key in self._defaults:
                dic.setdefault(key, 'null')

            type_check(dic)
        return u','.join([self._value_fmt.format(dic) for dic in diclist])

    def delete(self, code, period):
        r"""SUMMARY

        delete(code)

        @Arguments:
        - `code`:

        @Return:

        @Error:
        """
        query = "DELETE from {0.table} "
        query += "WHERE {0.code}='{1}' "
        query += "AND {0.period}='{2}'"
        query = query.format(self, code, period)
        self._execute(query)
        self.connection.commit()

    def insert(self, code, period, **kwargs):
        r"""SUMMARY

        insert()

        @Return:

        @Error:

        """
        if self.has_sales(code, period):
            raise AlreadyExistsError(
                'already exists (code: {}, period: {})'.format(code, period))
        values = kwargs.copy()
        values['code'] = code
        values['period'] = period
        if not self.goods.has_entry(code):
            self.goods.insert(**values)
        query = u"INSERT INTO "
        query += u"{0.table}"
        query += u"({0.code},{0.period},{0.price},{0.totalprice},"
        query += u"{0.order_no},{0.standard},{0.calorie}) "
        query += u"VALUES"
        query = query.format(self)
        query += self._make_values_fmt(values)
        self._execute(query)
        self.connection.commit()

    def __iter__(self):
        """Iterate all entrys."""
        query = "SELECT * FROM "
        query += "{0.table} "
        query += "LEFT OUTER JOIN {1.table} ON "
        query += "{0.table}.{0.code}={1.table}.{1.code}"
        query = query.format(self, self.goods)
        self._execute(query)
        return self

    def next(self, ):
        # for remove None
        entry = self.cursor.fetchone()
        if entry is None:
            raise StopIteration
        return self.key_convert(entry)

    def __del__(self):
        # Do not imprement "raise"!!
        self.cursor.close()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# sales.py ends here
