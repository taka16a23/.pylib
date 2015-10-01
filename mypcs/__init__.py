#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: __init__.py 464 2015-08-17 07:02:48Z t1 $
# $Revision: 464 $
# $Date: 2015-08-17 16:02:48 +0900 (Mon, 17 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-17 16:02:48 +0900 (Mon, 17 Aug 2015) $

r"""Name: __init__.py


"""
from mypcs.rook import Rook
from mypcs.rook import scripts as rookscripts
from mypcs.king import King
from mypcs.king import scripts as kingscripts
from mypcs import scripts


__revision__ = "$Revision: 464 $"
__version__ = "0.2.0"


__all__ = ['Rook', 'rookscripts', 'King', 'kingscripts', 'scripts']



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
