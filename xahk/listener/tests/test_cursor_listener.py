#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_desktop_cursor.py

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

import xcb
from xcb import xproto

from xahk.listener import CursorListener
from xahk.listener import CursorListenerObserver
from xahk.events.eventloop import EventLoop
from rectangle import Rectangle
from xahk.wm.window_client import WindowClient
from xahk.wm.display import Display


conn = Display()
stup = conn.get_setup()
root = stup.roots[0].root


def simple_teswindow(display, x, y, width, height, title=''):
    r"""SUMMARY
    simple_teswindow(c, 100,100,1000,1000)
    simple_teswindow()

    @Return:
    """
    # setup = display.get_setup()
    # root = setup.roots[0].root
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


def window1(display):
    return simple_teswindow(display, 0, 0, 1000, 1000, 'window1')

def window2(display):
    return simple_teswindow(display, 250, 250, 500, 500, 'window2')

def window3(display):
    return simple_teswindow(display, 500, 500, 350, 350, 'window3')


class CursorListenerObserverCalledCheck(CursorListenerObserver):
    r"""CursorListenerObserverCalledCheck

    CursorListenerObserverCalledCheck is a CursorListenerObserver.
    Responsibility:
    """
    def __init__(self, ):
        r"""
        """
        self._under_window = None

    def on_changed_under_window(self, cursor_listener):
        r"""SUMMARY

        on_changed_under_window()

        @Return:

        @Error:
        """
        self._under_window = cursor_listener.get_under_window()

    def under_window(self, ):
        r"""SUMMARY

        is_called()

        @Return:

        @Error:
        """
        return self._under_window


