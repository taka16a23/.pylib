#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_commandprototype.py

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
from .. import commandprototype
from .. import command
from .. import commandbuilder


class TestCommandProtoType(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.proto = commandprototype.CommandPrototype()
        self.mocker.replay()

    def test__build_prototype(self, ):
        lis = ['POWR', 'ITGD', 'ITVD', 'IAVD', 'IDEG', 'CBSD', 'CCSD', 'CTBD',
               'CHUP', 'CHDW', 'INP4', 'AVMD', 'VOLM', 'HPOS', 'VPOS', 'CLCK',
               'PHSE', 'WIDE', 'MUTE', 'ACSU', 'ACHA', 'OFTM', ]
        for cmdtype in lis:
            cmd = self.proto._prototypes[cmdtype]
            self.assertIsInstance(cmd, command.Command)
            self.assertEqual(cmdtype, cmd.get_cmdtype())

    def test_register_unregister(self, ):
        director = commandbuilder.CommandBuildDirector()
        director.set_builder(commandbuilder.POWRCommandBuilder())
        cmd = director.direct()

        self.proto.unregister('POWR')
        self.assertNotIn('POWR', self.proto._prototypes)
        self.proto.register(cmd)
        self.assertIn('POWR', self.proto._prototypes)
        self.assertEqual(cmd, self.proto._prototypes['POWR'])

    def test_clone(self, ):
        cmd = self.proto.clone('POWR')
        self.assertIsInstance(cmd, command.Command)

    def test_clone_check_cmdtype(self, ):
        original = id(self.proto._prototypes['POWR'].get_cmdtype())
        clone = id(self.proto.clone('POWR').get_cmdtype())
        self.assertNotEqual(original, clone)

    def test_clone_check_parameter(self, ):
        original = id(self.proto._prototypes['POWR'].get_parameter())
        clone = id(self.proto.clone('POWR').get_parameter())
        self.assertNotEqual(original, clone)

    def test_list_candidate(self, ):
        lis = ['POWR', 'ITGD', 'ITVD', 'IAVD', 'IDEG', 'CBSD', 'CCSD', 'CTBD',
               'CHUP', 'CHDW', 'INP4', 'AVMD', 'VOLM', 'HPOS', 'VPOS', 'CLCK',
               'PHSE', 'WIDE', 'MUTE', 'ACSU', 'ACHA', 'OFTM', ]
        candi = self.proto.list_candidate()
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
# test_commandprototype.py ends here
