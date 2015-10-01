#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_grabkey.py

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
from xcb2.xproto.ext import GrabKey, GrabKeyChecked, UngrabKeyboard


class TestGrabKeyBinary(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.args1 = [(False, 99999999, 0, 10, 1, 1),
            '\x00\x00\x00\x00\xff\xe0\xf5\x05\x00\x00\n\x01\x01\x00\x00\x00']
        cls.args2 = [(True, 99999999, 0, 11, 1, 1),
            '\x00\x01\x00\x00\xff\xe0\xf5\x05\x00\x00\x0b\x01\x01\x00\x00\x00']
        cls.args3 = [(False, 99999999, 0, 12, 1, 1),
            '\x00\x00\x00\x00\xff\xe0\xf5\x05\x00\x00\x0c\x01\x01\x00\x00\x00']
        cls.conn = xcb.connect()
        cls.protocol = GrabKey(cls.conn)
        cls.protocol_check = GrabKeyChecked(cls.conn)

    def setUp(self):
        self.conn.flush()
        self.mocker.replay()

    def test_binary1(self):
        r"""Test GrabKey binary1."""
        binary = self.protocol._getbinary(*self.args1[0])
        self.assertEqual(self.args1[1], binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._getbinary,
                                 str(self.args1[0])
                                 .replace('(', '').replace(')', ''),
                                 repr(self.args1[1]), repr(binary)))

    def test_binary2(self):
        r"""Test GrabKey binary2."""
        binary2 = self.protocol._getbinary(*self.args2[0])
        self.assertEqual(self.args2[1], binary2,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._getbinary,
                                 str(self.args2[0])
                                 .replace('(', '').replace(')', ''),
                                 repr(self.args2[1]), repr(binary2)))
    def test_binary3(self):
        r"""Test GrabKey binary3."""
        binary3 = self.protocol._getbinary(*self.args3[0])
        self.assertEqual(self.args3[1], binary3,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._getbinary,
                                 str(self.args3[0])
                                 .replace('(', '').replace(')', ''),
                                 repr(self.args3[1]), repr(binary3)))

    def test_get_async_binary(self, ):
        r"""Test GrabKey._get_async_binary."""
        binary = self.protocol._get_async_binary(False, 99999999, 0, 10)
        self.assertEqual(self.args1[1], binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(self.protocol, self.protocol._getbinary,
                                 repr(self.args1[1]), repr(binary)))

    def tearDown(self):
        self.conn.core.UngrabKeyboard(0)
        self.conn.flush()

    @classmethod
    def tearDownClass(cls, ):
        cls.conn.core.UngrabKeyboard(0)
        cls.conn.flush()
        cls.conn.disconnect()


class TestGrabKeyRequest(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.argsbin = [(False, 99999999, 0, 10, 1, 1),
            '\x00\x00\x00\x00\xff\xe0\xf5\x05\x00\x00\n\x01\x01\x00\x00\x00']
        cls.conn = xcb.connect()
        cls.protocol = GrabKey(cls.conn)
        cls.protocol_check = GrabKeyChecked(cls.conn)
        cls.cookie = VoidCookie

    def setUp(self):
        self.conn.flush()
        self.mocker.replay()

    def test_call(self):
        r"""Test GrabKey.__call__() expect return VoidCookie."""
        cookie = self.protocol(*self.argsbin[0])
        self.assertIsInstance(cookie, VoidCookie,
                              msg='Failed: {0}({1}) not returned'
                              ' VoidCookie\ngot: {2}'
                              .format(self.protocol.__class__.__name__,
                                      str(self.argsbin[0])
                                      .replace('(', '').replace(')', ''),
                                      cookie))

    def test_async(self):
        r"""Test GrabKey.async() expect return VoidCookie."""
        cookie = self.protocol.async(*self.argsbin[0][0:4])
        self.assertIsInstance(cookie, VoidCookie,
                              msg='Failed: {0}({1}) not returned'
                              ' VoidCookie\ngot: {2}'
                              .format(self.protocol.__class__.__name__,
                                      str(self.argsbin[0])
                                      .replace('(', '').replace(')', ''),
                                      cookie))

    def test_request(self, ):
        r"""Test GrabKey.request() expect return VoidCookie."""
        cookie = self.protocol.request(self.argsbin[1])
        self.assertIsInstance(cookie, self.cookie,
                              msg='Failed: {0}.request("{1}") not return'
                              ' VoidCookie\ngot: {2}'
                              .format(self.protocol.__class__.__name__,
                                      self.argsbin[1], cookie))

    def test_checkedrequest(self, ):
        r"""Test GrabKey.request() expect return VoidCookie."""
        cookie = self.protocol_check.request(self.argsbin[1])
        self.assertIsInstance(cookie, self.cookie,
                              msg='Failed: {0}.request("{1}") not return'
                              ' VoidCookie\ngot: {2}'
                              .format(self.protocol_check.__class__.__name__,
                                      self.argsbin[1], cookie))

    def tearDown(self):
        self.conn.core.UngrabKeyboard(0)
        self.conn.flush()

    @classmethod
    def tearDownClass(cls, ):
        cls.conn.core.UngrabKeyboard(0)
        cls.conn.flush()
        cls.conn.disconnect()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_grabkey.py ends here
