#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: test_functions.py 136 2014-04-05 08:42:53Z t1 $
# $Revision: 136 $
# $Date: 2014-04-05 17:42:53 +0900 (Sat, 05 Apr 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-04-05 17:42:53 +0900 (Sat, 05 Apr 2014) $

r"""Name: test_functions.py

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
from predicate import functions



# GLOBALVAR = 'value'


# class Testisglobalvariable(MockerTestCase):
#     def setUp(self):

#         self.mocker.replay()

#     # def test_True_isglobalvariable(self):
#     #     r"""True_isglobalvariable
#     #     """
#     #     self.assertTrue(functions.isglobalvariable('GLOBLAVAR'))

#     def tearDown(self):
#         pass


class Testispositive(MockerTestCase):
    def setUp(self):

        self.mocker.replay()

    def test_True_ispositive(self):
        r"""True_ispositive"""
        self.assertTrue(functions.ispositive(1))

    def test_False_ispositive(self, ):
        r"""False_ispositive"""
        self.assertFalse(functions.ispositive(-1))
        self.assertFalse(functions.ispositive(0))

    def tearDown(self):
        pass


class Testisnegative(MockerTestCase):
    def setUp(self):

        self.mocker.replay()

    def test_True_isnegative(self):
        r"""True_isnegative."""
        self.assertTrue(functions.isnegative(-1))

    def test_False_isnegative(self, ):
        r"""False_isnegative."""
        self.assertFalse(functions.isnegative(0))
        self.assertFalse(functions.isnegative(1))

    def tearDown(self):
        pass


class Testiszero(MockerTestCase):
    def setUp(self):

        self.mocker.replay()

    def test_True_iszero(self):
        r"""True_iszero
        """
        self.assertTrue(functions.iszero(0))

    def test_False_iszero(self):
        r"""False_iszero
        """
        self.assertFalse(functions.iszero(1))

    def tearDown(self):
        pass


class Testislist(MockerTestCase):
    def setUp(self):

        self.mocker.replay()

    def test_True_islist(self):
        r"""True_islist
        """
        self.assertTrue(functions.islist([]))

    def test_False_islist(self, ):
        r"""False_islist."""
        self.assertFalse(functions.islist(())) # tuple

    def tearDown(self):
        pass


class Testisnone(MockerTestCase):
    def setUp(self):

        self.mocker.replay()

    def test_True_isnone(self):
        r"""True_isnone
        """
        self.assertTrue(functions.isnone(None))

    def test_False_isnone(self, ):
        r"""False_isnone."""
        self.assertFalse(functions.isnone(1))

    def tearDown(self):
        pass


class Testistype(MockerTestCase):
    def setUp(self):
        class DummyClass(object):
            pass
        self.cls = DummyClass
        self.mocker.replay()

    def test_True_istype(self):
        r"""True_istype
        """
        self.assertTrue(functions.istype(self.cls))

    def test_False_istype(self, ):
        r"""False_istype."""
        self.assertFalse(functions.istype(1))

    def tearDown(self):
        pass


class Testisobject(MockerTestCase):
    def setUp(self):

        self.mocker.replay()

    def test_True_isobject(self):
        r"""True_isobject
        """
        self.assertTrue(functions.isobject(object))

    # def test_False_isobject(self, ):
    #     r"""test_False_isobject."""
    #     self.assertFalse(functions.isobject())

    def tearDown(self):
        pass


class Testisint(MockerTestCase):
    def setUp(self):

        self.mocker.replay()

    def test_True_isint(self):
        r"""True_isint
        """
        self.assertTrue(functions.isint(1))

    def test_False_isint(self, ):
        r"""False_isint."""
        self.assertFalse(functions.isint('a'))
        self.assertFalse(functions.isint(10L))
        self.assertFalse(functions.isint(1.0))

    def tearDown(self):
        pass


class Testislong(MockerTestCase):
    def setUp(self):

        self.mocker.replay()

    def test_True_islong(self):
        r"""True_islong
        """
        self.assertTrue(functions.islong(10000000000))
        self.assertTrue(functions.islong(10L))

    def test_False_islong(self, ):
        r"""False_islong."""
        self.assertFalse(functions.islong('a'))
        self.assertFalse(functions.islong(1))
        self.assertFalse(functions.islong(1.0))

    def tearDown(self):
        pass


