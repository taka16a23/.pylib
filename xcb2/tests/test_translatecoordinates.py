#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_translatecoordinates.py

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
from xcb2.xproto import TranslateCoordinatesCookie
from xcb2.xproto.ext import TranslateCoordinates, TranslateCoordinatesUnchecked


class TestTranslateCoordinatesBinary(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.args1 = [(67108867, 482, 0, 0),
                      '\x00\x00\x00\x00\x03\x00\x00\x04'
                      '\xe2\x01\x00\x00\x00\x00\x00\x00']
        cls.args2 = [(67108867, 482, 10, 10),
                      '\x00\x00\x00\x00\x03\x00\x00\x04'
                      '\xe2\x01\x00\x00\n\x00\n\x00']
        cls.args3 = [(99999999, 482, 0, 0),
                      '\x00\x00\x00\x00\xff\xe0\xf5\x05'
                      '\xe2\x01\x00\x00\x00\x00\x00\x00']
        cls.conn = xcb.connect()
        cls.protocol = TranslateCoordinates(cls.conn)
        cls.protocol_check = TranslateCoordinatesUnchecked(cls.conn)

    def setUp(self):
        self.conn.flush()
        self.mocker.replay()

    def test_binary1(self):
        r"""Test TranslateCoordinates binary1."""
        binary = self.protocol._getbinary(*self.args1[0])
        self.assertEqual(self.args1[1], binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._getbinary,
                                 str(self.args1[0])
                                 .replace('(', '').replace(')', ''),
                                 repr(self.args1[1]), repr(binary)))

    def test_binary2(self):
        r"""Test TranslateCoordinates binary2."""
        binary2 = self.protocol._getbinary(*self.args2[0])
        self.assertEqual(self.args2[1], binary2,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._getbinary,
                                 str(self.args2[0])
                                 .replace('(', '').replace(')', ''),
                                 repr(self.args2[1]), repr(binary2)))

    def test_binary3(self):
        r"""Test TranslateCoordinates binary3."""
        binary3 = self.protocol._getbinary(*self.args3[0])
        self.assertEqual(self.args3[1], binary3,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._getbinary,
                                 str(self.args3[0])
                                 .replace('(', '').replace(')', ''),
                                 repr(self.args3[1]), repr(binary3)))

    def tearDown(self):
        self.conn.flush()

    @classmethod
    def tearDownClass(cls, ):
        cls.conn.flush()
        cls.conn.disconnect()


class TestTranslateCoordinatesRequest(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.argsbin = [(67108867, 482, 0, 0),
                      '\x00\x00\x00\x00\x03\x00\x00\x04'
                      '\xe2\x01\x00\x00\x00\x00\x00\x00']
        cls.conn = xcb.connect()
        cls.protocol = TranslateCoordinates(cls.conn)
        cls.protocol_check = TranslateCoordinatesUnchecked(cls.conn)
        cls.cookie = TranslateCoordinatesCookie

    def setUp(self):
        self.conn.flush()
        self.mocker.replay()

    def test_call(self):
        r"""Test TranslateCoordinates.__call__() expect return
        TranslateCoordinatesCookie."""
        cookie = self.protocol(*self.argsbin[0])
        self.assertIsInstance(cookie, TranslateCoordinatesCookie,
                              msg='Failed: {0}({1}) not returned'
                              ' TranslateCoordinatesCookie\ngot: {2}'
                              .format(self.protocol.__class__.__name__,
                                      str(self.argsbin[0])
                                      .replace('(', '').replace(')', ''),
                                      cookie))

    def test_request(self, ):
        r"""Test TranslateCoordinates.request() expect return
        TranslateCoordinatesCookie."""
        cookie = self.protocol.request(self.argsbin[1])
        self.assertIsInstance(cookie, TranslateCoordinatesCookie,
                              msg='Failed: {0}.request("{1}") not return'
                              ' TranslateCoordinatesCookie\ngot: {2}'
                              .format(self.protocol.__class__.__name__,
                                      self.argsbin[1], cookie))

    def test_checkedrequest(self, ):
        r"""Test TranslateCoordinates.request() expect return
        TranslateCoordinatesCookie."""
        cookie = self.protocol_check.request(self.argsbin[1])
        self.assertIsInstance(cookie, TranslateCoordinatesCookie,
                              msg='Failed: {0}.request("{1}") not return'
                              ' TranslateCoordinatesCookie\ngot: {2}'
                              .format(self.protocol_check.__class__.__name__,
                                      self.argsbin[1], cookie))

    def tearDown(self):
        self.conn.flush()

    @classmethod
    def tearDownClass(cls, ):
        cls.conn.flush()
        cls.conn.disconnect()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_translatecoordinates.py ends here
