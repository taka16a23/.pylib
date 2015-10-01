#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: _image.py 455 2015-08-08 06:39:21Z t1 $
# $Revision: 455 $
# $Date: 2015-08-08 15:39:21 +0900 (Sat, 08 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-08 15:39:21 +0900 (Sat, 08 Aug 2015) $

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
