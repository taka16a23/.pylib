#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: test_grabbutton.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""Name: test_grabbutton.py

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
from xcb2.tests import simple_teswindow
import xcb, xcb.xproto
import xcb2, xcb2.xproto
from xcb2.xproto import NamedKeyButMask, GrabMode, NamedButtonIndex, EventMask
from xcb2 import VoidCookie
from xcb2.xproto.ext.grabbutton import (
    GrabButton, GrabButtonChecked, GrabButtonLeft, GrabButtonRight,
    GrabButtonMiddle, GrabButtonWheelUp, GrabButtonWheelDown)


class TestGrabButtonBinary(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.args1 = [(False, 482, xcb2.xproto.EventMask.ButtonPress,
                       xcb2.xproto.GrabMode.Async, xcb2.xproto.GrabMode.Async,
                       0, 0, xcb2.xproto.NamedButtonIndex.Left, 0),
                     '\x00\x00\x00\x00\xe2\x01\x00\x00\x04\x00\x01\x01'
                      '\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00']
        cls.args2 = [(False, 482, xcb2.xproto.EventMask.ButtonRelease,
                       xcb2.xproto.GrabMode.Async, xcb2.xproto.GrabMode.Async,
                       0, 0, xcb2.xproto.NamedButtonIndex.Right,
                       xcb2.xproto.NamedKeyButMask.Lock),
                      '\x00\x00\x00\x00\xe2\x01\x00\x00\x08\x00\x01\x01'
                      '\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x02\x00']
        cls.args3 = [(False, 482, xcb2.xproto.EventMask.ButtonPress,
                       xcb2.xproto.GrabMode.Async, xcb2.xproto.GrabMode.Async,
                       0, 0, xcb2.xproto.NamedButtonIndex.Middle,
                       xcb2.xproto.NamedKeyButMask.Lock),
                      '\x00\x00\x00\x00\xe2\x01\x00\x00\x04\x00\x01\x01'
                      '\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x02\x00']
        cls.conn = xcb.connect()
        cls.protocol = GrabButton(cls.conn)
        cls.protocol_check = GrabButtonChecked(cls.conn)

    def setUp(self):
        self.conn.flush()
        self.mocker.replay()

    def test_binary1(self):
        r"""Test GrabButton binary1."""
        binary = self.protocol._getbinary(*self.args1[0])
        self.assertEqual(self.args1[1], binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._getbinary,
                                 str(self.args1[0])
                                 .replace('(', '').replace(')', ''),
                                 repr(self.args1[1]), repr(binary)))

    def test_binary2(self):
        r"""Test GrabButton binary2."""
        binary2 = self.protocol._getbinary(*self.args2[0])
        self.assertEqual(self.args2[1], binary2,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._getbinary,
                                 str(self.args2[0])
                                 .replace('(', '').replace(')', ''),
                                 repr(self.args2[1]), repr(binary2)))
    def test_binary3(self):
        r"""Test GrabButton binary3."""
        binary3 = self.protocol._getbinary(*self.args3[0])
        self.assertEqual(self.args3[1], binary3,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._getbinary,
                                 str(self.args3[0])
                                 .replace('(', '').replace(')', ''),
                                 repr(self.args3[1]), repr(binary3)))

    def tearDown(self):
        self.conn.core.UngrabButton(
            self.args1[0][7], self.args1[0][1], self.args1[0][-1])
        self.conn.core.UngrabButton(
            self.args2[0][7], self.args2[0][1], self.args2[0][-1])
        self.conn.core.UngrabButton(
            self.args3[0][7], self.args3[0][1], self.args3[0][-1])
        self.conn.flush()

    @classmethod
    def tearDownClass(cls, ):
        cls.conn.core.UngrabButton(
            cls.args1[0][7], cls.args1[0][1], cls.args1[0][-1])
        cls.conn.core.UngrabButton(
            cls.args2[0][7], cls.args2[0][1], cls.args2[0][-1])
        cls.conn.core.UngrabButton(
            cls.args3[0][7], cls.args3[0][1], cls.args3[0][-1])
        cls.conn.flush()
        cls.conn.disconnect()


