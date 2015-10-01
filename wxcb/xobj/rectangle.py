#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: rectangle.py 280 2015-01-29 00:05:31Z t1 $
# $Revision: 280 $
# $Date: 2015-01-29 09:05:31 +0900 (Thu, 29 Jan 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-01-29 09:05:31 +0900 (Thu, 29 Jan 2015) $

import predicate
from peak.rules import dispatch
import enum

from userint import UserInt # use in dispatch
import point
import dimension


class Orientation(enum.IntEnum):
    r"""Orientation

    Orientation is a enum.Enum.
    Responsibility:
    """
    horizontal = 4
    vertical = 8
    both = vertical | horizontal


class Rectangle(object):
    r"""Rectangle

    Rectangle is a object.
    Responsibility:
    """
    # TODO: (Atami) [2014/12/24]
    # write document
    # ref. http://grepcode.com/file/repository.grepcode.com/java/root/jdk/openjdk/6-b14/java/awt/Rectangle.java#Rectangle
    # http://qt-project.org/doc/qt-4.8/qrect.html

    # Attributes:
    @dispatch.generic()
    def __init__(self, *args, **kwargs):
        r"""Initializes Rectangle.

        @Arguments:
        - `*args`:
        - `**kwargs`:

        @Error NoApplicableMethods:

        Rectangle()
        Rectangle(int)
        Rectangle(Point)
        Rectangle(Dimension)
        Rectangle(Rectangle)
        Rectangle(Point, Dimension)
        Rectangle(int, int)
        Rectangle(int, int, Dimention)
        Rectangle(Point, int, int)
        Rectangle(Dimension, x=10, y=10)
        Rectangle(int, int, int, int)
        """

    @__init__.when('len(args) == 0')
    def __init__len0(self, *args, **kwargs):
        r"""Rectangle()"""
        x, y, w, h = [kwargs.get(x, 0) for x in ('x', 'y', 'width', 'height')]
        self.__init__(x, y, w, h)

    @__init__.when('len(args) == 1 and isinstance(args[0], point.Point)')
    def __init__len1_point(self, *args, **kwargs):
        r"""Rectangle(Point())"""
        if 'x' in kwargs or 'y' in kwargs:
            raise TypeError()
        w, h = [kwargs.get(x, 0) for x in ('width', 'height')]
        self.__init__(args[0].get_x(), args[0].get_y(), w, h)

    @__init__.when('len(args) == 1 and isinstance(args[0], dimension.Dimension)')
    def __init__len1_dimension(self, *args, **kwargs):
        r"""Rectangle(Dimension())"""
        if 'width' in kwargs or 'height' in kwargs:
            raise TypeError()
        x, y = [kwargs.get(x, 0) for x in ('x', 'y')]
        self.__init__(x, y, args[0].get_width(), args[0].get_height())

    @__init__.when('len(args) == 1 and isinstance(args[0], self.__class__)')
    def __init__rectangle(self, *args, **kwargs):
        r"""Rectangle(Rectangle())"""
        if ('x' in kwargs or 'y' in kwargs or
            'width' in kwargs or 'height' in kwargs):
            raise TypeError()
        self.__init__(args[0].get_x(), args[0].get_y(),
                      args[0].get_width(), args[0].get_height())

    @__init__.when('len(args) == 1 and isinstance(args[0], (int, UserInt))')
    def __init__len1_int(self, *args, **kwargs):
        r"""Rectangle(0)"""
        if 'x' in kwargs:
            raise TypeError()
        y, w, h = [kwargs.get(x, 0) for x in ('y', 'width', 'height')]
        self.__init__(args[0], y, w, h)

    @__init__.when('len(args) == 2 '
                   'and isinstance(args[0], point.Point) '
                   'and isinstance(args[1], dimension.Dimension)')
    def __init__len2_point_dimension(self, *args, **kwargs):
        r"""Rectangle(Point(), Dimension())"""
        if ('x' in kwargs or 'y' in kwargs or
            'width' in kwargs or 'height' in kwargs):
            raise TypeError()
        self.__init__(args[0].get_x(), args[0].get_y(),
                      args[1].get_width(), args[1].get_height())

    @__init__.when('len(args) == 2 '
                   'and isinstance(args[0], dimension.Dimension) '
                   'and isinstance(args[1], point.Point)')
    def __init__len2_dimension_point(self, *args, **kwargs):
        r"""Rectangle(Dimension(), Point()) """
        if ('x' in kwargs or 'y' in kwargs or
            'width' in kwargs or 'height' in kwargs):
            raise TypeError()
        self.__init__(args[1].get_x(), args[1].get_y(),
                      args[0].get_width(), args[0].get_height())

    @__init__.when('len(args) == 2 '
                   'and isinstance(args[0], (int, UserInt)) '
                   'and isinstance(args[1], (int, UserInt))')
    def __init__len2_int(self, *args, **kwargs):
        r"""Rectangle(0, 0)"""
        if ('x' in kwargs or 'y' in kwargs):
            raise TypeError()
        w, h = [kwargs.get(x, 0) for x in ('width', 'height')]
        self.__init__(args[0], args[1], w, h)

    @__init__.when('len(args) == 3 and isinstance(args[0], point.Point)')
    def __init__len3_point(self, *args, **kwargs):
        r"""Rectangle(Point(), 0, 0)"""
        if len(kwargs):
            raise TypeError()
        self.__init__(args[0].get_x(), args[0].get_y(), args[1], args[2])

    @__init__.when('len(args) == 3 and isinstance(args[2], dimension.Dimension)')
    def __init__len3_dimension(self, *args, **kwargs):
        r"""Rectangle(0, 0, Dimension())"""
        if len(kwargs):
            raise TypeError()
        self.__init__(
            args[0], args[1], args[2].get_width(), args[2].get_height())

    @__init__.when('len(args) == 4')
    def __init__len4_int(self, *args, **kwargs):
        r"""Rectangle(0, 0, 0, 0)"""
        if len(kwargs):
            raise TypeError()
        self._point = point.Point(args[0], args[1])
        self._dimension = dimension.Dimension(args[2], args[3])

    def get_bounds(self):
        """get_bounds

        @Return:
        tuple
        """
        return tuple(self.location) + tuple(self.size)

    @dispatch.generic()
    def set_bounds(self, value):
        r"""SUMMARY

        set_bounds(value)

        @Arguments:
        - `value`:

        @Return:
        None

        @Error:

        set_bounds((0, 0, 0, 0)) # x, y, width, height
        set_bounds([0, 0, 0, 0]) # x, y, width, height
        set_bounds(Rectangle(0, 0, 0, 0))
        """

    @set_bounds.when('isinstance(value, (tuple, list)) and len(value) == 4')
    def __set_bounds_list(self, value):
        r"""SUMMARY
        """
        self.location = (value[0], value[1])
        self.size = (value[2], value[3])

    @set_bounds.when('isinstance(value, (self.__class__, ))')
    def __set_bounds_rectangle(self, value):
        r"""SUMMARY
        """
        self.location = value.get_location()
        self.size = value.get_size()

    def get_location(self):
        """function get_location

        @Return:
        Point
        """
        return self._point

    @dispatch.generic()
    def set_location(self, value):
        """set_location

        @Arguments:
        - `value`:

        @Return:
        None
        """

    @set_location.when('isinstance(value, (tuple, list)) and len(value) == 2')
    def __set_location_list(self, value):
        r"""SUMMARY

        """
        self._point.set((value[0], value[1]))

    @set_location.when('isinstance(value, (point.Point,))')
    def __set_location_point(self, value):
        r"""SUMMARY

        """
        self._point.set(value)

    def get_x(self):
        """get_x

        @Return:
        XCoordinate
        """
        return self._point.get_x()

    def set_x(self, newx):
        """set_x

        @Arguments:
        - `newx`:

        @Return:
        None
        """
        self._point.set_x(newx)

    def get_y(self):
        """get_y

        @Return:
        YCoordinate
        """
        return self._point.get_y()

    def set_y(self, newy):
        """set_y

        @Arguments:
        - `newy`:

        @Return:
        None
        """
        self._point.set_y(newy)

    def get_size(self, ):
        """get_size

        @Return: Dimension
        """
        return self._dimension

    @dispatch.generic()
    def set_size(self, value):
        """function set_size

        @Arguments:
        - `value`:

        @Return:
        None
        """

    @set_size.when('isinstance(value, (tuple, list)) and len(value) == 2')
    def __set_size_list(self, value):
        r"""SUMMARY
        """
        self._dimension.set(value[0], value[1])

    @set_size.when('isinstance(value, (dimension.Dimension, ))')
    def __set_size_dimension(self, value):
        r"""SUMMARY
        """
        self._dimension.set(value)

    def get_width(self):
        """get_width

        @Return:
        Width
        """
        return self._dimension.get_width()

    def set_width(self, newwidth):
        """set_width

        @Arguments:
        - `newwidth`:

        @Return:
        None
        """
        self._dimension.set_width(newwidth)

    def get_height(self, ):
        """get_height

        @Return:
        Height
        """
        return self._dimension.get_height()

    def set_height(self, newheight):
        """set_height

        @Arguments:
        - `newheight`:

        @Return:
        None
        """
        self._dimension.set_height(newheight)

    size = property(get_size, set_size)
    location = property(get_location, set_location)
    x = property(get_x, set_y)
    y = property(get_y, set_y)
    width = property(get_width, set_width)
    height = property(get_height, set_height)

    def isempty(self, ):
        """isempty

        @Return:
        bool
        """
        return self.width <= 0 or self.height <= 0

    def grow(self, dx=0, dy=0):
        """grow

        @Arguments:
        - `dx`: int
        - `dy`: int

        @Return:
        Rectangle
        """
        def calc(side, coord, add):
            sides, coords, adds = int(side), int(coord), int(add)
            newside = sides + adds * 2
            if predicate.isnegative(newside):
                newside = 0
                adds = abs(sides / 2)
                return (coords + adds), newside
            return (coords - adds), newside
        newx, neww = calc(self.width, self.x, dx)
        newy, newh = calc(self.height, self.y, dy)
        self.set_bounds((newx, newy, neww, newh))

    @dispatch.generic()
    def offset(self, value):
        """offset

        offset(Point(10, 10))
        offset((10, 10))

        @Arguments:
        - `value`:

        @Return:
        None

        @Error:
        NoApplicableMethods
        """

    @offset.when('isinstance(value, (point.Point,))')
    def __offset_point(self, value):
        r"""SUMMARY
        """
        self._point += value

    @offset.when('isinstance(value, (tuple, list)) and len(value) == 2')
    def __offset_list(self, value):
        r"""SUMMARY
        """
        self.location = (self.x + value[0], self.y + value[1])

    @dispatch.generic()
    def intersect(self, value):
        r"""SUMMARY

        intersect(value)

        @Arguments:
        - `value`:

        @Return:
        Rectangle, None

        intersect(Rectangle(0, 0, 10, 10))
        intersect((0, 0, 10, 10))
        """

    @intersect.when('isinstance(value, (self.__class__, ))')
    def __intersect_rectangle(self, value):
        """intersects

        """
        thisx, thisy, thisright, thisbottom = (
            self.x, self.y, self.right, self.bottom)
        otherx, othery, otherright, otherbottom = (
            value.get_x(), value.get_y(), value.get_right(), value.get_bottom())
        if thisx < otherx:
            thisx = otherx
        if thisy < othery:
            thisy = othery
        if otherright < thisright:
            thisright = otherright
        if otherbottom < thisbottom:
            thisbottom = otherbottom
        width = thisright - thisx + 1
        height = thisbottom - thisy + 1
        if width <= 0 or height <= 0:
            width = height = 0
        return self.__class__(thisx, thisy, width, height)

    @intersect.when('isinstance(value, (tuple, list)) and len(value) == 4')
    def __intersect_list(self, value):
        r"""SUMMARY

        """
        return self.intersect(
            self.__class__(value[0], value[1], value[2], value[3]))

    @dispatch.generic()
    def intersects(self, value):
        r"""SUMMARY

        intersects(value)

        @Arguments:
        - `value`:

        @Return:

        @Error:
        """

    @intersects.when('isinstance(value, (tuple, list)) and len(value) == 4')
    def __intersects_list(self, value):
        r"""SUMMARY

        """
        return self.intersects(
            self.__class__(value[0], value[1], value[2], value[3]))

    @intersects.when('isinstance(value, (self.__class__, ))')
    def __intersects_rectangle(self, value):
        r"""SUMMARY

        """
        rect = self.intersect(value)
        return rect.get_width() != 0

    @dispatch.generic()
    def union(self, value):
        r"""SUMMARY

        union(value)

        @Arguments:
        - `value`:

        @Return:
        Rectangle

        @Error:

        union((0, 0, 10, 10))
        union(Rectangle(0, 0, 10, 10))
        """

    @union.when('isinstance(value, (tuple, list)) and len(value) == 4')
    def __union_list(self, value):
        r"""SUMMARY

        """
        thisw, thish = self.width, self.height
        if (thisw | thish) < 0:
            return self.__class__(value[0], value[1], value[2], value[3])
        otherw, otherh = value[2], value[3]
        if (otherw | otherh) < 0:
            return self.__class__(self)

        thisx, thisy = self.x, self.y
        otherx, othery = value[0], value[1]
        newx = min(thisx, otherx)
        newy = min(thisy, othery)
        neww = max(thisx + thisw, otherx + otherw) - newx
        newh = max(thisy + thish, othery + otherh) - newy
        return self.__class__(newx, newy, neww, newh)

    @union.when('isinstance(value, (self.__class__, ))')
    def __union_rectangle(self, value):
        """union

        """
        return self.union(value.get_bounds())

    @dispatch.generic()
    def centerin(self, value, dir_=Orientation.both):
        """centerin

        rectangle:

        returns Rectangle

        """

    @centerin.when('isinstance(value, (tuple, list)) and len(value) == 4')
    def __centerin_list(self, value, dir_=Orientation.both):
        r"""SUMMARY

        """
        if dir_ & Orientation.horizontal:
            # cut off after the decimal point
            newx = value[0] + int(int((value[2] - self.width)) / 2.0)
        else:
            newx = self.x
        if dir_ & Orientation.vertical:
            # cut off after the decimal point
            newy = value[1] + int(int((value[3] - self.height)) / 2.0)
        else:
            newy = self.y
        return self.__class__(newx, newy, self.width, self.height)

    @centerin.when('isinstance(value, (self.__class__, ))')
    def __centerin_rectangle(self, value, dir_=Orientation.both):
        r"""SUMMARY

        """
        return self.centerin((value.get_x(), value.get_y(),
                              value.get_width(), value.get_height()), dir_=dir_)

    def get_top(self, ):
        r"""SUMMARY

        get_top()

        @Return:
        YCoordinate

        @Error:
        """
        return self.y

    def set_top(self, top):
        r"""SUMMARY

        set_top(top)

        @Arguments:
        - `top`: int

        @Return:
        None

        @Error:
        """
        self.set_y(top)

    def get_left(self):
        """get_left

        @Return:
        XCoordinate
        """
        return self.x

    def set_left(self, left):
        """function set_left

        @Arguments:
        - `left`: int

        @Return:
        None
        """
        self.set_x(left)

    def get_right(self):
        """get_right

        @Return:
        XCoordinate
        """
        return self.x + self.width - 1

    def set_right(self, right):
        """set_right

        @Arguments:
        - `right`:

        @Return:
        None
        """
        self.set_width(right - self.x + 1)

    def get_bottom(self):
        """get_bottom

        @Return:
        YCoordinate
        """
        return self.y + self.height - 1

    def set_bottom(self, y):
        """function set_bottom

        @Arguments:
        - `y`:

        @Return:
        None
        """
        self.set_height(y - self.y + 1)

    top = property(get_top, set_top)
    bottom = property(get_bottom, set_bottom)
    left = property(get_left, set_left)
    right = property(get_right, set_right)

    def get_top_left(self):
        """get_top_left

        @Return:
        Point
        """
        return self.location

    def set_top_left(self, value):
        """set_top_left

        @Arguments:
        - `value`:

        @Return:
        None
        """
        self.set_location(value)

    def get_bottom_right(self):
        """get_bottom_right

        @Return:
        Point
        """
        return point.Point(self.right, self.bottom)

    def set_bottom_right(self, value):
        """set_bottom_right

        @Arguments:
        - `value`: tuple

        @Return:
        None
        """
        self.set_right(value[0])
        self.set_bottom(value[1])

    def get_bottom_left(self):
        """get_bottom_left

        @Return:
        Point
        """
        return point.Point(self.x, self.bottom)

    def set_bottom_left(self, value):
        """set_bottom_left

        @Arguments:
        - `value`:

        @Return:
        None
        """
        self.set_left(value[0])
        self.set_bottom(value[1])

    def get_top_right(self, ):
        """get_top_right

        @Return:
        Point
        """
        return point.Point(self.right, self.top)

    def set_top_right(self, value):
        """set_top_right

        @Arguments:
        - `value`: Point

        @Return:
        None
        """
        self.set_right(value[0])
        self.set_top(value[1])

    def __nonzero__(self):
        return not self.isempty()

    def __str__(self):
        return str(tuple((int(x) for x in self.get_bounds())))

    def __repr__(self):
        return ('{0.__class__.__name__}(x={1}, y={2}, width={3}, height={4})'
                .format(self, int(self.x), int(self.y),
                        int(self.width), int(self.height)))

    def __len__(self):
        return len(self.get_bounds())

    def __getitem__(self, index):
        if 0 == index:
            return self.x
        elif 1 == index:
            return self.y
        elif 2 == index:
            return self.width
        elif 3 == index:
            return self.height
        else:
            raise IndexError()

    def __setitem__(self, index, val):
        if 0 == index:
            self.set_x(val)
        elif 1 == index:
            self.set_y(val)
        elif 2 == index:
            self.set_width(val)
        elif 3 == index:
            self.set_height(val)
        else:
            raise IndexError()

    @dispatch.generic()
    def __add__(self, other):
        """__add__

        other:

        returns Rectangle
        """

    @__add__.when('isinstance(other, (tuple, list)) and len(other) == 4')
    def __add__list(self, other):
        x1 = min(self.x, other[0])
        y1 = min(self.y, other[1])
        y2 = max(self.y + self.height, other[3] + other[1])
        x2 = max(self.x + self.width, other[2] + other[0])
        return self.__class__(x1, y1, x2 - x1, y2 - y1)

    @__add__.when('isinstance(other, (self.__class__, ))')
    def __add__rectangle(self, other):
        return self.__add__(other.get_bounds())

    def __iadd__(self, other):
        """__iadd__

        other:

        returns Rectangle
        """
        rect = self + other
        self.set_bounds(rect.get_bounds())
        return self

    @dispatch.generic()
    def __eq__(self, other):
        """__eq__

        other:

        returns bool
        """

    @__eq__.when('isinstance(other, (tuple, list)) and len(other) == 4')
    def __eq__list(self, other):
        return ((self.x == other[0]) and
                (self.y == other[1]) and
                (self.width == other[2]) and
                (self.height == other[3]))

    @__eq__.when('isinstance(other, (self.__class__, ))')
    def __eq__rectangle(self, other):
        return self.__eq__(other.get_bounds())

    def __ne__(self, other):
        return not self == other


    @dispatch.generic()
    def __contains__(self, value):
        """__contains__

        rect: Rectangle

        returns bool
        """

    @__contains__.when('isinstance(value, (tuple, list)) and len(value) == 2')
    def __contains__(self, value):
        return ((value[0] >= self.x) and
                (value[1] >= self.y) and
                ((value[1] - self.y) < self.height) and
                ((value[0] - self.x) < self.width))

    @__contains__.when('isinstance(value, (tuple, list)) and len(value) == 4')
    def __contains__(self, value):
        return self.__class__(value[0], value[1], value[2], value[3]) in self

    @__contains__.when('isinstance(value, (self.__class__, ))')
    def __contains__(self, value):
        topleft = value.get_top_left()
        bottomright = value.get_bottom_right()
        return ((topleft.get_x(), topleft.get_y()) in self and
                (bottomright.get_x(), bottomright.get_y()) in self)

    @__contains__.when('isinstance(value, (point.Point, ))')
    def __contains__(self, value):
        return (value.get_x(), value.get_y()) in self



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# rectangle.py ends here
