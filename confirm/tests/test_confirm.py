#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: test_confirm.py 230 2014-09-13 08:17:36Z t1 $
# $Revision: 230 $
# $Date: 2014-09-13 17:17:36 +0900 (Sat, 13 Sep 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-09-13 17:17:36 +0900 (Sat, 13 Sep 2014) $

r"""Name: test_confirm.py

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
from confirm.confirmobj import ConsoleConfirm, GUIConfirm


class TestConsoleConfirm_mock_input(MockerTestCase):
    """2014/09/12"""
    @classmethod
    def setUpClass(cls):
        cls.prompt = 'hello'
        cls.acceptables = ['y', 'yes']
        cls.disacceptables = ['n', 'no']

    def setUp(self):
        self.confirm = ConsoleConfirm(
            self.prompt, self.acceptables, self.disacceptables)
        rinput = self.mocker.replace('__builtin__.raw_input')
        for key in self.confirm.get_acceptables():
            rinput(ANY)
            self.mocker.result(key)
        for key in self.confirm.get_disacceptables():
            rinput(ANY)
            self.mocker.result(key)
        rinput(ANY)
        self.mocker.result('Nothing')
        self.mocker.replay()

    def test__input(self, ):
        for key in self.acceptables:
            self.assertEqual(key.lower(), self.confirm._input())
        for key in self.disacceptables:
            self.assertEqual(key.lower(), self.confirm._input())
        self.confirm._input() # dummy

    def test_confirm(self, ):
        for _ in self.confirm.get_acceptables():
            self.assertTrue(self.confirm.confirm())
        for _ in self.confirm.get_disacceptables():
            self.assertFalse(self.confirm.confirm())
        self.assertIsNone(self.confirm.confirm())

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        pass



class TestConsoleConfirm(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.prompt = 'hello'
        cls.acceptables = ['y', 'yes']
        cls.disacceptables = ['n', 'no']

    def setUp(self):
        self.confirm = ConsoleConfirm(
            self.prompt, self.acceptables, self.disacceptables)
        self.mocker.replay()

    def test_get_prompt(self, ):
        got = self.confirm.get_prompt()
        self.assertEqual(
            self.prompt, got,
            msg='Failed: ConsoleConfirm.get_prompt expect: \{}, got: \{}'
            .format(self.prompt, got))

    def test_set_prompt(self, ):
        expect = 'world'
        self.confirm.set_prompt(expect)
        got = self.confirm.get_prompt()
        self.assertEqual(
            expect, got,
            msg='Failed: ConsoleConfirm.set_prompt expect: \{}, got: \{}'
            .format(expect, got))

    def test_get_acceptables(self, ):
        got = self.confirm.get_acceptables()
        self.assertListEqual(got, self.acceptables)

    def test_set_acceptables(self, ):
        expect = ['y', ]
        self.confirm.set_acceptables(expect)
        got = self.confirm.get_acceptables()
        self.assertListEqual(expect, got)

    def test_get_disacceptables(self, ):
        got = self.confirm.get_disacceptables()
        self.assertListEqual(got, self.disacceptables)

    def test_set_disacceptables(self, ):
        expect = ['n', ]
        self.confirm.set_disacceptables(expect)
        got = self.confirm.get_disacceptables()
        self.assertListEqual(expect, got)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        pass


class TestGUIConfirm_mock_input(MockerTestCase):
    """2014/09/12"""
    @classmethod
    def setUpClass(cls):
        cls.title = 'TestTitle'
        cls.msg = 'TestMessage'

    def setUp(self):
        self.confirm = GUIConfirm(self.title, self.msg)
        askyesno = self.mocker.replace('tkMessageBox.askyesno')
        askyesno(ANY)
        self.mocker.result(True)
        askyesno(ANY)
        self.mocker.result(False)
        askyesno(ANY)
        self.mocker.result('Nothing')
        self.mocker.replay()

    def test_confirm(self):
        self.skipTest('GUI test not inpremented.')
        self.assertTrue(self.confirm.confirm())
        self.assertFalse(self.confirm.confirm())
        self.assertIsNone(self.confirm.confirm())

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        pass



class TestGUIConfirm(MockerTestCase):
    """2014/09/12"""
    @classmethod
    def setUpClass(cls):
        cls.title = 'TestTitle'
        cls.msg = 'TestMessage'

    def setUp(self):
        self.confirm = GUIConfirm(self.title, self.msg)
        self.mocker.replay()

    def test_get_title(self, ):
        got = self.confirm.get_title()
        self.assertEqual(self.title, got,
                         msg='Failed: GUIConfirm.get_title expect: \{}, got: \{}'
                         .format(self.title, got))

    def test_set_title(self, ):
        expect = 'TestTitle2'
        self.confirm.set_title(expect)
        got = self.confirm.get_title()
        self.assertEqual(expect, got,
                         msg='Failed: GUIConfirm.set_title expect: \{}, got: \{}'
                         .format(expect, got))

    def test_get_msg(self, ):
        got = self.confirm.get_msg()
        self.assertEqual(self.msg, got,
                         msg='Failed: GUIConfirm.get_msg expect: \{}, got: \{}'
                         .format(self.msg, got))

    def test_set_msg(self, ):
        expect = 'TestMessage2'
        self.confirm.set_msg(expect)
        got = self.confirm.get_msg()
        self.assertEqual(expect, got,
                         msg='Failed: GUIConfirm.set_msg expect: \{}, got: \{}'
                         .format(expect, got))

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        pass





# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_confirm.py ends here
