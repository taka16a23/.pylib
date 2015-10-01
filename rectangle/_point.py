#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: _point.py 333 2015-06-06 04:18:39Z t1 $
# $Revision: 333 $
# $Date: 2015-06-06 13:18:39 +0900 (Sat, 06 Jun 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-06-06 13:18:39 +0900 (Sat, 06 Jun 2015) $

from rectangle._coordinate import XCoordinate, YCoordinate


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
        self._x = XCoordinate(x)
        self._y = YCoordinate(y)

    # Operations
    def get(self, ):
        """function get

        returns tuple
        """
        return (self._x, self._y)

    def set(self, point):
        """function set

        set((1, 1)) -> Point(x=1, y=1)
        set(Point(1, 1)) -> Point(x=1, y=1)
        set(XCoordinate(0))
        set(YCoordinate(0))
        returns None
        """
        if isinstance(point, (tuple, list, Point)):
            self.set_x(point[0])
            self.set_y(point[1])
        elif isinstance(point, (XCoordinate, )):
            self.set_x(point)
        elif isinstance(point, (YCoordinate, )):
            self.set_y(point)
        else:
            # TODO: (Atami) [2015/02/17]
            raise TypeError()

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

    def del_x(self, ):
        r"""SUMMARY

        del_x()

        @Return:

        @Error:
        """
        self._x.set(0)

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

    def del_y(self, ):
        r"""SUMMARY

        del_y()

        @Return:

        @Error:
        """
        self._y.set(0)

    x = property(get_x, set_x, del_x)
    y = property(get_y, set_y, del_y)

    def rotate(self, ):
        r"""SUMMARY

        rotate()

        @Return:

        @Error:
        """
        return self.__class__(self.y, self.x)

    def __str__(self):
        return str((int(self._x), int(self._y)))

    def __repr__(self):
        return '{0.__class__.__name__}(x={0.x}, y={0.y})'.format(self)

    def __len__(self):
        return len(self.get())

    def __eq__(self, other):
        return (self.x, self.y) == other

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        if isinstance(other, (XCoordinate, )):
            return self.__class__(self.x + other, self.y)
        if isinstance(other, (YCoordinate, )):
            return self.__class__(self.x, self.y + other)
        if isinstance(other, (int, )):
            return self.__class__(self.x + other, self.y + other)
        return self.__class__(self.x + other[0], self.y + other[1])

    def __iadd__(self, other):
        point = self + other
        self.x = point.get_x()
        self.y = point.get_y()
        return self

    def __sub__(self, other):
        if isinstance(other, (XCoordinate, )):
            return self.__class__(self.x - other, self.y)
        if isinstance(other, (YCoordinate, )):
            return self.__class__(self.x, self.y - other)
        if isinstance(other, (int, )):
            return self.__class__(self.x - other, self.y - other)
        return self.__class__(self.x - other[0], self.y - other[1])

    def __isub__(self, other):
        point = self - other
        self.x = point.get_x()
        self.y = point.get_y()
        return self

    def __mul__(self, other):
        if isinstance(other, (XCoordinate, )):
            return self.__class__(self.x * other, self.y)
        if isinstance(other, (YCoordinate, )):
            return self.__class__(self.x, self.y * other)
        if isinstance(other, (int, )):
            return self.__class__(self.x * other, self.y * other)
        return self.__class__(self.x * other[0], self.y * other[1])

    def __imul__(self, other):
        point = self * other
        self.x = point.get_x()
        self.y = point.get_y()
        return self

    def __div__(self, other):
        if isinstance(other, (XCoordinate, )):
            return self.__class__(self.x / other, self.y)
        if isinstance(other, (YCoordinate, )):
            return self.__class__(self.x, self.y / other)
        if isinstance(other, (int, )):
            return self.__class__(self.x / other, self.y / other)
        return self.__class__(self.x / other[0], self.y / other[1])

    def __idiv__(self, other):
        point = self / other
        self.x = point.get_x()
        self.y = point.get_y()
        return self

    def __pos__(self):
        return self.__class__(-self.x, -self.y)

    def __neg__(self, ):
        return self.__class__(-self.x, -self.y)

    def __getitem__(self, index):
        return self.get()[index]

    def __setitem__(self, index, val):
        self[index].set(val)

    def __nonzero__(self):
        return not (self.x == 0 and self.y == 0)

    def __iter__(self):
        return iter(self.get())

    def __delitem__(self, index):
        if 0 == index:
            del self.x
        elif 1 == index:
            del self.y
        else:
            # TODO: (Atami) [2015/02/17]
            raise IndexError(index)

    def __del__(self):
        del self.x, self.y



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# point.py ends here
