#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: test_error.py 146 2014-04-12 09:38:34Z t1 $
# $Revision: 146 $
# $Date: 2014-04-12 18:38:34 +0900 (Sat, 12 Apr 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-04-12 18:38:34 +0900 (Sat, 12 Apr 2014) $

r"""Name: test_error.py

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
from bitflag.error import BitFlagError, BitLengthError, BitFlagValueError
from bitflag.cls import BitFlag8, BitFlag16, BitFlag32


class TestError(MockerTestCase):
    def setUp(self):

        self.mocker.replay()

    def test_BitFlag8_minus(self):
        r"""BitFlag8_minus
        """
        with self.assertRaises(BitFlagValueError) as context:
            BitFlag8(-1)
        self.assertTrue(isinstance(context.exception, BitFlagError))
        self.assertTrue(isinstance(context.exception, ValueError))

    def test_BitFlag16_minus(self, ):
        r"""BitFlag16_minus."""
        with self.assertRaises(BitFlagValueError) as context:
            BitFlag16(-1)
        self.assertTrue(isinstance(context.exception, BitFlagError))
        self.assertTrue(isinstance(context.exception, ValueError))

    def test_BitFlag32_minus(self, ):
        r"""BitFlag32_minus."""
        with self.assertRaises(BitFlagValueError) as context:
            BitFlag32(-1)
        self.assertTrue(isinstance(context.exception, BitFlagError))
        self.assertTrue(isinstance(context.exception, ValueError))

    def test_BitFlag8_outofrange(self, ):
        r"""BitFlag8_outofrange."""
        with self.assertRaises(BitLengthError) as context:
            arg = 1 << 9
            BitFlag8(arg)
        self.assertTrue(isinstance(context.exception, BitFlagValueError))
        self.assertTrue(isinstance(context.exception, BitFlagError))
        self.assertTrue(isinstance(context.exception, ValueError))

    def test_BitFlag16_outofrange(self, ):
        r"""BitFlag16_outofrange."""
        with self.assertRaises(BitLengthError) as context:
            arg = 1 << 17
            BitFlag16(arg)
        self.assertTrue(isinstance(context.exception, BitFlagValueError))
        self.assertTrue(isinstance(context.exception, BitFlagError))
        self.assertTrue(isinstance(context.exception, ValueError))

    def test_BitFlag32_outofrange(self, ):
        r"""BitFlag32_outofrange."""
        with self.assertRaises(BitLengthError) as context:
            arg = 1 << 30
            BitFlag32(arg)
        self.assertTrue(isinstance(context.exception, BitFlagValueError))
        self.assertTrue(isinstance(context.exception, BitFlagError))
        self.assertTrue(isinstance(context.exception, ValueError))

    def tearDown(self):
        pass



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_error.py ends here
