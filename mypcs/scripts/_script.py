#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""_script -- DESCRIPTION

"""
from abc import ABCMeta, abstractmethod


class Script(object):
    """Abstract class Script
    """
    __metaclass__ = ABCMeta

    # Operations
    @abstractmethod
    def execute_script(self, shell):
        """function execute_script

        shell:

        returns
        """
        raise NotImplementedError()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _script.py ends here
