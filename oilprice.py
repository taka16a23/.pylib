#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: oilprice.py 248 2014-12-21 05:16:53Z t1 $
# $Revision: 248 $
# $Date: 2014-12-21 14:16:53 +0900 (Sun, 21 Dec 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-12-21 14:16:53 +0900 (Sun, 21 Dec 2014) $

r"""oilprice -- DESCRIPTION

"""
import sys as _sys
import os as _os


# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__revision__ = '$Revision: 248 $'
__version__ = '0.1.0'



def oilprice_jp(doller, fx):
    r"""SUMMARY

    oilprice_jp(doller, fx)

    @Arguments:
    - `doller`:
    - `fx`:

    @Return:

    @Error:

    1 barrel == 158.9
    """

    return doller * fx / 158.9




def _test():
    r"""Test function."""
    return _os.EX_OK

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# oilprice.py ends here
