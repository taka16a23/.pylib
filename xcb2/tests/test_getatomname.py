#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: test_getatomname.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""Name: test_getatomname.py

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
from xcb2.xproto import GetAtomNameCookie, BadAtom
from xcb2.xproto.wcookie import WrapGetAtomNameCookie
from xcb2.xproto.ext import GetAtomName, GetAtomNameUnchecked
from xcb2.xproto.ext.getatomname import UseCache
from xcb2.xobj.atom.cacheatom import GlobalCacheAtoms


class TestGetAtomNameBinary(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.args1 = [(5, ), '\x00\x00\x00\x00\x05\x00\x00\x00']
        cls.args2 = [(39, ), "\x00\x00\x00\x00'\x00\x00\x00"]
        cls.args3 = [(293, ), '\x00\x00\x00\x00%\x01\x00\x00']
        cls.conn = xcb.connect()
        cls.protocol = GetAtomName(cls.conn)
        cls.protocol_check = GetAtomNameUnchecked(cls.conn)

    def setUp(self):
        self.conn.flush()
        self.mocker.replay()

    def test_binary1(self):
        r"""Test GetAtomName binary1."""
        binary = self.protocol._getbinary(*self.args1[0])
        self.assertEqual(self.args1[1], binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._getbinary,
                                 str(self.args1[0])
                                 .replace('(', '').replace(')', ''),
                                 repr(self.args1[1]), repr(binary)))

    def test_binary2(self):
        r"""Test GetAtomName binary2."""
        binary2 = self.protocol._getbinary(*self.args2[0])
        self.assertEqual(self.args2[1], binary2,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._getbinary,
                                 str(self.args2[0])
                                 .replace('(', '').replace(')', ''),
                                 repr(self.args2[1]), repr(binary2)))
    def test_binary3(self):
        r"""Test GetAtomName binary3."""
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