class Testisfloat(MockerTestCase):
    def setUp(self):

        self.mocker.replay()

    def test_True_isfloat(self):
        r"""True_isfloat
        """
        self.assertTrue(functions.isfloat(1.0))

    def test_False_isfloat(self, ):
        r"""False_isfloat."""
        self.assertFalse(functions.isfloat('a'))
        self.assertFalse(functions.isfloat(1))
        self.assertFalse(functions.isfloat(1L))

    def tearDown(self):
        pass


class Testisboolean(MockerTestCase):
    def setUp(self):

        self.mocker.replay()

    def test_True_isboolean(self):
        r"""True_isboolean
        """
        self.assertTrue(functions.isboolean(True))
        self.assertTrue(functions.isboolean(False))

    def test_False_isboolean(self, ):
        r"""False_isboolean."""
        self.assertFalse(functions.isboolean(1))

    def tearDown(self):
        pass


class Testisstring(MockerTestCase):
    def setUp(self):

        self.mocker.replay()

    def test_True_isstring(self):
        r"""True_isstring
        """
        self.assertTrue(functions.isstring('a'))

    def test_False_isstring(self, ):
        r"""False_isstring."""
        self.assertFalse(functions.isstring(1))
        self.assertFalse(functions.isstring(u'あ'))

    def tearDown(self):
        pass

class Testisstrings(MockerTestCase):
    def setUp(self):

        self.mocker.replay()

    def test_True_isstrings(self):
        r"""True_isstrings
        """
        self.assertTrue(functions.isstrings('a'))
        self.assertTrue(functions.isstrings(u'あ'))

    def test_False_isstrings(self, ):
        r"""False_isstrings."""
        self.assertFalse(functions.isboolean(1))

    def tearDown(self):
        pass


class Testistuple(MockerTestCase):
    def setUp(self):

        self.mocker.replay()

    def test_True_istuple(self):
        r"""True_istuple
        """
        self.assertTrue(functions.istuple(()))

    def test_False_istuple(self, ):
        r"""False_istuple."""
        self.assertFalse(functions.istuple([]))

    def tearDown(self):
        pass


class Testisdict(MockerTestCase):
    def setUp(self):

        self.mocker.replay()

    def test_True_isdict(self):
        r"""True_isdict
        """
        self.assertTrue(functions.isdict({}))

    def test_False_isdict(self, ):
        r"""False_isdict."""
        self.assertFalse(functions.isdict([]))

    def tearDown(self):
        pass


class Testislambda(MockerTestCase):
    def setUp(self):

        self.mocker.replay()

    def test_True_islambda(self):
        r"""True_islambda
        """
        self.assertTrue(functions.islambda(lambda args: None))

    def test_False_islambda(self, ):
        r"""False_islambda."""
        self.assertFalse(functions.islambda([]))

    def tearDown(self):
        pass


# class Testisunboundmethod(MockerTestCase):
#     def setUp(self):

#         self.mocker.replay()

#     def test_True_isunboundmethod(self):
#         r"""True_isunboundmethod
#         """
#         self.assertTrue(functions.isunboundmethod())

#     def test_False_isunboundmethod(self, ):
#         r"""False_isunboundmethod."""
#         self.assertFalse(functions.isunboundmethod())

#     def tearDown(self):
#         pass


# class TestisInstance(MockerTestCase):
#     def setUp(self):
#         class CLASS(object): pass
#         self.cls = CLASS
#         self.mocker.replay()

#     def test_True_isInstance(self):
#         r"""True_isInstance
#         """
#         self.assertTrue(functions.isInstance(self.cls()))

#     def test_False_isInstance(self, ):
#         r"""False_isInstance."""
#         self.assertFalse(functions.isInstance(self.cls))

#     def tearDown(self):
#         pass


class Testisbuiltinmethod(MockerTestCase):
    def setUp(self):

        self.mocker.replay()

    def test_True_isbuiltinmethod(self):
        r"""True_isbuitinmethod
        """
        self.assertTrue(functions.isbuiltinmethod([].append))

    def test_False_isbuiltinmethod(self, ):
        r"""False_isbuitinmethod."""
        class Tes(object):
            def tes(self, ):
                pass
        self.assertFalse(functions.isbuiltinmethod(Tes().tes))

    def tearDown(self):
        pass


