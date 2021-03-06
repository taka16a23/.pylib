#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""safeinput -- DESCRIPTION

python 2
input: tries to run input.
       if input 1 to return 1
       if input A to return "A"
python 3
input: like old raw_input on python 2
       if input 1 to return "1"
       if input A to return "A"

python2 "input" == python3 "eval(input())"
raw_input() does not exist in Python 3.x
python3 "input" == python2 "raw_input"

"""
import sys as _sys
import os as _os


def safeinput(prompt):
    r"""SUMMARY

    safeinput(prompt)

    @Arguments:
    - `prompt`:

    @Return:

    @Error:
    """
    if _sys.version_info <= (3, 0):
        return raw_input(prompt)
    return input(prompt)


def _test():
    r"""Test function."""
    return _os.EX_OK

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# safeinput.py ends here
