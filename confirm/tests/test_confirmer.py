#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: test_confirmer.py 230 2014-09-13 08:17:36Z t1 $
# $Revision: 230 $
# $Date: 2014-09-13 17:17:36 +0900 (Sat, 13 Sep 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-09-13 17:17:36 +0900 (Sat, 13 Sep 2014) $

r"""Name: test_confirmer.py

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
from confirm import confirmer


class DummyTrueConfirm(object):
    def confirm(self, ):
        return True

class DummyFalseConfirm(object):
    def confirm(self, ):
        return False


class TestConfirmer(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.confirmer = confirmer.Confirmer(DummyTrueConfirm())
        self.mocker.replay()

    def test_confirm(self, ):
        self.assertTrue(self.confirmer.confirm())

    def test_get_confirmer(self, ):
        got = self.confirmer.get_confirmer()
        self.assertIsInstance(got, DummyTrueConfirm)

    def test_set_confirmer(self, ):
        self.confirmer.set_confirmer(DummyFalseConfirm())
        got = self.confirmer.get_confirmer()
        self.assertIsInstance(got, DummyFalseConfirm)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        pass


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_confirmer.py ends here
