#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_wmclass.py

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
from time import sleep
from mocker import *

import xcb2
from xcb2.tests import simple_teswindow, NAME, WMCLASS as wmclass
from xcb2.xobj.window.wm_class import WMCLASS


class TestWMCLASS(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.conn = xcb2.connect()
        cls.window = simple_teswindow()

    def setUp(self):
        self.conn.flush()
        self.mocker.replay()

    # def test_match_client_list(self):
    #     r"""
    #     """
    #     wm = WMCLASS(self.conn, *wmclass.split('\x00')[0:2])
    #     got = wm.match_client_list()
    #     self.assertIn(self.window, got,
    #                   msg='Failed:'
    #                   ' WMCLASS.match_client_list expect {}, got: {}'
    #                   .format(self.window, got))

    def test_contains(self, ):
        r"""Test WMCLASS.__contains__."""
        res_name = 'test'
        wm = WMCLASS(self.conn, res_name, 'Test')
        self.assertIn(res_name, wm,
                      msg='Failed: WMCLASS.__contains__ expect: {}, got: {}'
                      .format(res_name, wm))

    def test_contains2(self, ):
        r"""Test WMCLASS.__contains__ 2"""
        res_class = 'Test'
        wm = WMCLASS(self.conn, 'test', res_class)
        self.assertIn(res_class, wm,
                      msg='Failed: WMCLASS.__contains__ expect: {}, got: {}'
                      .format(res_class, wm))

    def test_contains3(self, ):
        r"""Test WMCLASS.__contains__ 3"""
        res_class = 'notin'
        wm = WMCLASS(self.conn, 'test', 'Test')
        self.assertNotIn(res_class, wm,
                      msg='Failed: WMCLASS.__contains__ expect: {}, got: {}'
                      .format(res_class, wm))

    def test_iter(self, ):
        r"""Test WMCLASS.__iter__"""
        wm = WMCLASS(self.conn, 'test', 'Test')
        lis = list(wm)
        self.assertEqual('test', lis[0],
                         msg='Failed: WMCLASS.__iter__ expect: \{}, got: \{}'
                         .format('test', lis[0]))
        self.assertEqual('Test', lis[1],
                         msg='Failed: WMCLASS.__iter__ expect: \{}, got: \{}'
                         .format('Test', lis[1]))

    def test_nonzero_True(self, ):
        r"""Test WMCLASS.__nonzero__"""
        wm = WMCLASS(self.conn, 'test', 'Test')
        self.assertTrue(wm)

    def test_nonzero_False(self, ):
        r"""Test WMCLASS.__nonzero__"""
        wm = WMCLASS(self.conn, '', '')
        self.assertFalse(wm)

    def test_repr(self, ):
        r"""Test WMCLASS.__repr__"""
        wm = WMCLASS(self.conn, 'test', 'Test')
        expect = 'WMCLASS(res_name="test", res_class="Test")'
        got = repr(wm)
        self.assertEqual(expect, got,
                         msg='Failed: WMCLASS.__repr__ expect: \{}, got: \{}'
                         .format(expect, got))

    def test_str(self, ):
        r"""Test WMCLASS.__str__"""
        wm = WMCLASS(self.conn, *wmclass.split('\x00')[0:2])
        expect = wmclass
        got = str(wm)
        self.assertEqual(expect, got,
                         msg='Failed: WMCLASS.__str__ expect: \{}, got: \{}'
                         .format(expect, got))

    def test_len(self, ):
        r"""Test WMCLASS.__len__"""
        wm = WMCLASS(self.conn, *wmclass.split('\x00')[0:2])
        expect = 20
        got = len(wm)
        self.assertEqual(expect, got)

    def tearDown(self):
        self.conn.flush()

    @classmethod
    def tearDownClass(cls, ):
        cls.conn.core.DestroyWindow(cls.window)
        cls.conn.flush()
        cls.conn.disconnect()


# class TestWMCLASS2(MockerTestCase):
#     def setUp(self):
#         self.conn = xcb2.connect()
#         self.window = simple_teswindow()
#         self.mocker.replay()

#     def test_change(self, ):
#         r"""change."""
#         sleep(1)
#         newname, newclass = 'newname', 'newclass'
#         wm = WMCLASS(self.conn, newname, newclass)
#         wm.change(self.window)
#         self.conn.flush()
#         win = self.conn.get_windowtype(self.window)
#         self.assertEqual(newname, win.wmclass.res_name,
#                          msg='Failed: WMCLASS.change expect: \{}, got: \{}'
#                          .format(newname, win.wmclass.res_name))
#         self.assertEqual(newclass, win.wmclass.res_class,
#                          msg='Failed: WMCLASS.change expect: \{}, got: \{}'
#                          .format(newname, win.wmclass.res_class))

#     def tearDown(self):
#         self.conn.core.DestroyWindow(self.window)
#         self.conn.flush()


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_wmclass.py ends here
