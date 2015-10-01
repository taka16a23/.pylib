#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""pdf -- DESCRIPTION

"""
from time import sleep
from mygoogle import chrome

from . import _recipe


class PDFRecipe(_recipe.Recipe):
    """Class PDFRecipe
    """
    # Attributes:

    # Operations
    def show(self):
        """function show

        returns
        """
        chrome.run(unicode(self._path))
        sleep(0.5)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# pdf.py ends here
