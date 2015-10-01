#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_atom_cache.py

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
from xahk.wm.atom_cache import AtomCache, NotAtomCachedError
from xahk.wm.display import Display


class TestAtomCache(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.katom_to_cache = ['_NET_WM_NAME',
                              '_NET_WM_PID']
        cls.display = Display()

    def setUp(self):
        self.cache = AtomCache(self.display, self.katom_to_cache)
        self.mocker.replay()

    def test_get_atom(self, ):
        wm_name = '_NET_WM_NAME'
        self.assertIn(wm_name, self.cache._cached_atoms)
        atom = self.display.core.InternAtom(
            True, len(wm_name), wm_name).reply().atom
        self.assertEqual(atom, self.cache._cached_atoms[wm_name])
        self.assertEqual(atom, self.cache.get_atom(wm_name))
        window = 'WINDOW'
        atom2 = self.display.core.InternAtom(
            True, len(window), window).reply().atom
        self.assertEqual(atom2, self.cache.get_atom(window))

    def test_list_atoms(self, ):
        self.assertEqual(
            [self.display.core.InternAtom(
                True, len(name), name).reply().atom for name
             in self.katom_to_cache],
            self.cache.list_atoms(self.katom_to_cache))

    def test_disallow_uncached_atoms(self, ):
        self.cache.disallow_uncached_atoms()
        wm_name = '_NET_WM_NAME'
        atom = self.display.core.InternAtom(
            True, len(wm_name), wm_name).reply().atom
        self.assertEqual(atom, self.cache.get_atom(wm_name))
        with self.assertRaises(NotAtomCachedError):
            self.cache.get_atom('ATOM')

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        cls.display.disconnect()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_atom_cache.py ends here
