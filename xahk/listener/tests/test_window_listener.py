#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_window_listener.py

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

from xcb import xproto
from xcb.xproto import PropMode

from rectangle import Rectangle

from xahk.wm.display import Display
from xahk.events.eventloop import EventLoop
from xahk.listener._window_listener import WindowListener
from xahk.listener import WindowListenerFactory
from xahk.wm.window_client import WindowClient


def simple_teswindow(display, x, y, width, height, title=''):
    r"""SUMMARY
    simple_teswindow(c, 100,100,1000,1000)
    simple_teswindow()

    @Return:
    """
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
    client = WindowClient(display, window)
    client.set_title(title)
    client.set_bounds(Rectangle(x, y, width, height))
    return client


def window2(display):
    return simple_teswindow(display, 250, 250, 500, 500, 'window2')


class TestWindowListener(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.eventloop = EventLoop(Display())
        cls.display = cls.eventloop.get_display()
        cls.factory = WindowListenerFactory(cls.display)

    def setUp(self):
        self.windowbase = simple_teswindow(
            self.display, 0, 0, 500, 500, 'window')
        sleep(0.2)
        self._process_events()
        windows = WindowListenerFactory(self.display).list_windows()
        self.window = None
        for window in windows:
            if window == self.windowbase:
                self.window = window
        if self.window is None:
            raise StandardError()
        self.need_destroy = True
        self.mocker.replay()

    def _process_events(self, ):
        self.display.flush()
        self.eventloop._load_events()
        self.eventloop.dispatch_events()

    def test_get_id(self, ):
        self.assertEqual(self.windowbase.get_id(), self.window.get_id())

    def test_get_title(self, ):
        self.assertNotIn('title', self.window._prop_cache)
        self.assertEqual(self.windowbase.get_title(), self.window.get_title())
        self.assertEqual(self.windowbase.get_title(), self.window.title)
        self.assertIn('title', self.window._prop_cache)
        self.assertEqual(
            self.windowbase.get_title(), self.window._prop_cache['title'])
        expects = 'newtitle'
        self.window.set_title(expects)
        sleep(0.2)
        self._process_events()
        self.assertEqual(self.windowbase.get_title(), self.window.get_title())
        self.assertEqual(
            self.windowbase.get_title(), self.window._prop_cache['title'])

    def test_get_wmclass(self, ):
        self.assertNotIn('wmclass', self.window._prop_cache)
        self.assertEqual(
            self.windowbase.get_wmclass(), self.window.get_wmclass())
        self.assertEqual(
            self.windowbase.get_wmclass(), self.window.wmclass)
        self.assertIn('wmclass', self.window._prop_cache)
        self.assertEqual(
            self.windowbase.get_wmclass(), self.window._prop_cache['wmclass'])
        wmclass = 'test\x00test2\x00'
        self.windowbase.change_property(
            PropMode.Replace, 'WM_CLASS', 'STRING', 8, len(wmclass), wmclass)
        expects = ['test', 'test2']
        sleep(0.2)
        self._process_events()
        self.assertEqual(expects, self.window.get_wmclass())
        self.assertEqual(expects, self.window._prop_cache['wmclass'])

    def test_get_pid(self, ):
        self.assertNotIn('pid', self.window._prop_cache)
        self.assertEqual(self.windowbase.get_pid(), self.window.get_pid())
        self.assertEqual(self.windowbase.get_pid(), self.window.pid)
        self.assertIn('pid', self.window._prop_cache)
        self.assertEqual(
            self.windowbase.get_pid(), self.window._prop_cache['pid'])
        self.windowbase.change_property(
            PropMode.Replace, '_NET_WM_PID', 'CARDINAL', 32,
            1, '\xea\x0c\x00\x00')
        expects = 3306
        sleep(0.2)
        self._process_events()
        self.assertEqual(expects, self.window.get_pid())
        self.assertEqual(expects, self.window._prop_cache['pid'])

    def test_get_type(self, ):
        self.assertNotIn('type', self.window._prop_cache)
        self.assertEqual(self.windowbase.get_type(), self.window.get_type())
        self.assertEqual(self.windowbase.get_type(), self.window.type)
        self.assertIn('type', self.window._prop_cache)
        self.assertEqual(
            self.windowbase.get_type(), self.window._prop_cache['type'])
        self.windowbase.change_property(
            PropMode.Replace, '_NET_WM_WINDOW_TYPE', 'ATOM', 32,
            1, '2\x01\x00\x00')
        expects = 306
        sleep(0.2)
        self._process_events()
        self.assertEqual(expects, self.window.get_type())
        self.assertEqual(expects, self.window._prop_cache['type'])

    def test_get_bounds(self, ):
        self.skipTest('')
        self.assertNotIn('bounds', self.window._prop_cache)
        self.assertEqual(self.windowbase.get_bounds(), self.window.get_bounds())
        self.assertIn('bounds', self.window._prop_cache)
        self.assertEqual(
            self.windowbase.get_bounds(), self.window._prop_cache['bounds'])
        from rectangle import Rectangle
        expects = Rectangle(100, 100, 200, 200)
        self.assertNotEqual(self.windowbase.get_bounds(), expects)
        self.window.set_bounds(expects)
        sleep(0.2)
        self._process_events()
        self.assertEqual(self.windowbase.get_bounds(), expects)
        print(self.windowbase.get_bounds())
        self.assertEqual(expects, self.window._prop_cache['bounds'])

    def test_move(self, ):
        expectx, expecty = 150, 250
        point = self.window.get_bounds().get_location()
        self.assertNotEqual([expectx, expecty], [point.get_x(), point.get_y()])
        self.window.move(expectx, expecty)
        sleep(0.2)
        self._process_events()
        point2 = self.window.get_bounds().get_location()
        self.assertEqual([expectx, expecty], [point2.get_x(), point2.get_y()])

    def test_set_size(self, ):
        expectw, expecth = 150, 250
        size = self.window.get_bounds().get_size()
        self.assertNotEqual(
            [expectw, expecth], [size.get_width(), size.get_height()])
        self.window.set_size(expectw, expecth)
        sleep(0.2)
        self._process_events()
        size2 = self.window.get_bounds().get_size()
        self.assertEqual(
            [expectw, expecth], [size2.get_width(), size2.get_height()])

    def test_minimize(self, ):
        self.assertFalse(self.window.is_minimized())
        self.window.minimize()
        sleep(0.2)
        self.assertTrue(self.window.is_minimized())

    def test_show(self, ):
        self.skipTest('Not Implemented')

    def test_maximize(self, ):
        self.assertFalse(self.window.is_maximized())
        self.window.maximize()
        sleep(0.2)
        self.assertTrue(self.window.is_maximized())

    def test_restore(self, ):
        self.skipTest('Not Implemented')

    def test_activate(self, ):
        self.skipTest('Not Implemented')

    def test_is_active(self, ):
        self.skipTest('Not Implemented')

    def test_deactivate(self, ):
        self.skipTest('Not Implemented')

    def test_set_always_on_top(self, ):
        self.assertFalse(self.window.is_always_on_top())
        self.window.set_always_on_top()
        sleep(0.2)
        self.assertTrue(self.window.is_always_on_top())

    def test_set_always_on_bottom(self, ):
        self.assertFalse(self.window.is_always_on_bottom())
        self.window.set_always_on_bottom()
        sleep(0.2)
        self.assertTrue(self.window.is_always_on_bottom())

    def test_set_fullscreen(self, ):
        self.assertFalse(self.window.set_fullscreen())
        self.window.set_always_on_bottom()
        sleep(0.2)
        self.assertTrue(self.window.is_fullscreened())

    def test_hide(self, ):
        self.skipTest('Not Implemented')

    def test_set_shade(self, ):
        self.assertFalse(self.window.set_shade())
        self.window.set_always_on_bottom()
        sleep(0.2)
        self.assertTrue(self.window.is_shaded())

    def test_close(self, ):
        self.skipTest('TODO')
        windows = WindowListenerFactory(self.display).list_windows()
        self.assertIn(self.window.get_id(), windows)
        self.window.close()
        sleep(0.2)
        self._process_events()
        windows = WindowListenerFactory(self.display).list_windows()
        self.assertNotIn(self.window.get_id(), windows)

    def test_delete(self, ):
        self.skipTest('TODO')
        windows = WindowListenerFactory(self.display).list_windows()
        self.assertIn(self.window.get_id(), windows)
        self.window.delete()
        sleep(0.2)
        self._process_events()
        windows = WindowListenerFactory(self.display).list_windows()
        self.assertNotIn(self.window.get_id(), windows)

    def test_destroy(self, ):
        windows = WindowListenerFactory(self.display).list_windows()
        self.assertIn(self.window.get_id(), windows)
        self.window.destroy()
        self.need_destroy = False
        sleep(0.2)
        self._process_events()
        windows = WindowListenerFactory(self.display).list_windows()
        self.assertNotIn(self.window.get_id(), windows)

    def test_move_cursor_to(self, ):
        expectx, expecty = 10, 20
        self.window.move_cursor_to(expectx, expecty)
        sleep(0.2)
        point = self.window.get_cursor_point()
        self.assertEqual([expectx, expecty], [point.get_x(), point.get_y()])

    def test_raise_window(self, ):
        self.skipTest('Not Implemented')

    def test_lower_window(self, ):
        self.skipTest('Not Implemented')

    def test_get_workspace(self, ):
        self.skipTest('Not Implemented')

    def test_change_workspace(self, ):
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
            self.window.destroy()

    @classmethod
    def tearDownClass(cls, ):
        pass


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_window_listener.py ends here
