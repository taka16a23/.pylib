#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_attributes.py

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
from material.forms.tags.attributes.attributes import Attributes
from material.forms.tags.attributes.attr_value import AttrValue


class TestAttributes(TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        pass

    def test_set(self, ):
        t_attributes = Attributes()
        self.assertIsNone(t_attributes.get_value('test'))
        t_expect = ['value1', 'value2', ]
        t_expect.sort()
        t_attributes.set_value('test', t_expect)
        t_got = t_attributes.get_value('test').list()
        t_got.sort()
        self.assertListEqual(t_expect, t_got)
        # override
        t_expect = ['value1', ]
        t_attributes.set_value('test', t_expect)
        t_got = t_attributes.get_value('test').list()
        t_got.sort()
        self.assertListEqual(t_expect, t_got)
        # set none
        t_attributes.set_value('test', None)
        self.assertIsNone(t_attributes.get_value('test'))
        # set string
        t_expect_str = 'value1 value2'
        t_expect = t_expect_str.split(' ')
        t_expect.sort()
        t_attributes.set_value('test', t_expect_str)
        t_got = t_attributes.get_value('test').list()
        t_got.sort()
        self.assertListEqual(t_expect, t_got)
        # AttrValue
        t_attributes.set_value('test', AttrValue(t_expect_str))
        self.assertListEqual(t_expect, t_got)

    def test_append_value(self, ):
        t_attributes = Attributes()
        t_expect = ['value1', ]
        t_attributes.append_value('test', t_expect[0])
        t_got = t_attributes.get_value('test').list()
        self.assertListEqual(t_expect, t_got)
        # 2 values
        t_expect = ['value1', 'value2', ]
        t_attributes = Attributes()
        t_attributes.append_value('test', t_expect[0])
        t_attributes.append_value('test', t_expect[1])
        t_expect.sort()
        t_got = t_attributes.get_value('test').list()
        t_got.sort()
        self.assertListEqual(t_expect, t_got)

    def test_remove_value(self, ):
        t_attributes = Attributes()
        t_expect = ['value1', ]
        t_attributes.append_value('test', t_expect[0])
        t_got = t_attributes.get_value('test').list()
        self.assertEqual(t_expect, t_got)
        t_attributes.remove_value('test', 'value1')
        self.assertEqual('', str(t_attributes.get_value('test')))
        t_attributes.append_value('test', t_expect[0])
        t_attributes.remove_value('test', 'valueX')
        t_got = t_attributes.get_value('test').list()
        self.assertEqual(t_expect, t_got)

    def test_clear_value(self, ):
        t_attributes = Attributes()
        t_expect = ['value1', ]
        t_attributes.append_value('test', t_expect[0])
        t_got = t_attributes.get_value('test').list()
        self.assertEqual(t_expect, t_got)
        t_attributes.clear_value('test')
        self.assertEqual('', str(t_attributes.get_value('test')))

    def test_remove_attribute(self, ):
        t_attributes = Attributes()
        t_expect = ['value1', ]
        t_attributes.append_value('test', t_expect[0])
        self.assertIn('test', t_attributes)
        t_attributes.remove_attribute('test')
        self.assertNotIn('test', t_attributes)

    def test_none(self, ):
        t_attributes = Attributes()
        t_attributes.set_none('test')
        self.assertIsNone(t_attributes.get_value('test'))

    def test_get_value(self, ):
        t_attributes = Attributes()
        self.assertIsNone(t_attributes.get_value('test'))
        t_attributes.set_value('test', 'value1')
        self.assertEqual('value1', str(t_attributes.get_value('test')))

    def test_contain_value(self, ):
        t_attributes = Attributes()
        self.assertFalse(t_attributes.contains_value('noexists_key', 'value1'))
        t_attributes.set_value('NoneValue', None)
        self.assertFalse(t_attributes.contains_value('NoneValue', 'value1'))
        t_attributes.set_value('test', 'value1')
        self.assertTrue(t_attributes.contains_value('test', 'value1'))

    def test_update(self, ):
        t_expect = ['value1', 'value2', ]
        t_expect.sort()
        t_attributes1 = Attributes()
        t_attributes2 = Attributes()
        t_attributes2.append_value('test', 'value1')
        t_attributes2.append_value('test', 'value2')
        t_attributes1.update(t_attributes2)
        t_got = t_attributes1.get_value('test').list()
        t_got.sort()
        self.assertListEqual(t_expect, t_got)
        t_attributes1 = Attributes()
        t_attributes1.update(test='value1 value2')
        t_got = t_attributes1.get_value('test').list()
        t_got.sort()
        self.assertListEqual(t_expect, t_got)
        t_attributes1 = Attributes()
        t_attributes1.update({'test': 'value1 value2',})
        t_got = t_attributes1.get_value('test').list()
        t_got.sort()
        self.assertListEqual(t_expect, t_got)

    def test_setdefault(self, ):
        t_expect = ['value1', 'value2', ]
        t_expect.sort()
        t_attributes1 = Attributes()
        t_attributes1.setdefault('test', 'value1 value2')
        t_got = t_attributes1.get_value('test').list()
        t_got.sort()
        self.assertListEqual(t_expect, t_got)
        t_attributes1.setdefault('test', 'value3 value3')
        t_got = t_attributes1.get_value('test').list()
        t_got.sort()
        self.assertListEqual(t_expect, t_got)

    def test_setitem(self, ):
        t_expect = ['value1', 'value2', ]
        t_expect.sort()
        t_attributes1 = Attributes()
        t_attributes1['test'] = 'value1 value2'
        t_got = t_attributes1.get_value('test').list()
        t_got.sort()
        self.assertListEqual(t_expect, t_got)
        t_expect = AttrValue()
        t_attributes1['test2'] = t_expect
        self.assertEqual(id(t_attributes1['test2']), id(t_expect))

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        pass



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_attributes.py ends here
