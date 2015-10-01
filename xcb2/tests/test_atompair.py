#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_atompair.py

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
from xcb2.xobj.atom.atomtypes import AtomTypeSTRINGReply


class TestAtomPair(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.conn = xcb2.connect()
        cls.atomname = 'WM_NAME'
        cls.atom = int(cls.conn.core.InternAtom(
            True, len(cls.atomname), cls.atomname).reply().atom)
        cls.AtomName = AtomName(cls.conn, cls.atomname)
        cls.Atom = Atom(cls.conn, cls.atom)
        cls.pair = AtomPair(cls.AtomName, cls.Atom)

    def setUp(self):
        self.conn.flush()
        self.mocker.replay()

    def test_name_length(self):
        r"""Test AtomPair.name_length"""
        expect = len(self.atomname)
        length = self.pair.get_namelen()
        self.assertEqual(expect, length,
                         msg='Failed: AtomPair.name_length expect: {}, got: {}'
                         .format(expect, length))

    def test_types(self, ):
        r"""Test AtomPair.gettype"""
        expect = AtomTypeSTRINGReply
        types = self.pair.gettype()
        self.assertEqual(expect, types,
                         msg='Failed: AtomPair.gettypes expect: {}, got: {}'
                         .format(expect, types))

    def test_getformat(self, ):
        r"""Test AtomPair.getformat"""
        expect = AtomTypeSTRINGReply.length
        fmt = self.pair.getformat()
        self.assertEqual(expect, fmt,
                         msg='Failed: AtomPair.getformat expect: {}, got: {}'
                         .format(expect, fmt))

    def test_repr(self, ):
        r"""Test AtomPair.__repr__"""
        expect = "AtomPair(name='WM_NAME', atom=39)"
        repred = repr(self.pair)
        self.assertEqual(expect, repred,
                         msg='Failed: AtomPair.__repr__ expect: {}, got: {}'
                         .format(expect, repred))

    def test_cmp(self, ):
        r"""Test AtomPair.__cmp__"""
        cmped = self.pair.__cmp__(self.atomname)
        self.assertEqual(0, cmped,
                         msg='Failed: AtomPair.__cmp__ expect: 0, got: {}'
                         .format(cmped))

    def test_cmp2(self, ):
        r"""Test AtomPair.__cmp__2"""
        atomint = Atom(self.conn, self.atom)
        atomname = AtomName(self.conn, self.atomname)
        pair = AtomPair(atomname, atomint)
        cmped = self.pair.__cmp__(pair)
        self.assertEqual(0, cmped,
                         msg='Failed: AtomPair.__cmp__ expect: 0, got: {}'
                         .format(cmped))

    def test_cmp3(self, ):
        r"""Test AtomPair.__cmp__3"""
        cmped = self.pair.__cmp__(self.atom)
        self.assertEqual(0, cmped,
                         msg='Failed: AtomPair.__cmp__ expect: 0, got: {}'
                         .format(cmped))

    def test_cmp4_False(self, ):
        r"""Test AtomPair.__cmp__4 will returned 1"""
        cmped = self.pair.__cmp__(type)
        self.assertEqual(1, cmped,
                         msg='Failed: AtomPair.__cmp__ expect: 0, got: {}'
                         .format(cmped))

    def test_eq(self, ):
        r"""Test AtomPair.__eq__"""
        eqed = self.pair.__eq__(self.atomname)
        self.assertTrue(eqed, msg='Failed: AtomPair.__eq__ expect: True, got: {}'
                        .format(eqed))

    def test_eq2(self, ):
        r"""Test AtomPair.__eq__"""
        atomint = Atom(self.conn, self.atom)
        atomname = AtomName(self.conn, self.atomname)
        pair = AtomPair(atomname, atomint)
        eqed = self.pair.__eq__(pair)
        self.assertTrue(eqed, msg='Failed: AtomPair.__eq__ expect: True, got: {}'
                         .format(eqed))

    def test_eq3(self, ):
        r"""Test AtomPair.__cmp__"""
        eqed = self.pair.__eq__(self.atom)
        self.assertTrue(eqed, msg='Failed: AtomPair.__eq__ expect: True, got: {}'
                         .format(eqed))

    def test_eq4_False(self, ):
        r"""Test AtomPair.__eq__4 will returned False."""
        eqed = self.pair.__eq__(type)
        self.assertFalse(eqed, msg='Failed: AtomPair.__eq__ expect: True, got: {}'
                         .format(eqed))

    def test_ne(self, ):
        r"""Test AtomPair.__ne__"""
        ned = self.pair.__ne__('WM_CLASS')
        self.assertTrue(ned,
                         msg='Failed: AtomPair.__eq__ expect: True, got: {}'
                         .format(ned))

    def test_getitem(self, ):
        r"""Test AtomPair.__getitem__"""
        expect = self.atomname[1]
        char = self.pair.__getitem__(1)
        self.assertEqual(
            expect, char, msg='Failed: AtomPair.__getitem__ expect: {}, got: {}'
            .format(expect, char))
        expect = self.atomname[3]
        char = self.pair.__getitem__(3)
        self.assertEqual(
            expect, char, msg='Failed: AtomPair.__getitem__ expect: {}, got: {}'
            .format(expect, char))

    def test_str(self, ):
        r"""Test AtomPair.__str__"""
        string = str(self.pair)
        self.assertEqual(self.atomname, string,
                         msg='Failed: AtomPair.__str__ expect: {}, got: {}'
                         .format(self.atomname, string))

    def test_int(self, ):
        r"""Test AtomPair.__int__"""
        integer = int(self.pair)
        self.assertEqual(self.atom, integer,
                         msg='Failed: AtomPair.__int__ expect: {}, got: {}'
                         .format(self.atom, integer))

    def test_long(self, ):
        r"""Test AtomPair.__long__"""
        expect = long(self.atom)
        integer = long(self.pair)
        self.assertEqual(expect, integer,
                         msg='Failed: AtomPair.__long__ expect: {}, got: {}'
                         .format(expect, integer))

    def test_len(self, ):
        r"""Test AtomPair.__len__"""
        expect = len(self.atomname)
        length = len(self.pair)
        self.assertEqual(expect, length,
                         msg='Failed: AtomPair.__len__ expect: {}, got: {}'
                         .format(expect, length))

    def test_hash(self, ):
        r"""Test AtomPair.__hash__"""
        expect = hash(self.atom)
        hsh = hash(self.pair)
        self.assertEqual(expect, hsh,
                         msg='Failed: AtomPair.__hash__ expect: {}, got: {}'
                         .format(expect, hsh))

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
# test_atompair.py ends here
