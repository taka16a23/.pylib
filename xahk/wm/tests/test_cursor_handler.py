#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_cursor_handler.py

['skipTest', ]

['assertAlmostEqual', 'assertAlmostEquals', 'assertApproximates',
 'assertDictContainsSubget', 'assertDictEqual', 'assertEndsWith', 'assertEqual',
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

from xahk.wm.cursor_handler import CursorHandler
from xahk.wm.display import Display


class TestCursorHandler(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.display = Display()
        cls.root = cls.display.get_setup().roots[0].root

    def setUp(self):
        self.cursor = CursorHandler(self.display)
        self.mocker.replay()

    def test_move_cursor_to(self, ):
        self.display.core.WarpPointerChecked(
            0, self.root, 0, 0, 0, 0, 0, 0).check()
        pointer = self.display.core.QueryPointer(self.root).reply()
        self.assertEqual((0, 0), (pointer.root_x, pointer.root_y))
        expectx, expecty = 10, 100
        self.cursor.move_cursor_to(expectx, expecty)
        sleep(0.1)
        pointer2 = self.display.core.QueryPointer(self.root).reply()
        self.assertEqual((expectx, expecty), (pointer2.root_x, pointer2.root_y))

    def test_get_point(self, ):
        expectx, expecty = 100, 200
        self.display.core.WarpPointerChecked(
            0, self.root, 0, 0, 0, 0, expectx, expecty).check()
        point = self.cursor.get_point()
        self.assertEqual((expectx, expecty), (point.get_x(), point.get_y()))

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        pass


def simple_teswindow(display, x, y, width, height, title=''):
    r"""SUMMARY
    simple_teswindow(c, 100,100,1000,1000)
    simple_teswindow()

    @Return:
    """
    from xcb import xproto
    from rectangle import Rectangle
    from xahk.wm.window_client import WindowClient
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


def window1(display):
    return simple_teswindow(display, 0, 0, 1000, 1000, 'window1')

def window2(display):
    return simple_teswindow(display, 250, 250, 500, 500, 'window2')


class TestCursorHandler_get_under_window(MockerTestCase):
    """2015/07/21"""
    @classmethod
    def setUpClass(cls):
        cls.display = Display()
        cls.root = cls.display.get_setup().roots[0].root
        cls.window1 = window1(cls.display)

    def setUp(self):
        self.cursor = CursorHandler(self.display)
        self.mocker.replay()

    def test_get_under_window(self):
        """2015/07/21
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
        self.display.core.WarpPointerChecked(
            0, self.root, 0, 0, 0, 0, 500, 500).check()
        sleep(0.2)
        self.assertEqual(self.window1, self.cursor.get_under_window())
        win2 = window2(self.display)
        sleep(0.2)
        self.assertEqual(win2, self.cursor.get_under_window())
        win2.destroy()
        sleep(0.2)
        self.assertEqual(self.window1, self.cursor.get_under_window())

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        cls.window1.destroy()





# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_cursor_handler.py ends here
