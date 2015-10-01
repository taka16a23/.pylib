#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""pc_name -- DESCRIPTION

"""
import sys as _sys
import os as _os
from socket import gethostname


__version__ = '0.1.0'


def pc_name():
    r"""SUMMARY

    pc_name()

    @Return:
    """
    return gethostname()


def _test():
    r"""Test function."""
    return _os.EX_OK

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# pc_name.py ends here
