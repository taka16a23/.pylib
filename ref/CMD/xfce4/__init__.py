#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: __init__.py 102 2014-01-25 07:43:58Z t1 $    
# $Revision: 102 $
# $Date: 2014-01-25 16:43:58 +0900 (Sat, 25 Jan 2014) $    
# $Author: t1 $  
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-01-25 16:43:58 +0900 (Sat, 25 Jan 2014) $

r"""Name: __init__.py


"""
import os as _os

__revision__ = "$Revision: 102 $"
__version__ = "0.1.0"

__all__ = [ '' ]

if 'nt' == _os.name:
    raise NotImplementedError('not supported {.name} environment'.format(_os))
elif 'posix' == _os.name:
    from ref.CMD.xfce4.posix_functions import * 
else:
    raise NotImplementedError('not supported {.name} environment'.format(_os))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
