#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""options -- DESCRIPTION

"""

class RsyncOption(object):
    r"""SUMMARY
    """

    def __init__(self, list):
        r"""

        @Arguments:
        - `list`:
        """
        self.list = list

    def add_verbose(self, num=1):
        r"""SUMMARY

        add_verbose(num=1)

        @Arguments:
        - `num`:

        @Return:
        """
        self.list.extend(('--verbose', ) * num)

    def remove_verbose(self, ):
        r"""SUMMARY

        remove_verbose()

        @Return:
        """
        self.list.remove('--verbose')

    def add_quiet(self, ):
        r"""SUMMARY

        add_quiet()

        @Return:
        """
        self.list.append('--quiet')

    def remove_quiet(self, ):
        r"""SUMMARY

        remove_quiet()

        @Return:
        """
        self.list.remove('--quiet')

    def add_no_motd(self, ):
        r"""SUMMARY

        add_no_motd()

        @Return:
        """
        self.list.append('--no-motd')




# For Emacs
# Local Variables:
# coding: utf-8
# End:
# options.py ends here