class TestGetAtomNameRequest(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.argsbin = [(5, ), '\x00\x00\x00\x00\x05\x00\x00\x00']
        cls.conn = xcb.connect()
        cls.protocol = GetAtomName(cls.conn)
        cls.protocol_check = GetAtomNameUnchecked(cls.conn)
        cls.cookie = GetAtomNameCookie

    def setUp(self):
        self.conn.flush()
        self.mocker.replay()

    def test_call(self):
        r"""Test GetAtomName.__call__() expect return WrapGetAtomNameCookie."""
        cookie = self.protocol(*self.argsbin[0])
        self.assertIsInstance(cookie, WrapGetAtomNameCookie,
                              msg='Failed: {0}({1}) not returned'
                              ' WrapGetAtomNameCookie\ngot: {2}'
                              .format(self.protocol.__class__.__name__,
                                      str(self.argsbin[0])
                                      .replace('(', '').replace(')', ''),
                                      cookie))

    def test_request(self, ):
        r"""Test GetAtomName.request() expect return GetAtomNameCookie."""
        cookie = self.protocol.request(self.argsbin[1])
        self.assertIsInstance(cookie, GetAtomNameCookie,
                              msg='Failed: {0}.request("{1}") not return'
                              ' GetAtomNameCookie\ngot: {2}'
                              .format(self.protocol.__class__.__name__,
                                      self.argsbin[1], cookie))

    def test_checkedrequest(self, ):
        r"""Test GetAtomName.request() expect return GetAtomNameCookie."""
        cookie = self.protocol_check.request(self.argsbin[1])
        self.assertIsInstance(cookie, GetAtomNameCookie,
                              msg='Failed: {0}.request("{1}") not return'
                              ' GetAtomNameCookie\ngot: {2}'
                              .format(self.protocol_check.__class__.__name__,
                                      self.argsbin[1], cookie))

    def tearDown(self):
        self.conn.flush()

    @classmethod
    def tearDownClass(cls, ):
        cls.conn.flush()
        cls.conn.disconnect()


class TestGetAtomNameCheck(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.conn = xcb.connect()
        cls.protocol = GetAtomName(cls.conn)

    def setUp(self):
        self.conn.flush()
        self.mocker.replay()

    def test_badatom(self, ):
        r"""Test BadAtom."""
        with self.assertRaises(BadAtom):
            self.protocol(0).reply()

    def tearDown(self):
        self.conn.flush()

    @classmethod
    def tearDownClass(cls, ):
        cls.conn.flush()
        cls.conn.disconnect()


class TestGetAtomNameUseCacheBinary(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.args1 = [(6, ), '\x00\x00\x00\x00\x06\x00\x00\x00']
        cls.args2 = [(39, ), "\x00\x00\x00\x00'\x00\x00\x00"]
        cls.args3 = [(293, ), '\x00\x00\x00\x00%\x01\x00\x00']
        cls.conn = xcb.connect()
        cls.protocol = UseCache(GetAtomName(cls.conn))

    def setUp(self):
        self.conn.flush()
        self.mocker.replay()

    def test_binary1(self):
        r"""Test UseCache binary1."""
        binary = self.protocol._getbinary(*self.args1[0])
        self.assertEqual(self.args1[1], binary,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._getbinary,
                                 str(self.args1[0])
                                 .replace('(', '').replace(')', ''),
                                 repr(self.args1[1]), repr(binary)))

    def test_binary2(self):
        r"""Test UseCache binary2."""
        binary2 = self.protocol._getbinary(*self.args2[0])
        self.assertEqual(self.args2[1], binary2,
                         msg='Failed {0.__class__.__name__}.{1.__name__}({2}):\n'
                         'Expected: "{3}"\nReturned: "{4}"'
                         .format(self.protocol, self.protocol._getbinary,
                                 str(self.args2[0])
                                 .replace('(', '').replace(')', ''),
                                 repr(self.args2[1]), repr(binary2)))

    def test_binary3(self):
        r"""Test UseCache binary3."""
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


class TestGetAtomNameUseCache(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.args1 = [(6, ), '\x00\x00\x00\x00\x06\x00\x00\x00']
        cls.conn = xcb.connect()
        cls.conn.display = ''
        cls.protocol = GetAtomName(cls.conn)
        cls.usecache = UseCache(cls.protocol)
        cls.cache = GlobalCacheAtoms

    def setUp(self):
        self.conn.flush()
        self.cache.clearall()
        self.mocker.replay()

    def test_getcache(self):
        r"""Test UseCahce.getcache()"""
        atom = self.usecache(*self.args1[0])
        cache = self.usecache._getcache(*self.args1[0])
        self.assertEqual(atom, cache,
                         msg='Failed: Expect: {}, Got: {}'.format(atom, cache))
        # for if branch in UseCache__call__
        cache2 = self.usecache(*self.args1[0])
        self.assertEqual(atom, cache2,
                         msg='Failed: Expect: {}, Got: {}'.format(atom, cache2))

    def test_addcache(self, ):
        r"""Test UseCahce.addcache()."""
        ret = self.usecache._getcache(*self.args1[0])
        self.assertIsNone(ret,
                          msg='Failed: UseCache._getcache({}) expect None, Got:{}'
                          .format(6, ret))
        atom = self.protocol(*self.args1[0]).reply().name
        self.usecache._addcache(atom)
        cache = self.usecache._getcache(*self.args1[0])
        self.assertEqual(atom, cache,
                         msg='Failed: Expect: {}, Got: {}'.format(atom, cache))

    def tearDown(self):
        self.cache.clearall()
        self.conn.flush()

    @classmethod
    def tearDownClass(cls, ):
        cls.cache.clearall()
        cls.conn.flush()
        cls.conn.disconnect()


class TestGetAtomNameUseCache2(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.conn = xcb.connect()
        cls.protocol = GetAtomName(cls.conn)
        cls.usecache = UseCache(cls.protocol)

    def setUp(self):
        dummy = self.mocker.replace(
            'xcb2.xproto.ext.getatomname.UseCache.__call__')
        dummy(ANY)
        self.mocker.result('dummy')
        self.mocker.count(0, None)
        self.conn.flush()
        self.mocker.replay()

    def test_cachecheck(self):
        r"""Test UseCache cachecheck."""
        self.assertEqual('dummy', self.usecache.__call__(6), msg='Failed: ')

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
# test_getatomname.py ends here
