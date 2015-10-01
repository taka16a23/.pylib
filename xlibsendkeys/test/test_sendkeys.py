#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: test_sendkeys.py 302 2015-01-29 00:33:15Z t1 $
# $Revision: 302 $
# $Date: 2015-01-29 09:33:15 +0900 (Thu, 29 Jan 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-01-29 09:33:15 +0900 (Thu, 29 Jan 2015) $

r"""Name: test_sendkeys.py

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
from Xlib.display import Display
from Xlib import XK

from sendkeys import parse_line, replace_line, Keystring, Keysym, UPSTRINGS

# from mocker import *


# class TestSendkeys(MockerTestCase):
#     def setUp(self):

#         self.mocker.replay()

#     def test_sendkeys(self):
#         r"""sendkeys
#         """



#     def tearDown(self):
#         pass


def _main():
    d = Display()
    replaced_line = replace_line("hello{+}@world{{}Google\\{")
    print(replaced_line)
    token = parse_line(replaced_line)
    shift = Keysym(d, XK.XK_Shift_L).to_keycode()


    for str_ in token:
        if str_ in UPSTRINGS:
            shift.press_key()
        kstr = Keystring(d, str_)
        kstr.press_key()
        kstr.release_key()
        if str_ in UPSTRINGS:
            shift.release_key()
        d.sync()
    return 0

_main()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_sendkeys.py ends here
