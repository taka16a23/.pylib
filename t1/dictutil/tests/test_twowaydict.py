#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_twowaydict.py

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
from .. import twowaydict


class TestTwoWayDict(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.samplekey = 'key'
        cls.samplevalue = 1
        cls.sample1 = (('world', 2), ('google', 4), ('hello', 1), ('yahoo', 3))
        cls.sample2 = dict(cls.sample1)
        cls.sample3 = {}
        for key, value in cls.sample2.items():
            cls.sample3[key] = value
            cls.sample3[value] = key

    def setUp(self):
        self.dic = twowaydict.TwoWayDict()
        self.mocker.replay()

    def test_update_None(self, ):
        expects = {}
        self.dic.update()
        self.assertEqual(expects, self.dic)

    def test_update_TwoWayDict(self, ):
        expects = twowaydict.TwoWayDict(self.sample2)
        self.dic.update(expects)
        self.assertEqual(expects, self.dic)

    def test_update_dict(self, ):
        expects = self.sample3
        self.dic.update(expects)
        self.assertEqual(expects, self.dic)

    def test_update_tuple(self, ):
        expects = self.sample3
        self.dic.update(self.sample1)
        self.assertEqual(expects, self.dic)

    def test_update_kwargs(self, ):
        expects = self.sample3
        self.dic.update(world=2, google=4, hello=1, yahoo=3)
        self.assertEqual(expects, self.dic)

    def test___init__tuple(self, ):
        expects = self.sample3
        got = twowaydict.TwoWayDict(self.sample1)
        self.assertEqual(expects, got)

    def test___init__dict(self, ):
        expects = self.sample3
        got = twowaydict.TwoWayDict(self.sample2)
        self.assertEqual(expects, got)

    def test___init__TwoWayDict(self, ):
        expects = self.sample3
        got = twowaydict.TwoWayDict(twowaydict.TwoWayDict(self.sample2))
        self.assertEqual(expects, got)

    def test___init__None(self, ):
        expects = {}
        got = twowaydict.TwoWayDict()
        self.assertEqual(expects, got)

    def test___init__kwargs(self, ):
        expects = self.sample3
        got = twowaydict.TwoWayDict(world=2, google=4, hello=1, yahoo=3)
        self.assertEqual(expects, got)

    def test___setitem__(self, ):
        self.dic[self.samplekey] = self.samplevalue
        expects = self.samplevalue
        got = self.dic.get(self.samplekey)
        self.assertEqual(expects, got)
        expects = self.samplekey
        got = self.dic.get(self.samplevalue)
        self.assertEqual(expects, got)

    def test___setitem__samekey(self, ):
        self.dic[self.samplevalue] = self.samplevalue
        expects = self.samplevalue
        got = self.dic.get(self.samplevalue)
        self.assertEqual(expects, got)

    def test___delitem__(self, ):
        self.dic[self.samplekey] = self.samplevalue
        del self.dic[self.samplekey]
        expects = 0
        got = len(self.dic)
        self.assertEqual(expects, got)

    def test___delitem__samekey(self, ):
        self.dic[self.samplevalue] = self.samplevalue
        del self.dic[self.samplevalue]
        expects = 0
        got = len(self.dic)
        self.assertEqual(expects, got)

    def test_truelen(self, ):
        self.dic.update(self.sample2)
        expects = len(self.sample2) * 2
        got = self.dic.truelen()
        self.assertEqual(expects, got)

    def test_pop(self, ):
        self.dic.update(self.sample3)
        expects = self.sample3.copy()
        expects1 = expects.pop('hello')
        expects2 = expects.pop(1)
        got1, got2 = self.dic.pop('hello')
        got = self.dic
        self.assertEqual(expects, got)
        self.assertEqual(expects1, got1)
        self.assertEqual(expects2, got2)
        expects3 = expects.pop('nokey', 10)
        got3, got4 = self.dic.pop('nokey', 10)
        self.assertEqual(expects3, got3)
        self.assertEqual(expects3, got4)

    def test_popitem(self, ):
        self.dic.update(self.sample3)
        expects = self.sample3.copy()
        expects1, expects2 = expects.popitem()
        del expects[expects2]
        got1, got2 = self.dic.popitem()
        got = self.dic
        self.assertEqual(expects, got)
        self.assertEqual(expects1, got1)
        self.assertEqual(expects2, got2)

    def test___len__(self, ):
        self.dic.update(self.sample2)
        expects = len(self.sample2)
        got = len(self.dic)
        self.assertEqual(expects, got)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        pass


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_twowaydict.py ends here
