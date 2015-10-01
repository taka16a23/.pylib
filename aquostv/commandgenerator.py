#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: commandgenerator.py 227 2014-09-13 08:15:46Z t1 $
# $Revision: 227 $
# $Date: 2014-09-13 17:15:46 +0900 (Sat, 13 Sep 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-09-13 17:15:46 +0900 (Sat, 13 Sep 2014) $

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
