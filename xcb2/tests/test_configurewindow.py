#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_configurewindow.py

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

from cStringIO import StringIO
from struct import pack
from array import array

import xcb, xcb.xproto
from xcb2.xproto import ConfigWindow
from xcb2 import VoidCookie
from xcb2.xproto import BadValue, BadLength
from xcb2.tests import simple_teswindow
from xcb2.xproto.ext import ConfigureWindow, ConfigureWindowChecked


# TODO: (Atami) [2014/05/29]
# BadMatch, BadValue, BadWindow


class TestConfigureWindowBinary(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.args1 = [(81788931, ConfigWindow.X, [100]),
            '\x00\x00\x00\x00\x03\x00\xe0\x04\x01\x00\x00\x00d\x00\x00\x00']
        cls.args2 = [(56623107, ConfigWindow.Y, [200]),
            '\x00\x00\x00\x00\x03\x00`\x03\x02\x00\x00\x00\xc8\x00\x00\x00']
        cls.args3 = [(75497475, ConfigWindow.Width | ConfigWindow.Height,
                       [400, 500]),
                     '\x00\x00\x00\x00\x03\x00\x80\x04\x0c\x00\x00\x00'
                      '\x90\x01\x00\x00\xf4\x01\x00\x00']
        cls.conn = xcb.connect()
        cls.protocol = ConfigureWindow(cls.conn)
        cls.protocol_check = ConfigureWindowChecked(cls.conn)

    def setUp(self):
        self.conn.flush()
        self.mocker.replay()

    def test_binary1(self):
        r"""Test ConfigureWindow binary1."""
        binary = self.protocol._getbinary(*self.args1[0])
        self.assertEqual(self.args1[1], binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._getbinary,
                                 str(self.args1[0])
                                 .replace('(', '').replace(')', ''),
                                 repr(self.args1[1]), repr(binary)))

    def test_binary2(self):
        r"""Test ConfigureWindow binary2."""
        binary2 = self.protocol._getbinary(*self.args2[0])
        self.assertEqual(self.args2[1], binary2,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._getbinary,
                                 str(self.args2[0])
                                 .replace('(', '').replace(')', ''),
                                 repr(self.args2[1]), repr(binary2)))
    def test_binary3(self):
        r"""Test ConfigureWindow binary3."""
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


class TestConfigureWindowRequest(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.window = simple_teswindow()
        cls.conn = xcb.connect()
        cls.args = (cls.window, ConfigWindow.X, [100] )
        cls.protocol = ConfigureWindow(cls.conn)
        cls.protocol_check = ConfigureWindowChecked(cls.conn)
        cls.cookie = VoidCookie

    def setUp(self):
        self.conn.flush()
        self.mocker.replay()

    def test_call(self, ):
        r"""Test ConfigureWindow.__call__() expect return VoidCookie."""
        self.assertIsInstance(self.protocol(*self.args), self.cookie,
                              msg='Failed: {0}({1}) not returned {2}'
                              .format(self.protocol.__class__.__name__,
                                      str(self.args)
                                      .replace('(', '').replace(')', ''),
                                      VoidCookie.__class__.__name__))

    def test_request(self, ):
        r"""Test ConfigureWindow.request() expect return VoidCookie."""
        buf = StringIO()
        buf.write(pack('=xx2xIH2x', self.args[0], self.args[1]))
        buf.write(str(buffer(array('I', self.args[2]))))
        self.assertIsInstance(self.protocol.request(buf.getvalue()),
                              self.cookie,
                              msg='Failed: {0}.request("{0}") not return {1}'
                              .format(self.protocol.__class__.__name__,
                                      self.args,
                                      self.cookie.__class__.__name__))

    def test_checkedrequest(self, ):
        r"""Test ConfigureWindow.request() expect return VoidCookie."""
        buf = StringIO()
        buf.write(pack('=xx2xIH2x', self.args[0], self.args[1]))
        buf.write(str(buffer(array('I', self.args[2]))))
        self.assertIsInstance(
            self.protocol_check.request(buf.getvalue()), self.cookie,
            msg='Failed: {0}.request("{0}") not return {1}'
            .format(self.protocol_check.__class__.__name__,
            self.args, self.cookie.__class__.__name__))

    def tearDown(self):
        self.conn.flush()

    @classmethod
    def tearDownClass(cls, ):
        cls.conn.core.DestroyWindow(cls.window)
        cls.conn.flush()
        cls.conn.disconnect()


class TestConfigureWindowChecked(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.window = simple_teswindow()
        cls.args = (cls.window, ConfigWindow.X, [100])
        cls.args2 = (cls.window, ConfigWindow.X | ConfigWindow.Y, [0, 0])
        cls.args3 = (cls.window,
                      ConfigWindow.X | ConfigWindow.Y |
                      ConfigWindow.Width | ConfigWindow.Height,
                      [0, 0, 100, 100])
        cls.conn = xcb.connect()
        cls.protocol = ConfigureWindow(cls.conn)
        cls.protocol_check = ConfigureWindowChecked(cls.conn)

    def setUp(self):
        self.conn.flush()
        self.mocker.replay()

    def test_check_nonraise(self):
        r"""Test ConfigureWindowChecked() 1 nonraise."""
        cookie = self.protocol_check(*self.args)
        self.assertIsNone(cookie.check(),
                          msg='Failed: {}({}).check()'
                          .format(self.protocol_check.__class__.__name__,
                                  str(self.args)
                                  .replace('(', '').replace(')', '')))

    def test_check_nonraise2(self):
        r"""Test ConfigureWindowChecked() 2 nonraise."""
        cookie = self.protocol_check(*self.args2)
        self.assertIsNone(cookie.check(),
                          msg='Failed: {}({}).check()'
                          .format(self.protocol_check.__class__.__name__,
                                  str(self.args2)
                                  .replace('(', '').replace(')', '')))

    def test_check_nonraise3(self):
        r"""Test ConfigureWindowChecked() 3 nonraise."""
        cookie = self.protocol_check(*self.args3)
        self.assertIsNone(cookie.check(),
                          msg='Failed: {}({}).check()'
                          .format(self.protocol_check.__class__.__name__,
                                  str(self.args3)
                                  .replace('(', '').replace(')', '')))

    def test_checkraise_BadValue(self, ):
        r"""Test ConfigureWindowChecked() checkraise_BadValue."""
        with self.assertRaises(BadValue):
            cookie = self.protocol_check(self.window, 1 << 7, [100])
            cookie.check()

    def test_checkraise_BadLength(self, ):
        r"""Test ConfigureWindowChecked() checkraise_BadLength."""
        with self.assertRaises(BadLength):
            cookie = self.protocol_check(self.window, ConfigWindow.X,
                                         [100, 200])
            cookie.check()

    def tearDown(self):
        self.conn.flush()

    @classmethod
    def tearDownClass(cls, ):
        cls.conn.core.DestroyWindow(cls.window)
        cls.conn.flush()
        cls.conn.disconnect()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_configurewindow.py ends here
