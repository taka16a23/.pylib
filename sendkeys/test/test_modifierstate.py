#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: test_modifierstate.py 153 2014-04-19 08:33:26Z t1 $
# $Revision: 153 $
# $Date: 2014-04-19 17:33:26 +0900 (Sat, 19 Apr 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-04-19 17:33:26 +0900 (Sat, 19 Apr 2014) $

r"""Name: test_statecode.py

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
from predicate import isint
from sendkeys.modifierstate import ModifierState, NamedModifierMask


class TestModifierStatePack(MockerTestCase):
    """2014/04/09"""

    def setUp(self):
        self.mstate = ModifierState()
        self.mocker.replay()

    def test_shift(self):
        r"""pack shift"""
        result = '\x01\x00'
        self.mstate.setshift()
        self.assertEqual(self.mstate.pack(), result,
                         msg='Failed Equal: expect {0}.pack()="{1}"'
                         .format(repr(self.mstate), repr(result)))

    def test_lock(self, ):
        r"""pack lock"""
        result = '\x02\x00'
        self.mstate.setlock()
        self.assertEqual(self.mstate.pack(), result,
                         msg='Failed Equal: expect {0}.pack()="{1}"'
                         .format(repr(self.mstate), repr(result)))

    def test_control(self, ):
        r"""pack control"""
        result = '\x04\x00'
        self.mstate.setcontrol()
        self.assertEqual(self.mstate.pack(), result,
                         msg='Failed Equal: expect {0}.pack()="{1}"'
                         .format(repr(self.mstate), repr(result)))

    def test_alt(self, ):
        r"""pack alt"""
        result = '\x08\x00'
        self.mstate.setalt()
        self.assertEqual(self.mstate.pack(), result,
                         msg='Failed Equal: expect {0}.pack()="{1}"'
                         .format(repr(self.mstate), repr(result)))

    def test_numlock(self, ):
        r"""pack numlock"""
        result = '\x10\x00'
        self.mstate.setnumlock()
        self.assertEqual(self.mstate.pack(), result,
                         msg='Failed Equal: expect {0}.pack()="{1}"'
                         .format(repr(self.mstate), repr(result)))

    def test_hiper(self, ):
        r"""pack hiper"""
        result = ' \x00'
        self.mstate.sethiper()
        self.assertEqual(self.mstate.pack(), result,
                         msg='Failed Equal: expect {0}.pack()="{1}"'
                         .format(repr(self.mstate), repr(result)))

    def test_super(self, ):
        r"""pack super"""
        result = '@\x00'
        self.mstate.setsuper()
        self.assertEqual(self.mstate.pack(), result,
                         msg='Failed Equal: expect {0}.pack()="{1}"'
                         .format(repr(self.mstate), repr(result)))

    def test_mod5(self, ):
        r"""pack mod5"""
        result = '\x80\x00'
        self.mstate.setmod5()
        self.assertEqual(self.mstate.pack(), result,
                         msg='Failed Equal: expect {0}.pack()="{1}"'
                         .format(repr(self.mstate), repr(result)))

    def test_left(self, ):
        r"""pack left"""
        result = '\x00\x01'
        self.mstate.setleft()
        self.assertEqual(self.mstate.pack(), result,
                         msg='Failed Equal: expect {0}.pack()="{1}"'
                         .format(repr(self.mstate), repr(result)))

    def test_middle(self, ):
        r"""pack middle"""
        result = '\x00\x02'
        self.mstate.setmiddle()
        self.assertEqual(self.mstate.pack(), result,
                         msg='Failed Equal: expect {0}.pack()="{1}"'
                         .format(repr(self.mstate), repr(result)))

    def test_right(self, ):
        r"""pack right"""
        result = '\x00\x04'
        self.mstate.setright()
        self.assertEqual(self.mstate.pack(), result,
                         msg='Failed Equal: expect {0}.pack()="{1}"'
                         .format(repr(self.mstate), repr(result)))

    def test_wheelup(self, ):
        r"""pack wheelup"""
        result = '\x00\x08'
        self.mstate.setwheelup()
        self.assertEqual(self.mstate.pack(), result,
                         msg='Failed Equal: expect {0}.pack()="{1}"'
                         .format(repr(self.mstate), repr(result)))

    def test_wheeldown(self, ):
        r"""pack wheeldown"""
        result = '\x00\x10'
        self.mstate.setwheeldown()
        self.assertEqual(self.mstate.pack(), result,
                         msg='Failed Equal: expect {0}.pack()="{1}"'
                         .format(repr(self.mstate), repr(result)))

    def test_any(self, ):
        r"""pack any"""
        result = '\x00\x80'
        self.mstate.setany()
        self.assertEqual(self.mstate.pack(), result,
                         msg='Failed Equal: expect {0}.pack()="{1}"'
                         .format(repr(self.mstate), repr(result)))

    def tearDown(self):
        pass


class TestModifierStateSet(MockerTestCase):
    """2014/04/09"""

    def setUp(self):
        self.mstate = ModifierState()
        self.mocker.replay()

    def test_shift(self):
        r"""setshift"""
        self.mstate.setshift()
        self.assertTrue(self.mstate == NamedModifierMask.Shift)

    def test_lock(self):
        r"""setlock"""
        self.mstate.setlock()
        self.assertTrue(self.mstate == NamedModifierMask.Lock)

    def test_control(self):
        r"""setcontrol"""
        self.mstate.setcontrol()
        self.assertTrue(self.mstate == NamedModifierMask.Control)

    def test_alt(self):
        r"""setalt"""
        self.mstate.setalt()
        self.assertTrue(self.mstate == NamedModifierMask.Alt)

    def test_numlock(self):
        r"""setnumlock"""
        self.mstate.setnumlock()
        self.assertTrue(self.mstate == NamedModifierMask.Numlock)

    def test_hiper(self):
        r"""sethiper"""
        self.mstate.sethiper()
        self.assertTrue(self.mstate == NamedModifierMask.Hiper)

    def test_super(self):
        r"""setsuper"""
        self.mstate.setsuper()
        self.assertTrue(self.mstate == NamedModifierMask.Super)

    def test_mod5(self):
        r"""setmod5"""
        self.mstate.setmod5()
        self.assertTrue(self.mstate == NamedModifierMask.Mod5)

    def test_left(self):
        r"""setleft"""
        self.mstate.setleft()
        self.assertTrue(self.mstate == NamedModifierMask.Left)

    def test_middle(self):
        r"""setmiddle"""
        self.mstate.setmiddle()
        self.assertTrue(self.mstate == NamedModifierMask.Middle)

    def test_right(self):
        r"""setright"""
        self.mstate.setright()
        self.assertTrue(self.mstate == NamedModifierMask.Right)

    def test_wheelup(self):
        r"""setwheelup"""
        self.mstate.setwheelup()
        self.assertTrue(self.mstate == NamedModifierMask.WheelUp)

    def test_wheeldown(self):
        r"""setwheeldown"""
        self.mstate.setwheeldown()
        self.assertTrue(self.mstate == NamedModifierMask.WheelDown)

    def test_any(self):
        r"""setany"""
        self.mstate.setany()
        self.assertTrue(self.mstate == NamedModifierMask.Any)

    def tearDown(self):
        pass


class TestModifierStateIs(MockerTestCase):
    """2014/04/09"""

    def setUp(self):
        self.mstate = ModifierState(40959) # set all
        self.mocker.replay()

    def test_isshift(self):
        r"""isshift"""
        self.assertTrue(self.mstate.isshift())

    def test_islock(self):
        r"""islock"""
        self.assertTrue(self.mstate.islock())

    def test_iscontrol(self):
        r"""iscontrol"""
        self.assertTrue(self.mstate.iscontrol())

    def test_isalt(self):
        r"""isalt"""
        self.assertTrue(self.mstate.isalt())

    def test_isnumlock(self):
        r"""isnumlock"""
        self.assertTrue(self.mstate.isnumlock())

    def test_ishiper(self):
        r"""ishiper"""
        self.assertTrue(self.mstate.ishiper())

    def test_issuper(self):
        r"""issuper"""
        self.assertTrue(self.mstate.issuper())

    def test_ismod5(self):
        r"""ismod5"""
        self.assertTrue(self.mstate.ismod5())

    def test_isleft(self):
        r"""isleft"""
        self.assertTrue(self.mstate.isleft())

    def test_ismiddle(self):
        r"""ismiddle"""
        self.assertTrue(self.mstate.ismiddle())

    def test_isright(self):
        r"""isright"""
        self.assertTrue(self.mstate.isright())

    def test_iswheelup(self):
        r"""iswheelup"""
        self.assertTrue(self.mstate.iswheelup())

    def test_iswheeldown(self):
        r"""iswheeldown"""
        self.assertTrue(self.mstate.iswheeldown())

    def test_isany(self):
        r"""isany"""
        self.assertTrue(self.mstate.isany())

    def tearDown(self):
        pass


class TestModifierStateReset(MockerTestCase):
    """2014/04/09"""

    def setUp(self):
        self.mstate = ModifierState(40959) # set all
        self.mocker.replay()

    def test_resetshift(self):
        r"""resetshift"""
        self.mstate.resetshift()
        self.assertFalse(self.mstate.isshift())

    def test_resetlock(self):
        r"""resetlock"""
        self.mstate.resetlock()
        self.assertFalse(self.mstate.islock())

    def test_resetcontrol(self):
        r"""resetcontrol"""
        self.mstate.resetcontrol()
        self.assertFalse(self.mstate.iscontrol())

    def test_resetalt(self):
        r"""resetalt"""
        self.mstate.resetalt()
        self.assertFalse(self.mstate.isalt())

    def test_resetnumlock(self):
        r"""resetnumlock"""
        self.mstate.resetnumlock()
        self.assertFalse(self.mstate.isnumlock())

    def test_resethiper(self):
        r"""resethiper"""
        self.mstate.resethiper()
        self.assertFalse(self.mstate.ishiper())

    def test_resetsuper(self):
        r"""resetsuper"""
        self.mstate.resetsuper()
        self.assertFalse(self.mstate.issuper())

    def test_resetmod5(self):
        r"""resetmod5"""
        self.mstate.resetmod5()
        self.assertFalse(self.mstate.ismod5())

    def test_resetleft(self):
        r"""resetleft"""
        self.mstate.resetleft()
        self.assertFalse(self.mstate.isleft())

    def test_resetright(self):
        r"""resetright"""
        self.mstate.resetright()
        self.assertFalse(self.mstate.isright())

    def test_resetwheelup(self):
        r"""resetwheelup"""
        self.mstate.resetwheelup()
        self.assertFalse(self.mstate.iswheelup())

    def test_resetwheeldown(self):
        r"""resetwheeldown"""
        self.mstate.resetwheeldown()
        self.assertFalse(self.mstate.iswheeldown())

    def test_resetany(self):
        r"""resetany"""
        self.mstate.resetany()
        self.assertFalse(self.mstate.isany())

    def tearDown(self):
        pass


class TestModifierStateClear(MockerTestCase):
    """2014/04/09"""

    def setUp(self):
        self.mstate = ModifierState(40959) # set all
        self.mocker.replay()

    def test_clear(self):
        r"""clear
        """
        self.mstate.clear()
        state0 = ModifierState()
        self.assertEqual(state0, self.mstate,
                         msg='Failed: ModifierState(40959).clear()'
                         ' state0={}, mstate={}'.format(state0, self.mstate))

    def tearDown(self):
        pass


class TestModifierStateSpecialMethod(MockerTestCase):
    """2014/04/09"""

    def setUp(self):
        self.num0 = 0
        self.num1 = 1
        self.num128 = 128
        self.num40959 = 40959
        self.mstate0 = ModifierState(self.num0)
        self.mstate1 = ModifierState(self.num1)
        self.mstate128 = ModifierState(self.num128)
        self.mstate40959 = ModifierState(self.num40959) # set all
        self.mocker.replay()

    def test___iter__(self):
        r"""__iter__"""
        sclis = [ModifierState(0), ModifierState(1), ModifierState(2), ModifierState(4),
                 ModifierState(8), ModifierState(16), ModifierState(32), ModifierState(64),
                 ModifierState(128), ModifierState(256), ModifierState(512),
                 ModifierState(1024), ModifierState(2048), ModifierState(4096),
                 ModifierState(32768)]
        self.assertListEqual(sclis, list(self.mstate40959), msg='Failed: __iter__')

    def test___int__(self, ):
        r"""__int__."""
        self.assertTrue(isint(int(self.mstate40959)))
        self.assertEqual(self.num40959, int(self.mstate40959),
                         msg='Failed: __int__')

    def test___eq__(self, ):
        r"""__eq__."""
        self.assertTrue(self.mstate40959 == self.num40959)
        self.assertTrue(self.mstate40959 == ModifierState(self.num40959))
        self.assertFalse(self.mstate40959 == 1)
        self.assertFalse(self.mstate40959 == self.mstate1)

    def test___ne__(self, ):
        r"""__ne__."""
        self.assertTrue(self.mstate40959 != 1)
        self.assertTrue(self.mstate40959 != self.mstate1)
        self.assertFalse(self.mstate40959 != self.num40959)
        self.assertFalse(self.mstate40959 != ModifierState(self.num40959))

    def test___hash__(self, ):
        r"""__hash__."""
        self.assertEqual(hash(self.mstate40959), hash(self.num40959),
                         msg='Failed: __hash__')

    def test___and__(self, ):
        r"""__and__."""
        self.assertEqual(self.mstate128 & self.num128, self.num128 & self.num128,
                         msg='Failed: __and__')

    def test___xor__(self, ):
        r"""__xor__."""
        self.assertEqual(self.mstate128 ^ self.num128, self.num128 ^ self.num128,
                         msg='Failed: __xor__')

    def test___or__(self, ):
        r"""__or__."""
        self.assertEqual(self.mstate0 | self.num128, self.num0 | self.num128,
                         msg='Failed: __or__')

    def test___lshift__(self, ):
        r"""__lshift__."""
        num = self.num128 << 1
        code = self.mstate128 << 1
        self.assertEqual(num, code, msg='Failed: __lshift__ num={}, code={}'
                         .format(num, code))

    def test___rshift__(self, ):
        r"""__rshift__."""
        num = self.num128 >> 1
        code = self.mstate128 >> 1
        self.assertEqual(num, code, msg='Failed: __rshift__ num={}, code={}'
                         .format(num, code))

    # def test___invert__(self, ):
    #     r"""__invert__."""
    #     num = ~self.num1
    #     code = ~self.mstate1
    #     self.assertEqual(num, code, msg='Failed: __invert__ num={}, code={}'
    #                      .format(num, code))

    def test___iand__(self, ):
        r"""__iand__."""
        num128 = 128
        num128 &= self.num128
        self.mstate128 &= self.num128
        self.assertEqual(num128, self.mstate128,
                         msg='Failed: __iand__ num128={}, self.mstate128={}'
                         .format(num128, self.mstate128))

    def test___ixor__(self, ):
        r"""__ixor__."""
        num128 = 128
        num128 ^= self.num128
        self.mstate128 ^= self.num128
        self.assertEqual(num128, self.mstate128,
                         msg='Failed: __ixor__ num128={}, self.mstate128={}'
                         .format(num128, self.mstate128))

    def test___ior__(self, ):
        r"""__ior__."""
        num0 = 0
        num0 |= self.num128
        self.mstate0 |= self.num128
        self.assertEqual(num0, self.mstate0,
                         msg='Failed: __ior__ num0={}, self.mstate0={}'
                         .format(num0, self.mstate0))

    def test___ilshift__(self, ):
        r"""__ilshift__."""
        num128 = 128
        num128 <<= 1
        self.mstate128 <<= 1
        self.assertEqual(num128, self.mstate128,
                         msg='Failed: __ilshift__ num128={}, self.mstate128={}'
                         .format(num128, self.mstate128))

    def test___irshift__(self, ):
        r"""__irshift__."""
        num128 = 128
        num128 >>= 1
        self.mstate128 >>= 1
        self.assertEqual(num128, self.mstate128,
                         msg='Failed: __irshift__ num128={}, self.mstate128={}'
                         .format(num128, self.mstate128))

    def test___nonzero__(self, ):
        r"""__nonzero__."""
        self.assertTrue(self.mstate1)
        self.assertFalse(self.mstate0)

    def test___contains__(self, ):
        r"""__contains__."""
        self.assertTrue(128 in self.mstate128)
        self.assertFalse(128 in self.mstate1)

    def test___repr__(self, ):
        r"""__repr__."""
        self.skipTest('')

    def test___str__(self, ):
        r"""__str__."""
        self.skipTest('')

    def tearDown(self):
        pass



# For Emacs
# Local Variables:
# coding: utf-8
# no-check-type-miss: t
# End:
# test_statecode.py ends here
