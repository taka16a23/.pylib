#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""commandgenerator -- DESCRIPTION

"""
from . import commandprototype


class CommandGenerator(object):
    r"""CommandGenerator

    CommandGenerator is a object.
    Responsibility:
    """
    _prototypes = commandprototype.CommandPrototype()

    def generate(self, cmdtype):
        r"""SUMMARY

        generator(cmdtype)

        @Arguments:
        - `cmdtype`:

        @Return:

        @Error:
        """
        return self._prototypes.clone(cmdtype)

    def list_candidate(self, ):
        r"""SUMMARY

        list_candidate()

        @Return:

        @Error:
        """
        return self._prototypes.list_candidate()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# commandgenerator.py ends here
