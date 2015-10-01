#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""core -- DESCRIPTION

"""
from getpasswd.getter import PassGetter, CmdlinePassGetter


class GetPasswd(object):
    r"""GetPasswd

    GetPasswd is a object.
    Responsibility:
    """
    def __init__(self, getter=None):
        r"""

        @Arguments:
        - `getter`:
        """
        self._getter = None
        self.setgetter(getter or CmdlinePassGetter())

    def setgetter(self, getter):
        r"""SUMMARY

        setgetter(getter)

        @Arguments:
        - `getter`:

        @Return:

        @Error:
        """
        if not isinstance(getter, PassGetter):
            # TODO: (Atami) [2014/12/04]
            raise TypeError(str(getter))
        self._getter = getter

    def getgetter(self, ):
        r"""SUMMARY

        getgetter()

        @Return:

        @Error:
        """
        return self._getter

    def getpass(self, prompt='Password: '):
        r"""SUMMARY

        getpass(prompt='Password: ')

        @Arguments:
        - `prompt`:

        @Return:

        @Error:
        """
        return self._getter.getpass(prompt)

    def __call__(self, prompt='Password: '):
        return self.getpass(prompt)

    def __repr__(self):
        return '{0.__class__.__name__}(_getter={0._getter})'.format(self)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# core.py ends here
