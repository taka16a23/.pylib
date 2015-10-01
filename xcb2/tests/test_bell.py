#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_bell.py

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

import xcb, xcb.xproto
from xcb2 import VoidCookie
from xcb2.xproto import BadValue
from xcb2.xproto.ext import Bell, BellChecked


class TestBellBinary(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.conn = xcb.connect()
        cls.args1 = [(30, ), '\x00\x1e\x00\x00']
        cls.args2 = [(0, ), '\x00\x00\x00\x00']
        cls.args3 = [(-50, ), '\x00\xce\x00\x00']
        cls.protocol = Bell(cls.conn)
        cls.protocol_check = BellChecked(cls.conn)

    def setUp(self):
        self.conn.flush()
        self.mocker.replay()

    def test_binary1(self):
        r"""Test Bell binary1."""
        binary = self.protocol._getbinary(*self.args1[0])
        self.assertEqual(self.args1[1], binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._getbinary,
                                 str(self.args1[0])
                                 .replace('(', '').replace(')', ''),
                                 repr(self.args1[1]), repr(binary)))

    def test_binary2(self):
        r"""Test Bell binary2."""
        binary2 = self.protocol._getbinary(*self.args2[0])
        self.assertEqual(self.args2[1], binary2,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._getbinary,
                                 str(self.args2[0])
                                 .replace('(', '').replace(')', ''),
                                 repr(self.args2[1]), repr(binary2)))
    def test_binary3(self):
        r"""Test Bell binary3."""
        binary3 = self.protocol._getbinary(*self.args3[0])
        self.assertEqual(self.args3[1], binary3,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._getbinary,
                                 str(self.args3[0])
                                 .replace('(', '').replace(')', ''),
                                 repr(self.args3[1]), repr(binary3)))

    def tearDown(self):
        self.conn.flush()

    @classmethod
    def tearDownClass(cls, ):
        cls.conn.flush()
        cls.conn.disconnect()


class TestBellRequest(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.argsbin = [(30, ), '\x00\x1e\x00\x00']
        cls.conn = xcb.connect()
        cls.protocol = Bell(cls.conn)
        cls.protocol_check = BellChecked(cls.conn)
        cls.cookie = VoidCookie

    def setUp(self):
        self.conn.flush()
        self.mocker.replay()

    def test_call(self, ):
        r"""Test Bell.__call__() expect return VoidCookie."""
        self.assertIsInstance(self.protocol(*self.argsbin[0]), self.cookie,
                              msg='Failed: {0}({1}) not returned {2}'
                              .format(self.protocol.__class__.__name__,
                                      str(self.argsbin[0])
                                      .replace('(', '').replace(')', ''),
                                      self.cookie.__class__.__name__))

    def test_request(self, ):
        r"""Test Bell.request() expect return VoidCookie."""
        self.assertIsInstance(self.protocol.request(self.argsbin[1]),
                              self.cookie,
                              msg='Failed: {0}.request("{1}") not return {2}'
                              .format(self.protocol.__class__.__name__,
                                      self.argsbin[1],
                                      self.cookie.__class__.__name__))

    def test_checkedrequest(self, ):
        r"""Test BellChecked.request() expect return VoidCookie."""
        self.assertIsInstance(
            self.protocol_check.request(self.argsbin[1]), self.cookie,
            msg='Failed: {0}.request("{1}") not return {2}'
            .format(self.protocol_check.__class__.__name__,
            self.argsbin[1], self.cookie.__class__.__name__))

    def tearDown(self):
        self.conn.flush()

    @classmethod
    def tearDownClass(cls, ):
        cls.conn.flush()
        cls.conn.disconnect()


class TestBellChecked(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.conn = xcb.connect()
        cls.protocol_check = BellChecked(cls.conn)

    def setUp(self):
        self.conn.flush()
        self.mocker.replay()

    def test_check_nonraise(self):
        r"""Test BellChecked() nonraise."""
        cookie = self.protocol_check(100)
        self.assertIsNone(cookie.check(), msg='Failed: BellChecked(100).check()')

    def test_checkraise_BadValue(self, ):
        r"""Test BellChecked() checkraise_BadValue."""
        with self.assertRaises(BadValue):
            cookie = self.protocol_check(-110)
            cookie.check()

    def test_value_range(self, ):
        r"""Test BellChecked() value range."""
        with self.assertRaises(BadValue):
            cookie = self.protocol_check(-101)
            cookie.check()
        with self.assertRaises(BadValue):
            cookie = self.protocol_check(101)
            cookie.check()
        self.assertIsNone(self.protocol_check(100).check(),
                          msg='Failed: value 100.')
        self.assertIsNone(self.protocol_check(-100).check(),
                          msg='Failed: value -100.')

    def tearDown(self):
        self.conn.flush()

    @classmethod
    def tearDownClass(cls, ):
        cls.conn.flush()
        cls.conn.disconnect()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_bell.py ends here
