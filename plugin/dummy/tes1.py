#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: tes1.py 98 2014-01-11 10:09:59Z t1 $
# $Revision: 98 $
# $Date: 2014-01-11 19:09:59 +0900 (Sat, 11 Jan 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-01-11 19:09:59 +0900 (Sat, 11 Jan 2014) $

r"""tes1 -- DESCRIPTION

"""

import sys as _sys
import os as _os

from plugin import PluginAbstract

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__revision__ = '$Revision: 98 $'
__version__ = '0.1.0'


class Tesclass01(PluginAbstract):
    r"""
    """

    def __call__(self, ):
        r"""
        """

        pass



def _test():
    r"""Test function."""
    return _os.EX_OK

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# tes1.py ends here
