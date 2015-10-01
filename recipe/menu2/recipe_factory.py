#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
