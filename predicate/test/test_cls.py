#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: test_cls.py 136 2014-04-05 08:42:53Z t1 $
# $Revision: 136 $
# $Date: 2014-04-05 17:42:53 +0900 (Sat, 05 Apr 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-04-05 17:42:53 +0900 (Sat, 05 Apr 2014) $

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
from mocker import *
from predicate.cls import Predicate


class TestPredicate(MockerTestCase):
    def setUp(self):
        self.predicate_int = Predicate(0)
        # self.predicate_positive = Predicate(1)
        self.predicate_str = Predicate('a')
        self.mocker.replay()

    def test_False_isint(self):
        r"""False isint
        """
        self.assertFalse(self.predicate_str.isint())
    def test_False_iszero(self):
        r"""False iszero
        """
        self.assertFalse(self.predicate_str.iszero())
    def test_False_isMappingType(self):
        r"""False isMappingType
        """
        self.assertFalse(self.predicate_int.isMappingType())
    def test_False_isSequenceType(self):
        r"""False isSequenceType
        """
        self.assertFalse(self.predicate_int.isSequenceType())
    def test_False_isabstract(self):
        r"""False isabstract
        """
        self.assertFalse(self.predicate_int.isabstract())
    def test_False_isboolean(self):
        r"""False isboolean
        """
        self.assertFalse(self.predicate_int.isboolean())
    def test_False_isbuiltin(self):
        r"""False isbuiltin
        """
        self.assertFalse(self.predicate_int.isbuiltin())
    def test_False_isbuiltinmethod(self):
        r"""False isbuitinmethod
        """
        self.assertFalse(self.predicate_int.isbuiltinmethod())
    def test_False_isclass(self):
        r"""False isclass
        """
        self.assertFalse(self.predicate_int.isclass())
    def test_False_iscode(self):
        r"""False iscode
        """
        self.assertFalse(self.predicate_int.iscode())
    def test_False_isdict(self):
        r"""False isdict
        """
        self.assertFalse(self.predicate_int.isdict())
    def test_False_isdictproxy(self):
        r"""False isdictproxy
        """
        self.assertFalse(self.predicate_int.isdictproxy())
    def test_False_isellipsis(self):
        r"""False isellipsis
        """
        self.assertFalse(self.predicate_int.isellipsis())
    def test_False_isfile(self):
        r"""False isfile
        """
        self.assertFalse(self.predicate_int.isfile())
    def test_False_isfloat(self):
        r"""False isfloat
        """
        self.assertFalse(self.predicate_int.isfloat())
    def test_False_isframe(self):
        r"""False isframe
        """
        self.assertFalse(self.predicate_int.isframe())
    def test_False_isfunction(self):
        r"""False isfunction
        """
        self.assertFalse(self.predicate_int.isfunction())
    def test_False_isgenerator(self):
        r"""False isgenerator
        """
        self.assertFalse(self.predicate_int.isgenerator())
    def test_False_isgeneratorfunction(self):
        r"""False isgeneratorfunction
        """
        self.assertFalse(self.predicate_int.isgeneratorfunction())
    def test_False_islambda(self):
        r"""False islambda
        """
        self.assertFalse(self.predicate_int.islambda())
    def test_False_islist(self):
        r"""False islist
        """
        self.assertFalse(self.predicate_int.islist())
    def test_False_islong(self):
        r"""False islong
        """
        self.assertFalse(self.predicate_int.islong())
    def test_False_ismemberdescriptor(self):
        r"""False ismemberdescriptor
        """
        self.assertFalse(self.predicate_int.ismemberdescriptor())
    def test_False_ismethod(self):
        r"""False ismethod
        """
        self.assertFalse(self.predicate_int.ismethod())
    def test_False_ismodule(self):
        r"""False ismodule
        """
        self.assertFalse(self.predicate_int.ismodule())
    def test_False_isnegative(self):
        r"""False isnegative
        """
        self.assertFalse(self.predicate_int.isnegative())
    def test_False_isnone(self):
        r"""False isnone
        """
        self.assertFalse(self.predicate_int.isnone())
    def test_False_isnotimplemented(self):
        r"""False isnotimplemented
        """
        self.assertFalse(self.predicate_int.isnotimplemented())
    # def test_False_isobject(self):
    #     r"""False isobject
    #     """
    #     self.assertFalse(self.predicate_int.isobject())
    def test_False_isroutine(self):
        r"""False isroutine
        """
        self.assertFalse(self.predicate_int.isroutine())
    def test_False_isslice(self):
        r"""False isslice
        """
        self.assertFalse(self.predicate_int.isslice())
    def test_False_isstring(self):
        r"""False isstring
        """
        self.assertFalse(self.predicate_int.isstring())
    def test_False_isstrings(self):
        r"""False isstrings
        """
        self.assertFalse(self.predicate_int.isstrings())
    def test_False_istraceback(self):
        r"""False istraceback
        """
        self.assertFalse(self.predicate_int.istraceback())
    def test_False_istuple(self):
        r"""False istuple
        """
        self.assertFalse(self.predicate_int.istuple())
    def test_False_istype(self):
        r"""False istype
        """
        self.assertFalse(self.predicate_int.istype())
    def test_False_isunboundmethod(self):
        r"""False isunboundmethod
        """
        self.assertFalse(self.predicate_int.isunboundmethod())
    def test_False_isunicode(self):
        r"""False isunicode
        """
        self.assertFalse(self.predicate_int.isunicode())
    def test_False_isxrange(self):
        r"""False isxrange
        """
        self.assertFalse(self.predicate_int.isxrange())
    def test_False_ispositive(self):
        r"""False ispositive
        """
        self.assertFalse(self.predicate_int.ispositive())

    def test_True_ispositive(self, ):
        r"""True ispositive
        """
        self.assertTrue(Predicate(1).ispositive())
    def test_True_isnegative(self, ):
        r"""True isnegative
        """
        self.assertTrue(Predicate(-1).isnegative())
    def test_True_iszero(self, ):
        r"""True iszero
        """
        self.assertTrue(Predicate(0).iszero())
    def test_True_islist(self, ):
        r"""True islist
        """
        self.assertTrue(Predicate([]).islist())
    def test_True_isnone(self, ):
        r"""True isnone
        """
        self.assertTrue(Predicate(None).isnone())
    def test_True_istype(self, ):
        r"""True istype
        """
        class Tes(object): pass

        self.assertTrue(Predicate(Tes).istype())
    def test_True_isint(self, ):
        r"""True isint
        """
        self.assertTrue(Predicate(1).isint())
    def test_True_islong(self, ):
        r"""True islong
        """
        self.assertTrue(Predicate(10000000000).islong())
        self.assertTrue(Predicate(10L).islong())
    def test_True_isfloat(self, ):
        r"""True isfloat
        """
        self.assertTrue(Predicate(1.0).isfloat())
    def test_True_isboolean(self, ):
        r"""True isboolean
        """
        self.assertTrue(Predicate(True).isboolean())
        self.assertTrue(Predicate(False).isboolean())
    def test_True_isstring(self, ):
        r"""True isstring
        """
        self.assertTrue(Predicate('a').isstring())
    def test_True_isstrings(self, ):
        r"""True isstrings
        """
        self.assertTrue(Predicate('a').isstrings())
        self.assertTrue(Predicate(u'あ').isstrings())
    def test_True_istuple(self, ):
        r"""True istuple
        """
        self.assertTrue(Predicate(()).istuple())
    def test_True_isdict(self, ):
        r"""True isdict
        """
        self.assertTrue(Predicate({}).isdict())
    def test_True_islambda(self, ):
        r"""True islambda
        """
        self.assertTrue(Predicate(lambda args: None).islambda())
    def test_True_isbuiltinmethod(self, ):
        r"""True isbuiltinmethod
        """
        self.assertTrue(Predicate([].append).isbuiltinmethod())
    def test_True_isfile(self, ):
        r"""True isfile
        """
        self.assertTrue(Predicate(open('/tmp/test.txt', 'w')).isfile())
    def test_True_isxrange(self, ):
        r"""True isxrange
        """
        self.assertTrue(Predicate(xrange(1)).isxrange())
    def test_True_isslice(self, ):
        r"""True isslice
        """
        self.assertTrue(Predicate(slice(0)).isslice())
    def test_True_isellipsis(self, ):
        r"""True isellipsis
        """
        self.assertTrue(Predicate(Ellipsis).isellipsis())
    def test_True_isdictproxy(self, ):
        r"""True isdictproxy
        """
        self.assertTrue(Predicate(type.__dict__).isdictproxy())
    def test_True_isnotimplemented(self, ):
        r"""True isnotimplemented
        """
        self.assertTrue(Predicate(NotImplemented).isnotimplemented())
    def test_True_iscallable(self, ):
        r"""True iscallable
        """
        def func():
            pass
        self.assertTrue(Predicate(func).iscallable())
    def test_True_isiterable(self, ):
        r"""True isiterable
        """
        self.assertTrue(Predicate([1, 2, 3]).isiterable())

    def tearDown(self):
        pass


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_cls.py ends here
