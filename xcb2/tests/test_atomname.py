#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: test_atomname.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""Name: test_atomname.py

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

from array import array

import xcb, xcb.xproto
import xcb2
from xcb2.xobj.atom.atomname import AtomName


class TestAtomName(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.conn = xcb.connect()
        cls.atomname = 'BITMAP'
        cls.AtomName = AtomName(cls.conn, cls.atomname)
        cls.atom = cls.conn.core.InternAtom(
            True, len(cls.atomname), cls.atomname).reply().atom

    def setUp(self):
        self.conn.flush()
        self.mocker.replay()

    def test_intern_atom(self):
        r"""Test AtomName.intern"""
        atom = self.AtomName.intern(True).reply().atom
        self.assertEqual(self.atom, atom,
                         msg='Failed: AtomName.intern_atom() '
                         'expect: {}, got: {}'.format(self.atom, atom))

    def test_pack(self):
        r"""Test AtomName.pack"""
        expect = str(buffer(array('b', self.atomname)))
        binary = self.AtomName.pack()
        self.assertEqual(expect, binary,
                         msg='Failed: AtomName.pack() '
                         'expect: {}, got: {}'
                         .format(repr(expect), repr(binary)))

    def test_length(self):
        r"""Test AtomName.length"""
        expect = len(self.atomname)
        length = self.AtomName.getlength()
        self.assertEqual(expect, length,
                         msg='Failed: AtomName.length '
                         'expect: {}, got: {}'.format(expect, length))

    def test_format(self):
        r"""Test AtomName.format"""
        expect = 32
        fmt = self.AtomName.getformat()
        self.assertEqual(expect, fmt,
                         msg='Failed: AtomName.getformat '
                         'expect: {}, got: {}'.format(expect, fmt))

    def test_iter(self, ):
        r"""Test AtomName.__iter__"""
        for i, char in enumerate(self.AtomName, start=0):
            self.assertEqual(
                self.atomname[i], char,
                msg='Failed: AtomName.__iter__ expect: {}, got: {}'
                .format(self.atomname[i], char))

    def test_hash(self, ):
        r"""Test AtomName.__hash__"""
        expect = hash(self.atomname)
        hsh = hash(self.AtomName)
        self.assertEqual(expect, hsh,
                msg='Failed: AtomName.__hash__ expect: {}, got: {}'
                .format(expect, hsh))

    def test_repr(self, ):
        r"""Test AtomName.__repr__"""
        expect = repr(self.atomname)
        repred = repr(self.AtomName)
        self.assertEqual(expect, repred,
                msg='Failed: AtomName.__repr__ expect: {}, got: {}'
                         .format(expect, repred))

    def test_cmp(self, ):
        r"""Test AtomName.__cmp__"""
        atomname2 = AtomName(self.conn, self.atomname)
        self.assertEqual(self.AtomName.__cmp__(atomname2), 0,
                         msg='Failed: AtomName.__cmp__ cmp(AtomName, AtomName)')

    def test_cmp2(self, ):
        r"""Test AtomName.__cmp__ 2"""
        self.assertEqual(self.AtomName.__cmp__(self.atomname), 0,
                         msg='Failed: AtomName.__cmp__ cmp(AtomName, "{}")'
                         .format(self.atomname))

    def test_eq(self, ):
        r"""Test AtomName.__eq__"""
        atomname2 = AtomName(self.conn, self.atomname)
        self.assertTrue(self.AtomName.__eq__(atomname2),
                         msg='Failed: AtomName.__eq__')

    def test_eq2(self, ):
        r"""Test AtomName.__eq__ 2"""
        self.assertTrue(self.AtomName.__eq__(self.atomname),
                         msg='Failed: AtomName.__eq__ eq(AtomName, "{}")'
                         .format(self.atomname))

    def test_ne(self, ):
        r"""Test AtomName.__ne__"""
        self.assertTrue(self.AtomName.__ne__('CARDINAL'),
                         msg='Failed: AtomName.__ne__ ne(AtomName, "{}")'
                         .format('CARDINAL'))

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
# test_atomname.py ends here
