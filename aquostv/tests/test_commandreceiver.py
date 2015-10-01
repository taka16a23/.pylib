#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: test_commandreceiver.py 227 2014-09-13 08:15:46Z t1 $
# $Revision: 227 $
# $Date: 2014-09-13 17:15:46 +0900 (Sat, 13 Sep 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-09-13 17:15:46 +0900 (Sat, 13 Sep 2014) $

r"""Name: test_commandreceiver.py

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

DUMMYRECEIVE = 'OK\n'
DUMMYCOMMAND = 'dummy'


class TestCommandReceiver(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.receiver = order.CommandReceiver(DUMMYRECEIVE, DUMMYCOMMAND)
        self.mocker.replay()

    def test_set_received(self, ):
        newrecieved = 'new'
        self.receiver.set_received(newrecieved)
        self.assertEqual(newrecieved, self.receiver._received)

    def test_get_received(self, ):
        got = self.receiver.get_received()
        self.assertEqual(DUMMYRECEIVE, got)

    def test_set_command(self, ):
        newcommand = 'new'
        self.receiver.set_command(newcommand)
        self.assertEqual(newcommand, self.receiver._command)

    def test_get_command(self, ):
        got = self.receiver.get_command()
        self.assertEqual(DUMMYCOMMAND, got)

    def test_issuccess(self, ):
        self.assertTrue(self.receiver.issuccess())
        self.receiver.set_received('ERR\n')
        self.assertFalse(self.receiver.issuccess())
        self.receiver.set_received('')
        with self.assertRaises(StandardError) as _ex:
            self.receiver.issuccess()

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        pass


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_commandreceiver.py ends here