class TestUpdateUnderWindowBase(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.eventloop = EventLoop(conn)
        cls.display =   cls.eventloop.get_display()
        cls.root = root
        cls._cursor = CursorListener(cls.display)
        cls.observer = CursorListenerObserverCalledCheck()
        cls._cursor.add_observer(cls.observer)
        cls.window1 = window1(cls.display)

    def _process_events(self, ):
        self.display.flush()
        self.eventloop._load_events()
        self.eventloop.dispatch_events()

    @classmethod
    def tearDownClass(cls, ):
        cls.window1.destroy()
        # cls.display.disconnect()


class TestUpdateUnderWindowEnterWindow2FromWindow1(TestUpdateUnderWindowBase):
    """2015/07/13
    Mouse cursor move to Window2 from Window1.
    X is Cursor start point.
    +----------------------------------------------------+
    | Window 1                                           |
    |                                                    |
    |                                                    |
    |           +----------------------------+           |
    |           | Window 2                   |           |
    |           |                            |           |
    |           |                            |           |
    |           |                            |           |
    |           |                 <----------+------X    |
    |           |                            |    Cursor |
    |           |                            |           |
    |           |                            |           |
    |           |                            |           |
    |           |                            |           |
    |           |                            |           |
    |           +----------------------------+           |
    |                                                    |
    |                                                    |
    |                                                    |
    +----------------------------------------------------+
    """
    def setUp(self):
        self.window2 = window2(self.display)
        self._destroyed = False
        self.display.core.WarpPointerChecked(
            0, self.root, 0, 0, 0, 0, 900, 500).check() # set X point
        self.display.flush()
        self._process_events()
        sleep(0.5)
        self.mocker.replay()

    def test_enter_in_window2(self, ):
        self.assertEqual(
            self._cursor.get_under_window().get_id(),
            self.window1.get_id())
        self.display.core.WarpPointerChecked(
            0, self.root, 0, 0, 0, 0, 500, 500).check() # enter in window2
        self._process_events()
        self.assertEqual(self._cursor.get_under_window().get_id(),
                         self.window2.get_id())
        self.assertTrue(self._cursor.is_under_window(self.window2))

    def test_observer(self, ):
        self.assertEqual(
            self._cursor.get_under_window().get_id(),
            self.window1.get_id())
        self.display.core.WarpPointerChecked(
            0, self.root, 0, 0, 0, 0, 500, 500).check() # enter in window2
        self._process_events()
        self.assertEqual(self.observer.under_window(),
                         self.window2.get_id())
        self.assertTrue(self._cursor.is_under_window(self.window2))

    # def _destroy_subwindow(self, ):
    #     if self._destroyed:
    #         return
    #     self.window2.destroy()
    #     self._destroyed = True

    def tearDown(self):
        self.window2.destroy()


class TestUpdateUnderWindowEnterWindow1FromWindow2(TestUpdateUnderWindowBase):
    """2015/07/19
    +----------------------------------------------------+
    | Window 1                                           |
    |                                                    |
    |                                                    |
    |           +----------------------------+           |
    |           | Window 2                   |           |
    |           |                            |           |
    |           |                            |           |
    |           |                            |           |
    |           |                 X----------+------>    |
    |           |               Cursor       |           |
    |           |                            |           |
    |           |                            |           |
    |           |                            |           |
    |           |                            |           |
    |           |                            |           |
    |           +----------------------------+           |
    |                                                    |
    |                                                    |
    |                                                    |
    +----------------------------------------------------+
    """
    def setUp(self):
        self.window2 = window2(self.display)
        self._destroyed = False
        self.display.core.WarpPointerChecked(
            0, self.root, 0, 0, 0, 0, 500, 500).check() # set X point
        self.display.flush()
        self._process_events()
        sleep(0.5)
        self.mocker.replay()

    def test_enter_in_window1(self, ):
        r"""SUMMARY

        test_enter_in_window1()

        @Return:

        @Error:
        """
        self.assertEqual(self._cursor.get_under_window().get_id(),
                         self.window2.get_id())
        self.display.core.WarpPointerChecked(
            0, self.root, 0, 0, 0, 0, 900, 500).check()
        self.display.flush()
        self._process_events()
        self.assertEqual(self._cursor.get_under_window().get_id(),
                         self.window1.get_id())
        self.assertTrue(self._cursor.is_under_window(self.window1))

    def tearDown(self):
        self.window2.destroy()


class TestUpdateUnderWindowUnmapWindow2(TestUpdateUnderWindowBase):
    """2015/07/19
    Window2 Destroyed
    Window2 Minimized

    +----------------------------------------------------+
    | Window 1                                           |
    |                                                    |
    |                                                    |
    |           +----------------------------+           |
    |           | Window 2                   |           |
    |           |                            |           |
    |           |                            |           |
    |           |                            |           |
    |           |                            |           |
    |           |               X            |           |
    |           |             Cursor         |           |
    |           |                            |           |
    |           |                            |           |
    |           |                            |           |
    |           +----------------------------+           |
    |                                                    |
    |                                                    |
    |                                                    |
    +----------------------------------------------------+

                             ||
                             \/

    +----------------------------------------------------+
    | Window 1                                           |
    |                                                    |
    |                                                    |
    |                                                    |
    |                                                    |
    |                                                    |
    |                                                    |
    |                                                    |
    |                                                    |
    |                           X                        |
    |                         Cursor                     |
    |                                                    |
    |                                                    |
    |                                                    |
    |                                                    |
    |                                                    |
    |                                                    |
    |                                                    |
    +----------------------------------------------------+
    """
    def setUp(self):
        self.window2 = window2(self.display)
        self._destroyed = False
        self.display.core.WarpPointerChecked(
            0, self.root, 0, 0, 0, 0, 500, 500).check() # set X point
        self.display.flush()
        self._process_events()
        sleep(0.5)
        self.mocker.replay()

    def test_destroy_window2(self, ):
        self.assertEqual(self._cursor.get_under_window().get_id(),
                         self.window2.get_id())
        self.window2.destroy()
        sleep(0.3)
        self._process_events()
        self.assertEqual(
            self._cursor.get_under_window().get_id(),
            self.window1.get_id())
        self.assertTrue(self._cursor.is_under_window(self.window1))

    def test_minimize_window2(self, ):
        self.assertEqual(self._cursor.get_under_window().get_id(),
                         self.window2.get_id())
        self.window2.minimize()
        sleep(0.3)
        self._process_events()
        self.assertEqual(
            self._cursor.get_under_window().get_id(),
            self.window1.get_id())
        self.assertTrue(self._cursor.is_under_window(self.window1))

    def tearDown(self):
        pass


class TestUpdateUnderWindowMapWindow2(TestUpdateUnderWindowBase):
    """2015/07/19
    +----------------------------------------------------+
    | Window 1                                           |
    |                                                    |
    |                                                    |
    |                                                    |
    |                                                    |
    |                                                    |
    |                                                    |
    |                                                    |
    |                                                    |
    |                           X                        |
    |                         Cursor                     |
    |                                                    |
    |                                                    |
    |                                                    |
    |                                                    |
    |                                                    |
    |                                                    |
    |                                                    |
    |                                                    |
    +----------------------------------------------------+

                             ||
                             \/

    +----------------------------------------------------+
    | Window 1                                           |
    |                                                    |
    |                                                    |
    |           +----------------------------+           |
    |           | Window 2                   |           |
    |           |                            |           |
    |           |                            |           |
    |           |                            |           |
    |           |                            |           |
    |           |               X            |           |
    |           |             Cursor         |           |
    |           |                            |           |
    |           |                            |           |
    |           |                            |           |
    |           |                            |           |
    |           +----------------------------+           |
    |                                                    |
    |                                                    |
    |                                                    |
    +----------------------------------------------------+
    """
    def setUp(self):
        self.window2 = None
        self.display.core.WarpPointerChecked(
            0, self.root, 0, 0, 0, 0, 500, 500).check() # set X point
        self.display.flush()
        self._process_events()
        self.mocker.replay()

    def test_create_window2(self, ):
        self.assertEqual(
            self._cursor.get_under_window().get_id(),
            self.window1.get_id())
        self.window2 = window2(self.display)
        self._process_events()
        self.assertEqual(
            self._cursor.get_under_window().get_id(),
            self.window2.get_id())
        self.assertTrue(self._cursor.is_under_window(self.window2))

    # TODO: (Atami) [2015/07/20]
    # WindowClient.show imprement
    # def test_map_window(self, ):
    #     self.window2 = window2(self.display)
    #     sleep(3)
    #     self.window2.minimize()
    #     self.display.flush()
    #     sleep(3)
    #     self._process_events()
    #     self.assertEqual(
    #         self._cursor.get_under_window().get_id(),
    #         self.window1.get_id())
    #     self.window2.show()
    #     sleep(3)
    #     self._process_events()
    #     self.assertEqual(
    #         self._cursor.get_under_window().get_id(),
    #         self.window2.get_id())
    #     self.assertTrue(self.window2)

    def tearDown(self):
        if not self.window2 is None:
            self.window2.destroy()


class TestUpdateUnderWindowFlowupWindow3(TestUpdateUnderWindowBase):
    """2015/07/19
    +----------------------------------------------------+
    | Window1                                            |
    |                                                    |
    |                                                    |
    |           +----------------------------+           |
    |           | Window 2                   |           |
    |           |                            |           |
    |           |                            |----+      |
    |           |                            |    |      |
    |           |                            |    |      |
    |           |               X            |    |      |
    |           |             Cursor         |    |      |
    |           |                            |    |      |
    |           |                            |    |      |
    |           |                            |    |      |
    |           +----------------------------+    |      |
    |                     |                       |      |
    |                     +-----------------------+      |
    |                                                    |
    +----------------------------------------------------+

                             ||
                             \/

    +----------------------------------------------------+
    | Window 1                                           |
    |                                                    |
    |                                                    |
    |           +----------------------------+           |
    |           | Window 2                   |           |
    |           |                            |           |
    |           |         +-----------------------+      |
    |           |         | Window 3              |      |
    |           |         |                       |      |
    |           |         |     X                 |      |
    |           |         |   Cursor              |      |
    |           |         |                       |      |
    |           |         |                       |      |
    |           |         |                       |      |
    |           +---------|                       |      |
    |                     |                       |      |
    |                     +-----------------------+      |
    |                                                    |
    +----------------------------------------------------+
    """
    def setUp(self):
        self.window3 = window3(self.display)
        self.window2 = window2(self.display)
        self._destroyed = False
        self.display.core.WarpPointerChecked(
            0, self.root, 0, 0, 0, 0, 600, 600).check() # set X point
        self.display.flush()
        self._process_events()
        sleep(0.5)
        self.mocker.replay()

    def test_flowup_window3(self, ):
        self.assertEqual(
            self._cursor.get_under_window().get_id(),
            self.window2.get_id())
        self.window3.raise_window()
        sleep(0.5)
        self.display.flush()
        self._process_events()
        sleep(0.5)
        self.assertEqual(
            self._cursor.get_under_window().get_id(),
            self.window3.get_id())
        self.assertTrue(self._cursor.is_under_window(self.window3))

    def tearDown(self):
        self.window2.destroy()
        self.window3.destroy()


# TODO: (Atami) [2015/07/20]
class TestUpdateUnderWindowFlowdownWindow3(TestUpdateUnderWindowBase):
    """2015/07/19
    +----------------------------------------------------+
    | Window 1                                           |
    |                                                    |
    |                                                    |
    |           +----------------------------+           |
    |           | Window 2                   |           |
    |           |                            |           |
    |           |         +-----------------------+      |
    |           |         | Window 3              |      |
    |           |         |                       |      |
    |           |         |     X                 |      |
    |           |         |   Cursor              |      |
    |           |         |                       |      |
    |           |         |                       |      |
    |           |         |                       |      |
    |           +---------|                       |      |
    |                     |                       |      |
    |                     +-----------------------+      |
    |                                                    |
    +----------------------------------------------------+

                             ||
                             \/

    +----------------------------------------------------+
    | Window 1                                           |
    |                                                    |
    |                                                    |
    |           +----------------------------+           |
    |           | Window 2                   |           |
    |           |                            |           |
    |           |                            |----+      |
    |           |                            |    |      |
    |           |                            |    |      |
    |           |               X            |    |      |
    |           |             Cursor         |    |      |
    |           |                            |    |      |
    |           |                            |    |      |
    |           |                            |    |      |
    |           +----------------------------+    |      |
    |                     |                       |      |
    |                     +-----------------------+      |
    |                                                    |
    +----------------------------------------------------+
    """
    def setUp(self):
        self.window2 = window2(self.display)
        self.window3 = window3(self.display)
        self._destroyed = False
        self.display.core.WarpPointerChecked(
            0, self.root, 0, 0, 0, 0, 600, 600).check() # set X point
        self.display.flush()
        self._process_events()
        sleep(0.5)
        self.mocker.replay()

    def test_flowdown_window3(self, ):
        self.assertEqual(
            self._cursor.get_under_window().get_id(),
            self.window3.get_id())
        self.window3.lower_window()
        sleep(0.5)
        self.display.flush()
        self._process_events()
        sleep(0.5)
        under = self._cursor.get_under_window().get_id()
        self.assertEqual(
            under,
            self.window2.get_id(), '{},{},{},{}'.format(
                self.window1.id, self.window2.id, self.window3.id, under))
        self.assertTrue(self._cursor.is_under_window(self.window2))

    def tearDown(self):
        self.window2.destroy()
        self.window3.destroy()


class TestCursorListener(MockerTestCase):
    """2015/07/20"""
    @classmethod
    def setUpClass(cls):
        cls.cursor = CursorListener(conn)
        cls.display = conn
        cls.root = root

    def setUp(self):
        self.mocker.replay()

    def test_move_cursor_to(self):
        self.display.core.WarpPointerChecked(
            0, self.root, 0, 0, 0, 0, 0, 0).check()
        pointer = self.display.core.QueryPointer(self.root).reply()
        self.assertEqual((0, 0), (pointer.root_x, pointer.root_y))
        expectx, expecty = 10, 100
        self.cursor.move_cursor_to(expectx, expecty)
        pointer2 = self.display.core.QueryPointer(self.root).reply()
        self.assertEqual((expectx, expecty), (pointer2.root_x, pointer2.root_y))

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        pass





# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_desktop_cursor.py ends here
