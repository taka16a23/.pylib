#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_commandorder.py

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
from .. import order


COMMANDLINE = 'POWR1   '


class DummyCommand(object):
    r"""DummyCommand

    DummyCommand is a object.
    Responsibility:
    """
    def get_orderline(self, ):
        r"""SUMMARY

        get_orderline()

        @Return:

        @Error:
        """
        return COMMANDLINE


class TestCommandOrder(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.command = DummyCommand()

    def setUp(self):
        self.order = order.CommandOrder(self.command)
        self.mocker.replay()

    def test_get_orderline(self, ):
        expect = COMMANDLINE + '\n'
        got = self.order.get_orderline()
        self.assertEqual(
            expect, got, msg='Failed: expect: \{}, got: \{}'.format(expect, got))

    def test_receive(self, ):
        got = self.order.receive('OK\n')
        self.assertIsInstance(got, order.CommandReceiver)

    def test_set_command(self, ):
        expect = DummyCommand()
        self.order.set_command(expect)
        self.assertEqual(expect, self.order._command)

    def test_get_command(self, ):
        got = self.order.get_command()
        self.assertEqual(
            self.command, got,
            msg='Failed:  expect: \{}, got: \{}'.format(self.command, got))

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        pass


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_commandorder.py ends here
