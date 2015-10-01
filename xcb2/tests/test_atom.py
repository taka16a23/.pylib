#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: test_atom.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""Name: test_atom.py

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
from struct import pack
import xcb2
from xcb2.xobj.atom.atom import Atom


class TestAtom(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.conn = xcb2.connect()
        cls.int = 5
        cls.atom = Atom(cls.conn, cls.int)
        cls.atomname = str(cls.conn.core.GetAtomName(cls.int).reply().name)

    def setUp(self):
        self.conn.flush()
        self.mocker.replay()

    def test_getname(self):
        r"""Test Atom.getname"""
        name = self.atom.getname().reply().name
        self.assertEqual(self.atomname, name,
                         msg='Failed: Atom.getname expect: {}, got: {}'
                         .format(self.atomname, name))

    def test_pack(self, ):
        r"""Test Atom.pack"""
        expect = pack('I', self.int)
        binary = self.atom.pack()
        self.assertEqual(expect, binary,
                         msg='Failed: Atom.pack expect: {}, got: {}'
                         .format(expect, binary))

    def test_int(self, ):
        r"""Test Atom.__int__"""
        integer = int(self.atom)
        self.assertEqual(self.int, integer,
                         msg='Failed: Atom.__int__ expect: {}, got: {}'
                         .format(self.int,  integer))

    def test_long(self, ):
        r"""Test Atom.__long__"""
        expect = long(self.int)
        integer = long(self.atom)
        self.assertEqual(expect, integer,
                         msg='Failed: Atom.__long__ expect: {}, got: {}'
                         .format(expect,  integer))

    def test_hash(self, ):
        r"""Test Atom.__hash__"""
        expect = hash(self.int)
        hashed = hash(self.atom)
        self.assertEqual(expect, hashed,
                         msg='Failed: Atom.__hash__ expect: {}, got: {}'
                         .format(expect,  hashed))

    def test_repr(self, ):
        r"""Test Atom.__repr__"""
        expect = repr(self.int)
        repred = repr(self.atom)
        self.assertEqual(expect, repred,
                         msg='Failed: Atom.__repr__ expect: {}, got: {}'
                         .format(expect,  repred))

    def test_cmp(self, ):
        r"""Test Atom.__cmp__"""
        atom = Atom(self.conn, self.int)
        self.assertEqual(0, self.atom.__cmp__(atom),
                         msg='Failed: Atom.__cmp__(Atom)')
        self.assertEqual(0, self.atom.__cmp__(self.int),
                         msg='Failed: Atom.__cmp__(5)')

    def test_eq(self, ):
        r"""Test Atom.__eq__"""
        atom = Atom(self.conn, self.int)
        self.assertTrue(self.atom.__eq__(atom))
        self.assertTrue(self.atom.__eq__(self.int))

    def test_ne(self, ):
        r"""Test Atom.__ne__"""
        atom = Atom(self.conn, 6)
        self.assertTrue(self.atom.__ne__(atom))

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
# test_atom.py ends here
