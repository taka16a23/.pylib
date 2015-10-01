#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py


"""
from colorama import Fore, Style, Back, init, deinit, reinit
from coloramautil import formatter
from coloramautil.formatter import *



__version__ = "0.1.1"

__all__ = ['Fore', 'Style', 'Back', 'formatter', 'init', 'deinit', 'reinit']
__all__ += formatter.__all__



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
