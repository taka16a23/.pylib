#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_html_tag.py

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
from material.forms.tags.html_tag import HtmlTag


class TestHtmlTag(TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        pass

    def test_get_accesskey(self, ):
        t_tag = HtmlTag('div')
        t_got = t_tag.get_accesskey()
        self.assertIsNone(t_got)
        t_tag.append_accesskey('a')
        t_got = t_tag.get_accesskey()
        self.assertEqual(str(t_got), 'a')

    def test_append_accesskey(self, ):
        t_tag = HtmlTag('div')
        t_got = t_tag.attrs.get(t_tag.AttributeNames.ACCESSKEY, None)
        self.assertIsNone(t_got)
        t_tag.append_accesskey('a')
        t_got = t_tag.attrs.get(t_tag.AttributeNames.ACCESSKEY, None)
        self.assertEqual(str(t_got), 'a')
        t_tag.append_accesskey('b')
        t_got = t_tag.attrs.get(t_tag.AttributeNames.ACCESSKEY, None)
        t_got = str(t_got).split(' ')
        t_got.sort()
        t_expect = 'a b'.split(' ')
        t_expect.sort()
        self.assertListEqual(t_expect, t_got)

    def test_remove_accesskey(self, ):
        t_tag = HtmlTag('div')
        t_tag.append_accesskey('a')
        t_tag.append_accesskey('b')
        t_got = t_tag.attrs.get(t_tag.AttributeNames.ACCESSKEY, None)
        t_got = str(t_got).split(' ')
        t_got.sort()
        t_expect = 'a b'.split(' ')
        t_expect.sort()
        self.assertListEqual(t_expect, t_got)
        t_tag.remove_accesskey('b')
        t_got = t_tag.attrs.get(t_tag.AttributeNames.ACCESSKEY, None)
        self.assertEqual(str(t_got), 'a')

    def test_clear_accesskey(self, ):
        t_tag = HtmlTag('div')
        t_tag.append_accesskey('a')
        t_tag.append_accesskey('b')
        t_got = t_tag.attrs.get(t_tag.AttributeNames.ACCESSKEY, None)
        t_got = str(t_got).split(' ')
        t_got.sort()
        t_expect = 'a b'.split(' ')
        t_expect.sort()
        self.assertListEqual(t_expect, t_got)
        t_tag.clear_accesskeys()
        t_got = t_tag.attrs.get(t_tag.AttributeNames.ACCESSKEY, None)
        self.assertEqual(str(t_got), '')

    def test_delete_accesskey(self, ):
        t_tag = HtmlTag('div')
        t_tag.append_accesskey('a')
        t_got = t_tag.attrs.get(t_tag.AttributeNames.ACCESSKEY, None)
        self.assertEqual(str(t_got), 'a')
        t_tag.delete_accesskey()
        t_got = t_tag.attrs.get(t_tag.AttributeNames.ACCESSKEY, None)
        self.assertIsNone(t_got)

    def test_contains_accesskey(self, ):
        t_tag = HtmlTag('div')
        self.assertFalse(t_tag.contains_accesskey('a'))
        t_tag.append_accesskey('a')
        t_tag.append_accesskey('b')
        self.assertTrue(t_tag.contains_accesskey('a'))

    def test_set_autocapitalize(self, ):
        t_tag = HtmlTag('div')
        t_got = t_tag.get_attribute_value(HtmlTag.AttributeNames.AUTOCAPITALIZE, None)
        self.assertIsNone(t_got)
        t_tag.set_autocapitalize(HtmlTag.AutoCapitalize.OFF)
        t_got = t_tag.get_attribute_value(HtmlTag.AttributeNames.AUTOCAPITALIZE, None)
        self.assertEqual(HtmlTag.AutoCapitalize.OFF, t_got)

    def test_remove_autocapitalize(self, ):
        t_tag = HtmlTag('div')
        t_got = t_tag.get_attribute_value(HtmlTag.AttributeNames.AUTOCAPITALIZE, None)
        self.assertIsNone(t_got)
        t_tag.set_autocapitalize(HtmlTag.AutoCapitalize.OFF)
        t_got = t_tag.get_attribute_value(HtmlTag.AttributeNames.AUTOCAPITALIZE, None)
        self.assertEqual(HtmlTag.AutoCapitalize.OFF, t_got)
        t_tag.remove_autocapitalize()
        t_got = t_tag.get_attribute_value(HtmlTag.AttributeNames.AUTOCAPITALIZE, None)
        self.assertIsNone(t_got)

    def test_get_autocapitalize(self, ):
        t_tag = HtmlTag('div')
        t_got = t_tag.get_autocapitalize()
        self.assertIsNone(t_got)
        t_tag.set_autocapitalize(HtmlTag.AutoCapitalize.OFF)
        t_got = t_tag.get_autocapitalize()
        self.assertEqual(HtmlTag.AutoCapitalize.OFF, t_got)

    def test_append_class(self, ):
        t_tag = HtmlTag('div')
        t_got = t_tag.get_classes()
        self.assertIsNone(t_got)
        t_tag.append_class('test')
        t_got = str(t_tag.get_classes())
        self.assertEqual('test', t_got)
        t_tag.append_class('test2')
        t_got = str(t_tag.get_classes()).split(' ')
        t_got.sort()
        t_expect = ['test', 'test2']
        t_expect.sort()
        self.assertListEqual(t_expect, t_got)

    def test_remove_class(self, ):
        t_tag = HtmlTag('div')
        t_tag.append_class('test')
        t_tag.append_class('test2')
        t_got = str(t_tag.get_classes()).split(' ')
        t_got.sort()
        t_expect = ['test', 'test2']
        t_expect.sort()
        self.assertListEqual(t_expect, t_got)
        t_tag.remove_class('test2')
        t_got = str(t_tag.get_classes())
        t_expect = 'test'
        self.assertEqual(t_expect, t_got)

    def test_clear_classes(self, ):
        t_tag = HtmlTag('div')
        t_tag.append_class('test')
        t_tag.append_class('test2')
        t_got = str(t_tag.get_classes()).split(' ')
        t_got.sort()
        t_expect = ['test', 'test2']
        t_expect.sort()
        self.assertListEqual(t_expect, t_got)
        t_tag.clear_classes()
        t_got = str(t_tag.get_classes())
        self.assertEqual('', t_got)

    def test_delete_classes(self, ):
        t_tag = HtmlTag('div')
        t_tag.append_class('test')
        t_tag.append_class('test2')
        t_got = str(t_tag.get_classes()).split(' ')
        t_got.sort()
        t_expect = ['test', 'test2']
        t_expect.sort()
        self.assertListEqual(t_expect, t_got)
        t_tag.delete_classes()
        self.assertIsNone(t_tag.get_classes())

    def test_set_contentediatble(self, ):
        t_tag = HtmlTag('div')
        t_tag.set_contenteditable(t_tag.ContentEditable.TRUE)
        self.assertEqual(t_tag.ContentEditable.TRUE, t_tag.get_contenteditable())

    def test_enable_contenteditable(self, ):
        t_tag = HtmlTag('div')
        t_tag.enable_contenteditable()
        self.assertEqual(t_tag.ContentEditable.TRUE, t_tag.get_contenteditable())

    def test_disable_contenteditable(self, ):
        t_tag = HtmlTag('div')
        t_tag.disable_contenteditable()
        self.assertEqual(t_tag.ContentEditable.FALSE, t_tag.get_contenteditable())

    def test_remove_contenteditable(self, ):
        t_tag = HtmlTag('div')
        t_tag.enable_contenteditable()
        self.assertEqual(t_tag.ContentEditable.TRUE, t_tag.get_contenteditable())
        t_tag.remove_contenteditable()
        self.assertIsNone(t_tag.get_contenteditable())

    def test_contenteditable(self, ):
        t_tag = HtmlTag('div')
        t_tag.set_contenteditable(t_tag.ContentEditable.TRUE)
        self.assertEqual(t_tag.ContentEditable.TRUE, t_tag.get_contenteditable())

    def test_set_draggable(self, ):
        t_tag = HtmlTag('div')
        t_tag.set_draggable(t_tag.Draggable.TRUE)
        self.assertEqual(t_tag.Draggable.TRUE, t_tag.get_draggable())

    def test_enable_draggable(self, ):
        t_tag = HtmlTag('div')
        t_tag.enable_draggable()
        self.assertEqual(t_tag.Draggable.TRUE, t_tag.get_draggable())

    def test_disable_draggable(self, ):
        t_tag = HtmlTag('div')
        t_tag.disable_draggable()
        self.assertEqual(t_tag.Draggable.FALSE, t_tag.get_draggable())

    def test_remove_draggable(self, ):
        t_tag = HtmlTag('div')
        t_tag.disable_draggable()
        self.assertEqual(t_tag.Draggable.FALSE, t_tag.get_draggable())
        t_tag.remove_draggable()
        self.assertIsNone(t_tag.get_draggable())

    def test_get_draggable(self, ):
        t_tag = HtmlTag('div')
        t_tag.disable_draggable()
        self.assertEqual(t_tag.Draggable.FALSE, t_tag.get_draggable())

    def test_set_hidden(self, ):
        t_tag = HtmlTag('div')
        self.assertFalse(t_tag.has_hidden())
        t_tag.set_hidden()
        self.assertTrue(t_tag.has_hidden())

    def test_remove_hidden(self, ):
        t_tag = HtmlTag('div')
        t_tag.set_hidden()
        self.assertTrue(t_tag.has_hidden())
        t_tag.remove_hidden()
        self.assertFalse(t_tag.has_hidden())

    def test_has_hidden(self, ):
        t_tag = HtmlTag('div')
        t_tag.set_hidden()
        self.assertTrue(t_tag.has_hidden())

    def test_set_id(self, ):
        t_tag = HtmlTag('div')
        t_tag.set_id('test')
        self.assertEqual('test', t_tag.get_id())
        t_tag.set_id('test2')
        self.assertEqual('test2', t_tag.get_id())

    def test_remove_id(self, ):
        t_tag = HtmlTag('div')
        t_tag.set_id('test')
        t_tag.remove_id()
        self.assertIsNone(t_tag.get_id())

    def test_get_id(self, ):
        t_tag = HtmlTag('div')
        t_tag.set_id('test')
        self.assertEqual('test', t_tag.get_id())

    def test_append_itemprop(self, ):
        t_tag = HtmlTag('div')
        t_tag.append_itemprop('name')
        self.assertEqual('name', str(t_tag.get_itemprop()))

    def test_delete_itemprop(self, ):
        t_tag = HtmlTag('div')
        t_tag.append_itemprop('name')
        self.assertEqual('name', str(t_tag.get_itemprop()))
        t_tag.delete_itemprop()
        self.assertIsNone(t_tag.get_itemprop())

    def test_set_lang(self, ):
        t_tag = HtmlTag('div')
        t_tag.set_lang('test')
        self.assertEqual('test', str(t_tag.get_lang()))
        t_tag.set_lang('test2')
        self.assertEqual('test2', str(t_tag.get_lang()))

    def test_remove_lang(self, ):
        t_tag = HtmlTag('div')
        t_tag.set_lang('test')
        self.assertEqual('test', str(t_tag.get_lang()))
        t_tag.remove_lang()
        self.assertIsNone(t_tag.get_lang())

    def test_get_lang(self, ):
        t_tag = HtmlTag('div')
        t_tag.set_lang('test')
        self.assertEqual('test', str(t_tag.get_lang()))

    def test_set_spellcheck(self, ):
        t_tag = HtmlTag('div')
        t_tag.set_spellcheck(t_tag.Spellcheck.TRUE)
        self.assertEqual(t_tag.Spellcheck.TRUE, t_tag.get_spellcheck())

    def test_enable_spellcheck(self, ):
        t_tag = HtmlTag('div')
        t_tag.enable_spellcheck()
        self.assertEqual(t_tag.Spellcheck.TRUE, t_tag.get_spellcheck())

    def test_disable_spellcheck(self, ):
        t_tag = HtmlTag('div')
        t_tag.disable_spellcheck()
        self.assertEqual(t_tag.Spellcheck.FALSE, t_tag.get_spellcheck())

    def test_remove_spellcheck(self, ):
        t_tag = HtmlTag('div')
        t_tag.remove_spellcheck()
        self.assertIsNone(t_tag.get_spellcheck())

    def test_append_style(self, ):
        self.skipTest('')

    def test_set_tabindex(self, ):
        t_tag = HtmlTag('div')
        t_tag.set_tabindex('1')
        self.assertEqual('1', str(t_tag.get_tabindex()))

    def test_remove_tabindex(self, ):
        t_tag = HtmlTag('div')
        t_tag.set_tabindex('1')
        self.assertEqual('1', str(t_tag.get_tabindex()))
        t_tag.remove_tabindex()
        self.assertIsNone(t_tag.get_tabindex())
        with self.assertRaises(ValueError):
            t_tag.set_tabindex('a')
        t_tag.set_tabindex(32767)
        with self.assertRaises(ValueError):
            t_tag.set_tabindex(32768)

    def test_get_tabindex(self, ):
        t_tag = HtmlTag('div')
        t_tag.set_tabindex('1')
        self.assertEqual('1', str(t_tag.get_tabindex()))

    def test_set_title(self, ):
        t_tag = HtmlTag('div')
        t_tag.set_title('test')
        self.assertEqual('test', t_tag.get_title())

    def test_remove_title(self, ):
        t_tag = HtmlTag('div')
        t_tag.set_title('test')
        self.assertEqual('test', t_tag.get_title())
        t_tag.remove_title()
        self.assertIsNone(t_tag.get_title())

    def test_get_title(self, ):
        t_tag = HtmlTag('div')
        t_tag.set_title('test')
        self.assertEqual('test', t_tag.get_title())

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        pass



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_html_tag.py ends here
