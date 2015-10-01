#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_getproperty.py

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
import xcb2
from xcb2.xproto import GetPropertyCookie
from xcb2.xproto.wcookie import WrapGetPropertyCookie
from xcb2.xproto.ext.getproperty import (GetProperty, GetPropertyUnchecked, GetPropertyMethod, GetWM_NAME, GetWM_LOCALE_NAME, GetWM_ICON_NAME, GetWM_CLASS, GetWM_TRANSIENT_FOR, GetWM_PROTOCOLS, GetWM_COLORMAP_WINDOWS, GetWM_CLIENT_MACHINE, GetWM_STATE, Get_WIN_WORKSPACE, Get_WIN_STATE, Get_NET_SUPPORTED, Get_NET_CLIENT_LIST, Get_NET_CLIENT_LIST_STACKING, Get_NET_NUMBER_OF_DESKTOPS, Get_NET_DESKTOP_GEOMETRY, Get_NET_DESKTOP_VIEWPORT, Get_NET_CURRENT_DESKTOP, Get_NET_DESKTOP_NAMES, Get_NET_ACTIVE_WINDOW, Get_NET_WORKAREA, Get_NET_SUPPORTING_WM_CHECK, Get_NET_VIRTUAL_ROOTS, Get_NET_DESKTOP_LAYOUT, Get_NET_SHOWING_DESKTOP, Get_NET_CLOSE_WINDOW, Get_NET_MOVERESIZE_WINDOW, Get_NET_WM_MORERESIZE, Get_NET_RESTACK_WINDOW, Get_NET_REQUEST_FRAME_EXTENTS, Get_NET_WM_NAME, Get_NET_WM_VISIBLE_NAME, Get_NET_WM_ICON_NAME, Get_NET_WM_VISIBLE_ICON_NAME, Get_NET_WM_DESKTOP, Get_NET_WM_WINDOW_TYPE, Get_NET_WM_STATE, Get_NET_WM_ALLOWED_ACTIONS, Get_NET_WM_STRUT, Get_NET_WM_STRUT_PARTIAL, Get_NET_WM_ICON_GEOMETRY, Get_NET_WM_ICON, Get_NET_WM_PID, Get_NET_WM_HANDLED_ICONS, Get_NET_WM_USER_TIME, Get_NET_WM_USER_TIME_WINDOW, Get_NET_FRAME_EXTENTS, Get_OB_APP_TYPE)


class TestGetPropertyBinary(MockerTestCase):
    def setUp(self):
        self.args1 = [(False, 482, 39, 31, 0, 0),
                     "\x00\x00\x00\x00\xe2\x01\x00\x00'\x00\x00\x00\x1f"
                      "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"]
        self.args2 = [(False, 77594627, 351, 33, 0, 0),
                      '\x00\x00\x00\x00\x03\x00\xa0\x04_\x01\x00\x00!\x00'
                      '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00']
        self.args3 = [(False, 77594627, 285, 33, 0, 0),
                      '\x00\x00\x00\x00\x03\x00\xa0\x04\x1d\x01\x00\x00!\x00'
                      '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00']
        self.conn = xcb2.connect()
        self.protocol = GetProperty(self.conn)
        self.protocol_check = GetPropertyUnchecked(self.conn)
        self.mocker.replay()

    def test_binary1(self):
        r"""Test GetProperty binary1."""
        binary = self.protocol._getbinary(*self.args1[0])
        self.assertEqual(self.args1[1], binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._getbinary,
                                 str(self.args1[0])
                                 .replace('(', '').replace(')', ''),
                                 repr(self.args1[1]), repr(binary)))

    def test_binary2(self):
        r"""Test GetProperty binary2."""
        binary2 = self.protocol._getbinary(*self.args2[0])
        self.assertEqual(self.args2[1], binary2,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._getbinary,
                                 str(self.args2[0])
                                 .replace('(', '').replace(')', ''),
                                 repr(self.args2[1]), repr(binary2)))
    def test_binary3(self):
        r"""Test GetProperty binary3."""
        binary3 = self.protocol._getbinary(*self.args3[0])
        self.assertEqual(self.args3[1], binary3,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._getbinary,
                                 str(self.args3[0])
                                 .replace('(', '').replace(')', ''),
                                 repr(self.args3[1]), repr(binary3)))

    def tearDown(self):
        pass


