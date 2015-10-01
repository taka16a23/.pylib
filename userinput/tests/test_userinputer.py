#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_userinputer.py

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
from userinput.userinputer import UserInputer
from userinput.userinput import CommandlineUserInput, FileUserInput


class TestUserInputer(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.sampletext = 'sampletext'

    def setUp(self):
        self.inputer = UserInputer(CommandlineUserInput(self.sampletext))
        self.mocker.replay()

    def test_input(self, ):
        expect = self.sampletext
        got = self.inputer.input()
        self.assertEqual(
            expect, got, msg='Failed: UserInputer.input expect: \{}, got: \{}'
            .format(expect, got))

    def test_set_inputer(self, ):
        expect = FileUserInput('')
        self.inputer.set_inputer(expect)
        got = self.inputer.get_inputer()
        self.assertEqual(
            expect, got,
            msg='Failed: UserInputer.set_inputer expect: \{}, got: \{}'
            .format(expect, got))

    def test_get_inputer(self, ):
        got = self.inputer.get_inputer()
        self.assertIsInstance(got, CommandlineUserInput)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        pass


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_userinputer.py ends here
