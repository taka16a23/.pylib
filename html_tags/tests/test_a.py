#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_a.py

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
from material.forms.tags.a import a


class Test_a(TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        pass

    def test_set_download(self, ):
        t_expect = 'test.png'
        t_a = a()
        t_a.set_download(t_expect)
        t_got = str(t_a.get_download())
        self.assertEqual(t_expect, t_got)

    def test_get_download(self, ):
        t_expect = 'test.png'
        t_a = a()
        t_a.set_download(t_expect)
        t_got = str(t_a.get_download())
        self.assertEqual(t_expect, t_got)

    def test_remove_download(self, ):
        t_expect = 'test.png'
        t_a = a()
        t_a.set_download(t_expect)
        t_got = str(t_a.get_download())
        self.assertEqual(t_expect, t_got)
        t_a.remove_download()
        self.assertIsNone(t_a.get_download())

    def test_set_href(self, ):
        t_expect = 'http://google.com'
        t_a = a()
        t_a.set_href(t_expect)
        self.assertEqual(t_expect, str(t_a.get_href()))

    def test_get_href(self, ):
        t_expect = 'http://google.com'
        t_a = a()
        t_a.set_href(t_expect)
        self.assertEqual(t_expect, str(t_a.get_href()))

    def test_remove_href(self, ):
        t_expect = 'http://google.com'
        t_a = a()
        t_a.set_href(t_expect)
        self.assertEqual(t_expect, str(t_a.get_href()))
        t_a.remove_href()
        self.assertIsNone(t_a.get_href())

    def test_get_hreflang(self, ):
        t_expect = 'en'
        t_a = a()
        t_a.set_hreflang(t_expect)
        self.assertEqual(t_expect, str(t_a.get_hreflang()))

    def test_set_hreflang(self, ):
        t_expect = 'en'
        t_a = a()
        t_a.set_hreflang(t_expect)
        self.assertEqual(t_expect, str(t_a.get_hreflang()))

    def test_remove_hreflang(self, ):
        t_expect = 'en'
        t_a = a()
        t_a.set_hreflang(t_expect)
        self.assertEqual(t_expect, str(t_a.get_hreflang()))
        t_a.remove_hreflang()

    def test_append_ping(self, ):
        t_expect = ['http://google.com', 'http://yahoo.com', ]
        t_expect.sort()
        t_a = a()
        t_a.append_ping(t_expect[0])
        t_a.append_ping(t_expect[1])
        t_got = str(t_a.get_ping()).split(' ')
        t_got.sort()
        self.assertListEqual(t_expect, t_got)

    def test_remove_ping(self, ):
        t_expect = ['http://google.com', 'http://yahoo.com', ]
        t_expect.sort()
        t_a = a()
        t_a.append_ping(t_expect[0])
        t_a.append_ping(t_expect[1])
        t_got = str(t_a.get_ping()).split(' ')
        t_got.sort()
        self.assertListEqual(t_expect, t_got)
        t_a.remove_ping(t_expect[0])
        t_got = t_a.get_ping()
        self.assertEqual(t_expect[1], str(t_got))

    def test_clear_ping(self, ):
        t_expect = ['http://google.com', 'http://yahoo.com', ]
        t_expect.sort()
        t_a = a()
        t_a.append_ping(t_expect[0])
        t_a.append_ping(t_expect[1])
        t_got = str(t_a.get_ping()).split(' ')
        t_got.sort()
        self.assertListEqual(t_expect, t_got)
        t_a.clear_ping()
        self.assertEqual('', str(t_a.get_ping()))

    def test_delete_ping(self, ):
        t_expect = ['http://google.com', 'http://yahoo.com', ]
        t_expect.sort()
        t_a = a()
        t_a.append_ping(t_expect[0])
        t_a.append_ping(t_expect[1])
        t_got = str(t_a.get_ping()).split(' ')
        t_got.sort()
        self.assertListEqual(t_expect, t_got)
        t_a.delete_ping()
        self.assertIsNone(t_a.get_ping())

    def test_set_refererpolicy(self, ):
        t_a = a()
        t_a.set_refererpolicy(t_a.RefererPolicy.NO_REFERRER)
        self.assertEqual(t_a.RefererPolicy.NO_REFERRER, str(t_a.get_refererpolicy()))

    def test_get_refererpolicy(self, ):
        t_a = a()
        t_a.set_refererpolicy(t_a.RefererPolicy.NO_REFERRER)
        self.assertEqual(t_a.RefererPolicy.NO_REFERRER, str(t_a.get_refererpolicy()))

    def test_remove_refererpolicy(self, ):
        t_a = a()
        t_a.set_refererpolicy(t_a.RefererPolicy.NO_REFERRER)
        self.assertEqual(t_a.RefererPolicy.NO_REFERRER, str(t_a.get_refererpolicy()))
        t_a.remove_refererpolicy()
        self.assertIsNone(t_a.get_refererpolicy())

    def test_get_rel(self, ):
        t_a = a()
        t_a.append_rel(t_a.Rel.ALTERNATE)
        self.assertEqual(t_a.Rel.ALTERNATE, str(t_a.get_rel()))

    def test_remove_rel(self, ):
        t_a = a()
        t_a.append_rel(t_a.Rel.ALTERNATE)
        t_a.append_rel(t_a.Rel.AUTHOR)
        t_expect = [t_a.Rel.ALTERNATE, t_a.Rel.AUTHOR]
        t_expect.sort()
        t_got = str(t_a.get_rel()).split(' ')
        t_got.sort()
        self.assertListEqual(t_expect, t_got)
        t_a.remove_rel(t_a.Rel.ALTERNATE)
        self.assertEqual(t_a.Rel.AUTHOR, str(t_a.get_rel()))

    def test_append_rel(self, ):
        t_a = a()
        t_a.append_rel(t_a.Rel.ALTERNATE)
        t_a.append_rel(t_a.Rel.AUTHOR)
        t_expect = [t_a.Rel.ALTERNATE, t_a.Rel.AUTHOR]
        t_expect.sort()
        t_got = str(t_a.get_rel()).split(' ')
        t_got.sort()
        self.assertListEqual(t_expect, t_got)

    def test_clear_rel(self, ):
        t_a = a()
        t_a.append_rel(t_a.Rel.ALTERNATE)
        t_a.append_rel(t_a.Rel.AUTHOR)
        t_expect = [t_a.Rel.ALTERNATE, t_a.Rel.AUTHOR]
        t_expect.sort()
        t_got = str(t_a.get_rel()).split(' ')
        t_got.sort()
        self.assertListEqual(t_expect, t_got)
        t_a.clear_rel()
        self.assertEqual('', str(t_a.get_rel()))

    def test_delete_rel(self, ):
        t_a = a()
        t_a.append_rel(t_a.Rel.ALTERNATE)
        self.assertEqual(t_a.Rel.ALTERNATE, str(t_a.get_rel()))
        t_a.delete_rel()
        self.assertIsNone(t_a.get_rel())

    def test_set_target(self, ):
        t_a = a()
        t_a.set_target(t_a.Target.BLANK)
        self.assertEqual(t_a.Target.BLANK, str(t_a.get_target()))

    def test_get_target(self, ):
        t_a = a()
        t_a.set_target(t_a.Target.BLANK)
        self.assertEqual(t_a.Target.BLANK, str(t_a.get_target()))

    def test_remove_target(self, ):
        t_a = a()
        t_a.set_target(t_a.Target.BLANK)
        self.assertEqual(t_a.Target.BLANK, str(t_a.get_target()))
        t_a.remove_target()
        self.assertIsNone(t_a.get_target())

    def test_set_type(self, ):
        t_a = a()
        t_a.set_type("application/vnd.adobe.flash-movie")
        self.assertEqual("application/vnd.adobe.flash-movie", str(t_a.get_type()))

    def test_get_type(self, ):
        t_a = a()
        t_a.set_type("application/vnd.adobe.flash-movie")
        self.assertEqual("application/vnd.adobe.flash-movie", str(t_a.get_type()))

    def test_remove_type(self, ):
        t_a = a()
        t_a.set_type("application/vnd.adobe.flash-movie")
        self.assertEqual("application/vnd.adobe.flash-movie", str(t_a.get_type()))
        t_a.remove_type()
        self.assertIsNone(t_a.get_type())

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        pass



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_a.py ends here
