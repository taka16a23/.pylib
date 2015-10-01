#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: commandbuilder.py 227 2014-09-13 08:15:46Z t1 $
# $Revision: 227 $
# $Date: 2014-09-13 17:15:46 +0900 (Sat, 13 Sep 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-09-13 17:15:46 +0900 (Sat, 13 Sep 2014) $

r"""commandbuilder -- DESCRIPTION

"""
from abc import ABCMeta, abstractmethod
from . import command


class CommandBuildDirector(object):
    r"""CommandBuildDirector

    CommandBuildDirector is a object.
    Responsibility:
    """
    def __init__(self, builder=None):
        r"""

        @Arguments:
        - `builder`:
        """
        self._builder = builder

    def direct(self, ):
        r"""SUMMARY

        direct()

        @Return:

        @Error:
        """
        cmd = command.Command()
        cmd.set_cmdtype(self.get_builder().build_command_type())
        cmd.set_parameter(self.get_builder().build_parameter())
        return cmd

    def set_builder(self, builder):
        r"""SUMMARY

        set_builder(builder)

        @Arguments:
        - `builder`:

        @Return:

        @Error:
        """
        self._builder = builder

    def get_builder(self, ):
        r"""SUMMARY

        get_builder()

        @Return:

        @Error:
        """
        return self._builder


