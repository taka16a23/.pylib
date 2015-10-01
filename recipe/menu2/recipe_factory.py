#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: recipe_factory.py 454 2015-08-08 06:21:36Z t1 $
# $Revision: 454 $
# $Date: 2015-08-08 15:21:36 +0900 (Sat, 08 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-08 15:21:36 +0900 (Sat, 08 Aug 2015) $

r"""recipe_factory -- DESCRIPTION

"""
import magic

from recipe.menu2 import recipes


class RecipeFacroty(object):
    r"""RecipeFacroty

    RecipeFacroty is a object.
    Responsibility:
    """

    def create(self, path):
        r"""SUMMARY

        create(path)

        @Arguments:
        - `path`:

        @Return:

        @Error:
        """
        return self._create_implement(path)

    def _create_implement(self, path):
        r"""SUMMARY

        _create_implement(path)

        @Arguments:
        - `path`:

        @Return:

        @Error:
        """
        data = magic.from_file(path)
        if 'PDF' in data:
            return recipes.PDFRecipe(path)
        if 'image' in data:
            return recipes.ImageRecipe(path)
        if 'text' in data:
            return recipes.TextRecipe(path)
        if 'empty' in data:
            return recipes.FileRecipe(path)
        return None



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# recipe_factory.py ends here