class TestGetPropertyRequest(MockerTestCase):
    def setUp(self):
        self.window = simple_teswindow()
        self.argsbin = [(False, 482, 39, 31, 0, 0),
                        "\x00\x00\x00\x00\xe2\x01\x00\x00'\x00\x00\x00\x1f"
                        "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"]
        self.conn = xcb2.connect()
        self.protocol = GetProperty(self.conn)
        self.protocol_check = GetPropertyUnchecked(self.conn)
        self.cookie = GetPropertyCookie
        self.mocker.replay()

    def test_call(self):
        r"""Test GetProperty.__call__() expect return GetPropertyCookie."""
        self.assertIsInstance(self.protocol(*self.argsbin[0]), self.cookie,
                              msg='Failed: {0}({1}) not returned {2}'
                              .format(self.protocol.__class__.__name__,
                                      str(self.argsbin[0])
                                      .replace('(', '').replace(')', ''),
                                      'GetPropertyCookie'))

    def test_request(self, ):
        r"""Test GetProperty.request() expect return GetPropertyCookie."""
        self.assertIsInstance(self.protocol.request(self.argsbin[1]),
                              self.cookie,
                              msg='Failed: {0}.request("{1}") not return {2}'
                              .format(self.protocol.__class__.__name__,
                                      self.argsbin[1],
                                      'GetPropertyCookie'))

    def test_checkrequest(self, ):
        r"""Test GetPropertyUnchecked.request() expect return GetPropertyCookie."""
        self.assertIsInstance(self.protocol_check.request(self.argsbin[1]),
                              self.cookie,
                              msg='Failed: {0}.request("{1}") not return {2}'
                              .format(self.protocol_check.__class__.__name__,
                                      self.argsbin[1],
                                      'GetPropertyCookie'))

    def tearDown(self):
        self.conn.core.DestroyWindow(self.window)
        self.conn.flush()


class TestGetPropertyMethodBinary(MockerTestCase):
    def setUp(self):
        self.conn = xcb2.connect()
        self.protocol = GetPropertyMethod(GetProperty(self.conn))
        self.args1 = [(482, self.conn.core.InternAtom.usecache(39), 0, 0),
                     "\x00\x00\x00\x00\xe2\x01\x00\x00'\x00\x00\x00\x1f"
                      "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"]
        self.args2 = [(77594627, self.conn.core.InternAtom.usecache(351), 0, 0),
                      '\x00\x00\x00\x00\x03\x00\xa0\x04_\x01\x00\x00!\x00'
                      '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00']
        self.args3 = [(77594627, self.conn.core.InternAtom.usecache(285), 0, 0),
                      '\x00\x00\x00\x00\x03\x00\xa0\x04\x1d\x01\x00\x00!\x00'
                      '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00']
        self.mocker.replay()

    def test_binary1(self):
        r"""Test GetPropertyMethod binary1."""
        binary = self.protocol._getbinary(*self.args1[0])
        self.assertEqual(self.args1[1], binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._getbinary,
                                 str(self.args1[0])
                                 .replace('(', '').replace(')', ''),
                                 repr(self.args1[1]), repr(binary)))

    def test_binary2(self):
        r"""Test GetPropertyMethod binary2."""
        binary2 = self.protocol._getbinary(*self.args2[0])
        self.assertEqual(self.args2[1], binary2,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._getbinary,
                                 str(self.args2[0])
                                 .replace('(', '').replace(')', ''),
                                 repr(self.args2[1]), repr(binary2)))
    def test_binary3(self):
        r"""Test GetPropertyMethod binary3."""
        binary3 = self.protocol._getbinary(*self.args3[0])
        self.assertEqual(self.args3[1], binary3,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._getbinary,
                                 str(self.args3[0])
                                 .replace('(', '').replace(')', ''),
                                 repr(self.args3[1]), repr(binary3)))

    def tearDown(self):
        pass


