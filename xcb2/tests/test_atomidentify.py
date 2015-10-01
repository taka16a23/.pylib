#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_atomidentify.py

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
from xcb2.xobj.atom.atomidentify import AtomIdentifier
from xcb2.xobj.atom.atom import Atom
from xcb2.xobj.atom.atomname import AtomName
from xcb2.xobj.atom.atompair import AtomPair


class TestAtomIdentify(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.conn = xcb.connect()
        cls.conn2 = xcb2.connect()
        cls.identifier = AtomIdentifier(cls.conn2)
        cls.atomname = 'BITMAP'
        cls.rawatom = cls.conn.core.InternAtom(
            False, len(cls.atomname), cls.atomname).reply().atom

    def setUp(self):
        self.conn.flush()
        self.conn2.flush()
        self.mocker.replay()

    def test_identify_str(self, ):
        r"""Test AtomIdentifier._identify_str."""
        atom = self.identifier(self.atomname)
        self.assertEqual(self.rawatom, int(atom),
                         msg='Failed: AtomIdentifier._identify_str() '
                         'expect: {}, got: {}'
                         .format(int(self.rawatom), int(atom)))

    def test_identify_int(self, ):
        r"""Test AtomIdentifier._identify_int."""
        atom = self.identifier(self.rawatom)
        self.assertEqual(self.atomname, str(atom),
                         msg='Failed: AtomIdentifier._identify_int() '
                         'expect: {}, got: {}'.format(self.atomname, str(atom)))

    def test_identify_AtomPair(self, ):
        r"""Test AtomIdentifier._identify_AtomPair."""
        atomint = Atom(self.conn2, self.rawatom)
        atomname = AtomName(self.conn2, self.atomname)
        expect = AtomPair(atomname, atomint)
        atom = self.identifier(expect)
        self.assertEqual(expect, atom,
                         msg='Failed: AtomIdentifier._identify_AtomPair() '
                         'expect: {}, got: {}'.format(expect, atom))

    def tearDown(self):
        self.conn.flush()
        self.conn2.flush()

    @classmethod
    def tearDownClass(cls, ):
        cls.conn.flush()
        cls.conn2.flush()
        cls.conn.disconnect()
        cls.conn2.disconnect()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_atomidentify.py ends here
