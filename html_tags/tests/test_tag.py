#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_tag.py

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
from material.forms.tags.tag import Tag
from material.forms.tags.attributes.attributes import Attributes


class TestTag(TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        pass

    def test_get_name(self, ):
        t_expect = 'test'
        t_tag = Tag(t_expect)
        self.assertEqual(t_expect, t_tag.get_name())

    def test_set_name(self, ):
        t_expect = 'test'
        t_tag = Tag('other')
        self.assertEqual('other', t_tag.get_name())
        t_tag.set_name(t_expect)
        self.assertEqual(t_expect, t_tag.get_name())

    def test_get_attrs(self, ):
        t_expect = 'test'
        t_tag = Tag('test', test=t_expect)
        self.assertEqual(t_expect, str(t_tag.get_attrs().get('test', '')))

    def test_clear_attrs(self, ):
        t_expect = 'test'
        t_tag = Tag('test', test=t_expect)
        self.assertEqual(t_expect, str(t_tag.get_attrs().get('test', '')))
        t_tag.clear_attrs()
        self.assertEqual('', str(t_tag.get_attrs().get('test', '')))
        self.assertEqual(0, len(t_tag.get_attrs()))

    def test_set_attr_value(self, ):
        t_tag = Tag('test')
        self.assertEqual(0, len(t_tag.get_attrs()))
        t_expect = 'value1'
        t_tag.set_attr_value('test', t_expect)
        self.assertEqual(t_expect, str(t_tag.get_attrs().get('test', '')))

    def test_append_attribute_value(self, ):
        t_tag = Tag('test')
        self.assertEqual('', str(t_tag.get_attrs().get('test', '')))
        t_expect = ['value1', 'value2', ]
        t_expect.sort()
        t_tag.append_attribute_value('test', t_expect[0])
        self.assertEqual(t_expect[0], str(t_tag.get_attrs().get('test', '')))
        t_tag.append_attribute_value('test', t_expect[1])
        t_got = list(t_tag.get_attrs().get('test', []))
        t_got.sort()
        self.assertListEqual(t_expect, t_got)

    def test_remove_attribute_value(self, ):
        t_expect = ['value1', 'value2', ]
        t_tag = Tag('test', test=t_expect)
        t_tag.remove_attribute_value('test', 'value2')
        self.assertEqual('value1', str(t_tag.get_attrs().get('test', '')))

    def test_clear_attribute_value(self, ):
        t_expect = ['value1', 'value2', ]
        t_tag = Tag('test', test=t_expect)
        t_tag.clear_attribute_value('test')
        self.assertEqual('', str(t_tag.get_attrs().get('test', '')))

    def test_set_attribute_none(self, ):
        t_tag = Tag('test', test='value1')
        t_tag.set_attribute_none('test')
        self.assertIsNone(t_tag.get_attrs().get('test', ''))

    def test_get_attribute_value(self, ):
        t_expect = 'value1'
        t_tag = Tag('test', test=t_expect)
        self.assertEqual(t_expect, str(t_tag.get_attribute_value('test')))

    def test_contains_attribute_value(self, ):
        t_expect = 'value1 value2'
        t_tag = Tag('test', test=t_expect)
        self.assertTrue(t_tag.contains_attribute_value('test', 'value1'))
        self.assertFalse(t_tag.contains_attribute_value('test', 'none_value'))

    def test_update_attribute(self, ):
        t_tag = Tag('test')
        t_expect = Attributes(test='value1')
        t_tag.update_attribute(t_expect)
        self.assertEqual('value1', str(t_tag.get_attribute_value('test')))
        t_attributes = Attributes(test='value1 value2')
        t_tag.update_attribute(t_attributes)
        t_expect = ['value1', 'value2', ]
        t_expect.sort()
        t_got = list(t_tag.get_attribute_value('test'))
        t_got.sort()
        self.assertListEqual(t_expect, t_got)

    def test_setdefault_attribute(self, ):
        t_tag = Tag('test')
        t_expect = 'value1'
        t_tag.setdefault_attribute('test', t_expect)
        self.assertEqual('value1', str(t_tag.get_attribute_value('test')))
        t_tag.setdefault_attribute('test', 'value2')
        self.assertEqual('value1', str(t_tag.get_attribute_value('test')))

    def test_append_tag(self, ):
        t_tag1 = Tag('test1')
        t_tag2 = Tag('test2')
        t_tag1.append_tag(t_tag2)
        self.assertEqual(t_tag2, t_tag1.list_tags()[0])

    def test_clear_tags(self, ):
        t_tag1 = Tag('test1')
        t_tag2 = Tag('test2')
        t_tag1.append_tag(t_tag2)
        t_tag1.clear_tags()
        self.assertListEqual(list(t_tag1.list_tags()), [])

    def test_count_tags(self, ):
        t_tag1 = Tag('test1')
        t_tag2 = Tag('test2')
        self.assertEqual(0, len(t_tag1.list_tags()))
        t_tag1.append_tag(t_tag2)
        self.assertEqual(1, len(t_tag1.list_tags()))

    def test_extend_tags(self, ):
        t_tag1 = Tag('test1')
        t_tag2 = Tag('test2')
        t_tag3 = Tag('test3')
        t_expects = [t_tag2, t_tag3, ]
        t_tag1.extend_tags(t_expects)
        t_got = list(t_tag1.list_tags())
        self.assertListEqual(t_expects, t_got)

    def test_pop_tag(self, ):
        t_tag1 = Tag('test1')
        t_tag2 = Tag('test2')
        t_tag1.append_tag(t_tag2)
        self.assertEqual(t_tag2, t_tag1.pop_tag())

    def test_remove_tag(self, ):
        t_tag1 = Tag('test1')
        t_tag2 = Tag('test2')
        t_tag3 = Tag('test3')
        t_expects = [t_tag2, t_tag3, ]
        t_tag1.extend_tags(t_expects)
        t_expects.remove(t_tag3)
        t_tag1.remove_tag(t_tag3)
        t_got = list(t_tag1.list_tags())
        self.assertListEqual(t_expects, t_got)

    def test_list_tags(self, ):
        t_tag1 = Tag('test1')
        t_tag2 = Tag('test2')
        t_tag3 = Tag('test3')
        t_expects = [t_tag2, t_tag3, ]
        t_tag1.extend_tags(t_expects)
        t_got = list(t_tag1.list_tags())
        self.assertListEqual(t_expects, t_got)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        pass



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_tag.py ends here
