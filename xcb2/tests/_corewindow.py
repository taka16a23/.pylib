#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: _corewindow.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""Name: test_corewindow.py

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
from xcb2.tests import simple_teswindow
from xcb2.window.corewindow import Window
from xcb2.window.windowtypes import (
    WindowNormalType, WindowRootType, FundamentalWindow)
from xcb2.xproto.reply import GetWindowAttributesReply

import struct
import xcb, xcb.xproto
import xcb.render

NAME = 'TestName'
WMCLASS = 'testclass\x00TestClass\x00'

def simple_teswindow2():
    r"""SUMMARY

    simple_teswindow()

    @Return:
    """
    con = xcb.connect()
    con.render = con(xcb.render.key)

    setup = con.get_setup()
    root = setup.roots[0].root
    depth = setup.roots[0].root_depth
    visual = setup.roots[0].root_visual
    white = setup.roots[0].white_pixel

    window = con.generate_id()

    con.core.CreateWindow(depth, window, root,
                          0, 0, 640, 480, 0,
                          xcb.xproto.WindowClass.InputOutput,
                          visual,
                          xcb.xproto.CW.BackPixel | xcb.xproto.CW.EventMask,
                          [white, xcb.xproto.EventMask.Exposure |
                           xcb.xproto.EventMask.KeyPress])
    xa_wm_name = con.core.InternAtom(
        False, len('WM_NAME'), 'WM_NAME').reply().atom
    xa_net_wm_name = con.core.InternAtom(
        False, len('_NET_WM_NAME'), '_NET_WM_NAME').reply().atom
    xa_wmclass = con.core.InternAtom(
        False, len('WM_CLASS'), 'WM_CLASS').reply().atom
    xa_utf8_string = con.core.InternAtom(
        False, len('UTF8_STRING'), 'UTF8_STRING').reply().atom

    xa_net_wm_window_type = con.core.InternAtom(
        False, len('_NET_WM_WINDOW_TYPE'), '_NET_WM_WINDOW_TYPE').reply().atom
    xa_normal = con.core.InternAtom(
        False, len('_NET_WM_WINDOW_TYPE_NORMAL'),
        '_NET_WM_WINDOW_TYPE_NORMAL').reply().atom
    xa_atom = con.core.InternAtom(False, len('ATOM'), 'ATOM').reply().atom
    xa_string = con.core.InternAtom(False, len('STRING'), 'STRING').reply().atom

    con.core.ChangeProperty(xcb.xproto.PropMode.Replace, window,
                            xa_net_wm_name, xa_utf8_string, 8, len(NAME), NAME)

    con.core.ChangeProperty(
        xcb.xproto.PropMode.Replace, window, xa_wmclass, xa_string,
        8, len(WMCLASS), WMCLASS)

    # data = struct.pack('I', xa_normal)

    # con.core.ChangeProperty(
        # xcb.xproto.PropMode.Replace, window, xa_net_wm_window_type,
        # xa_atom, 32, 1, data)
    con.core.MapWindow(window)
    con.flush()
    return window


class TestCoreWindow(MockerTestCase):
    def setUp(self):
        self.conn = xcb2.connect()
        self.id = simple_teswindow()
        self.window = Window(self.conn, self.id)
        self.mocker.replay()

    def test_int(self, ):
        r"""int."""
        self.assertEqual(self.id, int(self.window),
                         msg='Failed: Window.__int__ expect: {}, got: {}'
                         .format(self.id, int(self.window)))

    def test_hash(self, ):
        r"""hash."""
        expect = hash(self.id)
        hashed = hash(self.window)
        self.assertEqual(expect, hashed,
                         msg='Failed: Window.__hash__ expect: {}, got: {}'
                         .format(expect, hashed))

    def test_repr(self, ):
        r"""repr."""
        expect = 'Window(id={})'.format(self.id)
        repred = repr(self.window)
        self.assertEqual(expect, repred,
                         msg='Failed: Window.__repr__ expect: {}, got: {}'
                         .format(expect, repred))

    def test_cmp(self, ):
        r"""cmp."""
        window = Window(self.conn, self.id)
        cmped = self.window.__cmp__(window)
        self.assertEqual(0, cmped,
                         msg='Failed: Window.__cmp__ expect: 0, got: {}'
                         .format(cmped))

    def test_cmp2(self, ):
        r"""cmp2."""
        cmped = self.window.__cmp__(self.id)
        self.assertEqual(0, cmped,
                         msg='Failed: Window.__cmp__ expect: 0, got: {}'
                         .format(cmped))

    def test_eq(self, ):
        r"""cmp."""
        window = Window(self.conn, self.id)
        eqed = self.window.__eq__(window)
        self.assertTrue(eqed)

    def test_eq2(self, ):
        r"""cmp."""
        eqed = self.window.__eq__(self.id)
        self.assertTrue(eqed)

    def test_pack(self):
        r"""pack
        """
        expect = pack('I', self.id)
        binary = self.window.pack()
        self.assertEqual(expect, binary,
                         msg='Failed: Window.pack expect: {}, got: {}'
                         .format(repr(expect), repr(binary)))

    def test_get_types(self, ):
        r"""get_types."""
        expect = FundamentalWindow
        wintype = self.window.get_types()
        self.assertIsInstance(wintype, expect,
                              msg='Failed: Window.get_types'
                              ' expect: {}, got: {}'.format(expect, wintype))

    def test_get_types_root(self, ):
        r"""get_types."""
        expect = WindowRootType
        root = self.conn.get_setup().roots[0].root
        wintype = Window(self.conn, int(root)).get_types()
        self.assertIsInstance(wintype, expect,
                              msg='Failed: Window.get_types'
                              ' expect: {}, got: {}'.format(expect, wintype))


    def test_get_types_fundamentalwindow(self, ):
        r"""get_types_fundamentalwindow."""
        expect = FundamentalWindow
        window = simple_teswindow2()
        wintype = Window(self.conn, window).get_types()
        self.assertIsInstance(wintype, expect,
                              msg='Failed: Window.get_types'
                              ' expect: {}, got: {}'.format(expect, wintype))
        self.conn.core.DestroyWindow(window)
        self.conn.flush()

    def test_get_attributes(self, ):
        r"""get_attributes."""
        expect = GetWindowAttributesReply
        reply = self.window.get_attributes()
        self.assertIsInstance(reply, expect,
                              msg='Failed: Window.get_attributes'
                              ' expect: GetWindowAttributesReply, got: {}'
                              .format(reply))

    def test_destroy(self, ):
        r"""destroy."""
        self.window.destroy()
        self.conn.flush()
        self.assertFalse(self.window in self.conn.root.client_list())

    # def test_destroy_subwindows(self, ):
    #     r"""destroy_subwindows."""
    #     self.window.destroy_subwindows()
    #     self.conn.flush()
    #     self.assertFalse(self.window in self.conn.root.client_list())

    def tearDown(self):
        self.conn.core.DestroyWindow(self.window)
        self.conn.flush()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_corewindow.py ends here
