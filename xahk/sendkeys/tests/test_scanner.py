#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_scanner.py

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
from ..scanner import Scanner, Token, TokenType

TOKENS_SAMPLE = {'hello': (Token(TokenType.key, 'h'),
                           Token(TokenType.key, 'e'),
                           Token(TokenType.key, 'l'),
                           Token(TokenType.key, 'l'),
                           Token(TokenType.key, 'o'),),
                 'hello{plus}': (Token(TokenType.key, 'h'),
                                 Token(TokenType.key, 'e'),
                                 Token(TokenType.key, 'l'),
                                 Token(TokenType.key, 'l'),
                                 Token(TokenType.key, 'o'),
                                 Token(TokenType.curly, '{'),
                                 Token(TokenType.key, 'plus'),
                                 Token(TokenType.curly, '}'),),
                 'hello{plus}world': (Token(TokenType.key, 'h'),
                                      Token(TokenType.key, 'e'),
                                      Token(TokenType.key, 'l'),
                                      Token(TokenType.key, 'l'),
                                      Token(TokenType.key, 'o'),
                                      Token(TokenType.curly, '{'),
                                      Token(TokenType.key, 'plus'),
                                      Token(TokenType.curly, '}'),
                                      Token(TokenType.key, 'w'),
                                      Token(TokenType.key, 'o'),
                                      Token(TokenType.key, 'r'),
                                      Token(TokenType.key, 'l'),
                                      Token(TokenType.key, 'd'),),
                 '{k}': (Token(TokenType.curly, '{'),
                         Token(TokenType.key, 'k'),
                         Token(TokenType.curly, '}'), ),
                 '+k#k!k^k': (Token(TokenType.modifier, '+'),
                              Token(TokenType.key, 'k'),
                              Token(TokenType.modifier, '#'),
                              Token(TokenType.key, 'k'),
                              Token(TokenType.modifier, '!'),
                              Token(TokenType.key, 'k'),
                              Token(TokenType.modifier, '^'),
                              Token(TokenType.key, 'k'),),

                 '{plus}': (Token(TokenType.curly, '{'),
                            Token(TokenType.key, 'plus'),
                            Token(TokenType.curly, '}'), ),
                 '{plus press}': (Token(TokenType.curly, '{'),
                                  Token(TokenType.key, 'plus'),
                                  Token(TokenType.behave, 'press'),
                                  Token(TokenType.curly, '}'), ),
                 '{plus 1}': (Token(TokenType.curly, '{'),
                              Token(TokenType.key, 'plus'),
                              Token(TokenType.repeat, 1),
                              Token(TokenType.curly, '}'), ),

                 '{lbutton}': (Token(TokenType.curly, '{'),
                               Token(TokenType.button, 'lbutton'),
                               Token(TokenType.curly, '}'), ),
                 '{lbutton 1}': (Token(TokenType.curly, '{'),
                                 Token(TokenType.button, 'lbutton'),
                                 Token(TokenType.repeat, 1),
                                 Token(TokenType.curly, '}'), ),
                 '{lbutton 1 1}': (Token(TokenType.curly, '{'),
                                   Token(TokenType.button, 'lbutton'),
                                   Token(TokenType.geometry, 1),
                                   Token(TokenType.geometry, 1),
                                   Token(TokenType.curly, '}'), ),
}


class TestScanner(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.scanner = Scanner()
        self.mocker.replay()

    def test_scan(self, ):
        for line, tokens in TOKENS_SAMPLE.iteritems():
            results = self.scanner.scan(line)
            self.assertEqual(list(tokens), results)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        pass



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_scanner.py ends here
