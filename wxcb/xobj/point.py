#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: point.py 280 2015-01-29 00:05:31Z t1 $
# $Revision: 280 $
# $Date: 2015-01-29 09:05:31 +0900 (Thu, 29 Jan 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-01-29 09:05:31 +0900 (Thu, 29 Jan 2015) $

from peak.rules import dispatch


import coordinate


class Point(object):
    """Class Point
    """
    # Attributes:
    def __init__(self, x=0, y=0):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        self._x = coordinate.XCoordinate()
        self._y = coordinate.YCoordinate()
        self.set((x, y))

    # Operations
    def get(self, ):
        """function get

        returns tuple
        """
        return (self._x, self._y)

    @dispatch.generic()
    def set(self, point):
        """function set

        set((1, 1)) -> Point(x=1, y=1)
        set(Point(1, 1)) -> Point(x=1, y=1)

        returns None
        """

    @set.when('len(point) == 2 and isinstance(point, (tuple, list))')
    def __set_list(self, point):
        r"""SUMMARY

        __set_list(point)

        @Arguments:
        - `point`:

        @Return:

        @Error:
        """
        self.x = point[0]
        self.y = point[1]

    @set.when('len(point) == 2 and isinstance(point, (self.__class__, ))')
    def __set_point(self, point):
        r"""SUMMARY

        __set_point(point)

        @Arguments:
        - `point`:

        @Return:

        @Error:
        """
        self.x = point.get_x()
        self.y = point.get_y()

    def get_x(self):
        """get_x

        returns XCoordinate
        """
        return self._x

    def set_x(self, x):
        """function set_x

        @Arguments:
        - `x`:

        @Return: None

        set_x()
        """
        self._x.set(x)

    def get_y(self):
        """function get_y

        @Returns YCoordinate
        """
        return self._y

    def set_y(self, y):
        """function set_y

        y:

        returns None
        """
        self._y.set(y)

    x = property(get_x, set_x)
    y = property(get_y, set_y)

    def rotate(self, ):
        r"""SUMMARY

        rotate()

        @Return:

        @Error:
        """
        return self.__class__(self.get_y(), self.get_x())

    def __str__(self):
        """function __str__

        returns str
        """
        return str((int(self._x), int(self._y)))

    def __repr__(self):
        """function __repr__

        returns str
        """
        return '{0.__class__.__name__}(x={0._x}, y={0._y})'.format(self)

    def __len__(self):
        """function __len__

        returns int
        """
        return len(self.get())

    def __eq__(self, other):
        """function __eq__

        returns bool
        """
        return (int(self._x), int(self._y)) == (int(other[0]), int(other[1]))

    def __ne__(self, other):
        """function __ne__

        returns bool
        """
        return not self == other

    def __add__(self, other):
        """function __add__

        returns Point
        """
        return self.__class__(self._x + other[0], self._y + other[1])

    def __sub__(self, other):
        """function __sub__

        returns Point
        """
        return self.__class__(self._x - other[0], self._y - other[1])

    def __iadd__(self, other):
        """function __iadd__

        other:

        returns Point
        """
        self._x += other[0]
        self._y += other[1]
        return self

    def __isub__(self, other):
        """function __isub__

        other:

        returns Point
        """
        self._x -= other[0]
        self._y -= other[1]
        return self

    def __pos__(self):
        return self.__class__(-self.get_x(), -self.get_y())

    def __neg__(self, ):
        return self.__class__(-self.get_x(), -self.get_y())

    def __getitem__(self, index):
        """function __getitem__

        index:

        returns
        """
        return self.get()[index]

    def __setitem__(self, index, val):
        """function __setitem__

        index:
        val:

        returns
        """
        self[index].set(val)

    def __nonzero__(self):
        """function __nonzero__

        returns
        """
        return not (self._x == 0 and self._y == 0)

    def __iter__(self):
        return iter(self.get())

    def __delitem__(self, index):
        self.get()[index].set(0)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# point.py ends here
