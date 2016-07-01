#!/usr/bin/env python
# -*- coding: utf-8 -*-
import enum
from dotavoider import ListDotAvoider

import predicate

from xahk.rectangle._point import Point
from xahk.rectangle._size import Size


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
    class Builder(object):
        """Builder

        Builder is a object.
        Responsibility:
        """
        def __init__(self, x=0, y=0, width=0, height=0):
            """

            @Arguments:
            - `args`:
            - `kwargs`:
            """
            self.x = x
            self.y = y
            self.width = width
            self.height = height

        def set_x(self, newx):
            """SUMMARY

            set_x(newx)

            @Arguments:
            - `newx`:

            @Return:

            @Error:
            """
            self.x = newx
            return self

        def set_y(self, newy):
            """SUMMARY

            set_y(newy)

            @Arguments:
            - `newy`:

            @Return:

            @Error:
            """
            self.y = newy
            return self

        def set_width(self, width):
            """SUMMARY

            set_width(width)

            @Arguments:
            - `width`:

            @Return:

            @Error:
            """
            self.width = width
            return self

        def set_height(self, height):
            """SUMMARY

            set_height(height)

            @Arguments:
            - `height`:

            @Return:

            @Error:
            """
            self.height = height
            return self

        def set_rectangle(self, rect):
            """SUMMARY

            set_rectangle(rect)

            @Arguments:
            - `rect`:

            @Return:

            @Error:
            """
            self.x = rect.x
            self.y = rect.y
            self.width = rect.width
            self.height = rect.height
            return self

        def build(self, ):
            """SUMMARY

            build()

            @Return:

            @Error:
            """
            return Rectangle(Point(self.x, self.y), Size(self.width, self.height))

    # Attributes:
    def __init__(self, point, size):
        """

        @Arguments:
        - `point`:
        - `size`:
        """
        self.point = point
        self.size = size

    def get_bounds(self):
        """get_bounds

        @Return:
        tuple
        """
        return tuple(self.point) + tuple(self.size)

    def set_bounds(self, rect):
        """SUMMARY

        set_bounds(rect)

        @Arguments:
        - `rect`:

        @Return:

        @Error:
        """
        self.point.set(rect.x, rect.y)
        self.size.set(rect.width, rect.height)

    def get_point(self, ):
        """SUMMARY

        get_point()

        @Return:

        @Error:
        """
        return self.point

    def set_point(self, point):
        """SUMMARY

        set_point(point)

        @Arguments:
        - `point`:

        @Return:

        @Error:
        """
        self.point.set(point.x, point.y)

    def get_x(self):
        """get_x

        @Return:
        XCoordinate
        """
        return self.point.get_x()

    def set_x(self, newx):
        """set_x

        @Arguments:
        - `newx`:

        @Return:
        None
        """
        self.point.set_x(newx)

    def get_y(self):
        """get_y

        @Return:
        YCoordinate
        """
        return self.point.get_y()

    def set_y(self, newy):
        """set_y

        @Arguments:
        - `newy`:

        @Return:
        None
        """
        self.point.set_y(newy)

    def get_size(self, ):
        """SUMMARY

        get_size()

        @Return:

        @Error:
        """
        return self.size

    def set_size(self, size):
        """SUMMARY

        set_size(size)

        @Arguments:
        - `size`:

        @Return:

        @Error:
        """
        self.size = size

    def get_width(self):
        """get_width

        @Return:
        Width
        """
        return self.size.get_width()

    def set_width(self, newwidth):
        """set_width

        @Arguments:
        - `newwidth`:

        @Return:
        None
        """
        self.size.set_width(newwidth)

    def get_height(self, ):
        """get_height

        @Return:
        Height
        """
        return self.size.get_height()

    def set_height(self, newheight):
        """set_height

        @Arguments:
        - `newheight`:

        @Return:
        None
        """
        self.size.set_height(newheight)

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
        self.set_bounds(self.__class__.Builder(newx, newy, neww, newh).build())

    def offset(self, point):
        """SUMMARY

        offset(point)

        @Arguments:
        - `point`:

        @Return:

        @Error:
        """
        self.point.set_x(self.point.x + point[0])
        self.point.set_y(self.point.y + point[1])

    def intersect(self, rect):
        r"""SUMMARY

        intersect(value)

        @Arguments:
        - `value`:

        @Return:
        Rectangle, None

        intersect(Rectangle(0, 0, 10, 10))
        intersect((0, 0, 10, 10))

                           intersects
                      +----   Width  ----+
                      |                  |

        +--------------------------------+
        |                                |
        |                                |
        |                                |
        |                                |
        |             +------------------+-------------+  -- +
        |             |..................|             |     |
        |             |..................|             |     |
        |             |..................|             |     |
        |             |..................|             |  intersects
        |             |..................|             |    height
        |             |..................|             |     |
        |             |..................|             |     |
        |             |..................|             |     |
        +-------------+------------------+             |  -- +
                      |                                |
                      |                                |
                      |                                |
                      |                                |
                      |                                |
                      +--------------------------------+

        """
        thisx, thisy, thisright, thisbottom = (
            self.x, self.y, self.right, self.bottom)
        otherx, othery, otherright, otherbottom = (
            rect.get_x(), rect.get_y(), rect.get_right(), rect.get_bottom())
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
        return self.__class__.Builder(thisx, thisy, width, height).build()

    def union(self, rect):
        r"""SUMMARY

        union(value)

        @Arguments:
        - `value`:

        @Return:
        Rectangle

        @Error:

        union((0, 0, 10, 10))
        union(Rectangle(0, 0, 10, 10))

        +---------------------- union.width ---------------------+
        |                                                        |
        |                                                        |

        +-------------------------------+------------------------+  --+
        |...............................|                        |    |
        |...............................|                        |    |
        |...............................|                        |    |
        |...............................|                        |    |
        |...............................|------------------------+    |
        |...............................|........................|    |
        |...............................|........................|    |
        |...............................|........................|    |
        |...............................|........................|    |
        |...............................|........................|  union
        |...............................|........................|  height
        +-------------------------------+........................|    |
        |             |..........................................|    |
        |             |..........................................|    |
        |             |..........................................|    |
        |             |..........................................|    |
        |             |..........................................|    |
        |             |..........................................|    |
        |             |..........................................|    |
        |             |..........................................|    |
        |             |..........................................|    |
        |             |..........................................|    |
        +-------------+------------------------------------------+  --+
        """
        thisw, thish = self.width, self.height
        if (thisw | thish) < 0:
            return self.__class__.Builder(rect[0], rect[1], rect[2], rect[3]).build()
        otherw, otherh = rect[2], rect[3]
        if (otherw | otherh) < 0:
            return self.__class__.Builder().set_rectangle(self).build()
        thisx, thisy = self.x, self.y
        otherx, othery = rect[0], rect[1]
        newx = min(thisx, otherx)
        newy = min(thisy, othery)
        neww = max(thisx + thisw, otherx + otherw) - newx
        newh = max(thisy + thish, othery + otherh) - newy
        return self.__class__.Builder(newx, newy, neww, newh).build()

    def centerin(self, rect, dir_=Orientation.both):
        """centerin

        rectangle:

        returns Rectangle

        """
        if dir_ & Orientation.horizontal:
            # cut off after the decimal point
            newx = rect[0] + int(int((rect[2] - self.width)) / 2.0)
        else:
            newx = self.x
        if dir_ & Orientation.vertical:
            # cut off after the decimal point
            newy = rect[1] + int(int((rect[3] - self.height)) / 2.0)
        else:
            newy = self.y
        return self.__class__.Builder(newx, newy, self.width, self.height).build()

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
        return self.point

    def set_top_left(self, value):
        """set_top_left

        @Arguments:
        - `value`:

        @Return:
        None
        """
        self.set_point(value)

    def get_bottom_right(self):
        """get_bottom_right

        @Return:
        Point
        """
        return Point(self.right, self.bottom)

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
        return Point(self.x, self.bottom)

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
        return Point(self.right, self.top)

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

    def __add__(self, other):
        if isinstance(other, (tuple, list)) and len(other) == 4:
            return self.__class__(
                self.point + other[0:2], self.size + other[2:4])
        if isinstance(other, (self.__class__, )):
            return self + other.get_bounds()
        if isinstance(other, (int, )):
            point = self.point + other
            size = self.size + other
            return self.__class__.Builder(point.x, point.y, size.width, size.height).build()
        raise TypeError()

    def __iadd__(self, other):
        rect = self + other
        self.set_bounds(rect)
        return self

    def __sub__(self, other):
        if isinstance(other, (tuple, list)) and len(other) == 4:
            return self.__class__(
                self.point - other[0:2], self.size - other[2:4])
        if isinstance(other, (self.__class__, )):
            return self - other.get_bounds() # recursive call
        if isinstance(other, (int, )):
            return self.__class__(self.point - other, self.size - other)
        raise TypeError()

    def __isub__(self, other):
        rect = self - other
        self.set_bounds(rect)
        return self

    def __mul__(self, other):
        if isinstance(other, (tuple, list)) and len(other) == 4:
            return self.__class__(
                self.point * other[0:2], self.size * other[2:4])
        if isinstance(other, (self.__class__, )):
            return self * other.get_bounds() # recursive call
        if isinstance(other, (int, )):
            return self.__class__(self.point * other, self.size * other)
        raise TypeError()

    def __imul__(self, other):
        rect = self * other
        self.set_bounds(rect)
        return self

    def __idiv__(self, other):
        if isinstance(other, (tuple, list)) and len(other) == 4:
            return self.__class__(
                self.point / other[0:2], self.size / other[2:4])
        if isinstance(other, (self.__class__, )):
            return self / other.get_bounds() # recursive call
        if isinstance(other, (int, )):
            return self.__class__(self.point / other, self.size / other)
        raise TypeError()

    def __imul__(self, other):
        rect = self / other
        self.set_bounds(rect)
        return self

    def __eq__(self, other):
        return ((self.x == other[0]) and
                (self.y == other[1]) and
                (self.width == other[2]) and
                (self.height == other[3]))

    def __ne__(self, other):
        return not self == other

    def __contains__(self, rect):
        return ((rect[0] >= self.x) and
                (rect[1] >= self.y) and
                ((rect[1] - self.y) < self.height) and
                ((rect[0] - self.x) < self.width))

    def split_vertical(self, rows):
        r"""SUMMARY

        split_vertical(num)

        @Arguments:
        - `num`:

        @Return:

        @Error:

        +--------------------+         +--------------------+
        |                    |         |                    |
        |                    |         |        row1        |
        |                    |         |                    |
        |                    |         +-------------------->
        |                    |         |                    |
        |                    |   ==>   |        row2        |
        |                    |         |                    |
        |                    |         +--------------------+
        |                    |         |                    |
        |                    |         |        row3        |
        |                    |         |                    |
        +--------------------+         +--------------------+
        """
        if rows <= 0:
            raise ValueError('num require integer than 0 (got {})'.format(rows))
        height = self.height / rows
        rects, append = ListDotAvoider().append
        append(self.__class__.Builder(self.x, self.y, self.width, height).build())
        newy = int(self.y)
        for _ in range(rows - 1):
            newy += height
            rects.append(self.__class__.Builder(self.x, newy, self.width, height).build())
        return rects

    def split_horizontal(self, columns):
        r"""SUMMARY

        split_horizontal(columns)

        @Arguments:
        - `num`:

        @Return:

        @Error:

        +---------------------------------------------+
        |                                             |
        |                                             |
        |                                             |
        |                                             |
        |                                             |
        +---------------------------------------------+

                             ||
                             \/

        +--------------+--------------+---------------+
        |              |              |               |
        |              |              |               |
        |     cols1    |     cols2    |     cols3     |
        |              |              |               |
        |              |              |               |
        +--------------+--------------+---------------+
        """
        if columns <= 0:
            raise ValueError(
                'num require integer than 0 (got {})'.format(columns))
        width = self.width / columns
        rects, append = ListDotAvoider().append
        append(self.__class__.Builder(self.x, self.y, width, self.height).build())
        newx = int(self.x)
        for _ in range(columns - 1):
            newx += width
            rects.append(self.__class__.Builder(newx, self.y, width, self.height).build())
        return rects

    def split_grid(self, rows, columns):
        r"""SUMMARY

        split_grid(rows, columns)

        @Arguments:
        - `rows`:
        - `columns`:

        @Return:

        @Error:

        +--------------------------------------------+
        |                                            |
        |                                            |
        |                                            |
        |                                            |
        |                                            |
        |                                            |
        |                                            |
        |                                            |
        |                                            |
        |                                            |
        |                                            |
        +--------------------------------------------+

                             ||
                             \/

        +--------------+--------------+--------------+ --+
        |              |              |              |   |
        |              |              |              |
        |    (0,0)     |     (0,1)    |     (0,2)    |  List[0]
        |              |              |              |
        |              |              |              |   |
        +--------------+--------------+--------------+ --+
        |              |              |              |   |
        |              |              |              |
        |    (1,0)     |     (1,1)    |     (1,2)    |  List[1]
        |              |              |              |
        |              |              |              |   |
        +--------------+--------------+--------------+ --+

        |              |              |              |
        +--- index1 ---+--- index2 ---+--- index3 ---+

        """
        return [r.split_horizontal(columns) for r in self.split_vertical(rows)]



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# rectangle.py ends here
