#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py


"""
from mypcs.scripts._ping import PingScript
from mypcs.scripts._reboot import RebootScript
from mypcs.scripts._halt import HaltScript
from mypcs.scripts._script import Script


__all__ = ['PingScript', 'RebootScript', 'HaltScript', 'Script']



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
