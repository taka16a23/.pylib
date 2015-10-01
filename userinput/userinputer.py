#!/usr/bin/env python
# -*- coding: utf-8 -*-

class UserInputer(object):
    """Class UserInputer
    """
    # Attributes:
    def __init__(self, inputer):
        r"""

        @Arguments:
        - `inputer`:
        """
        self._inputer = inputer

    # Operations
    def get_inputer(self):
        """function get_inputer

        returns
        """
        return self._inputer

    def set_inputer(self, inputer):
        """function set_inputer

        inputer: UserInput

        returns
        """
        self._inputer = inputer

    def input(self):
        """function input

        returns string
        """
        return self._inputer.input()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# userinputer.py ends here
