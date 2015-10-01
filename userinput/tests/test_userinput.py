#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_userinput.py

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
from userinput import userinput
import os
import tempfile


class TestSample(MockerTestCase):
    """2014/09/11"""
    @classmethod
    def setUpClass(cls):
        cls.sampletext = 'sampletext'


class TestCommandlineUserInput(TestSample):
    @classmethod
    def setUpClass(cls):
        cls.sampletext = 'sampletext'

    def get_obj(self, ):
        return userinput.CommandlineUserInput(self.sampletext)

    def setUp(self):
        self.uinput = self.get_obj()
        self.mocker.replay()

    def test_input(self, ):
        expect = self.sampletext
        got = self.uinput.input()
        self.assertEqual(expect, got, msg='Failed: {} expect: \{}, got: \{}'
                         .format(self.uinput.__class__.__name__, expect, got))

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        pass


class TestConsoleUserInput(TestCommandlineUserInput):
    """2014/09/11"""

    def get_obj(self, ):
        return userinput.ConsoleUserInput(self.sampletext)

    def setUp(self):
        self.uinput = self.get_obj()
        dummyinput = self.mocker.replace('__builtin__.input')
        dummyinput(ANY)
        self.mocker.result(self.sampletext)
        self.mocker.count(0, None)

        dummyrawinput = self.mocker.replace('__builtin__.raw_input')
        dummyrawinput(ANY)
        self.mocker.result(self.sampletext)
        self.mocker.count(0, None)

        self.mocker.replay()

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        pass


class TestFileUserInput(TestCommandlineUserInput):
    """2014/09/11"""
    @classmethod
    def setUpClass(cls):
        cls.tmppath = os.path.join(tempfile.gettempdir(), 'testfile.txt')
        files = open(cls.tmppath, 'w')
        files.writelines(cls.sampletext)
        files.close()

    def get_obj(self, ):
        return userinput.FileUserInput(self.tmppath)

    def setUp(self):
        self.uinput = self.get_obj()
        self.mocker.replay()

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        if os.path.exists(cls.tmppath):
            os.remove(cls.tmppath)


# class TestGUIUserInput(TestCommandlineUserInput):
#     """2014/09/11"""
#     # TODO: (Atami) [2014/09/11]
#     # wait window and send Enter key

#     def get_obj(self, ):
#         return userinput.GUIUserInput(default=self.sampletext)

#     def setUp(self):
#         self.uinput = self.get_obj()
#         dummyinput = self.mocker.replace('easygui.enterbox')
#         dummyinput(ANY)
#         self.mocker.result(self.sampletext)
#         self.mocker.count(0, None)
#         self.mocker.replay()

#     def tearDown(self):
#         pass

#     @classmethod
#     def tearDownClass(cls, ):
#         pass


###############################################################################
class TestCommandlineUserInput2(TestSample):
    """2014/09/11"""

    def setUp(self):
        self.uinput = userinput.CommandlineUserInput(self.sampletext)
        self.mocker.replay()

    def test_setcmdline(self):
        expect = 'anothertext'
        self.uinput.setcmdline(expect)
        got = self.uinput.getcmdline()
        self.assertEqual(
            expect, got,
            msg='Failed: CommandlineUserInput.setcmdline expect: \{}, got: \{}'
            .format(expect, got))

    def test_getcmdline(self, ):
        expect = self.sampletext
        got = self.uinput.getcmdline()
        self.assertEqual(
            expect, got,
            msg='Failed: CommandlineUserInput.getcmdline expect: \{}, got: \{}'
            .format(expect, got))

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        pass


class TestConsoleUserInput2(TestSample):
    """2014/09/11"""
    def setUp(self):
        self.uinput = userinput.ConsoleUserInput(self.sampletext)
        self.mocker.replay()

    def test_setprompt(self):
        expect = 'anothertext'
        self.uinput.setprompt(expect)
        got = self.uinput.getprompt()
        self.assertEqual(
            expect, got,
            msg='Failed: ConsoleUserInput.setprompt expect: \{}, got: \{}'
            .format(expect, got))

    def test_getcmdline(self, ):
        expect = self.sampletext
        got = self.uinput.getprompt()
        self.assertEqual(
            expect, got,
            msg='Failed: ConsoleUserInput.getcmdline expect: \{}, got: \{}'
            .format(expect, got))

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        pass


class TestFileUserInput2(TestSample):
    """2014/09/11"""

    def setUp(self):
        self.uinput = userinput.FileUserInput(self.sampletext)
        self.mocker.replay()

    def test_setpath(self):
        expect = 'anothertext'
        self.uinput.setpath(expect)
        got = self.uinput.getpath()
        self.assertEqual(
            expect, got,
            msg='Failed: FileUserInput.setpath expect: \{}, got: \{}'
            .format(expect, got))

    def test_getcmdline(self, ):
        expect = self.sampletext
        got = self.uinput.getpath()
        self.assertEqual(
            expect, got,
            msg='Failed: FileUserInput.getpath expect: \{}, got: \{}'
            .format(expect, got))

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        pass


class TestGUIUserInput(TestSample):
    """2014/09/11"""

    def setUp(self):
        self.uinput = userinput.GUIUserInput(
            self.sampletext, self.sampletext, self.sampletext)
        self.mocker.replay()

    def test_set_msg(self):
        expect = 'anothertext'
        self.uinput.set_msg(expect)
        got = self.uinput.get_msg()
        self.assertEqual(
            expect, got,
            msg='Failed: GUIUserInput.set_msg expect: \{}, got: \{}'
            .format(expect, got))

    def test_get_msg(self, ):
        expect = self.sampletext
        got = self.uinput.get_msg()
        self.assertEqual(
            expect, got,
            msg='Failed: GUIUserInput.get_msg expect: \{}, got: \{}'
            .format(expect, got))

    def test_set_title(self):
        expect = 'anothertext'
        self.uinput.set_title(expect)
        got = self.uinput.get_title()
        self.assertEqual(
            expect, got,
            msg='Failed: GUIUserInput.set_title expect: \{}, got: \{}'
            .format(expect, got))

    def test_get_title(self, ):
        expect = self.sampletext
        got = self.uinput.get_title()
        self.assertEqual(
            expect, got,
            msg='Failed: GUIUserInput.get_title expect: \{}, got: \{}'
            .format(expect, got))

    def test_set_default(self):
        expect = 'anothertext'
        self.uinput.set_default(expect)
        got = self.uinput.get_default()
        self.assertEqual(
            expect, got,
            msg='Failed: GUIUserInput.set_default expect: \{}, got: \{}'
            .format(expect, got))

    def test_get_default(self, ):
        expect = self.sampletext
        got = self.uinput.get_default()
        self.assertEqual(
            expect, got,
            msg='Failed: GUIUserInput.get_default expect: \{}, got: \{}'
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
# test_userinput.py ends here