class Testisfile(MockerTestCase):
    def setUp(self):

        self.mocker.replay()

    def test_True_isfile(self):
        r"""True_isfile
        """
        self.assertTrue(functions.isfile(open('/tmp/test.txt', 'w')))

    def test_False_isfile(self, ):
        r"""False_isfile."""
        self.assertFalse(functions.isfile(1))

    def tearDown(self):
        pass


class Testisxrange(MockerTestCase):
    def setUp(self):

        self.mocker.replay()

    def test_True_isxrange(self):
        r"""True_isxrange
        """
        self.assertTrue(functions.isxrange(xrange(1)))

    def test_False_isxrange(self, ):
        r"""False_isxrange."""
        self.assertFalse(functions.isxrange(range(1)))

    def tearDown(self):
        pass


class Testisslice(MockerTestCase):
    def setUp(self):

        self.mocker.replay()

    def test_True_isslice(self):
        r"""True_isslice
        """
        self.assertTrue(functions.isslice(slice(0)))

    def test_False_isslice(self, ):
        r"""False_isslice."""
        self.assertFalse(functions.isslice(1))

    def tearDown(self):
        pass


class Testisellipsis(MockerTestCase):
    def setUp(self):

        self.mocker.replay()

    def test_True_isellipsis(self):
        r"""True_isellipsis
        """
        self.assertTrue(functions.isellipsis(Ellipsis))

    def test_False_isellipsis(self, ):
        r"""False_isellipsis."""
        self.assertFalse(functions.isellipsis(0))

    def tearDown(self):
        pass


class Testisdictproxy(MockerTestCase):
    def setUp(self):

        self.mocker.replay()

    def test_True_isdictproxy(self):
        r"""True_isdictproxy
        """
        self.assertTrue(functions.isdictproxy(type.__dict__))

    def test_False_isdictproxy(self, ):
        r"""False_isdictproxy."""
        self.assertFalse(functions.isdictproxy(0))

    def tearDown(self):
        pass


class Testisnotimplemented(MockerTestCase):
    def setUp(self):

        self.mocker.replay()

    def test_True_isnotimplemented(self):
        r"""True_isnotimplemented
        """
        self.assertTrue(functions.isnotimplemented(NotImplemented))

    def test_False_isnotimplemented(self, ):
        r"""False_isnotimplemented."""
        self.assertFalse(functions.isnotimplemented(0))

    def tearDown(self):
        pass


class Testiscallable(MockerTestCase):
    def setUp(self):
        def func(self, ):
            pass
        self.func = func
        self.mocker.replay()

    def test_True_iscallable(self):
        r"""True_iscallable
        """
        self.assertTrue(functions.iscallable(self.func))

    def test_False_iscallable(self, ):
        r"""False_iscallable."""
        self.assertFalse(functions.iscallable(0))

    def tearDown(self):
        pass


# class Testispython2(MockerTestCase):
#     def setUp(self):

#         self.mocker.replay()

#     def test_True_ispython2(self):
#         r"""True_ispython2
#         """
#         self.assertTrue(functions.ispython2())

#     def test_False_ispython2(self, ):
#         r"""False_ispython2."""
#         self.assertFalse(functions.ispython2())

#     def tearDown(self):
#         pass


# class Testispython3(MockerTestCase):
#     def setUp(self):

#         self.mocker.replay()

#     def test_True_ispython3(self):
#         r"""True_ispython3
#         """
#         self.assertTrue(functions.ispython3())

#     def test_False_ispython3(self, ):
#         r"""False_ispython3."""
#         self.assertFalse(functions.ispython3())

#     def tearDown(self):
#         pass


class Testisiterable(MockerTestCase):
    def setUp(self):

        self.mocker.replay()

    def test_True_isiterable(self):
        r"""True_isiterable
        """
        self.assertTrue(functions.isiterable([1, 2, 3]))

    def test_False_isiterable(self, ):
        r"""False_isiterable."""
        self.assertFalse(functions.isiterable(0))

    def tearDown(self):
        pass



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_functions.py ends here
