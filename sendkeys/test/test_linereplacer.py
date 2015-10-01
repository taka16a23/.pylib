#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: test_linereplacer.py 136 2014-04-05 08:42:53Z t1 $
# $Revision: 136 $
# $Date: 2014-04-05 17:42:53 +0900 (Sat, 05 Apr 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-04-05 17:42:53 +0900 (Sat, 05 Apr 2014) $

r"""Name: test_linereplacer.py

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
from sendkeys.linereplacer import LineReplacer, REPLACE_MAP

class TestLineReplacerCollectReplaced(MockerTestCase):
    def setUp(self):

        self.mocker.replay()

    def test_replace_map(self):
        r"""Check by REPLACE_MAP."""
        for key, value in REPLACE_MAP.iteritems():
            replaced = LineReplacer(key).replace()
            self.assertEqual(
                value, replaced,
                msg='Failed: cannot replaced {} => {} result: {}'
                .format(key, value, replaced))

    def test_replace_by_sample(self, ):
        r"""Check by mix strings."""
        strpair = (('{+}', '{plus}'),
                   ('{!}\\+', '{exclam}{plus}'),
                   ('hello(world', 'hello{parenleft}world'),
                   ('&_|=*', '{ampersand}{underscore}{bar}{equal}{asterisk}'),
                   )
        for key, value in strpair:
            replaced = LineReplacer(key).replace()
            self.assertEqual(
                value, replaced,
                msg='Failed: cannot replaced {} => {} result: {}'
                .format(key, value, replaced))

    def tearDown(self):
        pass


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_linereplacer.py ends here
