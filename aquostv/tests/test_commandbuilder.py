#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_commandbuilder.py

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
from .. import command
from .. import commandbuilder


class TestCommandBuildDirector(MockerTestCase):
    """2014/09/09"""
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.director = commandbuilder.CommandBuildDirector()
        self.mocker.replay()

    def test_direct(self):
        cmd = command.Command()
        cmd.set_cmdtype(command.CommandType('POWR'))
        cmd.set_parameter(command.Parameter(' '))
        builder = commandbuilder.POWRCommandBuilder()
        self.director.set_builder(builder)
        got = self.director.direct()
        self.assertEqual(cmd, got,
                         msg='Failed: CommandBuildDirector expect: \{}, got: \{}'
                         .format(cmd, got))

    def test_set_builder(self, ):
        builder = commandbuilder.POWRCommandBuilder()
        self.director.set_builder(builder)
        expect = builder
        got = self.director.get_builder()
        self.assertEqual(
            expect, got,
            msg='Failed: CommandBuilder.set_builder expect: \{}, got: \{}'
            .format(expect, got))

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        pass


class TestPOWRCommandBuilder(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.cmdtype = 'POWR'
        self.builder = commandbuilder.POWRCommandBuilder()
        self.mocker.replay()

    def get_parameter(self, ):
        return command.Parameter(' ')

    def test_build_command_type(self, ):
        expect = command.CommandType(self.cmdtype)
        got = self.builder.build_command_type()
        self.assertEqual(
            expect, got,
            msg='Failed: CommandBuilder.build_command_type expect: \{}, got: \{}'
            .format(expect, got))

    def test_build_parameter(self, ):
        expect = self.get_parameter()
        got = self.builder.build_parameter()
        self.assertEqual(
            expect, got,
            msg='Failed: CommandBuilder.build_parameter expect: \{}, got: \{}'
            .format(expect, got))

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        pass


class TestITGDCommandBuilder(TestPOWRCommandBuilder):
    """2014/09/09"""
    def setUp(self, ):
        self.cmdtype = 'ITGD'
        self.builder = commandbuilder.ITGDCommandBuilder()
        self.mocker.replay()

    def get_parameter(self, ):
        return command.Parameter(' ')


class TestITVDCommandBuilder(TestPOWRCommandBuilder):
    """2014/09/09"""
    def setUp(self, ):
        self.cmdtype = 'ITVD'
        self.builder = commandbuilder.ITVDCommandBuilder()
        self.mocker.replay()

    def get_parameter(self, ):
        return command.Parameter(' ')


class TestIAVDCommandBuilder(TestPOWRCommandBuilder):
    """2014/09/09"""
    def setUp(self, ):
        self.cmdtype = 'IAVD'
        self.builder = commandbuilder.IAVDCommandBuilder()
        self.mocker.replay()

    def get_parameter(self, ):
        return command.Parameter(' ')


class TestIDEGCommandBuilder(TestPOWRCommandBuilder):
    """2014/09/09"""
    def setUp(self, ):
        self.cmdtype = 'IDEG'
        self.builder = commandbuilder.IDEGCommandBuilder()
        self.mocker.replay()

    def get_parameter(self, ):
        return command.Parameter(' ')


class TestCBSDCommandBuilder(TestPOWRCommandBuilder):
    """2014/09/09"""
    def setUp(self, ):
        self.cmdtype = 'CBSD'
        self.builder = commandbuilder.CBSDCommandBuilder()
        self.mocker.replay()

    def get_parameter(self, ):
        return command.Parameter(' ')


class TestCCSDCommandBuilder(TestPOWRCommandBuilder):
    """2014/09/09"""
    def setUp(self, ):
        self.cmdtype = 'CCSD'
        self.builder = commandbuilder.CCSDCommandBuilder()
        self.mocker.replay()

    def get_parameter(self, ):
        return command.Parameter(' ')


class TestCTBDCommandBuilder(TestPOWRCommandBuilder):
    """2014/09/09"""
    def setUp(self, ):
        self.cmdtype = 'CTBD'
        self.builder = commandbuilder.CTBDCommandBuilder()
        self.mocker.replay()

    def get_parameter(self, ):
        return command.Parameter(' ')


class TestCHUPCommandBuilder(TestPOWRCommandBuilder):
    """2014/09/09"""
    def setUp(self, ):
        self.cmdtype = 'CHUP'
        self.builder = commandbuilder.CHUPCommandBuilder()
        self.mocker.replay()

    def get_parameter(self, ):
        return command.Parameter(' ')


class TestCHDWCommandBuilder(TestPOWRCommandBuilder):
    """2014/09/09"""
    def setUp(self, ):
        self.cmdtype = 'CHDW'
        self.builder = commandbuilder.CHDWCommandBuilder()
        self.mocker.replay()

    def get_parameter(self, ):
        return command.Parameter(' ')


class TestINP4CommandBuilder(TestPOWRCommandBuilder):
    """2014/09/09"""
    def setUp(self, ):
        self.cmdtype = 'INP4'
        self.builder = commandbuilder.INP4CommandBuilder()
        self.mocker.replay()

    def get_parameter(self, ):
        return command.Parameter(' ')


class TestAVMDCommandBuilder(TestPOWRCommandBuilder):
    """2014/09/09"""
    def setUp(self, ):
        self.cmdtype = 'AVMD'
        self.builder = commandbuilder.AVMDCommandBuilder()
        self.mocker.replay()

    def get_parameter(self, ):
        return command.Parameter(' ')


class TestVOLMCommandBuilder(TestPOWRCommandBuilder):
    """2014/09/09"""
    def setUp(self, ):
        self.cmdtype = 'VOLM'
        self.builder = commandbuilder.VOLMCommandBuilder()
        self.mocker.replay()

    def get_parameter(self, ):
        return command.Parameter(' ')


class TestHPOSCommandBuilder(TestPOWRCommandBuilder):
    """2014/09/09"""
    def setUp(self, ):
        self.cmdtype = 'HPOS'
        self.builder = commandbuilder.HPOSCommandBuilder()
        self.mocker.replay()

    def get_parameter(self, ):
        return command.Parameter(' ')


class TestVPOSCommandBuilder(TestPOWRCommandBuilder):
    """2014/09/09"""
    def setUp(self, ):
        self.cmdtype = 'VPOS'
        self.builder = commandbuilder.VPOSCommandBuilder()
        self.mocker.replay()

    def get_parameter(self, ):
        return command.Parameter(' ')


class TestCLCKCommandBuilder(TestPOWRCommandBuilder):
    """2014/09/09"""
    def setUp(self, ):
        self.cmdtype = 'CLCK'
        self.builder = commandbuilder.CLCKCommandBuilder()
        self.mocker.replay()

    def get_parameter(self, ):
        return command.Parameter(' ')


class TestPHSECommandBuilder(TestPOWRCommandBuilder):
    """2014/09/09"""
    def setUp(self, ):
        self.cmdtype = 'PHSE'
        self.builder = commandbuilder.PHSECommandBuilder()
        self.mocker.replay()

    def get_parameter(self, ):
        return command.Parameter(' ')


class TestWIDECommandBuilder(TestPOWRCommandBuilder):
    """2014/09/09"""
    def setUp(self, ):
        self.cmdtype = 'WIDE'
        self.builder = commandbuilder.WIDECommandBuilder()
        self.mocker.replay()

    def get_parameter(self, ):
        return command.Parameter(' ')


class TestMUTECommandBuilder(TestPOWRCommandBuilder):
    """2014/09/09"""
    def setUp(self, ):
        self.cmdtype = 'MUTE'
        self.builder = commandbuilder.MUTECommandBuilder()
        self.mocker.replay()

    def get_parameter(self, ):
        return command.Parameter(' ')


class TestACSUCommandBuilder(TestPOWRCommandBuilder):
    """2014/09/09"""
    def setUp(self, ):
        self.cmdtype = 'ACSU'
        self.builder = commandbuilder.ACSUCommandBuilder()
        self.mocker.replay()

    def get_parameter(self, ):
        return command.Parameter(' ')


class TestACHACommandBuilder(TestPOWRCommandBuilder):
    """2014/09/09"""
    def setUp(self, ):
        self.cmdtype = 'ACHA'
        self.builder = commandbuilder.ACHACommandBuilder()
        self.mocker.replay()

    def get_parameter(self, ):
        return command.Parameter(' ')


class TestOFTMCommandBuilder(TestPOWRCommandBuilder):
    """2014/09/09"""
    def setUp(self, ):
        self.cmdtype = 'OFTM'
        self.builder = commandbuilder.OFTMCommandBuilder()
        self.mocker.replay()

    def get_parameter(self, ):
        return command.Parameter(' ')



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_commandbuilder.py ends here
