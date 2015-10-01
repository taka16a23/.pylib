#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: _recipe.py 468 2015-08-19 05:49:01Z t1 $
# $Revision: 468 $
# $Date: 2015-08-19 14:49:01 +0900 (Wed, 19 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-19 14:49:01 +0900 (Wed, 19 Aug 2015) $

r"""recipe -- DESCRIPTION

"""
from pathhandler import PathHandler

from recipe.menu2.common import DEFAULT_DIR

from . import _html_tag_gen
from . import _show


class Recipe(_show.Show, _html_tag_gen.HTMLTagGenerator):
    """Class Recipe
    """
    def __init__(self, path):
        r"""

        @Arguments:
        - `path`:
        """
        self._path = PathHandler(path)

    def get_path(self, ):
        r"""SUMMARY

        get_path()

        @Return:

        @Error:
        """
        return self._path

    def get_name(self):
        return unicode(self._path.basename.splitext()[0])

    def generate_html_tag(self):
        """function generate_html_tag

        returns
        """
        return _html_tag_gen.LINK_RECIPE_TEMPLATE.format(
            self._path.encode('utf-8').replace(DEFAULT_DIR, './menus'),
            self.get_name().encode('utf-8'))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# recipe.py ends here
