#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""oilprice -- DESCRIPTION

"""
import sys as _sys
import os as _os


# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


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
