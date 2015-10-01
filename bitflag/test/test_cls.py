#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: test_cls.py 146 2014-04-12 09:38:34Z t1 $
# $Revision: 146 $
# $Date: 2014-04-12 18:38:34 +0900 (Sat, 12 Apr 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-04-12 18:38:34 +0900 (Sat, 12 Apr 2014) $

r"""Name: test_cls.py

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
from bitflag.cls import BitFlag8, BitFlag16, BitFlag32


class TestBitFlag_Special_method(MockerTestCase):
    """2014/04/12"""

    def setUp(self):
        self.bitflag8 = BitFlag8(0)
        self.mocker.replay()

    def test___int__(self):
        r"""__int__."""
        self.assertEqual(int(self.bitflag8), 0, msg='Failed: __int__')

    def test___eq__(self, ):
        r"""__eq__."""
        self.assertTrue(self.bitflag8 == 0)

    def test___ne__(self, ):
        r"""__ne__."""
        self.assertTrue(self.bitflag8 != 1)

    def test___hash__(self, ):
        r"""__hash__."""
        self.assertEqual(hash(self.bitflag8), hash(0), msg='Failed: __hash__')

    def test___and__(self, ):
        r"""__and__."""
        self.bitflag8.set1()
        self.assertTrue(self.bitflag8.isflaged1())
        self.assertEqual(self.bitflag8 & 1, 1, msg='Failed: __and__')

    def test___xor__(self, ):
        r"""__xor__."""
        self.bitflag8.set1()
        self.assertTrue(self.bitflag8.isflaged1())
        self.assertEqual(self.bitflag8 ^ 1, 0, msg='Failed: __xor__')

    def test___or__(self, ):
        r"""__or__."""
        self.assertEqual(self.bitflag8 | 1, 1, msg='Failed: __or__')

    def test___lshift__(self, ):
        r"""__lshift__."""
        self.bitflag8.set1()
        self.assertTrue(self.bitflag8.isflaged1())
        self.assertEqual(self.bitflag8 << 1, 2, msg='Failed: __lshift__')

    def test___rshift__(self, ):
        r"""__rshift__."""
        self.bitflag8.set2()
        self.assertTrue(self.bitflag8.isflaged2())
        self.assertEqual(self.bitflag8 >> 1, 1, msg='Failed: __rshift__')

    # def test___invert__(self, ):
    #     r"""__invert__."""
    #     self.bitflag8.set1()
    #     self.assertTrue(self.bitflag8.isflaged1())
    #     self.assertEqual(~self.bitflag8, -2, msg='Failed: ')

    def test___iand__(self, ):
        r"""__iand__."""
        self.bitflag8.set1()
        self.assertTrue(self.bitflag8.isflaged1())
        self.bitflag8 &= 1
        self.assertEqual(self.bitflag8, 1, msg='Failed: __iand__')

    def test___ixor__(self, ):
        r"""__ixor__."""
        self.bitflag8.set1()
        self.assertTrue(self.bitflag8.isflaged1())
        self.bitflag8 ^= 1
        self.assertEqual(self.bitflag8, 0, msg='Failed: __ixor__')

    def test___ior__(self, ):
        r"""__ior__."""
        self.bitflag8 |= 1
        self.assertEqual(self.bitflag8, 1, msg='Failed: __ior__')

    def test___ilshift__(self, ):
        r"""__ilshift__."""
        self.bitflag8.set1()
        self.assertTrue(self.bitflag8.isflaged1())
        self.bitflag8 <<= 1
        self.assertEqual(self.bitflag8, 2, msg='Failed: __ilshift__')

    def test___irshift__(self, ):
        r"""__irshift__."""
        self.bitflag8.set2()
        self.assertTrue(self.bitflag8.isflaged2())
        self.bitflag8 >>= 1
        self.assertEqual(self.bitflag8, 1, msg='Failed: __irshift__')

    def test___nonzero__(self, ):
        r"""__nonzero__."""
        self.bitflag8.set1()
        self.assertTrue(self.bitflag8.isflaged1())
        self.assertTrue(bool(self.bitflag8))

    def test___contains__(self, ):
        r"""__contains__."""
        self.bitflag8.set1()
        self.assertTrue(self.bitflag8.isflaged1())
        self.assertTrue(1 in self.bitflag8)

    def test___repr__(self, ):
        r"""__repr__."""
        self.assertEqual(repr(self.bitflag8), 'BitFlag8(0)',
                         msg='Failed: __repr__')

    def tearDown(self):
        pass


class TestBitFlag_str(MockerTestCase):
    """2014/04/12"""

    def setUp(self):
        self.bitflag = BitFlag32()
        self.mocker.replay()

    def test___str__(self):
        r"""__str__."""
        self.bitflag.set1()
        self.assertTrue(self.bitflag.isflaged1())
        self.assertEqual(str(self.bitflag), '1', msg='Failed: str bit1')

        self.bitflag.set2()
        self.assertTrue(self.bitflag.isflaged2())
        self.assertEqual(str(self.bitflag), '11', msg='Failed: str bit2')

        self.bitflag.set3()
        self.assertTrue(self.bitflag.isflaged3())
        self.assertEqual(str(self.bitflag), '111', msg='Failed: str bit3')

        self.bitflag.set4()
        self.assertTrue(self.bitflag.isflaged4())
        self.assertEqual(str(self.bitflag), '1111', msg='Failed: str bit4')

        self.bitflag.set5()
        self.assertTrue(self.bitflag.isflaged5())
        self.assertEqual(str(self.bitflag), '11111', msg='Failed: str bit5')

        self.bitflag.set6()
        self.assertTrue(self.bitflag.isflaged6())
        self.assertEqual(str(self.bitflag), '111111', msg='Failed: str bit6')

        self.bitflag.set7()
        self.assertTrue(self.bitflag.isflaged7())
        self.assertEqual(str(self.bitflag), '1111111', msg='Failed: str bit7')

        self.bitflag.set8()
        self.assertTrue(self.bitflag.isflaged8())
        self.assertEqual(str(self.bitflag), '11111111', msg='Failed: str bit8')

        self.bitflag.set9()
        self.assertTrue(self.bitflag.isflaged9())
        self.assertEqual(str(self.bitflag), '111111111', msg='Failed: str bit9')

        self.bitflag.set10()
        self.assertTrue(self.bitflag.isflaged10())
        self.assertEqual(str(self.bitflag), '1111111111',
                         msg='Failed: str bit10')

        self.bitflag.set11()
        self.assertTrue(self.bitflag.isflaged11())
        self.assertEqual(str(self.bitflag), '11111111111',
                         msg='Failed: str bit11')

        self.bitflag.set12()
        self.assertTrue(self.bitflag.isflaged12())
        self.assertEqual(str(self.bitflag), '111111111111',
                         msg='Failed: str bit12')

        self.bitflag.set13()
        self.assertTrue(self.bitflag.isflaged13())
        self.assertEqual(str(self.bitflag), '1111111111111',
                         msg='Failed: str bit13')

        self.bitflag.set14()
        self.assertTrue(self.bitflag.isflaged14())
        self.assertEqual(str(self.bitflag), '11111111111111',
                         msg='Failed: str bit14')

        self.bitflag.set15()
        self.assertTrue(self.bitflag.isflaged15())
        self.assertEqual(str(self.bitflag), '111111111111111',
                         msg='Failed: str bit15')

        self.bitflag.set16()
        self.assertTrue(self.bitflag.isflaged16())
        self.assertEqual(str(self.bitflag), '1111111111111111',
                         msg='Failed: str bit16')

        self.bitflag.set17()
        self.assertTrue(self.bitflag.isflaged17())
        self.assertEqual(str(self.bitflag), '11111111111111111',
                         msg='Failed: str bit17')

        self.bitflag.set18()
        self.assertTrue(self.bitflag.isflaged18())
        self.assertEqual(str(self.bitflag), '111111111111111111',
                         msg='Failed: str bit18')

        self.bitflag.set19()
        self.assertTrue(self.bitflag.isflaged19())
        self.assertEqual(str(self.bitflag), '1111111111111111111',
                         msg='Failed: str bit19')

        self.bitflag.set20()
        self.assertTrue(self.bitflag.isflaged20())
        self.assertEqual(str(self.bitflag), '11111111111111111111',
                         msg='Failed: str bit20')

        self.bitflag.set21()
        self.assertTrue(self.bitflag.isflaged21())
        self.assertEqual(str(self.bitflag), '111111111111111111111',
                         msg='Failed: str bit21')

        self.bitflag.set22()
        self.assertTrue(self.bitflag.isflaged22())
        self.assertEqual(str(self.bitflag), '1111111111111111111111',
                         msg='Failed: str bit22')

        self.bitflag.set23()
        self.assertTrue(self.bitflag.isflaged23())
        self.assertEqual(str(self.bitflag), '11111111111111111111111',
                         msg='Failed: str bit23')

        self.bitflag.set24()
        self.assertTrue(self.bitflag.isflaged24())
        self.assertEqual(str(self.bitflag), '111111111111111111111111',
                         msg='Failed: str bit24')

        self.bitflag.set25()
        self.assertTrue(self.bitflag.isflaged25())
        self.assertEqual(str(self.bitflag), '1111111111111111111111111',
                         msg='Failed: str bit25')

        self.bitflag.set26()
        self.assertTrue(self.bitflag.isflaged26())
        self.assertEqual(str(self.bitflag), '11111111111111111111111111',
                         msg='Failed: str bit26')

        self.bitflag.set27()
        self.assertTrue(self.bitflag.isflaged27())
        self.assertEqual(str(self.bitflag), '111111111111111111111111111',
                         msg='Failed: str bit27')

        self.bitflag.set28()
        self.assertTrue(self.bitflag.isflaged28())
        self.assertEqual(str(self.bitflag), '1111111111111111111111111111',
                         msg='Failed: str bit28')

        self.bitflag.set29()
        self.assertTrue(self.bitflag.isflaged29())
        self.assertEqual(str(self.bitflag), '11111111111111111111111111111',
                         msg='Failed: str bit29')

    def tearDown(self):
        pass


class TestBitFlag8_set(MockerTestCase):
    def setUp(self):
        self.bitflag8 = BitFlag8(0)
        self.mocker.replay()

    def test_clear(self):
        r"""clear"""
        self.bitflag8.set1()
        self.assertEqual(self.bitflag8, 1)
        self.bitflag8.clear()
        self.assertEqual(self.bitflag8, 0, msg='Failed: clear')

    def test_set1(self, ):
        r"""set1."""
        self.bitflag8.set1()
        self.assertEqual(self.bitflag8, 1, msg='Failed: set1')

    def test_set2(self, ):
        r"""set2."""
        self.bitflag8.set2()
        self.assertEqual(self.bitflag8, 1 << 1, msg='Failed: set2')

    def test_set3(self, ):
        r"""set3."""
        self.bitflag8.set3()
        self.assertEqual(self.bitflag8, 1 << 2, msg='Failed: set3')

    def test_set4(self, ):
        r"""set4."""
        self.bitflag8.set4()
        self.assertEqual(self.bitflag8, 1 << 3, msg='Failed: set4')

    def test_set5(self, ):
        r"""set5."""
        self.bitflag8.set5()
        self.assertEqual(self.bitflag8, 1 << 4, msg='Failed: set5')

    def test_set6(self, ):
        r"""set6."""
        self.bitflag8.set6()
        self.assertEqual(self.bitflag8, 1 << 5, msg='Failed: set6')

    def test_set7(self, ):
        r"""set7."""
        self.bitflag8.set7()
        self.assertEqual(self.bitflag8, 1 << 6, msg='Failed: set7')

    def test_set8(self, ):
        r"""set8."""
        self.bitflag8.set8()
        self.assertEqual(self.bitflag8, 1 << 7, msg='Failed: set8')

    def tearDown(self):
        pass


class TestBitFlag8_is(MockerTestCase):
    """2014/04/11"""

    def setUp(self):
        self.bitflag8 = BitFlag8(0)
        self.mocker.replay()

    def test_isflaged1(self):
        r"""isflaged1."""
        self.bitflag8.set1()
        self.assertTrue(self.bitflag8.isflaged1())

    def test_isflaged2(self):
        r"""isflaged2."""
        self.bitflag8.set2()
        self.assertTrue(self.bitflag8.isflaged2())

    def test_isflaged3(self):
        r"""isflaged3."""
        self.bitflag8.set3()
        self.assertTrue(self.bitflag8.isflaged3())

    def test_isflaged4(self):
        r"""isflaged4."""
        self.bitflag8.set4()
        self.assertTrue(self.bitflag8.isflaged4())

    def test_isflaged5(self):
        r"""isflaged5."""
        self.bitflag8.set5()
        self.assertTrue(self.bitflag8.isflaged5())

    def test_isflaged6(self):
        r"""isflaged6."""
        self.bitflag8.set6()
        self.assertTrue(self.bitflag8.isflaged6())

    def test_isflaged7(self):
        r"""isflaged7."""
        self.bitflag8.set7()
        self.assertTrue(self.bitflag8.isflaged7())

    def test_isflaged8(self):
        r"""isflaged8."""
        self.bitflag8.set8()
        self.assertTrue(self.bitflag8.isflaged8())

    def tearDown(self):
        pass


class TestBitFlag8_reset(MockerTestCase):
    """2014/04/11"""

    def setUp(self):
        self.bitflag8 = BitFlag8(255) # all set
        self.mocker.replay()

    def test_reset1(self):
        r"""reset1."""
        self.bitflag8.reset1()
        self.assertFalse(self.bitflag8.isflaged1())

    def test_reset2(self):
        r"""reset2."""
        self.bitflag8.reset2()
        self.assertFalse(self.bitflag8.isflaged2())

    def test_reset3(self):
        r"""reset3."""
        self.bitflag8.reset3()
        self.assertFalse(self.bitflag8.isflaged3())

    def test_reset4(self):
        r"""reset4."""
        self.bitflag8.reset4()
        self.assertFalse(self.bitflag8.isflaged4())

    def test_reset5(self):
        r"""reset5."""
        self.bitflag8.reset5()
        self.assertFalse(self.bitflag8.isflaged5())

    def test_reset6(self):
        r"""reset6."""
        self.bitflag8.reset6()
        self.assertFalse(self.bitflag8.isflaged6())

    def test_reset7(self):
        r"""reset7."""
        self.bitflag8.reset7()
        self.assertFalse(self.bitflag8.isflaged7())

    def test_reset8(self):
        r"""reset8."""
        self.bitflag8.reset8()
        self.assertFalse(self.bitflag8.isflaged8())

    def tearDown(self):
        pass


class TestBitFlag16_set(MockerTestCase):
    def setUp(self):
        self.bitflag16 = BitFlag16(0)
        self.mocker.replay()

    def test_set9(self, ):
        r"""set9."""
        self.bitflag16.set9()
        self.assertEqual(self.bitflag16, 1 << 8, msg='Failed: set9')

    def test_set10(self, ):
        r"""set10."""
        self.bitflag16.set10()
        self.assertEqual(self.bitflag16, 1 << 9, msg='Failed: set10')

    def test_set11(self, ):
        r"""set11."""
        self.bitflag16.set11()
        self.assertEqual(self.bitflag16, 1 << 10, msg='Failed: set11')

    def test_set12(self, ):
        r"""set12."""
        self.bitflag16.set12()
        self.assertEqual(self.bitflag16, 1 << 11, msg='Failed: set12')

    def test_set13(self, ):
        r"""set13."""
        self.bitflag16.set13()
        self.assertEqual(self.bitflag16, 1 << 12, msg='Failed: set13')

    def test_set14(self, ):
        r"""set14."""
        self.bitflag16.set14()
        self.assertEqual(self.bitflag16, 1 << 13, msg='Failed: set14')

    def test_set15(self, ):
        r"""set15."""
        self.bitflag16.set15()
        self.assertEqual(self.bitflag16, 1 << 14, msg='Failed: set15')

    def test_set16(self, ):
        r"""set16."""
        self.bitflag16.set16()
        self.assertEqual(self.bitflag16, 1 << 15, msg='Failed: set16')

    def tearDown(self):
        pass


class TestBitFlag16_is(MockerTestCase):
    """2014/04/11"""

    def setUp(self):
        self.bitflag16 = BitFlag16(0)
        self.mocker.replay()

    def test_isflaged9(self):
        r"""isflaged9."""
        self.bitflag16.set9()
        self.assertTrue(self.bitflag16.isflaged9())

    def test_isflaged10(self):
        r"""isflaged10."""
        self.bitflag16.set10()
        self.assertTrue(self.bitflag16.isflaged10())

    def test_isflaged11(self):
        r"""isflaged11."""
        self.bitflag16.set11()
        self.assertTrue(self.bitflag16.isflaged11())

    def test_isflaged12(self):
        r"""isflaged12."""
        self.bitflag16.set12()
        self.assertTrue(self.bitflag16.isflaged12())

    def test_isflaged13(self):
        r"""isflaged13."""
        self.bitflag16.set13()
        self.assertTrue(self.bitflag16.isflaged13())

    def test_isflaged14(self):
        r"""isflaged14."""
        self.bitflag16.set14()
        self.assertTrue(self.bitflag16.isflaged14())

    def test_isflaged15(self):
        r"""isflaged15."""
        self.bitflag16.set15()
        self.assertTrue(self.bitflag16.isflaged15())

    def test_isflaged16(self):
        r"""isflaged16."""
        self.bitflag16.set16()
        self.assertTrue(self.bitflag16.isflaged16())

    def tearDown(self):
        pass


class TestBitFlag16_reset(MockerTestCase):
    """2014/04/11"""

    def setUp(self):
        self.bitflag16 = BitFlag16(65535) # all set
        self.mocker.replay()

    def test_reset9(self):
        r"""reset9."""
        self.assertTrue(self.bitflag16.isflaged9())
        self.bitflag16.reset9()
        self.assertFalse(self.bitflag16.isflaged9())

    def test_reset10(self):
        r"""reset10."""
        self.assertTrue(self.bitflag16.isflaged10())
        self.bitflag16.reset10()
        self.assertFalse(self.bitflag16.isflaged10())

    def test_reset11(self):
        r"""reset11."""
        self.assertTrue(self.bitflag16.isflaged11())
        self.bitflag16.reset11()
        self.assertFalse(self.bitflag16.isflaged11())

    def test_reset12(self):
        r"""reset12."""
        self.assertTrue(self.bitflag16.isflaged12())
        self.bitflag16.reset12()
        self.assertFalse(self.bitflag16.isflaged12())

    def test_reset13(self):
        r"""reset13."""
        self.assertTrue(self.bitflag16.isflaged13())
        self.bitflag16.reset13()
        self.assertFalse(self.bitflag16.isflaged13())

    def test_reset14(self):
        r"""reset14."""
        self.assertTrue(self.bitflag16.isflaged14())
        self.bitflag16.reset14()
        self.assertFalse(self.bitflag16.isflaged14())

    def test_reset15(self):
        r"""reset15."""
        self.assertTrue(self.bitflag16.isflaged15())
        self.bitflag16.reset15()
        self.assertFalse(self.bitflag16.isflaged15())

    def test_reset16(self):
        r"""reset16."""
        self.assertTrue(self.bitflag16.isflaged16())
        self.bitflag16.reset16()
        self.assertFalse(self.bitflag16.isflaged16())

    def tearDown(self):
        pass


class TestBitFlag32_set(MockerTestCase):
    """2014/04/12"""
    def setUp(self):
        self.bitflag = BitFlag32(0)
        self.mocker.replay()

    def test_set17(self, ):
        r"""set17."""
        self.bitflag.set17()
        self.assertEqual(self.bitflag, 1 << 16, msg='Failed: set17')

    def test_set18(self, ):
        r"""set18."""
        self.bitflag.set18()
        self.assertEqual(self.bitflag, 1 << 17, msg='Failed: set18')

    def test_set19(self, ):
        r"""set19."""
        self.bitflag.set19()
        self.assertEqual(self.bitflag, 1 << 18, msg='Failed: set19')

    def test_set20(self, ):
        r"""set20."""
        self.bitflag.set20()
        self.assertEqual(self.bitflag, 1 << 19, msg='Failed: set20')

    def test_set21(self, ):
        r"""set21."""
        self.bitflag.set21()
        self.assertEqual(self.bitflag, 1 << 20, msg='Failed: set21')

    def test_set22(self, ):
        r"""set22."""
        self.bitflag.set22()
        self.assertEqual(self.bitflag, 1 << 21, msg='Failed: set22')

    def test_set23(self, ):
        r"""set23."""
        self.bitflag.set23()
        self.assertEqual(self.bitflag, 1 << 22, msg='Failed: set23')

    def test_set24(self, ):
        r"""set24."""
        self.bitflag.set24()
        self.assertEqual(self.bitflag, 1 << 23, msg='Failed: set24')

    def test_set25(self, ):
        r"""set25."""
        self.bitflag.set25()
        self.assertEqual(self.bitflag, 1 << 24, msg='Failed: set25')

    def test_set26(self, ):
        r"""set26."""
        self.bitflag.set26()
        self.assertEqual(self.bitflag, 1 << 25, msg='Failed: set26')

    def test_set27(self, ):
        r"""set27."""
        self.bitflag.set27()
        self.assertEqual(self.bitflag, 1 << 26, msg='Failed: set27')

    def test_set28(self, ):
        r"""set28."""
        self.bitflag.set28()
        self.assertEqual(self.bitflag, 1 << 27, msg='Failed: set28')

    def test_set29(self, ):
        r"""set29."""
        self.bitflag.set29()
        self.assertEqual(self.bitflag, 1 << 28, msg='Failed: set29')

    # def test_set30(self, ):
    #     r"""set30."""
    #     self.bitflag.set30()
    #     self.assertEqual(self.bitflag, 1 << 29, msg='Failed: set30')

    # def test_set31(self, ):
    #     r"""set31."""
    #     self.bitflag.set31()
    #     self.assertEqual(self.bitflag, 1 << 30, msg='Failed: set31')

    # def test_set32(self, ):
    #     r"""set32."""
    #     self.bitflag.set32()
    #     self.assertEqual(self.bitflag, 1 << 31, msg='Failed: set32')

    def tearDown(self):
        pass



class TestBitFlag32_is(MockerTestCase):
    """2014/04/12"""

    def setUp(self):
        self.bitflag = BitFlag32(0)
        self.mocker.replay()

    def test_isflaged17(self):
        r"""isflaged17."""
        self.bitflag.set17()
        self.assertTrue(self.bitflag.isflaged17())

    def test_isflaged18(self):
        r"""isflaged18."""
        self.bitflag.set18()
        self.assertTrue(self.bitflag.isflaged18())

    def test_isflaged19(self):
        r"""isflaged19."""
        self.bitflag.set19()
        self.assertTrue(self.bitflag.isflaged19())

    def test_isflaged20(self):
        r"""isflaged20."""
        self.bitflag.set20()
        self.assertTrue(self.bitflag.isflaged20())

    def test_isflaged21(self):
        r"""isflaged21."""
        self.bitflag.set21()
        self.assertTrue(self.bitflag.isflaged21())

    def test_isflaged22(self):
        r"""isflaged22."""
        self.bitflag.set22()
        self.assertTrue(self.bitflag.isflaged22())

    def test_isflaged23(self):
        r"""isflaged23."""
        self.bitflag.set23()
        self.assertTrue(self.bitflag.isflaged23())

    def test_isflaged24(self):
        r"""isflaged24."""
        self.bitflag.set24()
        self.assertTrue(self.bitflag.isflaged24())

    def test_isflaged25(self):
        r"""isflaged25."""
        self.bitflag.set25()
        self.assertTrue(self.bitflag.isflaged25())

    def test_isflaged26(self):
        r"""isflaged26."""
        self.bitflag.set26()
        self.assertTrue(self.bitflag.isflaged26())

    def test_isflaged27(self):
        r"""isflaged27."""
        self.bitflag.set27()
        self.assertTrue(self.bitflag.isflaged27())

    def test_isflaged28(self):
        r"""isflaged28."""
        self.bitflag.set28()
        self.assertTrue(self.bitflag.isflaged28())

    def test_isflaged29(self):
        r"""isflaged29."""
        self.bitflag.set29()
        self.assertTrue(self.bitflag.isflaged29())

    # def test_isflaged30(self):
    #     r"""isflaged30."""
    #     self.bitflag.set30()
    #     self.assertTrue(self.bitflag.isflaged30())

    # def test_isflaged31(self):
    #     r"""isflaged31."""
    #     self.bitflag.set31()
    #     self.assertTrue(self.bitflag.isflaged31())

    # def test_isflaged32(self):
    #     r"""isflaged32."""
    #     self.bitflag.set32()
    #     self.assertTrue(self.bitflag.isflaged32())

    def tearDown(self):
        pass


class TestBitFlag32_reset(MockerTestCase):
    """2014/04/12"""

    def setUp(self):
        self.bitflag = BitFlag32(1073741823) # all set
        self.mocker.replay()

    def test_reset17(self):
        r"""reset17."""
        self.assertTrue(self.bitflag.isflaged17())
        self.bitflag.reset17()
        self.assertFalse(self.bitflag.isflaged17())

    def test_reset18(self):
        r"""reset18."""
        self.assertTrue(self.bitflag.isflaged18())
        self.bitflag.reset18()
        self.assertFalse(self.bitflag.isflaged18())

    def test_reset19(self):
        r"""reset19."""
        self.assertTrue(self.bitflag.isflaged19())
        self.bitflag.reset19()
        self.assertFalse(self.bitflag.isflaged19())

    def test_reset20(self):
        r"""reset20."""
        self.assertTrue(self.bitflag.isflaged20())
        self.bitflag.reset20()
        self.assertFalse(self.bitflag.isflaged20())

    def test_reset21(self):
        r"""reset21."""
        self.assertTrue(self.bitflag.isflaged21())
        self.bitflag.reset21()
        self.assertFalse(self.bitflag.isflaged21())

    def test_reset22(self):
        r"""reset22."""
        self.assertTrue(self.bitflag.isflaged22())
        self.bitflag.reset22()
        self.assertFalse(self.bitflag.isflaged22())

    def test_reset23(self):
        r"""reset23."""
        self.assertTrue(self.bitflag.isflaged23())
        self.bitflag.reset23()
        self.assertFalse(self.bitflag.isflaged23())

    def test_reset24(self):
        r"""reset24."""
        self.assertTrue(self.bitflag.isflaged24())
        self.bitflag.reset24()
        self.assertFalse(self.bitflag.isflaged24())

    def test_reset25(self):
        r"""reset25."""
        self.assertTrue(self.bitflag.isflaged25())
        self.bitflag.reset25()
        self.assertFalse(self.bitflag.isflaged25())

    def test_reset26(self):
        r"""reset26."""
        self.assertTrue(self.bitflag.isflaged26())
        self.bitflag.reset26()
        self.assertFalse(self.bitflag.isflaged26())

    def test_reset27(self):
        r"""reset27."""
        self.assertTrue(self.bitflag.isflaged27())
        self.bitflag.reset27()
        self.assertFalse(self.bitflag.isflaged27())

    def test_reset28(self):
        r"""reset28."""
        self.assertTrue(self.bitflag.isflaged28())
        self.bitflag.reset28()
        self.assertFalse(self.bitflag.isflaged28())

    def test_reset29(self):
        r"""reset29."""
        self.assertTrue(self.bitflag.isflaged29())
        self.bitflag.reset29()
        self.assertFalse(self.bitflag.isflaged29())

    # def test_reset30(self):
    #     r"""reset30."""
    #     self.assertTrue(self.bitflag.isflaged30())
    #     self.bitflag.reset30()
    #     self.assertFalse(self.bitflag.isflaged30())

    # def test_reset31(self):
    #     r"""reset31."""
    #     self.assertTrue(self.bitflag.isflaged31())
    #     self.bitflag.reset31()
    #     self.assertFalse(self.bitflag.isflaged31())

    # def test_reset32(self):
    #     r"""reset32."""
    #     self.assertTrue(self.bitflag.isflaged32())
    #     self.bitflag.reset32()
    #     self.assertFalse(self.bitflag.isflaged32())

    def tearDown(self):
        pass







# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_cls.py ends here
