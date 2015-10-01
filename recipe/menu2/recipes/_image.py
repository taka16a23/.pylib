#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""image -- DESCRIPTION

"""
from subprocess import Popen

from . import _recipe


class ImageRecipe(_recipe.Recipe):
    r"""ImageRecipe

    ImageRecipe is a recipe.RecipePath.
    Responsibility:
    """
    def show(self, ):
        r"""SUMMARY

        show()

        @Return:

        @Error:
        """
        Popen(('xnview', unicode(self._path)))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# image.py ends here
