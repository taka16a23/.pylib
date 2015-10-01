#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: test_redirect.py 92 2013-12-07 10:20:05Z t1 $
# $Revision: 92 $
# $Date: 2013-12-07 19:20:05 +0900 (Sat, 07 Dec 2013) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2013-12-07 19:20:05 +0900 (Sat, 07 Dec 2013) $

r"""\
Name: test_redirect.py

['skipTest']

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
from t1.sysutil import redirect
import sys


class TestRedirect(MockerTestCase):
    def setUp(self):
        self.hash_stdout = hash(sys.stdout)
        self.hash_stderr = hash(sys.stderr)
        self.mocker.replay()

    def test_with_mute_redirecting(self, ):
        r"""Confirm redirect to stdout/stderr."""
        with redirect.with_mute():
            self.assertNotEqual(self.hash_stdout, hash(sys.stdout),
                                msg='Failed: not replaced sys.stdout')
            self.assertNotEqual(self.hash_stderr, hash(sys.stderr),
                                msg='Failed: not replaced sys.stderr')
            replaced_stdout = hash(sys.stdout)
            replaced_stderr = hash(sys.stderr)
        self.assertEqual(self.hash_stdout, hash(sys.stdout),
                         msg='Failed: Not recover sys.stdout')
        self.assertEqual(self.hash_stderr, hash(sys.stderr),
                         msg='Failed: Not recover sys.stderr')
        self.assertNotEqual(self.hash_stdout, replaced_stdout)
        self.assertNotEqual(self.hash_stderr, replaced_stderr)

    def test_with_nostdout_redirecting(self, ):
        r"""Confirm redirect to stdout."""
        with redirect.with_nostdout():
            self.assertNotEqual(self.hash_stdout, hash(sys.stdout),
                                msg='Failed: not replaced sys.stdout')
            replaced_stdout = hash(sys.stdout)
        self.assertEqual(self.hash_stdout, hash(sys.stdout),
                         msg='Failed: Not recover sys.stdout')
        self.assertNotEqual(self.hash_stdout, replaced_stdout)

    def test_with_nostderr_redirecting(self, ):
        r"""Confirm redirect to stderr."""
        with redirect.with_nostderr():
            self.assertNotEqual(self.hash_stderr, hash(sys.stderr),
                                msg='Failed: not replaced sys.stderr')
            replaced_stderr = hash(sys.stderr)
        self.assertEqual(self.hash_stderr, hash(sys.stderr),
                         msg='Failed: Not recover sys.stderr')
        self.assertNotEqual(self.hash_stderr, replaced_stderr)

    def test_mute_redirecting(self, ):
        r"""Decorator `mute' redirect to stdout/stderr."""
        @redirect.mute
        def dummyfunc():
            return hash(sys.stdout), hash(sys.stderr)

        replaced_stdout, replaced_stderr = dummyfunc()
        self.assertNotEqual(self.hash_stdout, replaced_stdout, msg='Failed')
        self.assertNotEqual(self.hash_stderr, replaced_stderr, msg='Failed')

    def test_mute_stdout_redirecting(self, ):
        r"""Decorator `mute_stdout' redirect to stdout."""
        @redirect.mute_stdout
        def dummyfunc():
            return hash(sys.stdout)
        replaced_stdout = dummyfunc()
        self.assertNotEqual(self.hash_stdout, replaced_stdout, msg='Failed')

    def test_mute_stderr_redirecting(self, ):
        r"""Decorator `mute_stderr' redirect to stderr."""
        @redirect.mute_stderr
        def dummyfunc():
            return hash(sys.stderr)
        replaced_stderr = dummyfunc()
        self.assertNotEqual(self.hash_stderr, replaced_stderr, msg='Failed')

    def test_redirect_redirecting(self, ):
        r"""Decorator `redirect' redirect to stdout/stderr."""
        self.skipTest('need other redirection')

    def tearDown(self):
        pass


class TestPrintRedirect(MockerTestCase):
    def setUp(self):
        from cStringIO import StringIO
        self._stdout, self._stderr = sys.stdout, sys.stderr
        sys.stdout, sys.stderr = StringIO(), StringIO()
        self.mocker.replay()

    def test_with_mute_print(self):
        r"""Context `with_mute' comfirm prints."""
        with redirect.with_mute():
            print('dummyprint')
            sys.stderr.write('dummyprint')
        self.assertEqual(sys.stdout.getvalue(), '',
                         msg=("Failed: `with_mute' expect sys.stdout ''.\n"
                              "but we got {}".format(sys.stdout.getvalue())))
        self.assertEqual(sys.stderr.getvalue(), '',
                         msg=("Failed: `with_mute' expect sys.stderr ''.\n"
                              "but we got {}".format(sys.stderr.getvalue())))

    def test_with_nostdout_print(self, ):
        r"""Context `with_nostdout' comfirm prints."""
        with redirect.with_nostdout():
            print('dummyprint')
        self.assertEqual(sys.stdout.getvalue(), '',
                         msg=("Failed: `with_nostdout' expect sys.stdout ''.\n"
                              "but we got {}".format(sys.stdout.getvalue())))

    def test_with_nostderr_print(self, ):
        r"""Context `with_nostderr' comfirm prints."""
        with redirect.with_nostderr():
            sys.stdout.write('dummyprint')
        self.assertEqual(sys.stderr.getvalue(), '',
                         msg=("Failed: `with_nostdout' expect sys.stdout ''.\n"
                              "but we got {}".format(sys.stderr.getvalue())))

    def test_mute_print(self):
        r"""Context `mute_print' comfirm prints."""
        @redirect.mute
        def dummyfunc():
            print('dummyprint')
            sys.stderr.write('dummyprint')
        self.assertEqual(sys.stdout.getvalue(), '',
                         msg=("Failed: `mute' expect sys.stdout ''.\n"
                              "but we got {}".format(sys.stdout.getvalue())))

        self.assertEqual(sys.stderr.getvalue(), '',
                         msg=("Failed: `mute' expect sys.stderr ''.\n"
                              "but we got {}".format(sys.stderr.getvalue())))

    def test_mute_stdout_print(self):
        r"""Context `mute_stdout_print' comfirm prints."""
        @redirect.mute_stdout
        def dummyfunc():
            print('dummyprint')
        self.assertEqual(sys.stdout.getvalue(), '',
                         msg=("Failed: `mute_stdout' expect sys.stdout ''.\n"
                              "but we got {}".format(sys.stdout.getvalue())))

    def test_mute_stderr_print(self):
        r"""Context `mute_stdout_print' comfirm prints."""
        @redirect.mute_stdout
        def dummyfunc():
            print('dummyprint')
        self.assertEqual(sys.stderr.getvalue(), '',
                         msg=("Failed: `mute_stderr' expect sys.stderr ''.\n"
                              "but we got {}".format(sys.stderr.getvalue())))

    def test_redirect_print(self, ):
        r"""Context `redirect' comfirm prints."""
        from cStringIO import StringIO
        @redirect.redirect(stdout=StringIO(), stderr=StringIO())
        def dummyfunc():
            print('dummyprint')
            sys.stderr.write('dummyprint')
        self.assertEqual(sys.stdout.getvalue(), '',
                         msg=("Failed: `redirect' expect sys.stdout ''.\n"
                              "but we got {}".format(sys.stdout.getvalue())))
        self.assertEqual(sys.stderr.getvalue(), '',
                         msg=("Failed: `redirect' expect sys.stderr ''.\n"
                              "but we got {}".format(sys.stderr.getvalue())))

    def tearDown(self):
        sys.stdout, sys.stderr = self._stdout, self._stderr



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_redirect.py ends here
