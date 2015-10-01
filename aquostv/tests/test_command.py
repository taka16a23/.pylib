#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_command.py

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


class TestCommand(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.power = 'POWR'
        cls.val = 1
        cls.cmdtype = command.CommandType(cls.power)
        cls.param = command.Parameter(cls.val)

    def setUp(self):
        self.cmd = command.Command(self.cmdtype, self.param)
        self.mocker.replay()

    def test_get_command(self, ):
        expect = 'POWR1   '
        got = self.cmd.get_command()
        self.assertEqual(
            expect, got,
            msg='Failed: Command.get_command expect: \{}, got: \{}'
            .format(expect, got))

    def test_get_cmdtype(self, ):
        expect = self.cmdtype
        got = self.cmd.get_cmdtype()
        self.assertEqual(
            expect, got,
            msg='Failed: CommandType.get_cmdtype expect: \{}, got: \{}'
            .format(expect, got))

    def test_set_cmdtype(self, ):
        expect = command.CommandType('ITGD')
        self.cmd.set_cmdtype(expect)
        got = self.cmd._cmdtype
        self.assertEqual(expect, got,
                         msg='Failed: Command.set_cmdtype expect: \{}, got: \{}'
                         .format(expect, got))

    def test_get_parameter(self, ):
        expect = self.param
        got = self.cmd.get_parameter()
        self.assertEqual(
            expect, got,
            msg='Failed: Command.get_parameter expect: \{}, got: \{}'
            .format(expect, got))

    def test_set_parameter(self, ):
        expect = command.Parameter(2)
        self.cmd.set_parameter(expect)
        got = self.cmd._parameter
        self.assertEqual(
            expect, got,
            msg='Failed: Command.set_parameter expect: \{}, got: \{}'
            .format(expect, got))

    def test___add__(self, ):
        expect = 'POWR1   \n'
        got = self.cmd + '\n'
        self.assertEqual(expect, got,
                         msg='Failed: Command.__add__ expect: \{}, got: \{}'
                         .format(expect, got))

    def test___str__(self, ):
        expect = 'POWR1   '
        got = str(self.cmd)
        self.assertEqual(expect, got,
                         msg='Failed: Command.__str__ expect: \{}, got: \{}'
                         .format(expect, got))

    def test___repr__(self, ):
        expect = 'Command(_cmdtype="POWR", _parameter="1   ")'
        got = repr(self.cmd)
        self.assertEqual(expect, got,
                         msg='Failed: Command.__repr__ expect: \{}, got: \{}'
                         .format(expect, got))

    def test___eq__(self, ):
        self.assertTrue(self.cmd == command.Command(command.CommandType('POWR'),
                                                    command.Parameter(1)))
        self.assertTrue(self.cmd == 'POWR1   ')
        self.assertFalse(self.cmd == command.Command(command.CommandType('ITGD'),
                                                     command.Parameter(1)))
        self.assertFalse(self.cmd == 'ITGD1   ')

    def test___ne__(self, ):
        self.assertFalse(self.cmd != command.Command(command.CommandType('POWR'),
                                                     command.Parameter(1)))
        self.assertFalse(self.cmd != 'POWR1   ')
        self.assertTrue(self.cmd != command.Command(command.CommandType('ITGD'),
                                                    command.Parameter(1)))
        self.assertTrue(self.cmd != 'ITGD1   ')

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        pass


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_command.py ends here
