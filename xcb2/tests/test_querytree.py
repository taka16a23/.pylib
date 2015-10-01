#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_querytree.py

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
from xcb2.xproto import QueryTreeCookie
from xcb2.xproto.wcookie import WrapQueryTreeCookie
from xcb2.xproto.ext import QueryTree, QueryTreeUnchecked
from xcb2.xobj import Window


class TestQueryTreeBinary(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.args1 = [(77777777, ), '\x00\x00\x00\x00q\xcb\xa2\x04']
        cls.args2 = [(99999999, ), '\x00\x00\x00\x00\xff\xe0\xf5\x05']
        cls.args3 = [(482, ), '\x00\x00\x00\x00\xe2\x01\x00\x00']
        cls.conn = xcb.connect()
        cls.protocol = QueryTree(cls.conn)
        cls.protocol_check = QueryTreeUnchecked(cls.conn)

    def setUp(self):
        self.conn.flush()
        self.mocker.replay()

    def test_binary1(self):
        r"""Test QueryTree binary1."""
        binary = self.protocol._getbinary(*self.args1[0])
        self.assertEqual(self.args1[1], binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._getbinary,
                                 str(self.args1[0])
                                 .replace('(', '').replace(')', ''),
                                 repr(self.args1[1]), repr(binary)))

    def test_binary2(self):
        r"""Test QueryTree binary2."""
        binary2 = self.protocol._getbinary(*self.args2[0])
        self.assertEqual(self.args2[1], binary2,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._getbinary,
                                 str(self.args2[0])
                                 .replace('(', '').replace(')', ''),
                                 repr(self.args2[1]), repr(binary2)))

    def test_binary3(self):
        r"""Test QueryTree binary3."""
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


class TestQueryTreeRequest(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.argsbin = [(99999999, ), '\x00\x00\x00\x00\xff\xe0\xf5\x05']
        cls.conn = xcb.connect()
        cls.protocol = QueryTree(cls.conn)
        cls.protocol_check = QueryTreeUnchecked(cls.conn)
        cls.cookie = QueryTreeCookie

    def setUp(self):
        self.conn.flush()
        self.mocker.replay()

    def test_call(self):
        r"""Test QueryTree.__call__() expect return WrapQueryTreeCookie."""
        cookie = self.protocol(*self.argsbin[0])
        self.assertIsInstance(cookie, WrapQueryTreeCookie,
                              msg='Failed: {0}({1}) not returned'
                              ' WrapQueryTreeCookie\ngot: {2}'
                              .format(self.protocol.__class__.__name__,
                                      str(self.argsbin[0])
                                      .replace('(', '').replace(')', ''),
                                      cookie))

    def test_request(self, ):
        r"""Test QueryTree.request() expect return QueryTreeCookie."""
        cookie = self.protocol.request(self.argsbin[1])
        self.assertIsInstance(cookie, QueryTreeCookie,
                              msg='Failed: {0}.request("{1}") not return'
                              ' QueryTreeCookie\ngot: {2}'
                              .format(self.protocol.__class__.__name__,
                                      self.argsbin[1], cookie))

    def test_checkedrequest(self, ):
        r"""Test QueryTree.request() expect return QueryTreeCookie."""
        cookie = self.protocol_check.request(self.argsbin[1])
        self.assertIsInstance(cookie, QueryTreeCookie,
                              msg='Failed: {0}.request("{1}") not return'
                              ' QueryTreeCookie\ngot: {2}'
                              .format(self.protocol_check.__class__.__name__,
                                      self.argsbin[1], cookie))

    def tearDown(self):
        self.conn.flush()

    @classmethod
    def tearDownClass(cls, ):
        cls.conn.flush()
        cls.conn.disconnect()


class TestQueryTreeRecursive(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.conn = xcb2.connect()
        cls.protocol = QueryTree(cls.conn)

    def setUp(self):
        self.conn.flush()
        self.mocker.replay()

    def test_recursive(self):
        r"""Test QueryTree.recursive"""
        root = self.conn.get_setup().roots[0].root
        for win in self.protocol.recursive(root):
            self.assertIsInstance(win, Window,
                                  msg='Failed: win:{} is not Window type.'
                                  .format(win))

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
# test_querytree.py ends here
