#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_desktop_root_window.py

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

import xcb, xcb.xproto
# from xahk.desktop_root_window import DesktopRootWindow


# class TestMultiton(MockerTestCase):
#     @classmethod
#     def setUpClass(cls):
#         pass

#     def setUp(self):
#         self.display1 = xcb.connect()
#         self.display2 = xcb.connect()
#         self.mocker.replay()

#     def test_multition_display(self, ):
#         self.assertEqual(id(DesktopRootWindow(self.display1)),
#                          id(DesktopRootWindow(self.display1)))
#         self.assertNotEqual(id(DesktopRootWindow(self.display1)),
#                             id(DesktopRootWindow(self.display2)))
#         self.assertEqual(id(DesktopRootWindow(self.display2)),
#                          id(DesktopRootWindow(self.display2)))

#     def tearDown(self):
#         pass

#     @classmethod
#     def tearDownClass(cls, ):
#         pass


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_desktop_root_window.py ends here
