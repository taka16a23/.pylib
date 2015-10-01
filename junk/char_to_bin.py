#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""char_to_bin -- DESCRIPTION

"""

import sys as _sys
import os as _os

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__version__ = '0.1.0'


def ascii_to_bin(char):
    ascii = ord(char)
    bin = []
    while (ascii > 0):
        if (ascii & 1) == 1:
            bin.append("1")
        else:
            bin.append("0")
        ascii = ascii >> 1

    bin.reverse()
    binary = "".join(bin)
    zerofix = (8 - len(binary)) * '0'
    return zerofix + binary


def _test():
    r"""Test function."""
    return _os.EX_OK

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# char_to_bin.py ends here