class TestGetPropertyMethod(MockerTestCase):
    def setUp(self):
        self.conn = xcb2.connect()
        self.protocol = GetPropertyMethod(GetProperty(self.conn))
        self.args1 = [(self.conn.core.InternAtom.usecache(39), 77594627),
                     "\x00\x01\x00\x00\x03\x00\xa0\x04'\x00\x00\x00\x1f"
                      "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"]
        self.mocker.replay()

    def test_set_delete(self, ):
        r"""Test GetPropertyMethod.set_delete()."""
        self.protocol.set_delete(True)
        binary = self.protocol._getbinary(
            77594627, self.conn.core.InternAtom.usecache(39), 0, 0)
        self.assertEqual(self.args1[1], binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._getbinary,
                                 str(self.args1[0])
                                 .replace('(', '').replace(')', ''),
                                 repr(self.args1[1]), repr(binary)))

    def test_set_delete_raise_error(self, ):
        r"""Test GetPropertyMethod.set_delete raise_error."""
        # TODO: (Atami) [2014/05/29]
        with self.assertRaises(StandardError):
            self.protocol.set_delete(1) # dummy args

    def test_returned_cookie(self, ):
        r"""Test GetPropertyMethod returned_cookie."""
        cookie = self.protocol(*self.args1[0])
        self.assertIsInstance(cookie, WrapGetPropertyCookie,
                              msg='Failed: {0}() not return {2}\nGot: {3}'
                              .format(self.protocol.__class__.__name__,
                                      cookie, 'WrapGetAtomNameCookie',
                                      cookie))

    def tearDown(self):
        pass


