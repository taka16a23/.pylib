#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_pattern_factory.py

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
import sys
import unittest

import patterns


PatternFactory = patterns.PatternFactory


class TestPatternFactory(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        pass

    def test_normal_yuubin_bangou(self, ):
        """郵便番号正常系テスト

        test_yuubin_bangou()

        @Return:

        @Error:
        """
        regexp = PatternFactory.create_yuubin_bangou()
        self.assertIsNotNone(regexp.match('333-5555'))

    ABNORMAL_YUUBIN_BANGOU_LIST = (
        '33-5555',     #最初の3桁の桁数が不足
        '333-555',     #最後の4桁の桁数が不足
        '3333-5555',   #最初の3桁の桁数が超過
        '333-55555',   #最後の4桁の桁数が超過
        '3A3-5555',    #最初の3桁に数値以外の文字の混入
        '333-5X55',    #最後の4桁に数値以外の文字の混入
        '333-5555a',   #最後の4桁後に数値以外の文字追加
        'a333-5555',   #最初の3桁前に数値以外の文字追加
    )

    def test_abnormal_yuubin_bangou(self, ):
        """郵便番号異常系テスト

        test_abnormal_yuubin_bangou()

        @Return:

        @Error:
        """
        # require
        regexp = PatternFactory.create_yuubin_bangou(fullmatch=True)

        # do
        for string in TestPatternFactory.ABNORMAL_YUUBIN_BANGOU_LIST:
            self.assertIsNone(
                regexp.match(string),
                msg='Failed: 異常系テスト "{0}"で一致しました'.format(string))
        # ensure

    def test_normal_yuubin_bangou_none_hyphen(self, ):
        """郵便番号ハイフン無し 正常系テスト

        test_yuubin_bangou_none_hyphen()

        @Return:

        @Error:
        """
        regexp = PatternFactory.create_yuubin_bangou_none_hyphen()
        self.assertIsNotNone(regexp.match('3335555'))

    ABNORMAL_YUUBIN_BANGOU_NONE_HYPHEN_LIST = (
        '333555',     #桁数が不足
        '33355555',   #桁数が超過
        '3A35555',    #数値以外の文字の混入
        '3335555a',   #最後に数値以外の文字追加
        'a3335555',   #最初に数値以外の文字追加
    )

    def test_abnormal_yuubin_bangou_none_hyphen(self, ):
        """郵便番号ハイフン無し 異常系テスト

        test_abnormal_yuubin_bangou_none_hyphen()

        @Return:

        @Error:
        """
        # require
        regexp = PatternFactory.create_yuubin_bangou_none_hyphen(fullmatch=True)

        # do
        for string in TestPatternFactory.ABNORMAL_YUUBIN_BANGOU_NONE_HYPHEN_LIST:
            self.assertIsNone(
                regexp.match(string),
                msg='Failed: 異常系テスト "{0}"で一致しました'.format(string))

    def test_normal_phone_number_jp(self, ):
        """SUMMARY

        test_normal_phone_number_jp()

        @Return:

        @Error:
        """
        # require
        regexp = PatternFactory.create_phone_number_jp()
        # do
        self.assertIsNotNone(regexp.match('077-574-8202'))
        self.assertIsNotNone(regexp.match('090-5744-8202'))
        self.assertIsNotNone(regexp.match('050-5744-8202'))

    def test_abnormal_phone_number_jp(self, ):
        """SUMMARY

        test_abnormal_phone_number_jp()

        @Return:

        @Error:
        """
        # require
        regexp = PatternFactory.create_phone_number_jp(fullmatch=True)

        # do
        abnormal_fixed_phone_number_jp_list = (
            '07-574-8202',   #最初の桁数が不足
            '0774-574-8202', #最初の桁数が超過
            '07a-574-8202',  #最初に不正な文字
            '077-57-8202',   #２番目の桁数が不足
            '077-5744-8202', #２番目の桁数が超過
            '077-57a-8202',  #２番目に不正な文字
            '077-574-820',   #最後の4桁の桁数が不足
            '077-574-82022', #最後の4桁の桁数が超過
            '077-574-820a',  #最後に不正な文字
            '0120-574-8202', #フリーダイアル
            # TODO: (Atami) [2018/05/28]

        )

        for string in abnormal_fixed_phone_number_jp_list:
            self.assertIsNone(regexp.match(string),
                            msg='Failed: 異常系テスト "{0}"で一致しました'.format(string))

        # ensure

    def test_normal_fixed_phone_number_jp(self, ):
        """SUMMARY

        test_normal_fixed_phone_number_jp()

        @Return:

        @Error:
        """
        # require
        regexp = PatternFactory.create_fixed_phone_number_jp()

        # do
        self.assertIsNotNone(regexp.match('077-574-8202'))

    def test_abnormal_fixed_phone_number_jp(self, ):
        """SUMMARY

        test_abnormal_fixed_phone_number_jp()

        @Return:

        @Error:
        """
        # require
        regexp = PatternFactory.create_fixed_phone_number_jp(fullmatch=True)

        abnormal_fixed_phone_number_jp_list = (
            '07-574-8202',   #最初の桁数が不足
            '0774-574-8202', #最初の桁数が超過
            '07a-574-8202',  #最初に不正な文字
            '077-57-8202',   #２番目の桁数が不足
            '077-5744-8202', #２番目の桁数が超過
            '077-57a-8202',  #２番目に不正な文字
            '077-574-820',   #最後の4桁の桁数が不足
            '077-574-82022', #最後の4桁の桁数が超過
            '077-574-820a',  #最後に不正な文字
            '090-5744-8202',  #携帯番号
            '050-5744-8202',  #IP電話番号
            '0120-574-8202', #フリーダイアル
        )
        # do
        for string in abnormal_fixed_phone_number_jp_list:
            self.assertIsNone(regexp.match(string),
                            msg='Failed: 異常系テスト "{0}"で一致しました'.format(string))

        # ensure

    def test_normal_fixed_phone_number_none_hyphen_jp(self, ):
        """SUMMARY

        test_normal_fixed_phone_number_jp()

        @Return:

        @Error:
        """
        # require
        regexp = PatternFactory.create_fixed_phone_number_none_hyphen_jp()
        # do
        self.assertIsNotNone(regexp.match('0775748202'))
        # ensure

    def test_abnormal_fixed_phone_number_none_hyphen_jp(self, ):
        """SUMMARY

        test_abnormal_fixed_phone_number_none_hyphen_jp()

        @Return:

        @Error:
        """
        regexp = PatternFactory.create_fixed_phone_number_none_hyphen_jp(
            fullmatch=True)
        abnormal_fixed_phone_number_none_hyphen_jp = (
            '07757482022',  #桁数が超過
            '077574820',    #桁数が不足
            '07757482a2',   #不正な文字が混入
            '0905748202',   #携帯電話番号
            '077-574-8202', #ハイフン有
            )

        # do
        for string in abnormal_fixed_phone_number_none_hyphen_jp:
            self.assertIsNone(regexp.match(string),
                            msg='Failed: 異常系テスト "{0}"で一致しました'.format(string))

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        pass



def _main():
    unittest.main()
    return 0

if __name__ == '__main__':
    sys.exit(_main())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_pattern_factory.py ends here
