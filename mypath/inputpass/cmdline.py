#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: cmdline.py 263 2014-12-27 06:39:30Z t1 $
# $Revision: 263 $
# $Date: 2014-12-27 15:39:30 +0900 (Sat, 27 Dec 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-12-27 15:39:30 +0900 (Sat, 27 Dec 2014) $

r"""cmdline -- DESCRIPTION

"""
from getpass import getpass
from . import abstract



class CmdlineInputPass(abstract.InputPass):
    r"""CmdlineInputPass

    CmdlineInputPass is a abstract.InputPass.
    Responsibility:
    """
    def __init__(self, prompt='Password: ', stream=None):
        r"""

        @Arguments:
        - `prompt`:
        - `stream`:
        """
        self._prompt = prompt
        self._stream = stream

    def set_prompt(self, msg):
        r"""SUMMARY

        set_prompt(msg)

        @Arguments:
        - `msg`:

        @Return:

        @Error:
        """
        self._prompt = msg

    def get_prompt(self, ):
        r"""SUMMARY

        get_prompt()

        @Return:

        @Error:
        """
        return self._prompt

    def set_stream(self, fileobj):
        r"""SUMMARY

        set_stream(fileobj)

        @Arguments:
        - `fileobj`:

        @Return:

        @Error:
        """
        self._stream = fileobj

    def get_stream(self, ):
        r"""SUMMARY

        get_stream()

        @Return:

        @Error:
        """
        return self._stream

    def input(self, ):
        r"""SUMMARY

        input()

        @Return:

        @Error:
        """
        return getpass(self._prompt, self._stream)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# cmdline.py ends here
