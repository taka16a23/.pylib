#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_period.py

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
import datetime
from holiday.period import Period


class TestPeriod(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.start = datetime.date(2000, 1, 1)
        cls.end = datetime.date(2001, 1, 1)

    def setUp(self):
        self.period = Period(self.start, self.end)
        self.mocker.replay()

    def test_is_within(self, ):
        self.assertTrue(self.period.is_within(datetime.date(2000, 2, 1)))
        self.assertFalse(self.period.is_within(datetime.date(1999, 1, 1)))
        self.assertFalse(self.period.is_within(datetime.date(2002, 1, 1)))

    def test_get_start(self, ):
        self.assertEqual(self.start, self.period.get_start())

    def test_set_start(self, ):
        expects = datetime.date(1999, 1, 1)
        self.period.set_start(expects)
        self.assertEqual(expects, self.period.get_start())

    def test_get_end(self, ):
        self.assertEqual(self.end, self.period.get_end())

    def test_set_end(self, ):
        expects = datetime.date(2002, 1, 1)
        self.period.set_end(expects)
        self.assertEqual(expects, self.period.get_end())

    def test_init(self, ):
        period = Period(self.end, self.start)
        self.assertEqual(self.start, period.get_start())
        self.assertEqual(self.end, period.get_end())

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        pass


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_period.py ends here
