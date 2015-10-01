#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: test_internatom.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""Name: test_internatom.py

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
from xcb2.xproto import InternAtomCookie
from xcb2.xproto.wcookie import WrapInternAtomCookie
from xcb2.xproto.ext.internatom import InternAtom, InternAtomUnchecked, UseCache


class TestInternAtomBinary(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.args1 = [(True, len('WM_NAME'), 'WM_NAME'),
            '\x00\x01\x00\x00\x07\x00\x00\x00WM_NAME']
        cls.args2 = [(False, len('WM_NAME'), 'WM_NAME'),
            '\x00\x00\x00\x00\x07\x00\x00\x00WM_NAME']
        cls.args3 = [(False, len('_NET_WM_NAME'), '_NET_WM_NAME'),
            '\x00\x00\x00\x00\x0c\x00\x00\x00_NET_WM_NAME']
        cls.conn = xcb.connect()
        cls.protocol = InternAtom(cls.conn)
        cls.protocol_check = InternAtomUnchecked(cls.conn)

    def setUp(self):
        self.conn.flush()
        self.mocker.replay()

    def test_binary1(self):
        r"""Test InternAtom binary1."""
        binary = self.protocol._getbinary(*self.args1[0])
        self.assertEqual(self.args1[1], binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._getbinary,
                                 str(self.args1[0])
                                 .replace('(', '').replace(')', ''),
                                 repr(self.args1[1]), repr(binary)))

    def test_binary2(self):
        r"""Test InternAtom binary2."""
        binary2 = self.protocol._getbinary(*self.args2[0])
        self.assertEqual(self.args2[1], binary2,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._getbinary,
                                 str(self.args2[0])
                                 .replace('(', '').replace(')', ''),
                                 repr(self.args2[1]), repr(binary2)))
    def test_binary3(self):
        r"""Test InternAtom binary3."""
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


class TestGetAtomNameUseCacheBinary(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.args1 = [(True, len('WM_NAME'), 'WM_NAME'),
            '\x00\x01\x00\x00\x07\x00\x00\x00WM_NAME']
        cls.args2 = [(False, len('WM_NAME'), 'WM_NAME'),
            '\x00\x00\x00\x00\x07\x00\x00\x00WM_NAME']
        cls.args3 = [(False, len('_NET_WM_NAME'), '_NET_WM_NAME'),
            '\x00\x00\x00\x00\x0c\x00\x00\x00_NET_WM_NAME']
        cls.conn = xcb.connect()
        cls.protocol = UseCache(InternAtom(cls.conn))

    def setUp(self):
        self.conn.flush()
        self.mocker.replay()

    def test_binary1(self):
        r"""Test UseCache binary1."""
        binary = self.protocol._getbinary('WM_NAME')
        self.assertEqual(self.args1[1], binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._getbinary,
                                 'WM_NAME',
                                 repr(self.args1[1]), repr(binary)))

    def test_binary2(self):
        r"""Test UseCache binary2."""
        self.protocol.set_only_if_exists(False)
        binary2 = self.protocol._getbinary('WM_NAME')
        self.assertEqual(self.args2[1], binary2,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._getbinary,
                                 'WM_NAME',
                                 repr(self.args2[1]), repr(binary2)))

    def test_binary3(self):
        r"""Test UseCache binary3."""
        self.protocol.set_only_if_exists(False)
        binary3 = self.protocol._getbinary('_NET_WM_NAME')
        self.assertEqual(self.args3[1], binary3,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._getbinary,
                                 '_NET_WM_NAME',
                                 repr(self.args3[1]), repr(binary3)))

    def tearDown(self):
        self.conn.flush()

    @classmethod
    def tearDownClass(cls, ):
        cls.conn.flush()
        cls.conn.disconnect()


