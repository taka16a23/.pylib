#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_window_listener_factory.py

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

from xahk.wm.display import Display
from xahk.wm.window_client import WindowClient
from xahk.events.eventloop import EventLoop
from xahk.listener import WindowListenerFactory

from rectangle import Rectangle


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


class TestWindowListenerFactory(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.eventloop = EventLoop(Display())
        cls.display = cls.eventloop.get_display()
        cls.factory = WindowListenerFactory(cls.display)

    def _process_events(self, ):
        self.display.flush()
        self.eventloop._load_events()
        self.eventloop.dispatch_events()

    def setUp(self):
        self.mocker.replay()

    def test_create_destroy_window(self, ):
        self._process_events()
        win = simple_teswindow(self.display, 0, 0, 100, 100)
        sleep(0.2)
        self._process_events()
        self.assertIn(win, self.factory.list_windows())
        win.destroy()
        sleep(0.2)
        self._process_events()
        self.assertNotIn(win, self.factory.list_windows())

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        pass



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_window_listener_factory.py ends here
