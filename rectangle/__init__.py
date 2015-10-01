#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: __init__.py 333 2015-06-06 04:18:39Z t1 $
# $Revision: 333 $
# $Date: 2015-06-06 13:18:39 +0900 (Sat, 06 Jun 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-06-06 13:18:39 +0900 (Sat, 06 Jun 2015) $

r"""Name: __init__.py


"""
from rectangle._coordinate import XCoordinate, YCoordinate
from rectangle._side import Height, Width
from rectangle._dimension import Dimension
from rectangle._point import Point
from rectangle._rectangle import Rectangle


__revision__ = "$Revision: 333 $"
__version__ = "0.0.1"

__all__ = ['XCoordinate', 'YCoordinate', 'Height', 'Width', 'Dimension',
           'Point', 'Rectangle']



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
