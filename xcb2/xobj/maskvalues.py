#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: maskvalues.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""maskvalues -- DESCRIPTION

"""
from xcb2.xproto.define import ConfigWindow
from xcb2.xproto.define import StackMode


# class MaskValuesAbstract(object):
#     r"""SUMMARY
#     """
#     static_keys = ()


#     def __init__(self, ):
#         r"""
#         """
#         self.data = dict()

#     def __setitem__(self, key, item):
#         if not key in self.static_keys:
#             # TODO: (Atami) [2014/05/21]
#             raise StandardError()
#         self.data.__setitem__(key, item)


class MaskValuesDictAbstract(dict):
    r"""SUMMARY
    """
    static_keys = ()

    def __setitem__(self, key, item):
        if not key in self.static_keys:
            # TODO: (Atami) [2014/05/21]
            raise StandardError()
        if not isinstance(item, int):
            # TODO: (Atami) [2014/05/21]
            raise StandardError()
        super(MaskValuesDictAbstract, self).__setitem__(key, item)

    def get_maskvalues(self, ):
        r"""SUMMARY

        get_mask_values()

        @Return:
        """
        mask, value = 0, []
        for msk, val in self.iteritems():
            mask |= msk
            value.append(val)
        return mask, value

    def get_mask(self, ):
        r"""SUMMARY

        get_mask()

        @Return:
        """
        mask = 0
        for msk in self.iterkeys():
            mask |= msk
        return mask

    def get_values(self, ):
        r"""SUMMARY

        get_values()

        @Return:
        """
        value = []
        for val in self.itervalues():
            value.append(val)
        return value


class ConfigWindowMaskValuesDict(MaskValuesDictAbstract):
    r"""SUMMARY
    """
    static_keys = tuple(ConfigWindow)


class ConfigWindowMaskValues(object):
    r"""SUMMARY
    """

    def __init__(self, *dic, **kwargs):
        r"""

        @Arguments:
        - `dic`:
        - `kwargs`:
        """
        self._data = ConfigWindowMaskValuesDict()
        if dic:
            self._data.update(dic)
        if kwargs:
            self._data.update(dic)

    def clear(self, ):
        r"""SUMMARY

        clear()

        @Return:
        """
        self._data.clear()

    def get_maskvalues(self, ):
        r"""SUMMARY

        get_maskvalues()

        @Return:
        """
        return self._data.get_maskvalues()

    def get_mask(self, ):
        r"""SUMMARY

        get_mask()

        @Return:
        """
        return self._data.get_mask()

    def get_values(self, ):
        r"""SUMMARY

        get_values()

        @Return:
        """
        return self._data.get_values()

    def get_x(self, ):
        r"""SUMMARY

        get_x()

        @Return:
        """
        if not ConfigWindow.X in self._data:
            return None
        return self._data[ConfigWindow.X]

    def set_x(self, value):
        r"""SUMMARY

        set_x(value)

        @Arguments:
        - `value`:

        @Return:
        """
        self._data[ConfigWindow.X] = value

    def reset_x(self, ):
        r"""SUMMARY

        reset_x()

        @Return:
        """
        del self._data[ConfigWindow.X]

    def get_y(self, ):
        r"""SUMMARY

        get_y()

        @Return:
        """
        if not ConfigWindow.Y in self._data:
            return None
        return self._data[ConfigWindow.Y]

    def set_y(self, value):
        r"""SUMMARY

        set_y(value)

        @Arguments:
        - [yas] elisp error!:

        @Return:
        """
        self._data[ConfigWindow.Y] = value

    def reset_y(self, ):
        r"""SUMMARY

        reset_y()

        @Return:
        """
        del self._data[ConfigWindow.Y]

    def get_width(self, ):
        r"""SUMMARY

        get_width()

        @Return:
        """
        if not ConfigWindow.Width in self._data:
            return None
        return self._data[ConfigWindow.Width]

    def set_width(self, value):
        r"""SUMMARY

        set_width(value)

        @Arguments:
        - [yas] elisp error!:

        @Return:
        """
        self._data[ConfigWindow.Width] = value

    def reset_width(self, ):
        r"""SUMMARY

        reset_width()

        @Return:
        """
        del self._data[ConfigWindow.Width]

    def get_height(self, ):
        r"""SUMMARY

        get_height()

        @Return:
        """
        if not ConfigWindow.Height in self._data:
            return None
        return self._data[ConfigWindow.Height]

    def set_height(self, value):
        r"""SUMMARY

        set_height(value)

        @Arguments:
        - [yas] elisp error!:

        @Return:
        """
        self._data[ConfigWindow.Height] = value

    def reset_height(self, ):
        r"""SUMMARY

        reset_height()

        @Return:
        """
        del self._data[ConfigWindow.Height]

    def get_borderwidth(self, ):
        r"""SUMMARY

        get_borderwidth()

        @Return:
        """
        if not ConfigWindow.BorderWidth in self._data:
            return None
        return self._data[ConfigWindow.BorderWidth]

    def set_borderwidth(self, value):
        r"""SUMMARY

        set_borderwidth(value)

        @Arguments:
        - [yas] elisp error!:

        @Return:
        """
        self._data[ConfigWindow.BorderWidth] = value

    def reset_borderwidth(self, ):
        r"""SUMMARY

        reset_borderwidth()

        @Return:
        """
        del self._data[ConfigWindow.BorderWidth]

    def get_sibling(self, ):
        r"""SUMMARY

        get_sibling()

        @Return:
        """
        if not ConfigWindow.Sibling in self._data:
            return None
        return self._data[ConfigWindow.Sibling]

    def set_sibling(self, value):
        r"""SUMMARY

        set_sibling(value)

        @Arguments:
        - [yas] elisp error!:

        @Return:
        """
        self._data[ConfigWindow.Sibling] = value

    def reset_sibling(self, ):
        r"""SUMMARY

        reset_sibling()

        @Return:
        """
        del self._data[ConfigWindow.Sibling]

    def get_stackmode(self, ):
        r"""SUMMARY

        get_stackmode()

        @Return:
        """
        if not ConfigWindow.StackMode in self._data:
            return None
        return self._data[ConfigWindow.StackMode]

    def set_stackmode(self, value):
        r"""SUMMARY

        set_stackmode(value)

        @Arguments:
        - [yas] elisp error!:

        @Return:
        """
        if not value in list(StackMode):
            raise StandardError()
        self._data[ConfigWindow.StackMode] = value

    def reset_stackmode(self, ):
        r"""SUMMARY

        reset_stackmode()

        @Return:
        """
        del self._data[ConfigWindow.StackMode]



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# maskvalues.py ends here
