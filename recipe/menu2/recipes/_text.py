#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
