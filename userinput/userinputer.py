#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: userinputer.py 290 2015-01-29 00:19:07Z t1 $
# $Revision: 290 $
# $Date: 2015-01-29 09:19:07 +0900 (Thu, 29 Jan 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-01-29 09:19:07 +0900 (Thu, 29 Jan 2015) $


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
