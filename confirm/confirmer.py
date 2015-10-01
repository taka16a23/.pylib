#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: confirmer.py 229 2014-09-13 08:17:28Z t1 $
# $Revision: 229 $
# $Date: 2014-09-13 17:17:28 +0900 (Sat, 13 Sep 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-09-13 17:17:28 +0900 (Sat, 13 Sep 2014) $

r"""confirmer -- DESCRIPTION

"""


class Confirmer(object):
    r"""Confirmer

    Confirmer is a object.
    Responsibility:
    """
    def __init__(self, confirmer):
        r"""

        @Arguments:
        - `confirmer`:
        """
        self._confirmer = confirmer

    def confirm(self, ):
        r"""SUMMARY

        confirm()

        @Return:

        @Error:
        """
        return self._confirmer.confirm()

    def set_confirmer(self, confirmer):
        r"""SUMMARY

        set_confirmer(confirmer)

        @Arguments:
        - `confirmer`:

        @Return:

        @Error:
        """
        self._confirmer = confirmer

    def get_confirmer(self, ):
        r"""SUMMARY

        get_confirmer()

        @Return:

        @Error:
        """
        return self._confirmer



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# confirmer.py ends here
