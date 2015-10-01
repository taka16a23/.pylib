#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""atomidentify -- DESCRIPTION

"""
from peak.rules import dispatch

from xcb2.abstract import ConnectionAbstract
from xcb2.xobj.atom.atompair import AtomPair # do not remove


__all__ = ['AtomIdentifier']


class AtomIdentifier(ConnectionAbstract):
    r"""
    """

    # TODO: (Atami) [2014/02/17]
    # behave atom on 0

    @property
    def InternAtom(self, ):
        r"""SUMMARY

        InternAtom(name)

        @Arguments:
        - `name`:

        @Return:
        """
        return self.connection.core.InternAtom

    @property
    def GetAtomName(self, ):
        r"""SUMMARY

        InternAtom(name)

        @Arguments:
        - `name`:

        @Return:
        """
        return self.connection.core.GetAtomName

    @dispatch.generic()
    def identify(self, atom):
        r"""Base generic method of 'identify_atom'"""

    @identify.when('isinstance(atom, AtomPair)')
    def _identify_AtomPair(self, atom):
        r"""SUMMARY

        identify_atom_AtomPair(atom)

        @Arguments:
        - `atom`:

        @Return:
        """
        return atom

    @identify.when('isinstance(atom, str)')
    def _identify_str(self, atom):
        r"""SUMMARY

        identify_atom_str(atom)

        @Arguments:
        - `atom`:

        @Return:
        """
        return self.InternAtom.usecache(atom)

    @identify.when('isinstance(atom, int)')
    def _identify_int(self, atom):
        r"""SUMMARY

        identify_atom_int(atom)

        @Arguments:
        - `atom`:

        @Return:
        """
        return self.GetAtomName.usecache(atom)

    def __call__(self, atom):
        return self.identify(atom)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# atomidentify.py ends here
