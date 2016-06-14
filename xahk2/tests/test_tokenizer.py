#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_tokenizer.py

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
from itertools import izip

from mocker import *
from xahk2.input.sendkeys.token import Tokenizer, TokenTypes, Token


class TestToken(MockerTestCase):
    """2015/12/06"""
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.mocker.replay()

    def test_repr(self):
        token = Token(TokenTypes.KEY_NAME, 'a')
        self.assertEqual('Token(types=KEY_NAME, value="a")', repr(token))

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        pass


class TestTokenizer(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.mocker.replay()

    def test_tokenizer_abc(self, ):
        tokenizer = Tokenizer('abc')
        expects = [Token(TokenTypes.KEY_NAME, 'a'),
                   Token(TokenTypes.KEY_NAME, 'b'),
                   Token(TokenTypes.KEY_NAME, 'c')]
        for expect_token, token in izip(expects, tokenizer):
            self.assertTrue(token.equal(expect_token))

    def test_list_tokens(self, ):
        tokenizer = Tokenizer('abc')
        expects = [Token(TokenTypes.KEY_NAME, 'a'),
                   Token(TokenTypes.KEY_NAME, 'b'),
                   Token(TokenTypes.KEY_NAME, 'c')]
        for expect_token, token in izip(expects, tokenizer.list_tokens()):
            self.assertTrue(token.equal(expect_token))

    def test_count_tokens(self, ):
        tokenizer = Tokenizer('abc')
        self.assertEqual(3, tokenizer.count_tokens())

    def test_set_string(self, ):
        tokenizer = Tokenizer('abc')
        self.assertEqual('abc', tokenizer.get_string())
        tokenizer.set_string('def')
        self.assertEqual('def', tokenizer.get_string())

    def test_tokenizer_modifier(self, ):
        tokenizer = Tokenizer('+d^e#f!j')
        expects = [Token(TokenTypes.MODIFIER, '+'),
                   Token(TokenTypes.KEY_NAME, 'd'),
                   Token(TokenTypes.MODIFIER, '^'),
                   Token(TokenTypes.KEY_NAME, 'e'),
                   Token(TokenTypes.MODIFIER, '#'),
                   Token(TokenTypes.KEY_NAME, 'f'),
                   Token(TokenTypes.MODIFIER, '!'),
                   Token(TokenTypes.KEY_NAME, 'j'),
        ]
        for expect_token, token in izip(expects, tokenizer):
            self.assertTrue(token.equal(expect_token))

    def test_tokenizer_parenthesis(self, ):
        tokenizer = Tokenizer('{plus}')
        expects = [Token(TokenTypes.KEY_NAME, 'plus'),
        ]
        for expect_token, token in izip(expects, tokenizer):
            self.assertTrue(token.equal(expect_token))

    def test_tokenizer_parenthesis_repeat(self, ):
        tokenizer = Tokenizer('{plus 100}')
        expects = [Token(TokenTypes.KEY_NAME, 'plus'),
                   Token(TokenTypes.REPEAT, '100'),
        ]
        for expect_token, token in izip(expects, tokenizer):
            self.assertTrue(token.equal(expect_token))

    def test_tokenizer_parenthesis_keycode(self, ):
        tokenizer = Tokenizer('{100}')
        expects = [Token(TokenTypes.KEYCODE, '100'),
        ]
        for expect_token, token in izip(expects, tokenizer):
            self.assertTrue(token.equal(expect_token))

    def test_tokenizer_parenthesis_buttoncode(self, ):
        tokenizer = Tokenizer('{2}')
        expects = [Token(TokenTypes.BUTTONCODE, '2'),
        ]
        for expect_token, token in izip(expects, tokenizer):
            self.assertTrue(token.equal(expect_token))

    def test_tokenizer_parenthesis_buttonname_behave_point(self, ):
        tokenizer = Tokenizer('{MButton Press 100-100}')
        expects = [Token(TokenTypes.BUTTON_NAME, 'MButton'),
                   Token(TokenTypes.BEHAVE, 'Press'),
                   Token(TokenTypes.POINT, '100-100'),
        ]
        for expect_token, token in izip(expects, tokenizer):
            self.assertTrue(token.equal(expect_token))

    def test_tokenizer_parenthesis_uppper_key_name(self, ):
        tokenizer = Tokenizer('{H}{E}{L}{L}{O}')
        expects = [Token(TokenTypes.KEY_NAME, 'H'),
                   Token(TokenTypes.KEY_NAME, 'E'),
                   Token(TokenTypes.KEY_NAME, 'L'),
                   Token(TokenTypes.KEY_NAME, 'L'),
                   Token(TokenTypes.KEY_NAME, 'O'),
        ]
        for expect_token, token in izip(expects, tokenizer):
            self.assertTrue(token.equal(expect_token))

    def test_tokenizer_uppper_key_name(self, ):
        tokenizer = Tokenizer('HELLO')
        expects = [Token(TokenTypes.KEY_NAME, 'H'),
                   Token(TokenTypes.KEY_NAME, 'E'),
                   Token(TokenTypes.KEY_NAME, 'L'),
                   Token(TokenTypes.KEY_NAME, 'L'),
                   Token(TokenTypes.KEY_NAME, 'O'),
        ]
        for expect_token, token in izip(expects, tokenizer):
            self.assertTrue(token.equal(expect_token))

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        pass



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_tokenizer.py ends here
