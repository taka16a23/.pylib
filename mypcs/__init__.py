#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py


"""
from mypcs.rook import Rook
from mypcs.rook import scripts as rookscripts
from mypcs.king import King
from mypcs.king import scripts as kingscripts
from mypcs import scripts


__version__ = "0.2.0"


__all__ = ['Rook', 'rookscripts', 'King', 'kingscripts', 'scripts']



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
