#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: test_tokenize.py 141 2014-04-09 09:42:16Z t1 $
# $Revision: 141 $
# $Date: 2014-04-09 18:42:16 +0900 (Wed, 09 Apr 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-04-09 18:42:16 +0900 (Wed, 09 Apr 2014) $

r"""Name: test_tokenize.py

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
from sendkeys.tokenize import Tokenize
from sendkeys.code import KeyCode


# class TestTokenize(MockerTestCase):
#     def setUp(self):

#         self.mocker.replay()

#     def test_itertoken(self):
#         r"""itertoken
#         """
#         maps = {'hello': ('h', 'e', 'l', 'l', 'o'),
#         'hoge{plus}foo': ('h', 'o', 'g', 'e', 'plus', 'f', 'o', 'o'),
#         'hoge{plus}foo{numbersign}': (
#             'h', 'o', 'g', 'e', 'plus', 'f', 'o', 'o', 'numbersign'),
#             }
#         for key, values in maps.iteritems():
#             for analyze, expects in zip(Tokenize(key).itertoken(), values):
#                 self.assertEqual(analyze._token, expects,
#                                  msg='Failed: {}, got: {}'
#                                  .format(key, analyze._token))

#     def tearDown(self):
#         pass


# class TestTokens(MockerTestCase):
#     r"""SUMMARY
#     """

#     def setUp(self):
#         self.tokens = Tokenize('hello{+}wOrLd')
#         self.mocker.replay()

#     def test_tokens(self, ):
#         r"""SUMMARY

#         test_tokens()

#         @Return:
#         """
#         expects = [KeyCode(43), # 'h'
#                    KeyCode(26), # 'e'
#                    KeyCode(46), # 'l'
#                    KeyCode(46), # 'l'
#                    KeyCode(32), # 'o'
#                    KeyCode(20, 1), # '+'
#                    KeyCode(25), # 'w'
#                    KeyCode(32, 1), # 'o'
#                    KeyCode(27), # 'r'
#                    KeyCode(46, 1), # 'L'
#                    KeyCode(40), # 'd'
#         ]
#         for tokn, exp in zip(iter(self.tokens), expects):
#             self.assertEqual(tokn, exp, msg='Failed: tokn:{}, exp:{}'
#                              .format(tokn, exp))

#     def tearDown(self):
#         pass



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_tokenize.py ends here
