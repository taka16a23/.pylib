#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py


"""
import os as _os
from pathhandler import PathHandler as _PathHandler


__all__ = ['SSH_CONFIG_PATH', ]


SSH_CONFIG_PATH = _PathHandler(_os.getenv('HOME')).join('.ssh/config')




# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
