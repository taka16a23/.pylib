#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py


"""
import os as _os

if 'posix' == _os.name:
    from .posix import *
else:
    raise NotImplementedError('not supported {.name} environment'.format(_os))

# elif 'nt' == _os.name:
    # from .nt import add_keys

__version__ = "0.1.0"

__all__ = [ 'DumpKeys', 'UnpackError', 'RENAME_MAP', 'SPECIAL_KEY_FMT',
            'SPECIAL_UPKEY_FMT', 'KeyMap', 'KeyUpMap', 'KeyShiftMap',
            'KeyMaps', 'KeyMapAbstract', 'KeyMapUpAbstract',
            'KeyMapShiftAbstract', 'posix']


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
