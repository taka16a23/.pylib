#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""command -- DESCRIPTION

"""


class Command(object):
    r"""Command

    Command is a object.
    Responsibility:
    """
    def __init__(self, cmdtype='    ', parameter='    '):
        r"""

        @Arguments:
        - `cmdtype`:
        - `parameter`:
        """
        self._cmdtype = cmdtype
        self._parameter = parameter

    def get_command(self, ):
        r"""SUMMARY

        get_command()

        @Return:

        @Error:
        """
        return self._cmdtype + self._parameter

    def get_cmdtype(self, ):
        r"""SUMMARY

        get_cmdtype()

        @Return:

        @Error:
        """
        return self._cmdtype

    def set_cmdtype(self, cmdtype):
        r"""SUMMARY

        set_cmdtype(cmdtype)

        @Arguments:
        - `cmdtype`:

        @Return:

        @Error:
        """
        self._cmdtype = cmdtype

    def get_parameter(self, ):
        r"""SUMMARY

        get_parameter()

        @Return:

        @Error:
        """
        return self._parameter

    def set_parameter(self, param):
        r"""SUMMARY

        set_parameter(param)

        @Arguments:
        - `param`:

        @Return:

        @Error:
        """
        self._parameter = param

    def __add__(self, other):
        return self.get_command() + other

    def __str__(self):
        return self.get_command()

    def __repr__(self):
        return ('{0.__class__.__name__}(_cmdtype="{1}", _parameter="{2}")'
                .format(self, str(self._cmdtype), str(self._parameter)))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.get_command() == other.get_command()
        return self.get_command() == other

    def __ne__(self, other):
        return not (self.get_command() == other)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# command.py ends here
