#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""tes1 -- DESCRIPTION

"""

import sys as _sys
import os as _os

from plugin import PluginAbstract

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


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
