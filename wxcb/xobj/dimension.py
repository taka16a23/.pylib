#!/usr/bin/env python
# -*- coding: utf-8 -*-
import side


class Dimension(object):
    """Class Dimension
    """
    # Attributes:
    def __init__(self, *args, **kwargs):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:

        @Construct
        Dimension()
        Dimension(100)
        Dimension(100, 100)
        Dimension(100, height=100)
        Dimension(height=100)
        Dimension(width=100, height=100)
        """
        self.width = side.Width()
        self.height = side.Height()
        self.set(*args, **kwargs)

    # Operations
    def get_height(self):
        """function get_height

        returns Height
        """
        return self.height

    def set_height(self, height):
        """function set_height

        height:

        returns
        """
        self.height.set(height)

    def get_width(self):
        """function get_width

        returns Width
        """
        return self.width

    def set_width(self, width):
        """function set_width

        width:

        returns
        """
        self.width.set(width)

    def set(self, *args, **kwargs):
        """function set

        @return: None

        set(Dimension())
        set(width=100, height=100)
        set(100, height=100)
        set(height=100)
        set(100)
        set(100, 100)
        """
        arglen = len(args) + len(kwargs)
        if 2 < arglen:
            raise TypeError('{} take at most 2 arguments ({} given)'
                            .format(self.__class__.__name__, arglen))
        # parse kwargs
        width, height = kwargs.get('width', None), kwargs.get('height', None)
        size = kwargs.get('size', None)
        # parse args
        arguments = []
        for arg in args:
            if isinstance(arg, (self.__class__, )):
                if size is not None:
                    raise TypeError(
                        '{0.__class__.__name__} duplicated in args and kwargs'
                        .format(self))
                size = arg
            else:
                arguments.append(arg)
        while 2 != len(arguments):
            arguments.append(None)
        for val1, val2 in zip((width, height), arguments):
            if val1 is not None and val2 is not None:
                raise TypeError('duplicate parameter {}, {}'.format(val1, val2))
        width, height = width or arguments[0], height or arguments[1]
        if size is not None and (width is not None or height is not None):
            raise TypeError('Exclusive size and width, height')
        if size is not None:
            self.set_width(size.get_width())
            self.set_height(size.get_height())
        if width is not None:
            self.set_width(width)
        if height is not None:
            self.set_height(height)

    def get(self):
        """function get

        @return: tuple(Width, Height)
        """
        return (self.width, self.height)

    def __str__(self):
        """function __str__

        returns
        """
        return str((int(self.width), int(self.height)))

    def __repr__(self):
        """function __repr__

        returns
        """
        return ('{0.__class__.__name__}(width={0.width}, height={0.height})'
                .format(self))

    def __len__(self):
        """function __len__

        returns
        """
        return len(self.get())

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
        return not (self.width == 0 and self.height == 0)

    def __eq__(self, other):
        """function __eq__

        other:

        returns
        """
        return ((int(self.width), int(self.height)) ==
                (int(other[0]), int(other[1])))

    def __ne__(self, other):
        """function __ne__

        other:

        returns
        """
        return not self == other

    def __add__(self, other):
        """function __add__

        other:

        returns
        """
        return self.__class__(self.width + other[0], self.height + other[1])

    def __sub__(self, other):
        """function __sub__

        other:

        returns
        """
        return self.__class__(self.width - other[0], self.height - other[1])

    def __iadd__(self, other):
        self.width += other[0]
        self.height += other[1]
        return self

    def __isub__(self, other):
        self.width -= other[0]
        self.height -= other[1]
        return self

    def __iter__(self):
        return iter(self.get())

    def __delitem__(self, index):
        self.get()[index].set(0)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# size.py ends here
