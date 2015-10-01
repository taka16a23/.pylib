#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_cacheatom.py

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

import xcb2
from xcb2.xobj.atom.atom import Atom
from xcb2.xobj.atom.atomname import AtomName
from xcb2.xobj.atom.atompair import AtomPair
from xcb2.xobj.atom.cacheatom import (
    CacheAtomPair, DisplayCacheAtomPair, GlobalCacheAtoms)


class TestCacheAtomPair(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.conn = xcb2.connect()
        cls.cache = CacheAtomPair()

    def setUp(self):
        self.conn.flush()
        self.cache.clear()
        self.mocker.replay()

    def test_dual_add(self):
        r"""Test CacheAtomPair.dual_add"""
        atomint = Atom(self.conn, 5)
        atomname = AtomName(self.conn, str(self.conn.core.atomidentify(5)))
        pair = AtomPair(atomname, atomint)
        self.cache.dual_add(pair)
        self.assertIn(str(pair), self.cache, msg='Failed: {} not has {}'
                      .format(self.cache, str(pair)))
        self.assertIn(int(pair), self.cache, msg='Failed: {} not has {}'
                      .format(self.cache, int(pair)))

    def test_setitem(self, ):
        r"""Test CacheAtomPair.__setitem__"""
        with self.assertRaises(StandardError):
            self.cache[list()] = None

    def tearDown(self):
        self.cache.clear()
        self.conn.flush()

    @classmethod
    def tearDownClass(cls, ):
        cls.conn.flush()
        cls.conn.disconnect()
        cls.cache.clear()


class TestDisplayCacheAtomPair(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.cache = DisplayCacheAtomPair()

    def setUp(self):
        self.cache.clear()
        self.mocker.replay()

    def test_get(self):
        r"""Test DisplayCacheAtomPair.get"""
        cache = self.cache.get('')
        self.assertIsInstance(
            cache, CacheAtomPair,
            msg='Failed: DisplayCacheAtomPair.get returned {}'.format(cache))

    def tearDown(self):
        self.cache.clear()

    @classmethod
    def tearDownClass(cls, ):
        cls.cache.clear()


class TestGlobalCacheAtoms(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.conn = xcb2.connect()
        cls.cache = GlobalCacheAtoms()

    def setUp(self):
        self.conn.flush()
        self.cache.clear()
        self.mocker.replay()

    def test_getcaches(self):
        r"""Test GlobalCacheAtoms.getcaches"""
        atomint = Atom(self.conn, 5)
        atomname = AtomName(self.conn, str(self.conn.core.atomidentify(5)))
        pair = AtomPair(atomname, atomint)

        cache = self.cache.getcaches('')
        cache.dual_add(pair)
        cache2 = self.cache.getcaches(':0.0')
        self.assertIsInstance(
            cache, CacheAtomPair,
            msg='Failed: DisplayCacheAtomPair.get returned {}'.format(cache))
        self.assertIsInstance(
            cache2, CacheAtomPair,
            msg='Failed: DisplayCacheAtomPair.get returned {}'.format(cache2))
        self.assertNotEqual(cache, cache2,
                            msg='Failed:'
                            ' Not Equal CacheAtomPair.getcaches("{}")'
                            ' == CacheAtomPair.getcaches("{}")'
                            .format('', ':0.0'))

    def test_iscached(self, ):
        r"""Test GlobalCacheAtoms.iscached"""
        atomint = Atom(self.conn, 5)
        atomname = AtomName(self.conn, str(self.conn.core.atomidentify(5)))
        pair = AtomPair(atomname, atomint)
        self.cache.add(pair)
        self.assertTrue(self.cache.iscached(pair))

    def test_clear(self, ):
        r"""Test GlobalCacheAtoms.iscached"""
        atomint = Atom(self.conn, 5)
        atomname = AtomName(self.conn, str(self.conn.core.atomidentify(5)))
        pair = AtomPair(atomname, atomint)
        self.cache.add(pair)
        self.assertTrue(self.cache.iscached(pair))
        self.cache.clearall()
        self.assertFalse(self.cache.iscached(pair))

    def tearDown(self):
        self.cache.clear()
        self.conn.flush()

    @classmethod
    def tearDownClass(cls, ):
        cls.conn.flush()
        cls.conn.disconnect()
        cls.cache.clearall()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_cacheatom.py ends here
