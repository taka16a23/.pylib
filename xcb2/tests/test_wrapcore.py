#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_wrapcore.py

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
import xcb2
from inspect import getargspec


class TestWrapCore(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.xcbcon = xcb.connect()
        cls.xcb2con = xcb2.connect()

    def setUp(self):
        self.xcbcon.flush()
        self.xcb2con.flush()
        self.mocker.replay()

    def test_coreattributes(self):
        for name in dir(self.xcbcon.core):
            if name.startswith('_') or not name[0].isupper():
                continue
            self.assertTrue(hasattr(self.xcb2con.core, name),
                            msg='Failed: "{}" has not attribute.'.format(name))

    def test_coremethod_argspec(self, ):
        for name in dir(self.xcbcon.core):
            if name.startswith('_') or not name[0].isupper():
                continue
            xcbmethod = getattr(self.xcbcon.core, name)
            xcb2method = getattr(self.xcb2con.core, name)
            xcbspec = getargspec(xcbmethod)
            xcbspec.args.remove('self')
            xcb2spec = getargspec(xcb2method.__call__)
            xcb2spec.args.remove('self')
            self.assertEqual(xcbspec, xcb2spec,
                             msg='Failed: "{}" not equal argspec "{}" and "{}"'
                             .format(name, xcbspec, xcb2spec))

    def tearDown(self):
        self.xcbcon.flush()
        self.xcb2con.flush()

    @classmethod
    def tearDownClass(cls, ):
        cls.xcbcon.flush()
        cls.xcbcon.disconnect()
        cls.xcb2con.flush()
        cls.xcb2con.disconnect()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_wrapcore.py ends here
