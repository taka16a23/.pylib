#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""cmdline -- DESCRIPTION

"""
from getpass import getpass
from getpasswd.getter.abstract import PassGetter


class CmdlinePassGetter(PassGetter):
    r"""CmdlinePassGetter

    CmdlinePassGetter is a PassGetter.
    Responsibility:
    """
    def __init__(self, stream=None):
        r"""

        @Arguments:
        - `stream`:
        """
        self._stream = stream

    def getpass(self, prompt='Password: '):
        r"""SUMMARY

        getpass(prompt='Password: ')

        @Arguments:
        - `prompt`:

        @Return:

        @Error:
        """
        return getpass(prompt, self._stream)

    def getstream(self, ):
        r"""SUMMARY

        getstream()

        @Return:

        @Error:
        """
        return self._stream

    def setstream(self, stream=None):
        r"""SUMMARY

        setstream(stream=None)

        @Arguments:
        - `stream`:

        @Return:

        @Error:
        """
        self._stream = stream



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# cmdline.py ends here