class TestGetPropertyCoreMethod(MockerTestCase):
    def setUp(self):
        self.conn = xcb2.connect()
        self.getproperty = GetProperty(self.conn)
        self.mocker.replay()

    def test_WM_NAME_binary(self):
        r"""Test GetWM_NAME binary."""
        protocol = GetWM_NAME(self.getproperty)
        expectbin = ("\x00\x00\x00\x00\xe2\x01\x00\x00'\x00\x00\x00\x1f"
                      "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test_WM_LOCALE_NAME_binary(self):
        r"""Test GetWM_LOCALE_NAME binary."""
        protocol = GetWM_LOCALE_NAME(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00\x19\x01\x00\x00\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test_WM_ICON_NAME_binary(self):
        r"""Test GetWM_ICON_NAME binary."""
        protocol = GetWM_ICON_NAME(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00%\x00\x00\x00\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test_WM_CLASS_binary(self):
        r"""Test GetWM_CLASS binary."""
        protocol = GetWM_CLASS(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00C\x00\x00\x00\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test_WM_TRANSIENT_FOR_binary(self):
        r"""Test GetWM_TRANSIENT_FOR binary."""
        protocol = GetWM_TRANSIENT_FOR(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00D\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test_WM_PROTOCOLS_binary(self):
        r"""Test GetWM_PROTOCOLS binary."""
        protocol = GetWM_PROTOCOLS(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00\x1a\x01\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test_WM_COLORMAP_WINDOWS_binary(self):
        r"""Test GetWM_COLORMAP_WINDOWS binary."""
        protocol = GetWM_COLORMAP_WINDOWS(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00\x96\x01\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test_WM_CLIENT_MACHINE_binary(self):
        r"""Test GetWM_CLIENT_MACHINE binary."""
        protocol = GetWM_CLIENT_MACHINE(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00$\x00\x00\x00\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test_WM_STATE_binary(self):
        r"""Test GetWM_STATE binary."""
        protocol = GetWM_STATE(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00\x97\x01\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test__WIN_WORKSPACE_binary(self):
        r"""Test Get_WIN_WORKSPACE binary."""
        protocol = Get_WIN_WORKSPACE(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00\x93\x01\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test__WIN_STATE_binary(self):
        r"""Test Get_WIN_STATE binary."""
        protocol = Get_WIN_STATE(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00\x91\x01\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test__NET_SUPPORTED_binary(self):
        r"""Test Get_NET_SUPPORTED binary."""
        protocol = Get_NET_SUPPORTED(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00j\x01\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test__NET_CLIENT_LIST_binary(self):
        r"""Test Get_NET_CLIENT_LIST binary."""
        protocol = Get_NET_CLIENT_LIST(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00_\x01\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test__NET_CLIENT_LIST_STACKING_binary(self):
        r"""Test Get_NET_CLIENT_LIST_STACKING binary."""
        protocol = Get_NET_CLIENT_LIST_STACKING(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00`\x01\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test__NET_NUMBER_OF_DESKTOPS_binary(self):
        r"""Test Get_NET_NUMBER_OF_DESKTOPS binary."""
        protocol = Get_NET_NUMBER_OF_DESKTOPS(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00g\x01\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test__NET_DESKTOP_GEOMETRY_binary(self):
        r"""Test Get_NET_DESKTOP_GEOMETRY binary."""
        protocol = Get_NET_DESKTOP_GEOMETRY(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00b\x01\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test__NET_DESKTOP_VIEWPORT_binary(self):
        r"""Test Get_NET_DESKTOP_VIEWPORT binary."""
        protocol = Get_NET_DESKTOP_VIEWPORT(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00e\x01\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test__NET_CURRENT_DESKTOP_binary(self):
        r"""Test Get_NET_CURRENT_DESKTOP binary."""
        protocol = Get_NET_CURRENT_DESKTOP(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00\x1e\x01\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test__NET_DESKTOP_NAMES_binary(self):
        r"""Test Get_NET_DESKTOP_NAMES binary."""
        protocol = Get_NET_DESKTOP_NAMES(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00d\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test__NET_ACTIVE_WINDOW_binary(self):
        r"""Test Get_NET_ACTIVE_WINDOW binary."""
        protocol = Get_NET_ACTIVE_WINDOW(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00\x1d\x01\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test__NET_WORKAREA_binary(self):
        r"""Test Get_NET_WORKAREA binary."""
        protocol = Get_NET_WORKAREA(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00\x8b\x01\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test__NET_SUPPORTING_WM_CHECK_binary(self):
        r"""Test Get_NET_SUPPORTING_WM_CHECK binary."""
        protocol = Get_NET_SUPPORTING_WM_CHECK(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00k\x01\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test__NET_VIRTUAL_ROOTS_binary(self):
        r"""Test Get_NET_VIRTUAL_ROOTS binary."""
        protocol = Get_NET_VIRTUAL_ROOTS(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x007\x01\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test__NET_DESKTOP_LAYOUT_binary(self):
        r"""Test Get_NET_DESKTOP_LAYOUT binary."""
        protocol = Get_NET_DESKTOP_LAYOUT(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00c\x01\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test__NET_SHOWING_DESKTOP_binary(self):
        r"""Test Get_NET_SHOWING_DESKTOP binary."""
        protocol = Get_NET_SHOWING_DESKTOP(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00i\x01\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test__NET_CLOSE_WINDOW_binary(self):
        r"""Test Get_NET_CLOSE_WINDOW binary."""
        protocol = Get_NET_CLOSE_WINDOW(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00a\x01\x00\x00\\\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test__NET_MOVERESIZE_WINDOW_binary(self):
        r"""Test Get_NET_MOVERESIZE_WINDOW binary."""
        protocol = Get_NET_MOVERESIZE_WINDOW(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00f\x01\x00\x00\\\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test__NET_WM_MORERESIZE_binary(self):
        r"""Test Get_NET_WM_MORERESIZE binary."""
        protocol = Get_NET_WM_MORERESIZE(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00\x00\x00\x00\x00\\\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test__NET_RESTACK_WINDOW_binary(self):
        r"""Test Get_NET_RESTACK_WINDOW binary."""
        protocol = Get_NET_RESTACK_WINDOW(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00\x00\x00\x00\x00\\\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test__NET_REQUEST_FRAME_EXTENTS_binary(self):
        r"""Test Get_NET_REQUEST_FRAME_EXTENTS binary."""
        protocol = Get_NET_REQUEST_FRAME_EXTENTS(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00h\x01\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test__NET_WM_NAME_binary(self):
        r"""Test Get_NET_WM_NAME binary."""
        protocol = Get_NET_WM_NAME(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00%\x01\x00\x00\x16\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test__NET_WM_VISIBLE_NAME_binary(self):
        r"""Test Get_NET_WM_VISIBLE_NAME binary."""
        protocol = Get_NET_WM_VISIBLE_NAME(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00\xba\x01\x00\x00\x16\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test__NET_WM_ICON_NAME_binary(self):
        r"""Test Get_NET_WM_ICON_NAME binary."""
        protocol = Get_NET_WM_ICON_NAME(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00$\x01\x00\x00\x16\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test__NET_WM_VISIBLE_ICON_NAME_binary(self):
        r"""Test Get_NET_WM_VISIBLE_ICON_NAME binary."""
        protocol = Get_NET_WM_VISIBLE_ICON_NAME(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00\xbb\x01\x00\x00\x16\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test__NET_WM_DESKTOP_binary(self):
        r"""Test Get_NET_WM_DESKTOP binary."""
        protocol = Get_NET_WM_DESKTOP(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00"\x01\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test__NET_WM_WINDOW_TYPE_binary(self):
        r"""Test Get_NET_WM_WINDOW_TYPE binary."""
        protocol = Get_NET_WM_WINDOW_TYPE(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x004\x01\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test__NET_WM_STATE_binary(self):
        r"""Test Get_NET_WM_STATE binary."""
        protocol = Get_NET_WM_STATE(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00(\x01\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test__NET_WM_ALLOWED_ACTIONS_binary(self):
        r"""Test Get_NET_WM_ALLOWED_ACTIONS binary."""
        protocol = Get_NET_WM_ALLOWED_ACTIONS(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00x\x01\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test__NET_WM_STRUT_binary(self):
        r"""Test Get_NET_WM_STRUT binary."""
        protocol = Get_NET_WM_STRUT(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00\x82\x01\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test__NET_WM_STRUT_PARTIAL_binary(self):
        r"""Test Get_NET_WM_STRUT_PARTIAL binary."""
        protocol = Get_NET_WM_STRUT_PARTIAL(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00\x83\x01\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test__NET_WM_ICON_GEOMETRY_binary(self):
        r"""Test Get_NET_WM_ICON_GEOMETRY binary."""
        protocol = Get_NET_WM_ICON_GEOMETRY(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00{\x01\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test__NET_WM_ICON_binary(self):
        r"""Test Get_NET_WM_ICON binary."""
        protocol = Get_NET_WM_ICON(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00#\x01\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test__NET_WM_PID_binary(self):
        r"""Test Get_NET_WM_PID binary."""
        protocol = Get_NET_WM_PID(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00&\x01\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test__NET_WM_HANDLED_ICONS_binary(self):
        r"""Test Get_NET_WM_HANDLED_ICONS binary."""
        protocol = Get_NET_WM_HANDLED_ICONS(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test__NET_WM_USER_TIME_binary(self):
        r"""Test Get_NET_WM_USER_TIME binary."""
        protocol = Get_NET_WM_USER_TIME(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x006\x01\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test__NET_WM_USER_TIME_WINDOW_binary(self):
        r"""Test Get_NET_WM_USER_TIME_WINDOW binary."""
        protocol = Get_NET_WM_USER_TIME_WINDOW(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00C\x01\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test__NET_FRAME_EXTENTS_binary(self):
        r"""Test Get_NET_FRAME_EXTENTS binary."""
        protocol = Get_NET_FRAME_EXTENTS(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00\x1f\x01\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def test__OB_APP_TYPE_binary(self):
        r"""Test Get_OB_APP_TYPE binary."""
        protocol = Get_OB_APP_TYPE(self.getproperty)
        expectbin = ('\x00\x00\x00\x00\xe2\x01\x00\x00\x00\x00\x00\x00\x16\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        binary = protocol._getbinary(482, long_length=0)
        self.assertEqual(expectbin, binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}():\n'
                         'Expected: "{2}"\nReturned: "{3}"'
                         .format(protocol, protocol._getbinary,
                                 repr(expectbin), repr(binary)))

    def tearDown(self):
        pass



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_getproperty.py ends here
