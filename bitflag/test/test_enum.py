#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_enum.py

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
from mocker import MockerTestCase
from bitflag.flagenum import FlagEnum


class TestEnum(MockerTestCase):
    def setUp(self):

        self.mocker.replay()

    def test_flagenum0(self):
        r"""FlagEnum.flag0"""
        self.assertEqual(FlagEnum.flag0, 0, msg='Failed: flag0')

    def test_flagenum1(self):
        r"""FlagEnum.flag1"""
        self.assertEqual(FlagEnum.flag1, 1, msg='Failed: flag1')

    def test_flagenum2(self):
        r"""FlagEnum.flag2"""
        self.assertEqual(FlagEnum.flag2, 1 << 1, msg='Failed: flag2')

    def test_flagenum3(self):
        r"""FlagEnum.flag3"""
        self.assertEqual(FlagEnum.flag3, 1 << 2, msg='Failed: flag3')

    def test_flagenum4(self):
        r"""FlagEnum.flag4"""
        self.assertEqual(FlagEnum.flag4, 1 << 3, msg='Failed: flag4')

    def test_flagenum5(self):
        r"""FlagEnum.flag5"""
        self.assertEqual(FlagEnum.flag5, 1 << 4, msg='Failed: flag5')

    def test_flagenum6(self):
        r"""FlagEnum.flag6"""
        self.assertEqual(FlagEnum.flag6, 1 << 5, msg='Failed: flag6')

    def test_flagenum7(self):
        r"""FlagEnum.flag7"""
        self.assertEqual(FlagEnum.flag7, 1 << 6, msg='Failed: flag7')

    def test_flagenum8(self):
        r"""FlagEnum.flag8"""
        self.assertEqual(FlagEnum.flag8, 1 << 7, msg='Failed: flag8')

    def test_flagenum9(self):
        r"""FlagEnum.flag9"""
        self.assertEqual(FlagEnum.flag9, 1 << 8, msg='Failed: flag9')

    def test_flagenum10(self):
        r"""FlagEnum.flag10"""
        self.assertEqual(FlagEnum.flag10, 1 << 9, msg='Failed: flag10')

    def test_flagenum11(self):
        r"""FlagEnum.flag11"""
        self.assertEqual(FlagEnum.flag11, 1 << 10, msg='Failed: flag11')

    def test_flagenum12(self):
        r"""FlagEnum.flag12"""
        self.assertEqual(FlagEnum.flag12, 1 << 11, msg='Failed: flag12')

    def test_flagenum13(self):
        r"""FlagEnum.flag13"""
        self.assertEqual(FlagEnum.flag13, 1 << 12, msg='Failed: flag13')

    def test_flagenum14(self):
        r"""FlagEnum.flag14"""
        self.assertEqual(FlagEnum.flag14, 1 << 13, msg='Failed: flag14')

    def test_flagenum15(self):
        r"""FlagEnum.flag15"""
        self.assertEqual(FlagEnum.flag15, 1 << 14, msg='Failed: flag15')

    def test_flagenum16(self):
        r"""FlagEnum.flag16"""
        self.assertEqual(FlagEnum.flag16, 1 << 15, msg='Failed: flag16')

    def tearDown(self):
        pass



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_enum.py ends here
