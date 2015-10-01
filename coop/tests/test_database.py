#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: test_database.py 485 2015-09-29 03:10:26Z t1 $
# $Revision: 485 $
# $Date: 2015-09-29 12:10:26 +0900 (Tue, 29 Sep 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-09-29 12:10:26 +0900 (Tue, 29 Sep 2015) $

r"""Name: test_database.py

['skipTest', ]

['assertAlmostEqual', 'assertAlmostEquals', 'assertApproximates',
 'assertDictContainsSubset', 'assertDictEqual', 'assertEndsWith', 'assertEqual',
 'assertEquals', 'assertFalse', 'assertGreater', 'assertGreaterEqual',
 'assertIdentical', 'assertIn', 'assertIs', 'assertIsInstance', 'assertIsNone',
 'assertIsNot', 'assertIsNotInstance', 'assertIsNotNone', 'assertItemsEqual',
 'assertLess', 'assertLessEqual', 'assertListEqual', 'assertMethodsMatch',
 'assertMultiLineEqual', 'assertNotAlmostEqual', 'assertNotAlmostEquals',
 'assertNotApproximates', 'assertNotEndsWith', 'assertNotEqual',
 'assertNotEquals', 'assertNotIdentical', 'assertNotIn', 'assertNotIsInstance',
 'assertNotRegexpMatches', 'assertNotStartsWith', 'assertRaises',
 'assertRaisesRegexp', 'assertRegexpMatches', 'assertSequenceEqual',
 'assertSetEqual', 'assertStartsWith', 'assertTrue', 'assertTupleEqual', ]

['failIf', 'failIfAlmostEqual', 'failIfApproximates', 'failIfEndsWith',
 'failIfEqual', 'failIfIdentical', 'failIfIn', 'failIfIs', 'failIfIsInstance',
 'failIfStartsWith', 'failUnless', 'failUnlessAlmostEqual',
 'failUnlessApproximates', 'failUnlessEndsWith', 'failUnlessEqual',
 'failUnlessIdentical', 'failUnlessIn', 'failUnlessIs', 'failUnlessIsInstance',
 'failUnlessMethodsMatch', 'failUnlessRaises', 'failUnlessRaisesRegexp',
 'failUnlessStartsWith', 'failureException', ]

"""
from mocker import *
from coop.database import CoopDatabase
from coop.goods import CoopGoods
from collections import Iterable


class TestDatabase(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.dummy_goods = [CoopGoods(code=9999999999,
                                     jancode=9999999999999,
                                     name='dummy_name',
                                     maker=u'dummy_maker',
                                     origin_country=u'中国',
                                     explain='dummy_explain',
                                     period=2014011,
                                     price=100,
                                     totalprice=108,
                                     order_no=000001,
                                     standard=u'100g',
                                     calorie=u'100cal'),
                            CoopGoods(code=9999999998,
                                     jancode=9999999999998,
                                     name='dummy_name2',
                                     maker=u'dummy_maker2',
                                     origin_country=u'アメリカ',
                                     explain='dummy_explain2',
                                     period=2014011,
                                     price=200,
                                     totalprice=216,
                                     order_no=000002,
                                     standard=u'200g',
                                     calorie=u'200cal'),
                            CoopGoods(code=9999999997,
                                     jancode=9999999999997,
                                     name='dummy_name3',
                                     maker=u'dummy_maker3',
                                     origin_country=u'カナダ',
                                     explain='dummy_explain3',
                                     period=2014011,
                                     price=300,
                                     totalprice=324,
                                     order_no=000003,
                                     standard=u'300g',
                                     calorie=u'300cal'),
                                     ]

    def setUp(self):
        self.database = CoopDatabase()
        self.mocker.replay()

    def test_iter_goods(self, ):
        self.database.register_goods(self.dummy_goods[0])
        self.assertIsInstance(self.database.iter_goods(), Iterable)
        self.assertIsInstance(self.database.iter_goods().next(), CoopGoods)

    def test_list_goods(self, ):
        self.database.register_goods(self.dummy_goods[0])
        self.assertIsInstance(self.database.list_goods(), list)
        self.assertIsInstance(self.database.list_goods()[0], CoopGoods)




    def tearDown(self):
        for goods in self.dummy_goods:
            self.database.unregister_goods(goods)

    @classmethod
    def tearDownClass(cls, ):
        pass


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_database.py ends here
