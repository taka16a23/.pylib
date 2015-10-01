#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: test_commandtype.py 227 2014-09-13 08:15:46Z t1 $
# $Revision: 227 $
# $Date: 2014-09-13 17:15:46 +0900 (Sat, 13 Sep 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-09-13 17:15:46 +0900 (Sat, 13 Sep 2014) $

r"""Name: test_commandtype.py

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
from .. import command


class TestCommandType(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.expect = 'POWR'
        self.cmdtype = command.CommandType(self.expect)
        self.mocker.replay()

    def test_get(self, ):
        got = self.cmdtype.get()
        self.assertEqual(
            self.expect, got,
            msg='Failed: CommandType.get expect: \{}, got: \{}'
            .format(self.expect, got))

    def test_set(self, ):
        expect = 'ITGD'
        self.cmdtype.set(expect)
        got = self.cmdtype.get()
        self.assertEqual(
            expect, got,
            msg='Failed: CommandType.set expect: \{}, got: \{}'
            .format(expect, got))

    def test__check_length(self, ):
        with self.assertRaises(ValueError):
            self.cmdtype.set('TESTCMD')
        with self.assertRaises(ValueError):
            self.cmdtype.set('T')

    def test___hash__(self, ):
        expect = hash(self.expect)
        got = hash(self.cmdtype)
        self.assertEqual(
            expect, got,
            msg='Failed: CommandType.__hash__ expect: \{}, got: \{}'
            .format(expect, got))

    def test___eq__(self, ):
        self.assertTrue(self.cmdtype == command.CommandType(self.expect))
        self.assertTrue(self.cmdtype == self.expect)

    def test___ne__(self, ):
        self.assertTrue(self.cmdtype != command.CommandType('ITGD'))
        self.assertTrue(self.cmdtype != 'ITGD')

    def test___add__(self, ):
        parameter = '1   '
        expect = self.expect + parameter
        got = self.cmdtype + parameter
        self.assertEqual(
            expect, got,
            msg='Failed: CommandType.__add__ expect: \{}, got: \{}'
            .format(expect, got))

    def test___str__(self, ):
        got = str(self.cmdtype)
        self.assertEqual(self.expect, got,
                         msg='Failed: CommandType.__str__ expect: \{}, got: \{}'
                         .format(self.expect, got))

    def test___repr__(self, ):
        expect = 'CommandType("POWR")'
        got = repr(self.cmdtype)
        self.assertEqual(expect, got,
                         msg='Failed: CommandType.__repr__ expect: \{}, got: \{}'
                         .format(expect, got))

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        pass


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_commandtype.py ends here
