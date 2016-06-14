#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""vertical -- DESCRIPTION

"""
from collections import deque

from .layout_item import LayoutItem
from .resize import spacing_vertical


class VerticalLayout(LayoutItem):
    """VerticalLayout

    VerticalLayout is a LayoutItem.
    Responsibility:

    -----------------
    |               |
    |       1       |
    |               |
    |---------------|
    |               |
    |       2       |
    |               |
    |---------------|
    |               |
    |       3       |
    |               |
    |---------------|
    |               |
    |       4       |
    |               |
    -----------------
    """
    def __init__(self, border_width=1):
        """

        @Arguments:
        - `rectangle`:
        """
        self._layout_items = deque()
        self._border_width = border_width

    def appendleft(self, layout_item):
        """SUMMARY

        appendleft(layout_item)

        @Arguments:
        - `layout_item`:

        @Return:

        @Error:
        """
        self._layout_items.appendleft(layout_item)

    def append(self, layout_item):
        """SUMMARY

        append(layout_item)

        @Arguments:
        - `layout_item`:

        @Return:

        @Error:
        """
        self._layout_items.append(layout_item)

    def pop(self, ):
        """SUMMARY

        pop()

        @Return:

        @Error:
        """
        return self._layout_items.pop()

    def popleft(self, ):
        """SUMMARY

        popleft()

        @Return:

        @Error:
        """
        return self._layout_items.popleft()

    def remove(self, layout_item):
        """SUMMARY

        remove_client(layout_item)

        @Arguments:
        - `client`:

        @Return:

        @Error:
        """
        self._layout_items.remove(layout_item)

    def clear(self, ):
        """SUMMARY

        clear()

        @Return:

        @Error:
        """
        self._layout_items.clear()

    def index_layout_item(self, layout_item):
        """SUMMARY

        index_layout_item(layout_item)

        @Arguments:
        - `layout_item`:

        @Return:

        @Error:
        """
        return list(self._layout_items).index(layout_item)

    def get_border_width(self, ):
        """SUMMARY

        get_border_width()

        @Return:

        @Error:
        """
        return self._border_width

    def set_border_width(self, border_width):
        """SUMMARY

        set_border_width(border_width)

        @Arguments:
        - `border_width`:

        @Return:

        @Error:
        """
        self._border_width = border_width

    border_width = property(get_border_width, set_border_width)

    def layout(self, rect):
        """SUMMARY

        layout()

        @Return:

        @Error:
        """
        rects = rect.split_vertical(len(self._layout_items))
        rects = spacing_vertical(rects, self.border_width)
        for rct, client in zip(rects, self._layout_items):
            client.layout(rct)

    def __getitem__(self, num):
        return self._layout_items[num]

    def __setitem__(self, num, layout_item):
        self._layout_items[num] = layout_item

    def __iter__(self):
        return iter(self._layout_items)

    def __len__(self):
        return len(self._layout_items)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# vertical.py ends here
