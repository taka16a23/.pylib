#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_button.py

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
from material.forms.tags.button import Button


class TestButton(TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.tag = Button()

    def test_enable_autofocus(self, ):
        self.tag.enable_autofocus()
        self.assertTrue(self.tag.is_autofocus())
        self.assertEqual('', str(self.tag.attrs[self.tag.AttributeNames.AUTOFOCUS]))

    def test_disable_autofocus(self, ):
        self.tag.enable_autofocus()
        self.assertTrue(self.tag.is_autofocus())
        self.assertEqual('', str(self.tag.attrs[self.tag.AttributeNames.AUTOFOCUS]))
        self.tag.disable_autofocus()
        self.assertFalse(self.tag.is_autofocus())
        self.assertFalse(self.tag.AttributeNames.AUTOFOCUS in self.tag.attrs)

    def test_is_autofocus(self, ):
        self.tag.enable_autofocus()
        self.assertTrue(self.tag.is_autofocus())
        self.assertEqual('', str(self.tag.attrs[self.tag.AttributeNames.AUTOFOCUS]))
        self.tag.disable_autofocus()
        self.assertFalse(self.tag.is_autofocus())
        self.assertFalse(self.tag.AttributeNames.AUTOFOCUS in self.tag.attrs)

    def test_set_autocomplete(self, ):
        self.tag.set_autocomplete(self.tag.AutoComplete.ON)
        self.assertEqual(self.tag.get_autocomplete(), self.tag.AutoComplete.ON)

    def test_get_autocomplete(self, ):
        self.tag.set_autocomplete(self.tag.AutoComplete.ON)
        self.assertEqual(self.tag.get_autocomplete(), self.tag.AutoComplete.ON)

    def test_enable_autocomplete(self, ):
        self.tag.enable_autocomplete()
        self.assertEqual(self.tag.get_autocomplete(), self.tag.AutoComplete.ON)

    def test_disable_autocomplete(self, ):
        self.tag.disable_autocomplete()
        self.assertEqual(self.tag.get_autocomplete(), self.tag.AutoComplete.OFF)

    def test_remove_autocomplete(self, ):
        self.tag.disable_autocomplete()
        self.tag.remove_autocomplete()
        self.assertEqual(self.tag.get_autocomplete(), None)

    def test_disable_button(self, ):
        self.tag.disable_button()
        self.assertTrue(self.tag.is_enable_button())

    def test_enable_button(self, ):
        self.tag.disable_button()
        self.assertTrue(self.tag.is_enable_button())
        self.tag.enable_button()
        self.assertFalse(self.tag.is_enable_button())

    def test_is_enable_button(self, ):
        self.tag.disable_button()
        self.assertTrue(self.tag.is_enable_button())
        self.tag.enable_button()
        self.assertFalse(self.tag.is_enable_button())

    def test_set_form(self, ):
        self.tag.set_form('id')
        self.assertEqual('id', str(self.tag.get_form()))

    def test_get_form(self, ):
        self.tag.set_form('id')
        self.assertEqual('id', str(self.tag.get_form()))

    def test_remove_form(self, ):
        self.tag.set_form('id')
        self.assertEqual('id', str(self.tag.get_form()))
        self.tag.remove_form()
        self.assertIsNone(self.tag.get_form())

    def test_set_formaction(self, ):
        self.tag.set_formaction('/test')
        self.assertEqual('/test', str(self.tag.get_formaction()))

    def test_get_formaction(self, ):
        self.tag.set_formaction('/test')
        self.assertEqual('/test', str(self.tag.get_formaction()))

    def test_remove_formaction(self, ):
        self.tag.set_formaction('/test')
        self.assertEqual('/test', str(self.tag.get_formaction()))
        self.tag.remove_formaction()

    def test_set_formenctype(self, ):
        self.tag.set_formenctype('multipart/form-data')
        self.assertEqual('multipart/form-data', self.tag.get_formenctype())

    def test_get_formenctype(self, ):
        self.tag.set_formenctype('multipart/form-data')
        self.assertEqual('multipart/form-data', self.tag.get_formenctype())

    def test_remove_formenctype(self, ):
        self.tag.set_formenctype('multipart/form-data')
        self.assertEqual('multipart/form-data', self.tag.get_formenctype())
        self.tag.remove_formenctype()
        self.assertIsNone(self.tag.get_formenctype())

    def test_set_formmethod(self, ):
        self.tag.set_formmethod('get')
        self.assertEqual('get', self.tag.get_formmethod())

    def test_get_formmethod(self, ):
        self.tag.set_formmethod('get')
        self.assertEqual('get', self.tag.get_formmethod())

    def test_remove_formmethod(self, ):
        self.tag.set_formmethod('get')
        self.assertEqual('get', self.tag.get_formmethod())
        self.tag.remove_formmethod()
        self.assertIsNone(self.tag.get_formmethod())

    def test_set_formtarget(self, ):
        self.tag.set_formtarget(self.tag.FormTarget.SELF)
        self.assertEqual(self.tag.FormTarget.SELF, self.tag.get_formtarget())

    def test_get_formtarget(self, ):
        self.tag.set_formtarget(self.tag.FormTarget.SELF)
        self.assertEqual(self.tag.FormTarget.SELF, self.tag.get_formtarget())

    def test_remove_formtarget(self, ):
        self.tag.set_formtarget(self.tag.FormTarget.SELF)
        self.assertEqual(self.tag.FormTarget.SELF, self.tag.get_formtarget())
        self.tag.remove_formtarget()
        self.assertIsNone(self.tag.get_formtarget())

    def test_set_name(self, ):
        self.tag.set_name('test')
        self.assertEqual('test', self.tag.get_name())

    def test_get_name(self, ):
        self.tag.set_name('test')
        self.assertEqual('test', self.tag.get_name())

    def test_remove_name(self, ):
        self.tag.set_name('test')
        self.assertEqual('test', self.tag.get_name())
        self.tag.remove_name()
        self.assertIsNone(self.tag.get_name())

    def test_set_type(self, ):
        self.tag.set_type(self.tag.Type.SUBMIT)
        self.assertEqual(self.tag.Type.SUBMIT, self.tag.get_type())

    def test_get_type(self, ):
        self.tag.set_type(self.tag.Type.SUBMIT)
        self.assertEqual(self.tag.Type.SUBMIT, self.tag.get_type())

    def test_remove_type(self, ):
        self.tag.set_type(self.tag.Type.SUBMIT)
        self.assertEqual(self.tag.Type.SUBMIT, self.tag.get_type())
        self.tag.remove_type()
        self.assertIsNone(self.tag.get_type())

    def test_set_value(self, ):
        self.tag.set_value('test')
        self.assertEqual('test', self.tag.get_value())

    def test_get_value(self, ):
        self.tag.set_value('test')
        self.assertEqual('test', self.tag.get_value())

    def test_remove_value(self, ):
        self.tag.set_value('test')
        self.assertEqual('test', self.tag.get_value())
        self.tag.remove_value()
        self.assertIsNone(self.tag.get_value())

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        pass



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_button.py ends here
