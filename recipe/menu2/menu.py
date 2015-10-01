#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""menu -- DESCRIPTION

"""
from datetime import datetime
from subprocess import Popen
from ref.CMD import thunar
from pathhandler import PathHandler

from recipe.menu2 import recipe_factory


WEEKDAY_JP = {0: '月',
              1: '火',
              2: '水',
              3: '木',
              4: '金',
              5: '土',
              6: '日',}


# def dispatch_recipe(path):
#     r"""SUMMARY

#     dispatch_recipe(path)

#     @Arguments:
#     - `path`:

#     @Return:

#     @Error:
#     """
#     data = magic.from_file(unicode(path))
#     if 'PDF' in data:
#         return recipe.PDFRecipe(unicode(path))
#     elif 'image' in data:
#         return recipe.ImageRecipe(unicode(path))
#     elif 'text' in data:
#         return recipe.TextRecipe(unicode(path))
#     elif 'empty' in data:
#         return recipe.FileRecipe(unicode(path))
#     else:
#         return None


class Menu(object):
    """Class Menu
    """
    # Attributes:
    def __init__(self, directory):
        r"""

        @Arguments:
        - `name`:
        """
        self._dir = PathHandler(directory)
        if self._dir.isfile():
            # TODO: (Atami) [2015/04/06]
            raise StandardError()
        if not self.exists():
            self._dir.mkdir(0755)

    # Operations
    def get_name(self):
        """function get_name

        returns
        """
        return self._dir.basename

    def get_date(self, ):
        r"""SUMMARY

        get_date()

        @Return:

        @Error:
        """
        return datetime.strptime(unicode(self.get_name()), '%Y_%m_%d')

    def get_path(self, ):
        r"""SUMMARY

        get_path()

        @Return:

        @Error:
        """
        return self._dir

    def _check_create(self, ):
        r"""SUMMARY

        _check_create()

        @Return:

        @Error:
        """
        if not self._dir.exists():
            self._dir.mkdir()

    def iter_recipes(self):
        """function list_recipes

        returns
        """
        self._check_create()
        factory = recipe_factory.RecipeFacroty()
        for rcp in self._dir.listdir():
            rcpobj = factory.create(unicode(rcp))
            # rcpobj = dispatch_recipe(rcp)
            if rcpobj is None:
                continue
            yield rcpobj

    def list_recipes(self, ):
        r"""SUMMARY

        list_recipes()

        @Return:

        @Error:
        """
        return list(self.iter_recipes())

    def has_recipes(self):
        """function has_recipes

        returns
        """
        return bool(self.list_recipes())

    def generate_html_tag(self):
        """function generate_html_tag

        returns
        """
        week = WEEKDAY_JP.get(self.get_date().weekday())
        date = '{0.month}月 {0.day}日 ({1})'.format(self.get_date(), week)
        tags = []
        for rcp in self.iter_recipes():
            tags.append(rcp.generate_html_tag())
        return "<h2><u>{0}</u></h2><h3><ul>{1}</ul></h3>".format(
            date, ''.join(tags))

    def add_recipe(self, path):
        """function add_recipe

        path:

        returns
        """
        return None # should raise NotImplementedError()

    def add_recipe(self, fobj):
        """function add_recipe

        fobj:

        returns
        """
        return None # should raise NotImplementedError()

    def remove(self):
        """function remove

        returns
        """
        self._dir.remove()

    def exists(self):
        """function exists

        returns
        """
        return self._dir.exists()

    def open_editor(self):
        """function open_editor

        returns
        """
        Popen([thunar.BINPATH, self._dir])

    def show_recipes(self):
        """function show_recipes

        returns
        """
        for rcp in self.iter_recipes():
            rcp.show()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# menu.py ends here
