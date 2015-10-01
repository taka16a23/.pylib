#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""shell -- DESCRIPTION

"""
from abc import ABCMeta, abstractmethod


class Shell(object):
    """Abstract class Shell
    """
    __metaclass__ = ABCMeta
    # Operations
    @abstractmethod
    def execute_command(self, cmdline):
        """function execute_command

        cmdline:

        returns StandardStream
        """
        raise NotImplementedError()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# shell.py ends here
