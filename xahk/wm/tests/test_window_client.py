#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: test_window_client.py 339 2015-07-23 18:01:26Z t1 $
# $Revision: 339 $
# $Date: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $

r"""Name: test_window_client.py

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
from struct import pack, unpack
from array import array


from xahk.wm.display import Display
from xahk.wm.window_client import WindowClient, PropMode
from xahk.wm.root_window import RootWindow
from xahk.wm.cursor_handler import CursorHandler
from xahk.wm.atom_cache import AtomCache


def simple_teswindow(display, x, y, width, height):
    r"""SUMMARY
    simple_teswindow(c, 100,100,1000,1000)
    simple_teswindow()

    @Return:
    """
    from xcb import xproto
    stup = display.get_setup()
    root = stup.roots[0].root
    depth = stup.roots[0].root_depth
    visual = stup.roots[0].root_visual
    white = stup.roots[0].white_pixel

    window = display.generate_id()

    display.core.CreateWindow(depth, window, root,
                              0, 0, width, height, 0,
                              xproto.WindowClass.InputOutput,
                              visual,
                              xproto.CW.BackPixel, [white])
    display.core.MapWindow(window)
    display.flush()
    return window


def window1(display):
    return simple_teswindow(display, 0, 0, 1000, 1000)

def window2(display):
    return simple_teswindow(display, 250, 250, 1000, 1000)


class TestWindowClient(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.display = Display()
        cls.root = RootWindow(cls.display)
        cls.atom_cache = AtomCache(cls.display, ['_NET_WM_STATE',
                                                 'ATOM',
                                                 '_NET_WM_STATE_HIDDEN',
                                                 ])

    def setUp(self):
        self.window_id = window1(self.display)
        self.client = WindowClient(self.display, self.window_id)
        self.need_destroy = True
        self.mocker.replay()

    def test___init__(self, ):
        self.skipTest('Not Implemented')

    def test_get_display(self, ):
        self.assertEqual(self.display, self.client.get_display())
        self.assertEqual(self.display, self.client.display)

    def test___int__(self, ):
        self.assertEqual(self.window_id, int(self.client))

    def test___eq__(self, ):
        self.assertEqual(self.window_id, self.client)
        self.assertEqual(
            WindowClient(self.display, self.window_id), self.client)

    def test___ne__(self, ):
        self.assertTrue(482 != self.client)
        self.assertTrue(WindowClient(self.display, 482) != self.client)

    def test___hash__(self, ):
        self.assertEqual(hash(self.window_id), hash(self.client))

    def test___repr__(self, ):
        self.skipTest('Not Implemented')

    def test_get_root(self, ):
        self.assertEqual(self.display.get_setup().roots[0].root,
                         self.client.get_root())
        self.assertEqual(self.display.get_setup().roots[0].root,
                         self.client.root)

    def test_get_id(self, ):
        self.assertEqual(self.window_id, self.client.get_id())
        self.assertEqual(self.window_id, self.client.id)

    def test_get_property(self, ):
        self.skipTest('Not Implemented')

    def test_change_property(self, ):
        self.skipTest('Not Implemented')

    def test_get_title(self, ):
        expects = 'test_title'
        self.client.set_title(expects)
        self.assertEqual(expects, self.client.get_title())

    def test_get_wmclass(self, ):
        expects = 'test\x00test\x00'
        self.client.change_property(
            PropMode.Replace, 'WM_CLASS', 'STRING', 8, len(expects), expects)
        expects = expects.split('\x00')
        expects.remove('')
        self.assertEqual(expects, self.client.get_wmclass())
        self.assertEqual(expects, self.client.wmclass)

    def test_get_pid(self, ):
        expects = 3333
        self.client.change_property(
            PropMode.Replace, '_NET_WM_PID', 'CARDINAL',
            32, 1, pack('I', expects))
        self.assertEqual(expects, self.client.get_pid())
        self.assertEqual(expects, self.client.pid)

    def test_get_type(self, ):
        expects = self.display.core.InternAtom(
            False, len('_NET_WM_WINDOW_TYPE_NORMAL'),
                '_NET_WM_WINDOW_TYPE_NORMAL').reply().atom
        self.client.change_property(
            PropMode.Replace, '_NET_WM_WINDOW_TYPE', 'ATOM', 32, 1,
            pack('I', expects))
        self.assertEqual(expects, self.client.get_type())
        self.assertEqual(expects, self.client.type)

    def test_get_workspace(self, ):
        if self.root.get_number_of_desktop() <= 1:
            self.skipTest('Need other Workspaces.')
        expects = 1
        self.client.change_workspace(expects)
        self.assertEqual(expects, self.client.get_workspace())
        self.assertEqual(expects, self.client.workspace)

    def test_get_bounds(self, ):
        expectsx, expectsy, expectsw, expectsh = 15, 15, 200, 300
        self.client.set_bounds(expectsx, expectsy, expectsw, expectsh)
        sleep(0.3)
        bounds = self.client.get_bounds()
        self.assertEqual(expectsx, bounds.x)
        self.assertEqual(expectsy, bounds.y)
        self.assertEqual(expectsw, bounds.width)
        self.assertEqual(expectsh, bounds.height)

    def test_set_size(self, ):
        expectsw, expectsh = 200, 300
        self.client.set_size(expectsw, expectsh)
        sleep(0.3)
        bounds = self.client.get_bounds()
        self.assertEqual(expectsw, bounds.width)
        self.assertEqual(expectsh, bounds.height)

    def test_move(self, ):
        expectsx, expectsy = 15, 15
        self.client.move(expectsx, expectsy)
        sleep(0.3)
        bounds = self.client.get_bounds()
        self.assertEqual(expectsx, bounds.x)
        self.assertEqual(expectsy, bounds.y)

    def test_raise_window(self, ):
        """
         +------------------------------+
         |  Window1                     |
         |                              |
         |      +-----------------------------+
         |      |  Window2                    |
         |      |                             |
         |      |                             |
         |      |                             |
         |      |                             |
         |      |                             |
         |      |                             |
         |      |                             |
         +------|                             |
                |                             |
                |                             |
                +-----------------------------+

                       ||
                       \/

         +------------------------------+
         |  Window1                     |
         |                              |
         |                              |-----+
         |                              |     |
         |                              |     |
         |                              |     |
         |                              |     |
         |                              |     |
         |                              |     |
         |                              |     |
         |                              |     |
         +------------------------------+     |
                |                             |
                |  Window2                    |
                +-----------------------------+
        """
        self.client.set_bounds(0, 0, 1000, 1000)
        win2 = window2(self.display)
        client2 = WindowClient(self.display, win2)
        client2.set_bounds(250, 250, 1000, 1000)
        self.display.core.WarpPointerChecked(
            0, self.root, 0, 0, 0, 0, 500, 500).check()
        sleep(0.2)
        cursor = CursorHandler(self.display)
        self.assertEqual(win2, cursor.get_under_window())
        self.client.raise_window()
        sleep(0.2)
        self.assertEqual(self.client, cursor.get_under_window())
        client2.destroy()

    def test_lower_window(self, ):
        """
         +------------------------------+
         |  Window1                     |
         |                              |
         |      +-----------------------------+
         |      |  Window2                    |
         |      |                             |
         |      |                             |
         |      |                             |
         |      |                             |
         |      |                             |
         |      |                             |
         |      |                             |
         +------|                             |
                |                             |
                |                             |
                +-----------------------------+

                       ||
                       \/

         +------------------------------+
         |  Window1                     |
         |                              |
         |                              |-----+
         |                              |     |
         |                              |     |
         |                              |     |
         |                              |     |
         |                              |     |
         |                              |     |
         |                              |     |
         |                              |     |
         +------------------------------+     |
                |                             |
                |  Window2                    |
                +-----------------------------+
        """
        self.client.set_bounds(0, 0, 1000, 1000)
        win2 = window2(self.display)
        client2 = WindowClient(
            self.display, win2)
        client2.set_bounds(250, 250, 1000, 1000)
        self.display.core.WarpPointerChecked(
            0, self.root, 0, 0, 0, 0, 500, 500).check()
        sleep(0.2)
        cursor = CursorHandler(self.display)
        self.assertEqual(win2, cursor.get_under_window())
        client2.lower_window()
        sleep(0.2)
        self.assertEqual(self.client, cursor.get_under_window())
        client2.destroy()

    def _get_state(self, ):
        reply = self.display.core.GetProperty(
            False, self.client, self.atom_cache.get_atom('_NET_WM_STATE'),
            self.atom_cache.get_atom('ATOM'), 0, 100).reply()
        return unpack('I' * reply.value_len, array('B', reply.value).tostring())

    def test_minimize(self, ):
        self.assertNotIn(self.atom_cache.get_atom('_NET_WM_STATE_HIDDEN'),
                         self._get_state())
        self.assertFalse(self.client.is_minimized())
        self.client.minimize()
        sleep(0.2)
        self.assertIn(self.atom_cache.get_atom('_NET_WM_STATE_HIDDEN'),
                      self._get_state())
        self.assertTrue(self.client.is_minimized())

    def test_show(self, ):

        self.client.minimize()
        sleep(0.2)
        self.assertTrue(self.client.is_minimized())
        self.client.show()
        sleep(0.2)
        self.assertFalse(self.client.is_minimized())

    def test_maximize(self, ):
        self.client.set_bounds(0, 0, 500, 500) # do not remove
        states = self._get_state()
        self.assertNotIn(
            self.atom_cache.get_atom('_NET_WM_STATE_MAXIMIZED_VERT'), states)
        self.assertNotIn(
            self.atom_cache.get_atom('_NET_WM_STATE_MAXIMIZED_HORZ'), states)
        self.assertFalse(self.client.is_minimized())
        self.client.maximize()
        sleep(0.5)
        states = self._get_state()
        self.assertIn(
            self.atom_cache.get_atom('_NET_WM_STATE_MAXIMIZED_VERT'), states)
        self.assertIn(
            self.atom_cache.get_atom('_NET_WM_STATE_MAXIMIZED_HORZ'), states)
        self.assertTrue(self.client.is_maximized())

    def test_restore(self, ):
        self.client.set_bounds(0, 0, 500, 500) # do not remove
        self.client.maximize()
        self.client.minimize()
        sleep(0.5)
        self.assertTrue(self.client.is_maximized())
        self.assertTrue(self.client.is_minimized())
        self.client.restore()
        sleep(0.5)
        self.assertFalse(self.client.is_maximized())
        self.assertFalse(self.client.is_minimized())

    def test_activate(self, ):
        win2 = window2(self.display)
        client2 = WindowClient(
            self.display, win2)
        sleep(0.2)
        self.assertNotEqual(self.client, self.root.get_active_window())
        self.client.activate()
        sleep(0.2)
        self.assertEqual(self.client, self.root.get_active_window())
        client2.destroy()

    def test_deactivate(self, ):
        self.skipTest('Not Implemented')

    def test_set_always_on_top(self, ):
        self.client.set_bounds(0, 0, 1000, 1000)
        win2 = window2(self.display)
        client2 = WindowClient(self.display, win2)
        client2.set_bounds(250, 250, 1000, 1000)
        self.display.core.WarpPointerChecked(
            0, self.root, 0, 0, 0, 0, 500, 500).check()
        sleep(0.2)
        cursor = CursorHandler(self.display)
        self.assertFalse(self.client.is_always_on_top())
        self.assertEqual(win2, cursor.get_under_window())
        self.client.set_always_on_top()
        sleep(0.2)
        self.assertEqual(self.client, cursor.get_under_window())
        self.assertTrue(self.client.is_always_on_top())
        client2.raise_window()
        sleep(0.2)
        self.assertEqual(self.client, cursor.get_under_window())
        client2.destroy()

    def test_set_always_on_bottom(self, ):
        self.assertFalse(self.client.is_always_on_bottom())
        self.assertNotIn(self.atom_cache.get_atom('_NET_WM_STATE_BELOW'),
                         self._get_state())
        self.client.set_always_on_bottom()
        sleep(0.2)
        self.assertIn(self.atom_cache.get_atom('_NET_WM_STATE_BELOW'),
                         self._get_state())
        self.assertTrue(self.client.is_always_on_bottom())

    def test_set_fullscreen(self, ):
        self.assertFalse(self.client.is_fullscreened())
        self.assertNotIn(self.atom_cache.get_atom('_NET_WM_STATE_FULLSCREEN'),
                         self._get_state())
        self.client.set_fullscreen()
        sleep(0.2)
        self.assertIn(self.atom_cache.get_atom('_NET_WM_STATE_FULLSCREEN'),
                      self._get_state())
        self.assertTrue(self.client.is_fullscreened())

    def test_set_shade(self, ):
        self.assertFalse(self.client.is_shaded())
        self.assertNotIn(self.atom_cache.get_atom('_NET_WM_STATE_SHADED'),
                         self._get_state())
        self.client.set_shade()
        sleep(0.2)
        self.assertIn(self.atom_cache.get_atom('_NET_WM_STATE_SHADED'),
                      self._get_state())
        self.assertTrue(self.client.is_shaded())

    def test_hide(self, ):
        self.skipTest('Not Implemented')

    def test_close(self, ):
        self.skipTest('Connection error')
        self.assertIn(self.client, self.root.client_list())
        self.client.close()
        sleep(0.2)
        self.assertNotIn(self.client, self.root.client_list())
        self.need_destroy = False

    def test_delete(self, ):
        self.skipTest('Not Implemented')

    def test_destroy(self, ):
        self.skipTest('Not Implemented')

    def test_move_cursor_to(self, ):
        self.skipTest('Not Implemented')

    def test_query_pointer(self, ):
        self.skipTest('Not Implemented')

    def test_get_cursor_point(self, ):
        self.skipTest('Not Implemented')

    def test_grab_key(self, ):
        self.skipTest('Not Implemented')

    def test_grab_keys(self, ):
        self.skipTest('Not Implemented')

    def test_ungrab_key(self, ):
        self.skipTest('Not Implemented')

    def test_ungrab_keys(self, ):
        self.skipTest('Not Implemented')

    def test_grab_button(self, ):
        self.skipTest('Not Implemented')

    def test_grab_buttons(self, ):
        self.skipTest('Not Implemented')

    def test_ungrab_button(self, ):
        self.skipTest('Not Implemented')

    def test_ungrab_buttons(self, ):
        self.skipTest('Not Implemented')

    def tearDown(self):
        if self.need_destroy:
            self.client.destroy()

    @classmethod
    def tearDownClass(cls, ):
        pass


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_window_client.py ends here
