#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py


"""
from itertools import chain, product


__version__ = "0.1.0"

__all__ = ['iter_bruteforce', ]


def iter_bruteforce(charset, min_, max_):
    return (
        ''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(min_, max_ + 1)))




# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
