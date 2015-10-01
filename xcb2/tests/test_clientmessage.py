#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_clientmessage.py

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

from struct import pack
import xcb2
from xcb2 import VoidCookie
from xcb2.xproto.ext import SendEvent, SendEventChecked
from xcb2.xproto.ext.sendevent.clientmessage import *
from xcb2.tests import simple_teswindow


class TestClientMessageBinary(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.window = simple_teswindow()
        winbin = pack('I', cls.window)
        cls.args1 = [(False, cls.window, 32, 0, cls.window, 296,
                       '\x01\x00\x00\x00)\x01\x00\x00\x00\x00\x00\x00'
                       '\x00\x00\x00\x00\x00\x00\x00\x00'),
                      '\x00\x00\x00\x00' + winbin + '\xff\xff\xff\x00! \x00'
                      '\x00' + winbin + '(\x01\x00\x00\x01\x00\x00\x00)\x01'
                      '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00']
        cls.conn = xcb2.connect()
        cls.protocol = SendEvent(cls.conn)
        cls.protocol_check = SendEventChecked(cls.conn)

    def setUp(self):
        self.conn.flush()
        self.mocker.replay()

    def test_binary1(self):
        r"""Test SendEvent.ClientMessage binary1."""
        binary = self.protocol.ClientMessage._getbinary(*self.args1[0])
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
        cls.conn.core.DestroyWindow(cls.window)
        cls.conn.flush()
        cls.conn.disconnect()


class TestClientMessageRequest(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.window = simple_teswindow()
        winbin = pack('I', cls.window)
        cls.argsbin = [(False, cls.window, 32, 0, cls.window, 296,
                       '\x01\x00\x00\x00)\x01\x00\x00\x00\x00\x00\x00'
                       '\x00\x00\x00\x00\x00\x00\x00\x00'),
                      '\x00\x00\x00\x00' + winbin + '\xff\xff\xff\x00! \x00'
                      '\x00' + winbin + '(\x01\x00\x00\x01\x00\x00\x00)\x01'
                      '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00']
        cls.conn = xcb2.connect()
        cls.protocol = SendEvent(cls.conn)
        cls.protocol_check = SendEventChecked(cls.conn)
        cls.cookie = VoidCookie

    def setUp(self):
        self.conn.flush()
        self.mocker.replay()

    def test_call(self):
        r"""Test SendEvent.ClientMessage.__call__() expect return VoidCookie."""
        cookie = self.protocol.ClientMessage(*self.argsbin[0])
        self.assertIsInstance(cookie, VoidCookie,
                              msg='Failed: {0}({1}) not returned'
                              ' VoidCookie\ngot: {2}'
                              .format(self.protocol.ClientMessage
                                      .__class__.__name__,
                                      str(self.argsbin[0])
                                      .replace('(', '').replace(')', ''),
                                      cookie))

    def tearDown(self):
        self.conn.flush()

    @classmethod
    def tearDownClass(cls, ):
        cls.conn.core.DestroyWindow(cls.window)
        cls.conn.flush()
        cls.conn.disconnect()


class TestAbove(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.window = simple_teswindow()
        cls.conn = xcb2.connect()
        cls.sendevent = SendEvent(cls.conn)
        cls.protocol = Above(cls.sendevent)

    def setUp(self):
        self.conn.flush()
        self.mocker.replay()

    def test_setbinary(self):
        r"""Test Above._get_setbinary"""
        winbin = pack('I', self.window)
        expect = ('\x00\x00\x00\x00' + winbin + '\xff\xff\xff\x00! \x00'
                  '\x00' + winbin + '(\x01\x00\x00\x01\x00\x00\x00)\x01'
                  '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = self.protocol._get_setbinary(self.window, False, 0)
        self.assertEqual(expect, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._get_setbinary,
                                 expect, repr(expect), repr(binary)))

    def test_unsetbinary(self, ):
        r"""Test Above._get_unsetbinary"""
        winbin = pack('I', self.window)
        expect = ('\x00\x00\x00\x00' + winbin + '\xff\xff\xff\x00! \x00\x00'
                  + winbin + '(\x01\x00\x00\x00\x00\x00\x00)\x01\x00\x00'
                  '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = self.protocol._get_unsetbinary(self.window, False, 0)
        self.assertEqual(expect, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._get_unsetbinary,
                                 expect, repr(expect), repr(binary)))

    def test_togglebinary(self, ):
        r"""Test Above._get_togglebinary"""
        winbin = pack('I', self.window)
        expect = ('\x00\x00\x00\x00' + winbin + '\xff\xff\xff\x00! \x00\x00'
                  + winbin + '(\x01\x00\x00\x02\x00\x00\x00)\x01\x00\x00'
                  '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = self.protocol._get_togglebinary(self.window, False, 0)
        self.assertEqual(expect, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._get_togglebinary,
                                 expect, repr(expect), repr(binary)))

    def test_set(self, ):
        r"""Test Above.set."""
        cookie = self.protocol.set(self.window, False, 0)
        self.assertIsInstance(cookie, VoidCookie,
                              msg='Failed: {0}() not returned'
                              ' VoidCookie\ngot: {1}'
                              .format(self.protocol.set.__name__, cookie))

    def test_unset(self, ):
        r"""Test Above.unset."""
        cookie = self.protocol.unset(self.window, False, 0)
        self.assertIsInstance(cookie, VoidCookie,
                              msg='Failed: {0}() not returned'
                              ' VoidCookie\ngot: {1}'
                              .format(self.protocol.unset.__name__, cookie))

    def test_toggle(self, ):
        r"""Test Above.toggle."""
        cookie = self.protocol.toggle(self.window, False, 0)
        self.assertIsInstance(cookie, VoidCookie,
                              msg='Failed: {0}() not returned'
                              ' VoidCookie\ngot: {1}'
                              .format(self.protocol.toggle.__name__, cookie))

    def tearDown(self):
        self.conn.flush()

    @classmethod
    def tearDownClass(cls, ):
        cls.conn.core.DestroyWindow(cls.window)
        cls.conn.flush()
        cls.conn.disconnect()


class TestBelow(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.window = simple_teswindow()
        cls.conn = xcb2.connect()
        cls.sendevent = SendEvent(cls.conn)
        cls.protocol = Below(cls.sendevent)

    def setUp(self):
        self.conn.flush()
        self.mocker.replay()

    def test_setbinary(self):
        r"""Test Below._get_setbinary"""
        winbin = pack('I', self.window)
        expect = ('\x00\x00\x00\x00' + winbin + '\xff\xff\xff\x00! \x00\x00'
                  + winbin + '(\x01\x00\x00\x01\x00\x00\x00*\x01\x00\x00'
                  '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = self.protocol._get_setbinary(self.window, False, 0)
        self.assertEqual(expect, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._get_setbinary,
                                 expect, repr(expect), repr(binary)))

    def test_unsetbinary(self, ):
        r"""Test Below._get_unsetbinary"""
        winbin = pack('I', self.window)
        expect = ('\x00\x00\x00\x00' + winbin + '\xff\xff\xff\x00! \x00\x00'
                  + winbin + '(\x01\x00\x00\x00\x00\x00\x00*\x01\x00\x00'
                  '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = self.protocol._get_unsetbinary(self.window, False, 0)
        self.assertEqual(expect, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._get_unsetbinary,
                                 expect, repr(expect), repr(binary)))

    def test_togglebinary(self, ):
        r"""Test Below._get_togglebinary"""
        winbin = pack('I', self.window)
        expect = ('\x00\x00\x00\x00' + winbin + '\xff\xff\xff\x00! \x00\x00'
                  + winbin + '(\x01\x00\x00\x02\x00\x00\x00*\x01\x00\x00'
                  '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = self.protocol._get_togglebinary(self.window, False, 0)
        self.assertEqual(expect, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._get_togglebinary,
                                 expect, repr(expect), repr(binary)))

    def test_set(self, ):
        r"""Test Below.set."""
        cookie = self.protocol.set(self.window, False, 0)
        self.assertIsInstance(cookie, VoidCookie,
                              msg='Failed: {0}() not returned'
                              ' VoidCookie\ngot: {1}'
                              .format(self.protocol.set.__name__, cookie))

    def test_unset(self, ):
        r"""Test Below.unset."""
        cookie = self.protocol.unset(self.window, False, 0)
        self.assertIsInstance(cookie, VoidCookie,
                              msg='Failed: {0}() not returned'
                              ' VoidCookie\ngot: {1}'
                              .format(self.protocol.unset.__name__, cookie))

    def test_toggle(self, ):
        r"""Test Below.toggle."""
        cookie = self.protocol.toggle(self.window, False, 0)
        self.assertIsInstance(cookie, VoidCookie,
                              msg='Failed: {0}() not returned'
                              ' VoidCookie\ngot: {1}'
                              .format(self.protocol.toggle.__name__, cookie))

    def tearDown(self):
        self.conn.flush()

    @classmethod
    def tearDownClass(cls, ):
        cls.conn.core.DestroyWindow(cls.window)
        cls.conn.flush()
        cls.conn.disconnect()


class TestShade(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.window = simple_teswindow()
        cls.conn = xcb2.connect()
        cls.sendevent = SendEvent(cls.conn)
        cls.protocol = Shade(cls.sendevent)

    def setUp(self):
        self.conn.flush()
        self.mocker.replay()

    def test_setbinary(self):
        r"""Test Shade._get_setbinary"""
        winbin = pack('I', self.window)
        expect = ('\x00\x00\x00\x00' + winbin + '\xff\xff\xff\x00! \x00\x00'
                  + winbin + '(\x01\x00\x00\x01\x00\x00\x00\x81\x01\x00'
                  '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = self.protocol._get_setbinary(self.window, False, 0)
        self.assertEqual(expect, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._get_setbinary,
                                 expect, repr(expect), repr(binary)))

    def test_unsetbinary(self, ):
        r"""Test Shade._get_unsetbinary"""
        winbin = pack('I', self.window)
        expect = ('\x00\x00\x00\x00' + winbin + '\xff\xff\xff\x00! \x00\x00'
                  + winbin + '(\x01\x00\x00\x00\x00\x00\x00\x81\x01\x00'
                  '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = self.protocol._get_unsetbinary(self.window, False, 0)
        self.assertEqual(expect, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._get_unsetbinary,
                                 expect, repr(expect), repr(binary)))

    def test_togglebinary(self, ):
        r"""Test Shade._get_togglebinary"""
        winbin = pack('I', self.window)
        expect = ('\x00\x00\x00\x00' + winbin + '\xff\xff\xff\x00! \x00\x00'
                  + winbin + '(\x01\x00\x00\x02\x00\x00\x00\x81\x01\x00'
                  '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = self.protocol._get_togglebinary(self.window, False, 0)
        self.assertEqual(expect, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._get_togglebinary,
                                 expect, repr(expect), repr(binary)))

    def test_set(self, ):
        r"""Test Shade.set."""
        cookie = self.protocol.set(self.window, False, 0)
        self.assertIsInstance(cookie, VoidCookie,
                              msg='Failed: {0}() not returned'
                              ' VoidCookie\ngot: {1}'
                              .format(self.protocol.set.__name__, cookie))

    def test_unset(self, ):
        r"""Test Shade.unset."""
        cookie = self.protocol.unset(self.window, False, 0)
        self.assertIsInstance(cookie, VoidCookie,
                              msg='Failed: {0}() not returned'
                              ' VoidCookie\ngot: {1}'
                              .format(self.protocol.unset.__name__, cookie))

    def test_toggle(self, ):
        r"""Test Shade.toggle."""
        cookie = self.protocol.toggle(self.window, False, 0)
        self.assertIsInstance(cookie, VoidCookie,
                              msg='Failed: {0}() not returned'
                              ' VoidCookie\ngot: {1}'
                              .format(self.protocol.toggle.__name__, cookie))

    def tearDown(self):
        self.conn.flush()

    @classmethod
    def tearDownClass(cls, ):
        cls.conn.core.DestroyWindow(cls.window)
        cls.conn.flush()
        cls.conn.disconnect()


class TestFullScreen(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.window = simple_teswindow()
        cls.conn = xcb2.connect()
        cls.sendevent = SendEvent(cls.conn)
        cls.protocol = FullScreen(cls.sendevent)

    def setUp(self):
        self.conn.flush()
        self.mocker.replay()

    def test_setbinary(self):
        r"""Test FullScreen._get_setbinary"""
        winbin = pack('I', self.window)
        expect = ('\x00\x00\x00\x00' + winbin + '\xff\xff\xff\x00! \x00\x00'
                  + winbin + '(\x01\x00\x00\x01\x00\x00\x00+\x01\x00\x00'
                  '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = self.protocol._get_setbinary(self.window, False, 0)
        self.assertEqual(expect, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._get_setbinary,
                                 expect, repr(expect), repr(binary)))

    def test_unsetbinary(self, ):
        r"""Test FullScreen._get_unsetbinary"""
        winbin = pack('I', self.window)
        expect = ('\x00\x00\x00\x00' + winbin + '\xff\xff\xff\x00! \x00\x00'
                  + winbin + '(\x01\x00\x00\x00\x00\x00\x00+\x01\x00\x00'
                  '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = self.protocol._get_unsetbinary(self.window, False, 0)
        self.assertEqual(expect, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._get_unsetbinary,
                                 expect, repr(expect), repr(binary)))

    def test_togglebinary(self, ):
        r"""Test FullScreen._get_togglebinary"""
        winbin = pack('I', self.window)
        expect = ('\x00\x00\x00\x00' + winbin + '\xff\xff\xff\x00! \x00\x00'
                  + winbin + '(\x01\x00\x00\x02\x00\x00\x00+\x01\x00\x00'
                  '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = self.protocol._get_togglebinary(self.window, False, 0)
        self.assertEqual(expect, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._get_togglebinary,
                                 expect, repr(expect), repr(binary)))

    def test_set(self, ):
        r"""Test FullScreen.set."""
        cookie = self.protocol.set(self.window, False, 0)
        self.assertIsInstance(cookie, VoidCookie,
                              msg='Failed: {0}() not returned'
                              ' VoidCookie\ngot: {1}'
                              .format(self.protocol.set.__name__, cookie))

    def test_unset(self, ):
        r"""Test FullScreen.unset."""
        cookie = self.protocol.unset(self.window, False, 0)
        self.assertIsInstance(cookie, VoidCookie,
                              msg='Failed: {0}() not returned'
                              ' VoidCookie\ngot: {1}'
                              .format(self.protocol.unset.__name__, cookie))

    def test_toggle(self, ):
        r"""Test FullScreen.toggle."""
        cookie = self.protocol.toggle(self.window, False, 0)
        self.assertIsInstance(cookie, VoidCookie,
                              msg='Failed: {0}() not returned'
                              ' VoidCookie\ngot: {1}'
                              .format(self.protocol.toggle.__name__, cookie))

    def tearDown(self):
        self.conn.flush()

    @classmethod
    def tearDownClass(cls, ):
        cls.conn.core.DestroyWindow(cls.window)
        cls.conn.flush()
        cls.conn.disconnect()


class TestHidden(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.window = simple_teswindow()
        cls.conn = xcb2.connect()
        cls.sendevent = SendEvent(cls.conn)
        cls.protocol = Hidden(cls.sendevent)

    def setUp(self):
        self.conn.flush()
        self.mocker.replay()

    def test_setbinary(self):
        r"""Test Hidden._get_setbinary"""
        self.skipTest('not implemented')
        winbin = pack('I', self.window)
        expect = ()
        binary = self.protocol._get_setbinary(self.window, False, 0)
        self.assertEqual(expect, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._get_setbinary,
                                 expect, repr(expect), repr(binary)))

    def test_unsetbinary(self, ):
        r"""Test Hidden._get_unsetbinary"""
        self.skipTest('not implemented')
        winbin = pack('I', self.window)
        expect = ()
        binary = self.protocol._get_unsetbinary(self.window, False, 0)
        self.assertEqual(expect, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._get_unsetbinary,
                                 expect, repr(expect), repr(binary)))

    def test_togglebinary(self, ):
        r"""Test Hidden._get_togglebinary"""
        self.skipTest('not implemented')
        winbin = pack('I', self.window)
        expect = ()
        binary = self.protocol._get_togglebinary(self.window, False, 0)
        self.assertEqual(expect, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._get_togglebinary,
                                 expect, repr(expect), repr(binary)))

    def test_set(self, ):
        r"""Test Hidden.set."""
        self.skipTest('not implemented')
        cookie = self.protocol.set(self.window, False, 0)
        self.assertIsInstance(cookie, VoidCookie,
                              msg='Failed: {0}() not returned'
                              ' VoidCookie\ngot: {1}'
                              .format(self.protocol.set.__name__, cookie))

    def test_unset(self, ):
        r"""Test Hidden.unset."""
        self.skipTest('not implemented')
        cookie = self.protocol.unset(self.window, False, 0)
        self.assertIsInstance(cookie, VoidCookie,
                              msg='Failed: {0}() not returned'
                              ' VoidCookie\ngot: {1}'
                              .format(self.protocol.unset.__name__, cookie))

    def test_toggle(self, ):
        r"""Test Hidden.toggle."""
        self.skipTest('not implemented')
        cookie = self.protocol.toggle(self.window, False, 0)
        self.assertIsInstance(cookie, VoidCookie,
                              msg='Failed: {0}() not returned'
                              ' VoidCookie\ngot: {1}'
                              .format(self.protocol.toggle.__name__, cookie))

    def tearDown(self):
        self.conn.flush()

    @classmethod
    def tearDownClass(cls, ):
        cls.conn.core.DestroyWindow(cls.window)
        cls.conn.flush()
        cls.conn.disconnect()


class TestMinimize(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.window = simple_teswindow()
        cls.conn = xcb2.connect()
        cls.sendevent = SendEvent(cls.conn)
        cls.protocol = Minimize(cls.sendevent)

    def setUp(self):
        self.conn.flush()
        self.mocker.replay()

    def test_setbinary(self):
        r"""Test Minimize._get_setbinary"""
        self.skipTest('not implemented')
        winbin = pack('I', self.window)
        expect = ()
        binary = self.protocol._get_setbinary(self.window, False, 0)
        self.assertEqual(expect, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._get_setbinary,
                                 expect, repr(expect), repr(binary)))

    def test_unsetbinary(self, ):
        r"""Test Minimize._get_unsetbinary"""
        self.skipTest('not implemented')
        winbin = pack('I', self.window)
        expect = ()
        binary = self.protocol._get_unsetbinary(self.window, False, 0)
        self.assertEqual(expect, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._get_unsetbinary,
                                 expect, repr(expect), repr(binary)))

    def test_togglebinary(self, ):
        r"""Test Minimize._get_togglebinary"""
        self.skipTest('not implemented')
        expect = ()
        binary = self.protocol._get_togglebinary(self.window, False, 0)
        self.assertEqual(expect, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._get_togglebinary,
                                 expect, repr(expect), repr(binary)))

    def test_set(self, ):
        r"""Test Minimize.set."""
        self.skipTest('not implemented')
        cookie = self.protocol.set(self.window, False, 0)
        self.assertIsInstance(cookie, VoidCookie,
                              msg='Failed: {0}() not returned'
                              ' VoidCookie\ngot: {1}'
                              .format(self.protocol.set.__name__, cookie))

    def test_unset(self, ):
        r"""Test Minimize.unset."""
        self.skipTest('not implemented')
        cookie = self.protocol.unset(self.window, False, 0)
        self.assertIsInstance(cookie, VoidCookie,
                              msg='Failed: {0}() not returned'
                              ' VoidCookie\ngot: {1}'
                              .format(self.protocol.unset.__name__, cookie))

    def test_toggle(self, ):
        r"""Test Minimize.toggle."""
        self.skipTest('not implemented')
        cookie = self.protocol.toggle(self.window, False, 0)
        self.assertIsInstance(cookie, VoidCookie,
                              msg='Failed: {0}() not returned'
                              ' VoidCookie\ngot: {1}'
                              .format(self.protocol.toggle.__name__, cookie))

    def tearDown(self):
        self.conn.flush()

    @classmethod
    def tearDownClass(cls, ):
        cls.conn.core.DestroyWindow(cls.window)
        cls.conn.flush()
        cls.conn.disconnect()


class TestMaximize(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.window = simple_teswindow()
        cls.conn = xcb2.connect()
        cls.sendevent = SendEvent(cls.conn)
        cls.protocol = Maximize(cls.sendevent)

    def setUp(self):
        self.conn.flush()
        self.mocker.replay()

    def test_setbinary(self):
        r"""Test Maximize._get_setbinary"""
        winbin = pack('I', self.window)
        expect = ('\x00\x00\x00\x00' + winbin + '\xff\xff\xff\x00! \x00\x00'
                  + winbin + '(\x01\x00\x00\x01\x00\x00\x00-\x01\x00'
                  '\x00.\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = self.protocol._get_setbinary(self.window, False, 0)
        self.assertEqual(expect, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._get_setbinary,
                                 expect, repr(expect), repr(binary)))

    def test_unsetbinary(self, ):
        r"""Test Maximize._get_unsetbinary"""
        winbin = pack('I', self.window)
        expect = ('\x00\x00\x00\x00' + winbin + '\xff\xff\xff\x00! \x00\x00'
                  + winbin + '(\x01\x00\x00\x00\x00\x00\x00-\x01\x00'
                  '\x00.\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = self.protocol._get_unsetbinary(self.window, False, 0)
        self.assertEqual(expect, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._get_unsetbinary,
                                 expect, repr(expect), repr(binary)))

    def test_togglebinary(self, ):
        r"""Test Maximize._get_togglebinary"""
        winbin = pack('I', self.window)
        expect = ('\x00\x00\x00\x00' + winbin + '\xff\xff\xff\x00! \x00\x00'
                  + winbin + '(\x01\x00\x00\x02\x00\x00\x00-\x01\x00'
                  '\x00.\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = self.protocol._get_togglebinary(self.window, False, 0)
        self.assertEqual(expect, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._get_togglebinary,
                                 expect, repr(expect), repr(binary)))

    def test_set(self, ):
        r"""Test Maximize.set."""
        cookie = self.protocol.set(self.window, False, 0)
        self.assertIsInstance(cookie, VoidCookie,
                              msg='Failed: {0}() not returned'
                              ' VoidCookie\ngot: {1}'
                              .format(self.protocol.set.__name__, cookie))

    def test_unset(self, ):
        r"""Test Maximize.unset."""
        cookie = self.protocol.unset(self.window, False, 0)
        self.assertIsInstance(cookie, VoidCookie,
                              msg='Failed: {0}() not returned'
                              ' VoidCookie\ngot: {1}'
                              .format(self.protocol.unset.__name__, cookie))

    def test_toggle(self, ):
        r"""Test Maximize.toggle."""
        cookie = self.protocol.toggle(self.window, False, 0)
        self.assertIsInstance(cookie, VoidCookie,
                              msg='Failed: {0}() not returned'
                              ' VoidCookie\ngot: {1}'
                              .format(self.protocol.toggle.__name__, cookie))

    def tearDown(self):
        self.conn.flush()

    @classmethod
    def tearDownClass(cls, ):
        cls.conn.core.DestroyWindow(cls.window)
        cls.conn.flush()
        cls.conn.disconnect()


class TestDelete(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.window = simple_teswindow()
        cls.conn = xcb2.connect()
        cls.sendevent = SendEvent(cls.conn)
        cls.protocol = DeleteWindow(cls.sendevent)

    def setUp(self):
        self.conn.flush()
        self.mocker.replay()

    def test_setbinary(self):
        r"""Test DeleteWindow._getbinary"""
        winbin = pack('I', self.window)
        expect = ('\x00\x00\x00\x00' + winbin + '\xff\xff\xff\x00! \x00\x00'
                  + winbin + '\x1a\x01\x00\x00\x18\x01\x00\x00\x00\x00\x00'
                  '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = self.protocol._getbinary(self.window, 0, False, 0)
        self.assertEqual(expect, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._getbinary,
                                 expect, repr(expect), repr(binary)))

    def test_setbinary2(self):
        r"""Test DeleteWindow._getbinary 2"""
        winbin = pack('I', self.window)
        expect = ('\x00\x00\x00\x00' + winbin + '\xff\xff\xff\x00! \x00\x00'
                  + winbin + '\x1a\x01\x00\x00\x18\x01\x00\x00\x00\x00\x00'
                  '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = self.protocol._getbinary(self.window, None, False, 0)
        self.assertEqual(expect, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._getbinary,
                                 expect, repr(expect), repr(binary)))

    def test_cookie(self, ):
        r"""Test DeleteWindow."""
        cookie = self.protocol(self.window, 0, False, 0)
        self.assertIsInstance(cookie, VoidCookie,
                              msg='Failed: {0}() not returned'
                              ' VoidCookie\ngot: {1}'
                              .format(self.protocol.__class__.__name__, cookie))

    def test_cookie2(self, ):
        r"""Test DeleteWindow."""
        cookie = self.protocol(self.window)
        self.assertIsInstance(cookie, VoidCookie,
                              msg='Failed: {0}() not returned'
                              ' VoidCookie\ngot: {1}'
                              .format(self.protocol.__class__.__name__, cookie))

    def tearDown(self):
        self.conn.flush()

    @classmethod
    def tearDownClass(cls, ):
        cls.conn.core.DestroyWindow(cls.window)
        cls.conn.flush()
        cls.conn.disconnect()


class TestClose(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.window = simple_teswindow()
        cls.conn = xcb2.connect()
        cls.sendevent = SendEvent(cls.conn)
        cls.protocol = CloseWindow(cls.sendevent)

    def setUp(self):
        self.conn.flush()
        self.mocker.replay()

    def test_setbinary(self):
        r"""Test CloseWindow._getbinary"""
        winbin = pack('I', self.window)
        expect = ('\x00\x00\x00\x00' + winbin + '\xff\xff\xff\x00! \x00\x00'
                  + winbin + 'a\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                  '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = self.protocol._getbinary(self.window, 0, False, 0)
        self.assertEqual(expect, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._getbinary,
                                 expect, repr(expect), repr(binary)))

    def test_cookie(self, ):
        r"""Test CloseWindow."""
        cookie = self.protocol(self.window, 0, False, 0)
        self.assertIsInstance(cookie, VoidCookie,
                              msg='Failed: {0}() not returned'
                              ' VoidCookie\ngot: {1}'
                              .format(self.protocol.__class__.__name__, cookie))

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
# test_clientmessage.py ends here
