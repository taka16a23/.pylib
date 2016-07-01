#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Size(object):
    """Class Size
    """
    # Attributes:
    def __init__(self, width=0, height=0):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:

        @Construct
        Size()
        Size(width=100, height=100)
        """
        self.width = width
        self.height = height

    # Operations
    def get(self):
        """function get

        @return: tuple(Width, Height)
        """
        return (self.width, self.height)

    def set(self, size):
        """function set

        @return: None

        set(Size())
        """
        if isinstance(size, (tuple, list, Size)):
            self.set_width(size[0])
            self.set_height(size[1])
        else:
            # TODO: (Atami) [2015/02/17]
            raise TypeError()

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
        self.width = width

    def del_width(self, ):
        r"""SUMMARY

        del_width()

        @Return:

        @Error:
        """
        self.width = 0

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
        self.height = height

    def del_height(self, ):
        r"""SUMMARY

        del_height()

        @Return:

        @Error:
        """
        self.height = 0

    def __str__(self):
        return str((int(self.width), int(self.height)))

    def __repr__(self):
        return ('{0.__class__.__name__}(width={0.width}, height={0.height})'
                .format(self))

    def __len__(self):
        return len(self.get())

    def __nonzero__(self):
        return not (self.width == 0 and self.height == 0)

    def __eq__(self, other):
        return (self.width, self.height) == other

    def __ne__(self, other):
        return not self == other

    # def __add__(self, other):
    #     if isinstance(other, (Width, )):
    #         return self.__class__(self.width + other, self.height)
    #     if isinstance(other, (Height, )):
    #         return self.__class__(self.width, self.height + other)
    #     if isinstance(other, (int, )):
    #         return self.__class__(self.width + other, self.height + other)
    #     return self.__class__(self.width + other[0], self.height + other[1])

    # def __iadd__(self, other):
    #     size = self + other
    #     self.width = size.get_width()
    #     self.height = size.get_height()
    #     return self

    # def __sub__(self, other):
    #     if isinstance(other, (Width, )):
    #         return self.__class__(self.width - other, self.height)
    #     if isinstance(other, (Height, )):
    #         return self.__class__(self.width, self.height - other)
    #     if isinstance(other, (int, )):
    #         return self.__class__(self.width - other, self.height - other)
    #     return self.__class__(self.width - other[0], self.height - other[1])

    # def __isub__(self, other):
    #     size = self - other
    #     self.width = size.get_width()
    #     self.height = size.get_height()
    #     return self

    # def __mul__(self, other):
    #     if isinstance(other, (Width, )):
    #         return self.__class__(self.width * other, self.height)
    #     if isinstance(other, (Height, )):
    #         return self.__class__(self.width, self.height * other)
    #     if isinstance(other, (int, )):
    #         return self.__class__(self.width * other, self.height * other)
    #     return self.__class__(self.width * other[0], self.height * other[1])

    # def __imul__(self, other):
    #     size = self * other
    #     self.width = size.get_width()
    #     self.height = size.get_height()
    #     return self

    # def __div__(self, other):
    #     if isinstance(other, (Width, )):
    #         return self.__class__(self.width / other, self.height)
    #     if isinstance(other, (Height, )):
    #         return self.__class__(self.width, self.height / other)
    #     if isinstance(other, (int, )):
    #         return self.__class__(self.width / other, self.height / other)
    #     return self.__class__(self.width / other[0], self.height / other[1])

    # def __idiv__(self, other):
    #     size = self / other
    #     self.width = size.get_width()
    #     self.height = size.get_height()
    #     return self

    def __iter__(self):
        return iter(self.get())

    def __getitem__(self, index):
        return self.get()[index]

    def __setitem__(self, index, val):
        self[index].set(val)

    def __delitem__(self, index):
        if 0 == index:
            self.width = 0
        elif 1 == index:
            self.height = 0
        else:
            raise TypeError()

    # def __del__(self):
    #     self.width, self.height = 0, 0



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# size.py ends here
