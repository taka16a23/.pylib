#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_keypress.py

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
import xcb2
from xcb2 import VoidCookie
from xcb2.xproto import EventMask
from xcb2.xproto.ext import SendEvent, SendEventChecked


class TestKeyPressBinary(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.args1 = [(False, 44040214,
                       10, 0, 0, 482, 44040214, 0, 0, 0, 0, 0, 0, 1),
                      '\x00\x00\x00\x00\x16\x00\xa0\x02\x01\x00\x00\x00\x02'
                      '\n\x00\x00\x00\x00\x00\x00\xe2\x01\x00\x00\x16\x00'
                      '\xa0\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                      '\x00\x00\x00\x01\x00']
        cls.conn = xcb2.connect()
        cls.protocol = SendEvent(cls.conn)
        cls.protocol_check = SendEventChecked(cls.conn)

    def setUp(self):
        self.conn.flush()
        self.mocker.replay()

    def test_binary1(self):
        r"""Test SendEvent.KeyPress binary1."""
        binary = self.protocol.KeyPress._getbinary(*self.args1[0])
        self.assertEqual(self.args1[1], binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._getbinary,
                                 str(self.args1[0])
                                 .replace('(', '').replace(')', ''),
                                 repr(self.args1[1]), repr(binary)))

    def tearDown(self):
        self.conn.flush()

    @classmethod
    def tearDownClass(cls, ):
        cls.conn.flush()
        cls.conn.disconnect()


class TestSendEventRequest(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.argsbin = [(False, 44040214,
                       10, 0, 0, 482, 44040214, 0, 0, 0, 0, 0, 0, 1),
                      '\x00\x00\x00\x00\x16\x00\xa0\x02\x01\x00\x00\x00\x02'
                      '\n\x00\x00\x00\x00\x00\x00\xe2\x01\x00\x00\x16\x00'
                      '\xa0\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                      '\x00\x00\x00\x01\x00']
        cls.conn = xcb2.connect()
        cls.protocol = SendEvent(cls.conn)
        cls.protocol_check = SendEventChecked(cls.conn)
        cls.cookie = VoidCookie

    def setUp(self):
        self.conn.flush()
        self.mocker.replay()

    def test_call(self):
        r"""Test SendEvent.KeyPress.__call__() expect return VoidCookie."""
        cookie = self.protocol.KeyPress(*self.argsbin[0])
        self.assertIsInstance(cookie, VoidCookie,
                              msg='Failed: {0}({1}) not returned'
                              ' VoidCookie\ngot: {2}'
                              .format(self.protocol.KeyPress.__class__.__name__,
                                      str(self.argsbin[0])
                                      .replace('(', '').replace(')', ''),
                                      cookie))

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
# test_keypress.py ends here