class CommandBuilder(object):
    r"""CommandBuilder

    CommandBuilder is a object.
    Responsibility:
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def build_command_type(self, ):
        raise NotImplementedError()

    @abstractmethod
    def build_parameter(self, ):
        raise NotImplementedError()


class POWRCommandBuilder(CommandBuilder):
    r"""POWRCommandBuilder

    POWRCommandBuilder is a CommandBuilder.
    Responsibility:
    """

    def build_command_type(self, ):
        r"""SUMMARY

        build_command_type()

        @Return:

        @Error:
        """
        return command.CommandType('POWR')

    def build_parameter(self, ):
        r"""SUMMARY

        build_parameter()

        @Return:

        @Error:
        """
        return command.Parameter(' ')


class ITGDCommandBuilder(CommandBuilder):
    r"""ITGDCommandBuilder

    ITGDCommandBuilder is a CommandBuilder.
    Responsibility:
    """
    def build_command_type(self, ):
        r"""SUMMARY

        build_command_type()

        @Return:

        @Error:
        """
        return command.CommandType('ITGD')

    def build_parameter(self, ):
        r"""SUMMARY

        build_parameter()

        @Return:

        @Error:
        """
        return command.Parameter(' ')


class ITVDCommandBuilder(CommandBuilder):
    r"""ITVDCommandBuilder

    ITVDCommandBuilder is a CommandBuilder.
    Responsibility:
    """
    def build_command_type(self, ):
        r"""SUMMARY

        build_command_type()

        @Return:

        @Error:
        """
        return command.CommandType('ITVD')

    def build_parameter(self, ):
        r"""SUMMARY

        build_parameter()

        @Return:

        @Error:
        """
        return command.Parameter(' ')


class IAVDCommandBuilder(CommandBuilder):
    r"""IAVDCommandBuilder

    IAVDCommandBuilder is a CommandBuilder.
    Responsibility:
    """
    def build_command_type(self, ):
        r"""SUMMARY

        build_command_type()

        @Return:

        @Error:
        """
        return command.CommandType('IAVD')

    def build_parameter(self, ):
        r"""SUMMARY

        build_parameter()

        @Return:

        @Error:
        """
        return command.Parameter(' ')


class IDEGCommandBuilder(CommandBuilder):
    r"""IDEGCommandBuilder

    IDEGCommandBuilder is a CommandBuilder.
    Responsibility:
    """
    def build_command_type(self, ):
        r"""SUMMARY

        build_command_type()

        @Return:

        @Error:
        """
        return command.CommandType('IDEG')

    def build_parameter(self, ):
        r"""SUMMARY

        build_parameter()

        @Return:

        @Error:
        """
        return command.Parameter(' ')


class CBSDCommandBuilder(CommandBuilder):
    r"""CBSDCommandBuilder

    CBSDCommandBuilder is a CommandBuilder.
    Responsibility:
    """
    def build_command_type(self, ):
        r"""SUMMARY

        build_command_type()

        @Return:

        @Error:
        """
        return command.CommandType('CBSD')

    def build_parameter(self, ):
        r"""SUMMARY

        build_parameter()

        @Return:

        @Error:
        """
        return command.Parameter(' ')


class CCSDCommandBuilder(CommandBuilder):
    r"""CCSDCommandBuilder

    CCSDCommandBuilder is a CommandBuilder.
    Responsibility:
    """
    def build_command_type(self, ):
        r"""SUMMARY

        build_command_type()

        @Return:

        @Error:
        """
        return command.CommandType('CCSD')

    def build_parameter(self, ):
        r"""SUMMARY

        build_parameter()

        @Return:

        @Error:
        """
        return command.Parameter(' ')


class CTBDCommandBuilder(CommandBuilder):
    r"""CTBDCommandBuilder

    CTBDCommandBuilder is a CommandBuilder.
    Responsibility:
    """
    def build_command_type(self, ):
        r"""SUMMARY

        build_command_type()

        @Return:

        @Error:
        """
        return command.CommandType('CTBD')

    def build_parameter(self, ):
        r"""SUMMARY

        build_parameter()

        @Return:

        @Error:
        """
        return command.Parameter(' ')


class CHUPCommandBuilder(CommandBuilder):
    r"""CHUPCommandBuilder

    CHUPCommandBuilder is a CommandBuilder.
    Responsibility:
    """
    def build_command_type(self, ):
        r"""SUMMARY

        build_command_type()

        @Return:

        @Error:
        """
        return command.CommandType('CHUP')

    def build_parameter(self, ):
        r"""SUMMARY

        build_parameter()

        @Return:

        @Error:
        """
        return command.Parameter(' ')


class CHDWCommandBuilder(CommandBuilder):
    r"""CHDWCommandBuilder

    CHDWCommandBuilder is a CommandBuilder.
    Responsibility:
    """
    def build_command_type(self, ):
        r"""SUMMARY

        build_command_type()

        @Return:

        @Error:
        """
        return command.CommandType('CHDW')

    def build_parameter(self, ):
        r"""SUMMARY

        build_parameter()

        @Return:

        @Error:
        """
        return command.Parameter(' ')


class INP4CommandBuilder(CommandBuilder):
    r"""INP4CommandBuilder

    INP4CommandBuilder is a CommandBuilder.
    Responsibility:
    """
    def build_command_type(self, ):
        r"""SUMMARY

        build_command_type()

        @Return:

        @Error:
        """
        return command.CommandType('INP4')

    def build_parameter(self, ):
        r"""SUMMARY

        build_parameter()

        @Return:

        @Error:
        """
        return command.Parameter(' ')


class AVMDCommandBuilder(CommandBuilder):
    r"""AVMDCommandBuilder

    AVMDCommandBuilder is a CommandBuilder.
    Responsibility:
    """
    def build_command_type(self, ):
        r"""SUMMARY

        build_command_type()

        @Return:

        @Error:
        """
        return command.CommandType('AVMD')

    def build_parameter(self, ):
        r"""SUMMARY

        build_parameter()

        @Return:

        @Error:
        """
        return command.Parameter(' ')


class VOLMCommandBuilder(CommandBuilder):
    r"""VOLMCommandBuilder

    VOLMCommandBuilder is a CommandBuilder.
    Responsibility:
    """
    def build_command_type(self, ):
        r"""SUMMARY

        build_command_type()

        @Return:

        @Error:
        """
        return command.CommandType('VOLM')

    def build_parameter(self, ):
        r"""SUMMARY

        build_parameter()

        @Return:

        @Error:
        """
        return command.Parameter(' ')


class HPOSCommandBuilder(CommandBuilder):
    r"""HPOSCommandBuilder

    HPOSCommandBuilder is a CommandBuilder.
    Responsibility:
    """
    def build_command_type(self, ):
        r"""SUMMARY

        build_command_type()

        @Return:

        @Error:
        """
        return command.CommandType('HPOS')

    def build_parameter(self, ):
        r"""SUMMARY

        build_parameter()

        @Return:

        @Error:
        """
        return command.Parameter(' ')


class VPOSCommandBuilder(CommandBuilder):
    r"""VPOSCommandBuilder

    VPOSCommandBuilder is a CommandBuilder.
    Responsibility:
    """
    def build_command_type(self, ):
        r"""SUMMARY

        build_command_type()

        @Return:

        @Error:
        """
        return command.CommandType('VPOS')

    def build_parameter(self, ):
        r"""SUMMARY

        build_parameter()

        @Return:

        @Error:
        """
        return command.Parameter(' ')


class CLCKCommandBuilder(CommandBuilder):
    r"""CLCKCommandBuilder

    CLCKCommandBuilder is a CommandBuilder.
    Responsibility:
    """
    def build_command_type(self, ):
        r"""SUMMARY

        build_command_type()

        @Return:

        @Error:
        """
        return command.CommandType('CLCK')

    def build_parameter(self, ):
        r"""SUMMARY

        build_parameter()

        @Return:

        @Error:
        """
        return command.Parameter(' ')


class PHSECommandBuilder(CommandBuilder):
    r"""PHSECommandBuilder

    PHSECommandBuilder is a CommandBuilder.
    Responsibility:
    """
    def build_command_type(self, ):
        r"""SUMMARY

        build_command_type()

        @Return:

        @Error:
        """
        return command.CommandType('PHSE')

    def build_parameter(self, ):
        r"""SUMMARY

        build_parameter()

        @Return:

        @Error:
        """
        return command.Parameter(' ')


class WIDECommandBuilder(CommandBuilder):
    r"""WIDECommandBuilder

    WIDECommandBuilder is a CommandBuilder.
    Responsibility:
    """
    def build_command_type(self, ):
        r"""SUMMARY

        build_command_type()

        @Return:

        @Error:
        """
        return command.CommandType('WIDE')

    def build_parameter(self, ):
        r"""SUMMARY

        build_parameter()

        @Return:

        @Error:
        """
        return command.Parameter(' ')


class MUTECommandBuilder(CommandBuilder):
    r"""MUTECommandBuilder

    MUTECommandBuilder is a CommandBuilder.
    Responsibility:
    """
    def build_command_type(self, ):
        r"""SUMMARY

        build_command_type()

        @Return:

        @Error:
        """
        return command.CommandType('MUTE')

    def build_parameter(self, ):
        r"""SUMMARY

        build_parameter()

        @Return:

        @Error:
        """
        return command.Parameter(' ')


class ACSUCommandBuilder(CommandBuilder):
    r"""ACSUCommandBuilder

    ACSUCommandBuilder is a CommandBuilder.
    Responsibility:
    """
    def build_command_type(self, ):
        r"""SUMMARY

        build_command_type()

        @Return:

        @Error:
        """
        return command.CommandType('ACSU')

    def build_parameter(self, ):
        r"""SUMMARY

        build_parameter()

        @Return:

        @Error:
        """
        return command.Parameter(' ')


class ACHACommandBuilder(CommandBuilder):
    r"""ACHACommandBuilder

    ACHACommandBuilder is a CommandBuilder.
    Responsibility:
    """
    def build_command_type(self, ):
        r"""SUMMARY

        build_command_type()

        @Return:

        @Error:
        """
        return command.CommandType('ACHA')

    def build_parameter(self, ):
        r"""SUMMARY

        build_parameter()

        @Return:

        @Error:
        """
        return command.Parameter(' ')


class OFTMCommandBuilder(CommandBuilder):
    r"""OFTMCommandBuilder

    OFTMCommandBuilder is a CommandBuilder.
    Responsibility:
    """
    def build_command_type(self, ):
        r"""SUMMARY

        build_command_type()

        @Return:

        @Error:
        """
        return command.CommandType('OFTM')

    def build_parameter(self, ):
        r"""SUMMARY

        build_parameter()

        @Return:

        @Error:
        """
        return command.Parameter(' ')



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# commandbuilder.py ends here
