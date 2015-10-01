#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""file -- DESCRIPTION

"""
from . import _recipe
from . import _html_tag_gen


class FileRecipe(_recipe.Recipe):
    r"""FileRecipe

    FileRecipe is a recipe.Recipe.
    Responsibility:
    """
    def generate_html_tag(self):
        """function generate_html_tag

        returns
        """
        return _html_tag_gen.RECIPE_TEMPLATE.format(
            unicode(self._path.basename).encode('utf-8'),
            self.get_name().encode('utf-8'))





# For Emacs
# Local Variables:
# coding: utf-8
# End:
# file.py ends here
