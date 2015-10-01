#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: test_commandgenerator.py 227 2014-09-13 08:15:46Z t1 $
# $Revision: 227 $
# $Date: 2014-09-13 17:15:46 +0900 (Sat, 13 Sep 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-09-13 17:15:46 +0900 (Sat, 13 Sep 2014) $

r"""Name: test_commandgenerator.py

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
from .. import commandgenerator
from .. import command


class TestCommandGenerator(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.gen = commandgenerator.CommandGenerator()
        self.mocker.replay()

    def test_generate(self, ):
        lis = ['POWR', 'ITGD', 'ITVD', 'IAVD', 'IDEG', 'CBSD', 'CCSD', 'CTBD',
               'CHUP', 'CHDW', 'INP4', 'AVMD', 'VOLM', 'HPOS', 'VPOS', 'CLCK',
               'PHSE', 'WIDE', 'MUTE', 'ACSU', 'ACHA', 'OFTM', ]
        for cmdtype in lis:
            cmd = self.gen.generate(cmdtype)
            self.assertIsInstance(cmd, command.Command)
            self.assertEqual(cmdtype, cmd.get_cmdtype())

    def test_list_candidate(self, ):
        lis = ['POWR', 'ITGD', 'ITVD', 'IAVD', 'IDEG', 'CBSD', 'CCSD', 'CTBD',
               'CHUP', 'CHDW', 'INP4', 'AVMD', 'VOLM', 'HPOS', 'VPOS', 'CLCK',
               'PHSE', 'WIDE', 'MUTE', 'ACSU', 'ACHA', 'OFTM', ]
        candi = self.gen.list_candidate()
        for cmdtype in lis:
            self.assertIn(cmdtype, candi)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        pass


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_commandgenerator.py ends here
