#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py


"""
from rectangle._coordinate import XCoordinate, YCoordinate
from rectangle._side import Height, Width
from rectangle._dimension import Dimension
from rectangle._point import Point
from rectangle._rectangle import Rectangle


__version__ = "0.0.1"

__all__ = ['XCoordinate', 'YCoordinate', 'Height', 'Width', 'Dimension',
           'Point', 'Rectangle']



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
