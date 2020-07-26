#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_attribute.py

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
from material.forms.tags.attributes.attr_value import AttrValue


class TestAttrValue(TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        pass

    def test_init(self, ):
        t_attribute = AttrValue()
        self.assertEqual('', str(t_attribute))
        t_expect = 'test1'
        t_attribute = AttrValue(t_expect)
        self.assertEqual(t_expect, str(t_attribute))
        t_expect = 'test1 test2'
        t_attribute = AttrValue(t_expect)
        t_expect_list = t_expect.split(' ')
        t_expect_list.sort()
        t_got = str(t_attribute).split(' ')
        t_got.sort()
        self.assertListEqual(t_expect_list, t_got)

    def test_set(self, ):
        t_attribute = AttrValue()
        self.assertEqual('', str(t_attribute))
        t_expect = 'test'
        t_attribute.set(t_expect)
        self.assertEqual(t_expect, str(t_attribute))
        t_expect2 = 'test2'
        t_attribute.set(t_expect2)
        t_expect = t_expect + ' ' + t_expect2
        t_expect_list = t_expect.split(' ')
        t_expect_list.sort()
        t_got = str(t_attribute).split(' ')
        t_got.sort()
        self.assertListEqual(t_expect_list, t_got)
        t_attribute = AttrValue()
        t_expect_list = ['test1', 'test2', ]
        t_attribute.set(t_expect_list)
        t_expect_list.sort()
        t_got = str(t_attribute).split(' ')
        t_got.sort()
        self.assertListEqual(t_expect_list, t_got)
        t_attribute = AttrValue()
        t_attribute.set(' '.join(t_expect_list))
        t_got = str(t_attribute).split(' ')
        t_got.sort()
        self.assertListEqual(t_expect_list, t_got)

    def test_list(self, ):
        t_expect_list = ['test1', 'test2', ]
        t_attribute = AttrValue()
        t_attribute.set(t_expect_list[0])
        t_attribute.set(t_expect_list[1])
        t_expect_list.sort()
        t_got = t_attribute.list()
        t_got.sort()
        self.assertListEqual(t_expect_list, t_got)

    def test_remove(self, ):
        t_attribute = AttrValue(['test1', 'test2', ])
        t_attribute.remove('test2')
        self.assertEqual('test1', str(t_attribute))

    def test_contains(self, ):
        t_attribute = AttrValue('test1 test2')
        self.assertTrue(t_attribute.contains('test1'))
        self.assertFalse(t_attribute.contains('notExistsValue'))

    def test_clear(self, ):
        t_expect_list = ['test1', 'test2', ]
        t_attribute = AttrValue()
        t_attribute.set(t_expect_list[0])
        t_attribute.set(t_expect_list[1])
        t_expect_list.sort()
        t_got = t_attribute.list()
        t_got.sort()
        self.assertListEqual(t_expect_list, t_got)
        t_attribute.clear()
        self.assertEqual('', str(t_attribute))

    def test_as_values(self, ):
        t_attribute = AttrValue('test1')
        self.assertEqual('test1', t_attribute.as_values())

    def test_iter(self, ):
        t_expect_list = ['test1', 'test2', ]
        t_expect_list.sort()
        t_attribute = AttrValue(t_expect_list)
        t_got = list(t_attribute)
        t_got.sort()
        self.assertListEqual(t_expect_list, t_got)

    def test_add(self, ):
        t_attribute1 = AttrValue()
        t_attribute2 = AttrValue('test1')
        t_attribute3 = t_attribute1 + t_attribute2
        self.assertEqual(str(t_attribute2), str(t_attribute3))
        self.assertNotEqual(str(t_attribute1), str(t_attribute3))
        t_attribute3 = t_attribute2 + 'test2'
        t_expect_list = ['test1', 'test2', ]
        t_expect_list.sort()
        t_got = t_attribute3.list()
        t_got.sort()
        self.assertListEqual(t_expect_list, t_got)
        t_attribute4 = t_attribute1 + t_expect_list
        t_got = t_attribute4.list()
        t_got.sort()
        self.assertListEqual(t_expect_list, t_got)

    def test_iadd(self, ):
        t_expect = 'test1'
        t_attribute1 = AttrValue()
        t_attribute1 += AttrValue(t_expect)
        self.assertEqual(t_expect, str(t_attribute1))
        t_attribute1 = AttrValue()
        t_attribute1 += t_expect
        self.assertEqual(t_expect, str(t_attribute1))
        t_attribute1 = AttrValue()
        t_expect_list = ['test1', 'test2', ]
        t_expect_list.sort()
        t_attribute1 += t_expect_list
        t_got = t_attribute1.list()
        t_got.sort()
        self.assertEqual(t_expect_list, t_got)

    def test_len(self, ):
        t_attribute = AttrValue()
        self.assertEqual(0, len(t_attribute))
        t_attribute = AttrValue('test1')
        self.assertEqual(1, len(t_attribute))
        t_attribute.set('test2')
        self.assertEqual(2, len(t_attribute))
        t_attribute.clear()
        self.assertEqual(0, len(t_attribute))

    def test_eq(self, ):
        t_expect = 'test1'
        t_attribute = AttrValue(t_expect)
        self.assertEqual(t_expect, t_attribute)
        t_expect = 'test1 test2'
        t_attribute = AttrValue(t_expect)
        self.assertEqual(t_expect, t_attribute)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        pass



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_attribute.py ends here
