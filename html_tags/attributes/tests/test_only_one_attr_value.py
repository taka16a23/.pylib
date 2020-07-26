#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_only_one_attribute.py

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
from django.test import TestCase
from material.forms.attributes.only_one_attr_value import OnlyOneAttrValue


class TestOnlyOneAttribute(TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        pass

    def test_init(self, ):
        t_attribute = OnlyOneAttrValue()
        self.assertEqual('', str(t_attribute))
        t_expect = 'test1'
        t_attribute = OnlyOneAttrValue(t_expect)
        self.assertEqual(t_expect, str(t_attribute))
        t_expect = 'test1 test2'
        with self.assertRaises(ValueError):
            OnlyOneAttrValue(t_expect)

    def test_set(self, ):
        t_attribute = OnlyOneAttrValue()
        self.assertEqual('', str(t_attribute))
        t_expect = 'test'
        t_attribute.set(t_expect)
        self.assertEqual(t_expect, str(t_attribute))
        t_expect2 = 'test2'
        t_attribute.set(t_expect2)
        self.assertEqual(t_expect2, str(t_attribute))
        t_attribute = OnlyOneAttrValue()
        t_expect_list = ['test1', 'test2', ]
        with self.assertRaises(ValueError):
            t_attribute.set(t_expect_list)

    def test_list(self, ):
        t_attribute = OnlyOneAttrValue()
        t_attribute.set('test')
        self.assertListEqual(['test'], t_attribute.list())

    def test_remove(self, ):
        t_attribute = OnlyOneAttrValue()
        t_attribute.set('test1')
        self.assertEqual('test1', str(t_attribute))
        t_attribute.remove('test1')
        self.assertEqual('', str(t_attribute))
        t_attribute.set('test1')
        t_attribute.remove('missing')
        self.assertEqual('test1', str(t_attribute))

    def test_contains(self, ):
        t_attribute = OnlyOneAttrValue('test1')
        self.assertTrue(t_attribute.contains('test1'))
        self.assertFalse(t_attribute.contains('notExistsValue'))

    def test_clear(self, ):
        t_attribute = OnlyOneAttrValue()
        t_attribute.set('test1')
        self.assertEqual('test1', str(t_attribute))
        t_attribute.clear()
        self.assertEqual('', str(t_attribute))

    def test_as_values(self, ):
        t_attribute = OnlyOneAttrValue('test1')
        self.assertEqual('test1', t_attribute.as_values())

    def test_iter(self, ):
        t_expect_list = ['test1', ]
        t_attribute = OnlyOneAttrValue('test1')
        t_got = list(t_attribute)
        self.assertListEqual(t_expect_list, t_got)

    def test_add(self, ):
        t_attribute1 = OnlyOneAttrValue()
        t_attribute2 = OnlyOneAttrValue('test1')
        t_attribute3 = t_attribute1 + t_attribute2
        self.assertEqual(str(t_attribute2), str(t_attribute3))
        self.assertNotEqual(str(t_attribute1), str(t_attribute3))
        t_attribute3 = t_attribute1 + 'test2'
        self.assertEqual('test2', str(t_attribute3))

    def test_iadd(self, ):
        t_expect = 'test1'
        t_attribute1 = OnlyOneAttrValue()
        t_attribute1 += OnlyOneAttrValue(t_expect)
        self.assertEqual(t_expect, str(t_attribute1))
        t_attribute1 = OnlyOneAttrValue()
        t_attribute1 += t_expect
        self.assertEqual(t_expect, str(t_attribute1))

    def test_len(self, ):
        t_attribute = OnlyOneAttrValue()
        self.assertEqual(0, len(t_attribute))
        t_attribute = OnlyOneAttrValue('test1')
        self.assertEqual(1, len(t_attribute))
        t_attribute.set('test2')
        self.assertEqual(1, len(t_attribute))
        t_attribute.clear()
        self.assertEqual(0, len(t_attribute))

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        pass



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_only_one_attribute.py ends here
