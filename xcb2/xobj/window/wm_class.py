#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: wm_class.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""wm_class -- DESCRIPTION

"""
from xcb2.abstract import ConnectionAbstract


class WMCLASS(ConnectionAbstract):
    r"""SUMMARY
    """
    atomname = 'WM_CLASS'

    __slots__ = ('res_name', 'res_class')

    def __init__(self, connection=None, res_name=None, res_class=None):
        r"""

        @Arguments:
        - `res_name`:
        - `res_class`:
        """
        if connection:
            ConnectionAbstract.__init__(self, connection)
        self.res_name = res_name or ''
        self.res_class = res_class or ''

    def match_client_list(self, ):
        r"""SUMMARY

        match_client_list()

        @Return:
        """
        name = self.connection.root.client_list().to_types().filter_wmclass(
            self.res_name)
        cls = self.connection.root.client_list().to_types().filter_wmclass(
            self.res_class)
        return name + cls

    @property
    def atom(self, ):
        r"""SUMMARY

        atom()

        @Return:
        """
        return self.connection.core.atomidentify(self.atomname)

    def change(self, window, mode=0):
        r"""ChangeProperty

        setwmclass(window)

        @Arguments:
        - `window`:

        @Return:
        """
        atom = self.atom
        return self.connection.core.ChangeProperty(
            mode, window, atom, atom.gettype(), atom.getformat(),
            len(self), str(self))

    def __contains__(self, other):
        return other in (self.res_name, self.res_class)

    def __iter__(self, ):
        return iter((self.res_name, self.res_class))

    def __repr__(self, ):
        fmt = ('{0.__class__.__name__}'
               '(res_name="{0.res_name}", res_class="{0.res_class}")').format
        return (fmt(self))

    def __str__(self, ):
        return '{}\x00{}\x00'.format(self.res_name, self.res_class)

    def __len__(self, ):
        return len(str(self))

    def __nonzero__(self, ):
        return bool(self.res_name or self.res_class)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# wm_class.py ends here
