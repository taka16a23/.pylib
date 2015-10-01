#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: test_resource.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""Name: test_resource.py

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
from xcb2 import VoidCookie
from xcb2.xobj.window.resource import Resource


class TestResource(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.conn = xcb2.connect()
        cls.resource = Resource(cls.conn, 482)

    def setUp(self):
        self.conn.flush()
        self.mocker.replay()

    def test_flush(self):
        r"""Test Resource.flush"""
        self.resource.flush()

    def test_int(self, ):
        r"""Test Resource.__int__"""
        expect = 482
        got = int(self.resource)
        self.assertEqual(
            expect, got,
            msg='Failed: Resource.__int__ expect: {}, got: {}'
            .format(expect, got))

    def test_cmp(self, ):
        r"""Test Resource.__cmp__"""
        expect = 0
        got = self.resource.__cmp__(self.resource)
        self.assertEqual(expect, got,
                         msg='Failed: Resource.__cmp__ expect: \{}, got: \{}'
                         .format(expect, got))

    def test_cmp_other_connection(self, ):
        r"""Test Resource.__cmp__"""
        conn = xcb.connect()
        resource = Resource(conn, 482)
        expect = -1
        got = self.resource.__cmp__(resource)
        self.assertEqual(expect, got,
                         msg='Failed: Resource.__cmp__ expect: \{}, got: \{}'
                         .format(expect, got))

    def test_cmp_int(self, ):
        r"""Test Resource.__cmp__"""
        expect = 1
        got = self.resource.__cmp__(482)
        self.assertEqual(expect, got,
                         msg='Failed: Resource.__cmp__ expect: \{}, got: \{}'
                         .format(expect, got))

    def test_hash(self, ):
        r"""Test Resource.__hash__"""
        expect = hash(482)
        got = hash(self.resource)
        self.assertEqual(expect, got,
                         msg='Failed: Resource.__hash__ expect: \{}, got: \{}'
                         .format(expect, got))

    def test_repr(self, ):
        r"""Test Resource.__repr__"""
        expect = '<Resource 482>'
        got = repr(self.resource)
        self.assertEqual(expect, got,
                         msg='Failed: Resource.__repr__ expect: \{}, got: \{}'
                         .format(expect, got))

    def test_str(self, ):
        r"""Test Resource.__str__"""
        expect = 'Resource(id=482)'
        got = str(self.resource)
        self.assertEqual(expect, got,
                         msg='Failed: Resource.__str__ expect: \{}, got: \{}'
                         .format(expect, got))

    def test_kill_client(self, ):
        r"""Test Resource.kill_client"""
        expect = VoidCookie
        got = self.resource.kill_client()
        self.assertIsInstance(got, expect,
                msg='Failed: Resource.kill_client expect: \{}, got: \{}'
                .format(expect, got))

    def test_core(self, ):
        r"""Test Resource.core"""
        expect = self.conn.core
        got = self.resource.core
        self.assertEqual(expect, got,
                         msg='Failed: Resource.core expect: \{}, got: \{}'
                         .format(expect, got))

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
# test_resource.py ends here
