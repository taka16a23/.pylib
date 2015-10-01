#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: _pdf.py 455 2015-08-08 06:39:21Z t1 $
# $Revision: 455 $
# $Date: 2015-08-08 15:39:21 +0900 (Sat, 08 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-08 15:39:21 +0900 (Sat, 08 Aug 2015) $

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
