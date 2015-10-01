#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: geometry.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""geometry -- DESCRIPTION

"""
from struct import pack as _pack
from xcb2.xobj.bitmask import BitConfigWindow


class GeometryAbstract(object):
    r"""SUMMARY
    """
    fmt = 'I'
    key = ''

    def __init__(self, connection, data, window):
        r"""

        @Arguments:
        - `connection`:
        - `data`:
        """
        self.connection = connection
        self._data = data
        self._window = window

    def pack(self, ):
        r"""SUMMARY

        pack()

        @Return:
        """
        return _pack(self.fmt, self._data)

    def __int__(self, ):
        return int(self._data)

    def __hash__(self, ):
        return hash(self._data)

    def __nonzero__(self, ):
        return self._data is not None

    def __repr__(self, ):
        return '{0.__class__.__name__}({0._data})'.format(self)

    def __lt__(self, other):
        return self._data < other

    def __le__(self, other):
        return self._data <= other

    def __gt__(self, other):
        return self._data > other

    def __ge__(self, other):
        return self._data >= other

    def __eq__(self, other):
        return self._data == other

    def __ne__(self, other):
        return self._data != other

    def __add__(self, other):
        self._data = self._data + other
        self.move()

    def __iadd__(self, other):
        self._data += other
        self.move()

    def __sub__(self, other):
        self._data = self._data - other
        self.move()

    def __isub__(self, other):
        self._data -= other
        self.move()

    def __mul__(self, other):
        self._data = self._data * other
        self.move()

    def __imul__(self, other):
        self._data *= other
        self.move()

    def __div__(self, other):
        self._data = self._data / other
        self.move()

    def __idiv__(self, other):
        self._data /= other
        self.move()

    def __pow__(self, other):
        self._data = self._data ** other
        self.move()

    def __ipow__(self, other):
        self._data **= other
        self.move()

    def __mod__(self, other):
        # TODO: (Atami) [2014/05/04]
        raise NotImplementedError()

    def __divmod__(self, other):
        # TODO: (Atami) [2014/05/04]
        raise NotImplementedError()

    def __and__(self, other):
        # TODO: (Atami) [2014/05/04]
        raise NotImplementedError()

    def __xor__(self, other):
        # TODO: (Atami) [2014/05/04]
        raise NotImplementedError()

    def __or__(self, other):
        # TODO: (Atami) [2014/05/04]
        raise NotImplementedError()

    def __lshift__(self, other):
        # TODO: (Atami) [2014/05/04]
        raise NotImplementedError()

    def __rshift__(self, other):
        # TODO: (Atami) [2014/05/04]
        raise NotImplementedError()

    def __imod__(self, other):
        # TODO: (Atami) [2014/05/04]
        raise NotImplementedError()

    def __ifloormod__(self, other):
        # TODO: (Atami) [2014/05/04]
        raise NotImplementedError()

    def __iand__(self, other):
        # TODO: (Atami) [2014/05/04]
        raise NotImplementedError()

    def __ixor__(self, other):
        # TODO: (Atami) [2014/05/04]
        raise NotImplementedError()

    def __ior__(self, other):
        # TODO: (Atami) [2014/05/04]
        raise NotImplementedError()

    def __ilshift__(self, other):
        # TODO: (Atami) [2014/05/04]
        raise NotImplementedError()

    def __irshift__(self, other):
        # TODO: (Atami) [2014/05/04]
        raise NotImplementedError()

    def __neg__(self, other):
        # TODO: (Atami) [2014/05/04]
        raise NotImplementedError()

    def __pos__(self, other):
        # TODO: (Atami) [2014/05/04]
        raise NotImplementedError()

    def move(self, ):
        r"""SUMMARY

        move()

        @Return:
        """
        geo = WindowGeometry(self.connection,
                             GeometryInfo(**{self.key: self._data,}),
                             self._window)
        geo.move()


class GeometryX(GeometryAbstract):
    r"""SUMMARY
    """
    key = 'x'


class GeometryY(GeometryAbstract):
    r"""SUMMARY
    """
    key = 'y'


class GeometryWidth(GeometryAbstract):
    r"""SUMMARY
    """
    key = 'width'


class GeometryHeight(GeometryAbstract):
    r"""SUMMARY
    """
    key = 'height'


class GeometryInfo(object):
    r"""SUMMARY
    """
    __slots__ = ('depth', 'root', 'x', 'y', 'width', 'height', 'border_width')

    def __init__(self, depth=None, root=None, x=None, y=None,
                 width=None, height=None, border_width=None):
        r"""

        @Arguments:
        - `x`:
        - `y`:
        - `width`:
        - `height`:
        """
        self.depth = depth
        self.root = root
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.border_width = border_width


class Geometry(object):
    r"""SUMMARY
    """

    def __init__(self, connection, geometry=None):
        r"""

        @Arguments:
        - `x`:
        - `y`:
        - `width`:
        - `height`:
        """
        self.connection = connection
        self._geo = geometry or GeometryInfo()

    @property
    def depth(self, ):
        r"""SUMMARY

        depth()

        @Return:
        """
        return self._geo.depth

    @property
    def root(self, ):
        r"""SUMMARY

        root()

        @Return:
        """
        return self._geo.root

    @property
    def x(self, ):
        r"""SUMMARY

        x()

        @Return:
        """
        return self._geo.x

    @property
    def y(self, ):
        r"""SUMMARY

        y()

        @Return:
        """
        return self._geo.y

    @property
    def width(self, ):
        r"""SUMMARY

        width()

        @Return:
        """
        return self._geo.width

    @property
    def height(self, ):
        r"""SUMMARY

        height()

        @Return:
        """
        return self._geo.height

    @property
    def border_width(self, ):
        r"""SUMMARY

        border_width()

        @Return:
        """
        return self._geo.border_width

    def __setattr__(self, name, value):
        if hasattr(self, '_geo') and name in GeometryInfo.__slots__:
            setattr(self._geo, name, value)
        else:
            super(Geometry, self).__setattr__(name, value)

    def translate_coordinates(self, window):
        r"""SUMMARY

        translate_coordinates(window)

        @Arguments:
        - `window`:

        @Return:
        """
        reply = self.connection.core.TranslateCoordinates(
            window, self.root, self.x, self.y).reply()
        posx = reply.dst_x - (2 * int(self.x))
        posy = reply.dst_y - (2 * int(self.y))
        return Geometry(self.connection,
                        GeometryInfo(self.depth, self.root, posx, posy,
                                     self.width, self.height,
                                     self.border_width))

    def move(self, window):
        r"""SUMMARY

        move(window)

        @Arguments:
        - `window`:

        @Return:
        """
        mask, result_value = BitConfigWindow(), []
        for value, method in zip((self.x, self.y, self.width, self.height),
                                 (mask.set_x, mask.set_y,
                                  mask.set_width, mask.set_height)):
            if value is None:
                continue
            if isinstance(value, GeometryAbstract) and not value:
                continue
            method()
            result_value.append(value)
        if mask == 0:
            return
        self.connection.core.ConfigureWindow(window, mask, result_value)

    def flush(self, ):
        r"""SUMMARY

        flush_()

        @Return:
        """
        self.connection.flush()


class WindowGeometry(Geometry):
    r"""SUMMARY
    """

    def __init__(self, connection, geometry, window):
        r"""

        @Arguments:
        - `connection`:
        - `geometry`:
        - `window`:
        """
        Geometry.__init__(self, connection, geometry)
        self.window = window

    @property
    def x(self, ):
        r"""SUMMARY

        x()

        @Return:
        """
        if self._geo.x is None:
            return None
        return GeometryX(self.connection, self._geo.x, self.window)

    @property
    def y(self, ):
        r"""SUMMARY

        y()

        @Return:
        """
        if self._geo.y is None:
            return None
        return GeometryY(self.connection, self._geo.y, self.window)

    @property
    def width(self, ):
        r"""SUMMARY

        width()

        @Return:
        """
        if self._geo.width is None:
            return None
        return GeometryWidth(self.connection, self._geo.width, self.window)

    @property
    def height(self, ):
        r"""SUMMARY

        height()

        @Return:
        """
        if self._geo.height is None:
            return None
        return GeometryHeight(self.connection, self._geo.height, self.window)

    def translate_coordinates(self, ):
        r"""SUMMARY

        translate_coords()

        @Return:
        """
        geo = super(WindowGeometry, self).translate_coordinates(self.window)
        return self.__class__(self.connection, geo, self.window)

    def move(self, ):
        r"""SUMMARY

        move()

        @Return:
        """
        return super(WindowGeometry, self).move(self.window)

    def __repr__(self, ):
        return ('{0.__class__.__name__}(window={1}, x={2}, y={3}, width={4}, '
                'height={5}, depth={6}, border_width={7}, root={8})'
                .format(self, int(self.window), int(self.x), int(self.y),
                        int(self.width), int(self.height), int(self.depth),
                        int(self.border_width), int(self.root)))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# geometry.py ends here
