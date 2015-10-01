#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: commandprototype.py 227 2014-09-13 08:15:46Z t1 $
# $Revision: 227 $
# $Date: 2014-09-13 17:15:46 +0900 (Sat, 13 Sep 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-09-13 17:15:46 +0900 (Sat, 13 Sep 2014) $

r"""commandprototype -- DESCRIPTION

"""
from copy import deepcopy
from . import commandbuilder


class CommandPrototype(object):
    r"""CommandPrototype

    CommandPrototype is a object.
    Responsibility:
    """

    def __init__(self, ):
        r"""
        """
        self._prototypes = {}
        self._build_commands()

    def _build_commands(self, ):
        r"""SUMMARY

        _build_commands()

        @Return:

        @Error:
        """
        director = commandbuilder.CommandBuildDirector()
        builders = [commandbuilder.POWRCommandBuilder(),
                    commandbuilder.ITGDCommandBuilder(),
                    commandbuilder.ITVDCommandBuilder(),
                    commandbuilder.IAVDCommandBuilder(),
                    commandbuilder.IDEGCommandBuilder(),
                    commandbuilder.CBSDCommandBuilder(),
                    commandbuilder.CCSDCommandBuilder(),
                    commandbuilder.CTBDCommandBuilder(),
                    commandbuilder.CHUPCommandBuilder(),
                    commandbuilder.CHDWCommandBuilder(),
                    commandbuilder.INP4CommandBuilder(),
                    commandbuilder.AVMDCommandBuilder(),
                    commandbuilder.VOLMCommandBuilder(),
                    commandbuilder.HPOSCommandBuilder(),
                    commandbuilder.VPOSCommandBuilder(),
                    commandbuilder.CLCKCommandBuilder(),
                    commandbuilder.PHSECommandBuilder(),
                    commandbuilder.WIDECommandBuilder(),
                    commandbuilder.MUTECommandBuilder(),
                    commandbuilder.ACSUCommandBuilder(),
                    commandbuilder.ACHACommandBuilder(),
                    commandbuilder.OFTMCommandBuilder(),
                    ]
        for builder in builders:
            director.set_builder(builder)
            self.register(director.direct())

    def register(self, cmd):
        r"""SUMMARY

        register(cmd)

        @Arguments:
        - `cmd`:

        @Return:

        @Error:
        """
        self._prototypes[cmd.get_cmdtype()] = cmd

    def unregister(self, cmdtype):
        r"""SUMMARY

        unregister(cmdtype)

        @Arguments:
        - `cmdtype`:

        @Return:

        @Error:
        """
        del self._prototypes[cmdtype]

    def clone(self, cmdtype):
        r"""SUMMARY

        clone(cmdtype)

        @Arguments:
        - `cmdtype`:

        @Return:

        @Error:
        """
        return deepcopy(self._prototypes[cmdtype])

    def list_candidate(self, ):
        r"""SUMMARY

        list_candidate()

        @Return:

        @Error:
        """
        return self._prototypes.keys()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# commandprototype.py ends here