class TestGrabButtonRequest(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.argsbin = [(False, 482, xcb2.xproto.EventMask.ButtonPress,
                       xcb2.xproto.GrabMode.Async, xcb2.xproto.GrabMode.Async,
                       0, 0, xcb2.xproto.NamedButtonIndex.Left, 0),
                     '\x00\x00\x00\x00\xe2\x01\x00\x00\x04\x00\x01\x01'
                      '\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00']
        cls.conn = xcb.connect()
        cls.protocol = GrabButton(cls.conn)
        cls.protocol_check = GrabButtonChecked(cls.conn)
        cls.cookie = VoidCookie

    def setUp(self):
        self.conn.flush()
        self.mocker.replay()

    def test_call(self):
        r"""Test GrabButton.__call__() expect return VoidCookie."""
        self.assertIsInstance(self.protocol(*self.argsbin[0]), self.cookie,
                              msg='Failed: {0}({1}) not returned {2}'
                              .format(self.protocol.__class__.__name__,
                                      str(self.argsbin[0])
                                      .replace('(', '').replace(')', ''),
                                      'GetPropertyCookie'))

    def test_request(self, ):
        r"""Test GrabButton.request() expect return VoidCookie."""
        self.assertIsInstance(self.protocol.request(self.argsbin[1]),
                              self.cookie,
                              msg='Failed: {0}.request("{1}") not return {2}'
                              .format(self.protocol.__class__.__name__,
                                      self.argsbin[1], 'VoidCookie'))

    def test_checkrequest(self, ):
        r"""Test GrabButton.request() expect return VoidCookie."""
        self.assertIsInstance(self.protocol_check.request(self.argsbin[1]),
                              self.cookie,
                              msg='Failed: {0}.request("{1}") not return {2}'
                              .format(self.protocol_check.__class__.__name__,
                                      self.argsbin[1], 'VoidCookie'))

    def tearDown(self):
        self.conn.core.UngrabButton(
            self.argsbin[0][7], self.argsbin[0][1], self.argsbin[0][-1])
        self.conn.flush()

    @classmethod
    def tearDownClass(cls, ):
        cls.conn.core.UngrabButton(
            cls.argsbin[0][7], cls.argsbin[0][1], cls.argsbin[0][-1])
        cls.conn.flush()
        cls.conn.disconnect()


class TestGrabButtonMethodBinary(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.conn = xcb.connect()
        cls.grabbutton = GrabButton(cls.conn)

    def setUp(self):
        self.conn.flush()
        self.mocker.replay()

    def test_press_cookie(self, ):
        r"""Test GrabButton.request() expect return VoidCookie."""
        protocol = GrabButtonLeft(self.grabbutton)
        self.assertIsInstance(
            protocol.press(False, 482, 0, 0, NamedKeyButMask.Lock,),
            VoidCookie,
            msg='Failed: {0}.request() not return {1}'
            .format(protocol.__class__.__name__, 'VoidCookie'))

    def test_left_getbinary(self, ):
        r"""Test GrabButtonLeft.getbinary"""
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00\x04\x00\x01\x01'
                     '\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00')
        protocol = GrabButtonLeft(self.grabbutton)
        binary = protocol._getbinary(
            False, 482, EventMask.ButtonPress, 0, 0, NamedKeyButMask.Lock,
            GrabMode.Async, GrabMode.Async)
        self.assertEqual(expectbin, binary,
                         msg='Failed: {0.__class__.__name__}._getbinary()'
                         '\nExpected: {1}\nReturned: {2}'
                         .format(protocol, repr(expectbin), repr(binary)))

    def test_left_press(self):
        r"""Test GrabButtonLeft.press"""
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00\x04\x00\x01\x01'
                     '\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00')
        protocol = GrabButtonLeft(self.grabbutton)
        binary = protocol._get_press_binary(
            False, 482, 0, 0, NamedKeyButMask.Lock,
            GrabMode.Async, GrabMode.Async)
        self.assertEqual(expectbin, binary,
                         msg='Failed: {0.__class__.__name__}._getpress_binary()'
                         '\nExpected: {1}\nReturned: {2}'
                         .format(protocol, repr(expectbin), repr(binary)))

    def test_left_release(self, ):
        r"""Test GrabButtonLeft.release"""
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00\x08\x00\x01\x01'
                     '\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00')
        protocol = GrabButtonLeft(self.grabbutton)
        binary = protocol._get_release_binary(
            False, 482, 0, 0, NamedKeyButMask.Lock,
            GrabMode.Async, GrabMode.Async)
        self.assertEqual(expectbin, binary,
                         msg='Failed: {0.__class__.__name__}._getrelease_binary()'
                         '\nExpected: {1}\nReturned: {2}'
                         .format(protocol, repr(expectbin), repr(binary)))

    def test_right_getbinary(self, ):
        r"""Test GrabButtonRight.getbinary"""
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00\x04\x00\x01\x01'
                     '\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x02\x00')
        protocol = GrabButtonRight(self.grabbutton)
        binary = protocol._getbinary(
            False, 482, EventMask.ButtonPress, 0, 0, NamedKeyButMask.Lock,
            GrabMode.Async, GrabMode.Async)
        self.assertEqual(expectbin, binary,
                         msg='Failed: {0.__class__.__name__}._getbinary()'
                         '\nExpected: {1}\nReturned: {2}'
                         .format(protocol, repr(expectbin), repr(binary)))

    def test_right_press(self):
        r"""Test GrabButtonRight.press"""
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00\x04\x00\x01\x01'
                     '\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x02\x00')
        protocol = GrabButtonRight(self.grabbutton)
        binary = protocol._get_press_binary(
            False, 482, 0, 0, NamedKeyButMask.Lock,
            GrabMode.Async, GrabMode.Async)
        self.assertEqual(expectbin, binary,
                         msg='Failed: {0.__class__.__name__}._getpress_binary()'
                         '\nExpected: {1}\nReturned: {2}'
                         .format(protocol, repr(expectbin), repr(binary)))

    def test_right_release(self, ):
        r"""Test GrabButtonRight.release"""
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00\x08\x00\x01\x01'
                     '\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x02\x00')
        protocol = GrabButtonRight(self.grabbutton)
        binary = protocol._get_release_binary(
            False, 482, 0, 0, NamedKeyButMask.Lock,
            GrabMode.Async, GrabMode.Async)
        self.assertEqual(expectbin, binary,
                         msg='Failed: {0.__class__.__name__}._getrelease_binary()'
                         '\nExpected: {1}\nReturned: {2}'
                         .format(protocol, repr(expectbin), repr(binary)))

    def test_middle_getbinary(self, ):
        r"""Test GrabButtonMiddle.getbinary"""
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00\x04\x00\x01\x01'
                     '\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x02\x00')
        protocol = GrabButtonMiddle(self.grabbutton)
        binary = protocol._getbinary(
            False, 482, EventMask.ButtonPress, 0, 0, NamedKeyButMask.Lock,
            GrabMode.Async, GrabMode.Async)
        self.assertEqual(expectbin, binary,
                         msg='Failed: {0.__class__.__name__}._getbinary()'
                         '\nExpected: {1}\nReturned: {2}'
                         .format(protocol, repr(expectbin), repr(binary)))

    def test_middle_press(self):
        r"""Test GrabButtonMiddle.press"""
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00\x04\x00\x01\x01'
                     '\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x02\x00')
        protocol = GrabButtonMiddle(self.grabbutton)
        binary = protocol._get_press_binary(
            False, 482, 0, 0, NamedKeyButMask.Lock,
            GrabMode.Async, GrabMode.Async)
        self.assertEqual(expectbin, binary,
                         msg='Failed: {0.__class__.__name__}._getpress_binary()'
                         '\nExpected: {1}\nReturned: {2}'
                         .format(protocol, repr(expectbin), repr(binary)))

    def test_middle_release(self, ):
        r"""Test GrabButtonMiddle.release"""
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00\x08\x00\x01\x01'
                     '\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x02\x00')
        protocol = GrabButtonMiddle(self.grabbutton)
        binary = protocol._get_release_binary(
            False, 482, 0, 0, NamedKeyButMask.Lock,
            GrabMode.Async, GrabMode.Async)
        self.assertEqual(expectbin, binary,
                         msg='Failed: {0.__class__.__name__}._getrelease_binary()'
                         '\nExpected: {1}\nReturned: {2}'
                         .format(protocol, repr(expectbin), repr(binary)))

    def test_wheelup_getbinary(self, ):
        r"""Test GrabButtonWheelUp.getbinary"""
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00\x04\x00\x01\x01'
                     '\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x02\x00')
        protocol = GrabButtonWheelUp(self.grabbutton)
        binary = protocol._getbinary(
            False, 482, EventMask.ButtonPress, 0, 0, NamedKeyButMask.Lock,
            GrabMode.Async, GrabMode.Async)
        self.assertEqual(expectbin, binary,
                         msg='Failed: {0.__class__.__name__}._getbinary()'
                         '\nExpected: {1}\nReturned: {2}'
                         .format(protocol, repr(expectbin), repr(binary)))

    def test_wheelup_press(self):
        r"""Test GrabButtonWheelUp.press"""
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00\x04\x00\x01\x01'
                     '\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x02\x00')
        protocol = GrabButtonWheelUp(self.grabbutton)
        binary = protocol._get_press_binary(
            False, 482, 0, 0, NamedKeyButMask.Lock,
            GrabMode.Async, GrabMode.Async)
        self.assertEqual(expectbin, binary,
                         msg='Failed: {0.__class__.__name__}._getpress_binary()'
                         '\nExpected: {1}\nReturned: {2}'
                         .format(protocol, repr(expectbin), repr(binary)))

    def test_wheelup_release(self, ):
        r"""Test GrabButtonWheelUp.release"""
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00\x08\x00\x01\x01'
                     '\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x02\x00')
        protocol = GrabButtonWheelUp(self.grabbutton)
        binary = protocol._get_release_binary(
            False, 482, 0, 0, NamedKeyButMask.Lock,
            GrabMode.Async, GrabMode.Async)
        self.assertEqual(expectbin, binary,
                         msg='Failed: {0.__class__.__name__}._getrelease_binary()'
                         '\nExpected: {1}\nReturned: {2}'
                         .format(protocol, repr(expectbin), repr(binary)))

    def test_wheeldown_getbinary(self, ):
        r"""Test GrabButtonWheelDown.getbinary"""
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00\x04\x00\x01\x01'
                     '\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x02\x00')
        protocol = GrabButtonWheelDown(self.grabbutton)
        binary = protocol._getbinary(
            False, 482, EventMask.ButtonPress, 0, 0, NamedKeyButMask.Lock,
            GrabMode.Async, GrabMode.Async)
        self.assertEqual(expectbin, binary,
                         msg='Failed: {0.__class__.__name__}._getbinary()'
                         '\nExpected: {1}\nReturned: {2}'
                         .format(protocol, repr(expectbin), repr(binary)))

    def test_wheeldown_press(self):
        r"""Test GrabButtonWheelDown.press"""
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00\x04\x00\x01\x01'
                     '\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x02\x00')
        protocol = GrabButtonWheelDown(self.grabbutton)
        binary = protocol._get_press_binary(
            False, 482, 0, 0, NamedKeyButMask.Lock,
            GrabMode.Async, GrabMode.Async)
        self.assertEqual(expectbin, binary,
                         msg='Failed: {0.__class__.__name__}._getpress_binary()'
                         '\nExpected: {1}\nReturned: {2}'
                         .format(protocol, repr(expectbin), repr(binary)))

    def test_wheeldown_release(self, ):
        r"""Test GrabButtonWheelDown.release"""
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00\x08\x00\x01\x01'
                     '\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x02\x00')
        protocol = GrabButtonWheelDown(self.grabbutton)
        binary = protocol._get_release_binary(
            False, 482, 0, 0, NamedKeyButMask.Lock,
            GrabMode.Async, GrabMode.Async)
        self.assertEqual(expectbin, binary,
                         msg='Failed: {0.__class__.__name__}._getrelease_binary()'
                         '\nExpected: {1}\nReturned: {2}'
                         .format(protocol, repr(expectbin), repr(binary)))

    def test_left_getbinary_auto_async(self, ):
        r"""Test GrabButtonLeft.getbinary async"""
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00\x04\x00\x01\x01'
                     '\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00')
        protocol = GrabButtonLeft(self.grabbutton)
        binary = protocol._getbinary(
            False, 482, EventMask.ButtonPress, 0, 0, NamedKeyButMask.Lock,
            None, None)
        self.assertEqual(expectbin, binary,
                         msg='Failed: {0.__class__.__name__}._getbinary()'
                         '\nExpected: {1}\nReturned: {2}'
                         .format(protocol, repr(expectbin), repr(binary)))

    def test_left_press_auto_async(self):
        r"""Test GrabButtonLeft.press async"""
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00\x04\x00\x01\x01'
                     '\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00')
        protocol = GrabButtonLeft(self.grabbutton)
        binary = protocol._get_press_binary(
            False, 482, 0, 0, NamedKeyButMask.Lock,
            None, None)
        self.assertEqual(expectbin, binary,
                         msg='Failed: {0.__class__.__name__}._getpress_binary()'
                         '\nExpected: {1}\nReturned: {2}'
                         .format(protocol, repr(expectbin), repr(binary)))

    def test_left_release_auto_async(self, ):
        r"""Test GrabButtonLeft.release async"""
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00\x08\x00\x01\x01'
                     '\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00')
        protocol = GrabButtonLeft(self.grabbutton)
        binary = protocol._get_release_binary(
            False, 482, 0, 0, NamedKeyButMask.Lock,
            None, None)
        self.assertEqual(expectbin, binary,
                         msg='Failed: {0.__class__.__name__}._getrelease_binary()'
                         '\nExpected: {1}\nReturned: {2}'
                         .format(protocol, repr(expectbin), repr(binary)))

    def tearDown(self):
        self.conn.core.UngrabButton(
            NamedButtonIndex.Left, 482, NamedKeyButMask.Lock)
        self.conn.core.UngrabButton(
            NamedButtonIndex.Right, 482, NamedKeyButMask.Lock)
        self.conn.core.UngrabButton(
            NamedButtonIndex.Middle, 482, NamedKeyButMask.Lock)
        self.conn.core.UngrabButton(
            NamedButtonIndex.WheelUp, 482, NamedKeyButMask.Lock)
        self.conn.core.UngrabButton(
            NamedButtonIndex.WheelDown, 482, NamedKeyButMask.Lock)
        self.conn.flush()

    @classmethod
    def tearDownClass(cls, ):
        cls.conn.core.UngrabButton(
            NamedButtonIndex.Left, 482, NamedKeyButMask.Lock)
        cls.conn.core.UngrabButton(
            NamedButtonIndex.Right, 482, NamedKeyButMask.Lock)
        cls.conn.core.UngrabButton(
            NamedButtonIndex.Middle, 482, NamedKeyButMask.Lock)
        cls.conn.core.UngrabButton(
            NamedButtonIndex.WheelUp, 482, NamedKeyButMask.Lock)
        cls.conn.core.UngrabButton(
            NamedButtonIndex.WheelDown, 482, NamedKeyButMask.Lock)
        cls.conn.flush()
        cls.conn.disconnect()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_grabbutton.py ends here
