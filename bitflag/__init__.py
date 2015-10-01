#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: __init__.py 146 2014-04-12 09:38:34Z t1 $
# $Revision: 146 $
# $Date: 2014-04-12 18:38:34 +0900 (Sat, 12 Apr 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-04-12 18:38:34 +0900 (Sat, 12 Apr 2014) $

r"""Name: __init__.py


"""
from bitflag.cls import BitFlag8, BitFlag16, BitFlag32
from bitflag.abstract import BitFlagAbstract
from bitflag.flagenum import FlagEnum
from bitflag.error import BitFlagError, BitLengthError


__revision__ = "$Revision: 146 $"
__version__ = "0.1.0"

__all__ = [ '' ]



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