class TestInternAtomRequest(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.argsbin = [(True, len('WM_NAME'), 'WM_NAME'),
            '\x00\x01\x00\x00\x07\x00\x00\x00WM_NAME']
        cls.conn = xcb.connect()
        cls.conn.display = ''
        cls.protocol = InternAtom(cls.conn)
        cls.protocol_check = InternAtomUnchecked(cls.conn)
        cls.cookie = InternAtomCookie

    def setUp(self):
        self.conn.flush()
        self.mocker.replay()

    def test_call(self):
        r"""Test InternAtom.__call__() expect return WrapInternAtomCookie."""
        cookie = self.protocol(*self.argsbin[0])
        self.assertIsInstance(cookie, WrapInternAtomCookie,
                              msg='Failed: {0}({1}) not returned'
                              ' WrapInternAtomCookie\ngot: {2}'
                              .format(self.protocol.__class__.__name__,
                                      str(self.argsbin[0])
                                      .replace('(', '').replace(')', ''),
                                      cookie))

    def test_request(self, ):
        r"""Test InternAtom.request() expect return InternAtomCookie."""
        cookie = self.protocol.request(self.argsbin[1])
        self.assertIsInstance(cookie, self.cookie,
                              msg='Failed: {0}.request("{1}") not return'
                              ' InternAtomCookie\ngot: {2}'
                              .format(self.protocol.__class__.__name__,
                                      self.argsbin[1], cookie))

    def test_checkedrequest(self, ):
        r"""Test InternAtom.request() expect return InternAtomCookie."""
        cookie = self.protocol_check.request(self.argsbin[1])
        self.assertIsInstance(cookie, self.cookie,
                              msg='Failed: {0}.request("{1}") not return'
                              ' InternAtomCookie\ngot: {2}'
                              .format(self.protocol_check.__class__.__name__,
                                      self.argsbin[1], cookie))

    def tearDown(self):
        self.conn.flush()

    @classmethod
    def tearDownClass(cls, ):
        cls.conn.flush()
        cls.conn.disconnect()


class TestInternAtomUseCache(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.conn = xcb.connect()
        cls.conn.display = ''
        cls.protocol = InternAtom(cls.conn)
        cls.usecache = UseCache(cls.protocol)

    def setUp(self):
        self.conn.flush()
        self.mocker.replay()

    def test_getcache(self):
        r"""Test UseCahce.getcache()"""
        atom = self.usecache('WM_NAME')
        cache = self.usecache._getcache('WM_NAME')
        self.assertEqual(atom, cache,
                         msg='Failed: Expect: {}, Got: {}'.format(atom, cache))
        # for if branch in UseCache__call__
        cache2 = self.usecache('WM_NAME')
        self.assertEqual(atom, cache2,
                         msg='Failed: Expect: {}, Got: {}'.format(atom, cache2))

    def test_addcache(self, ):
        r"""Test UseCahce.addcache()."""
        self.assertIsNone(self.usecache._getcache('BITMAP'),
                          msg='Failed: UseCache._getcache({}) expect None'
                          .format('BITMAP'))
        atom = self.protocol(True, len('BITMAP'), 'BITMAP').reply().atom
        self.usecache._addcache(atom)
        cache = self.usecache._getcache('BITMAP')
        self.assertEqual(atom, cache,
                         msg='Failed: Expect: {}, Got: {}'.format(atom, cache))

    def test_set_only_if_exists_raise(self, ):
        r"""Test InternAtom.UseCache.set_only_if_exists raise."""
        with self.assertRaises(StandardError):
            self.usecache.set_only_if_exists('strings')

    def tearDown(self):
        self.conn.flush()

    @classmethod
    def tearDownClass(cls, ):
        cls.conn.flush()
        cls.conn.disconnect()


# class TestGetAtomNameUseCache2(MockerTestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.conn = xcb.connect()
#         cls.protocol = InternAtom(cls.conn)
#         cls.usecache = UseCache(cls.protocol)

#     def setUp(self):
#         dummy = self.mocker.replace(
#             'xcb2.xproto.ext.internatom.UseCache.__call__')
#         dummy(ANY)
#         self.mocker.result('dummy')
#         self.mocker.count(1, None)
#         self.conn.flush()
#         self.mocker.replay()

#     def test_cachecheck(self):
#         r"""Test UseCache cachecheck."""
#         self.assertEqual(
#             'dummy', self.usecache.__call__('WM_NAME'),
#             msg='Failed: ')

#     def tearDown(self):
#         self.conn.flush()

#     @classmethod
#     def tearDownClass(cls, ):
#         cls.conn.flush()
#         cls.conn.disconnect()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_internatom.py ends here
