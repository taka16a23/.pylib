#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""\
Name: __init__.py


"""
import os as _os

__version__ = "0.1.0"

__all__ = [ 'MYTEMP', 'KAGI', 'KAGIMD5']

if 'nt' == _os.name:
    from portable import P_SECURITY
    MYTEMP = 'D:\\MYTEMP'
    KAGI = _os.path.join(P_SECURITY, 'Password\\kagi\\kagi.ppk')

elif 'posix' == _os.name:
    KAGI = _os.path.expanduser('~/.ssh/kagi')
    KAGIMD5 = '\xc8\xa6k\xe5\xd9\xef\xa1.[\xd8Y\xc7\xd3\x95[\xd2'

else:
    raise NotImplementedError('not supported {.name} environment'.format(_os))


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
