#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: test_authuserorder.py 227 2014-09-13 08:15:46Z t1 $
# $Revision: 227 $
# $Date: 2014-09-13 17:15:46 +0900 (Sat, 13 Sep 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-09-13 17:15:46 +0900 (Sat, 13 Sep 2014) $

r"""Name: test_authuserorder.py

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
from .. import order

USER = 'dummy'


class TestAuthUserOrder(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.order = order.AuthUserOrder(USER)
        self.mocker.replay()

    def test_get_orderline(self, ):
        expect = USER + '\n'
        got = self.order.get_orderline()
        self.assertEqual(expect, got,
                         msg='Failed: expect: \{}, got: \{}'.format(expect, got))

    def test_receive(self, ):
        got = self.order.receive('')
        self.assertIsInstance(got, order.AuthUserReceiver)

    def test_set_user(self, ):
        newuser = 'newuser'
        self.order.set_user(newuser)
        self.assertEqual(newuser, self.order._user)

    def test_get_user(self, ):
        got = self.order.get_user()
        self.assertEqual(USER, got)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        pass


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_authuserorder.py ends here
