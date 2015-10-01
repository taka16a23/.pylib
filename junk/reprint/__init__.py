#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py


"""
import sys as _sys

__version__ = "0.1.0"

__all__ = [ 'reprint' ]


def reprint(str_):
    r"""SUMMARY

    reprint(str_)

    @Arguments:
    - `str_`:

    @Return:
    """
    _sys.stdout.write('\r' + str_)
    _sys.stdout.flush()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
