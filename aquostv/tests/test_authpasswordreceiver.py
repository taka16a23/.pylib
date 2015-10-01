#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_authpasswordreceiver.py

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
from .. import order

DUMMYRECEIVE = '\r\n'


class TestAuthPasswordReceiver(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.receiver = order.AuthPasswordReceiver(DUMMYRECEIVE)
        self.mocker.replay()

    def test_set_received(self, ):
        new = ''
        self.receiver.set_received(new)
        self.assertEqual(new, self.receiver._received)

    def test_get_received(self, ):
        self.assertEqual(DUMMYRECEIVE, self.receiver.get_received())

    def test_issuccess(self, ):
        self.assertTrue(self.receiver.issuccess())
        self.receiver.set_received(self.receiver.false_code)
        self.assertFalse(self.receiver.issuccess())
        self.receiver.set_received('dummy')
        with self.assertRaises(StandardError) as _ex:
            self.receiver.issuccess()

    def test_get_expect(self, ):
        self.assertEqual(DUMMYRECEIVE, self.receiver.get_expect())

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        pass


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_authpasswordreceiver.py ends here
