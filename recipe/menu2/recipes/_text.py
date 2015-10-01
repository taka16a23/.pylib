#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: _text.py 455 2015-08-08 06:39:21Z t1 $
# $Revision: 455 $
# $Date: 2015-08-08 15:39:21 +0900 (Sat, 08 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-08 15:39:21 +0900 (Sat, 08 Aug 2015) $

r"""text -- DESCRIPTION

"""
from subprocess import Popen

from . import _recipe


class TextRecipe(_recipe.Recipe):
    r"""TextRecipe

    TextRecipe is a recipe.Recipe.
    Responsibility:
    """
    def show(self, ):
        r"""SUMMARY

        show()

        @Return:

        @Error:
        """
        Popen(('mousepad', unicode(self._path)))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# text.py ends here
