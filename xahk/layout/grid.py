#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""grid -- DESCRIPTION

"""
from xahk.layout.layout_item import LayoutItem
from xahk.layout.resize import spacing_horizon, spacing_vertical


class GridSpec(object):
    r"""GridSpec

    GridSpec is a object.
    Responsibility:
    """
    def __init__(self, start, size):
        """

        @Arguments:
        - `start`:
        - `size`:
        """
        self._start = start
        self._size = size

    @classmethod
    def create(cls, start=0):
        """SUMMARY

        create(start)

        @Arguments:
        - `start`:

        @Return:

        @Error:
        """
        return cls(start, start)

    @classmethod
    def create_with_size(cls, start, size):
        """SUMMARY

        create_with_size(start, size)

        @Arguments:
        - `start`:
        - `size`:

        @Return:

        @Error:
        """
        return cls(start, start + size)

    def get_start(self, ):
        """SUMMARY

        get_start()

        @Return:

        @Error:
        """
        return self._start

    def set_start(self, start):
        """SUMMARY

        set_start(start)

        @Arguments:
        - `start`:

        @Return:

        @Error:
        """
        self._start = start

    start = property(get_start, set_start)

    def get_size(self, ):
        """SUMMARY

        get_size()

        @Return:

        @Error:
        """
        return self._size

    def set_size(self, size):
        """SUMMARY

        set_size(size)

        @Arguments:
        - `size`:

        @Return:

        @Error:
        """
        self._size = size

    size = property(get_size, set_size)

    def get_span(self, ):
        """SUMMARY

        get_span()

        @Return:

        @Error:
        """
        return [self.start, self.size]

    def set_span(self, start, size):
        """SUMMARY

        set_span(start, size)

        @Arguments:
        - `start`:
        - `size`:

        @Return:

        @Error:
        """
        self.set_start(start)
        self.set_size(size)

    span = property(get_span, set_span)

    def __getitem__(self, index):
        if index == 0:
            return self.start
        elif index == 1:
            return self.size
        else:
            # TODO: (Atami) [2015/07/29]
            raise IndexError('index range 0 to 1 (got {})'.format(index))

    def __setitem__(self, index, val):
        if index == 0:
            self.start = val
        elif index == 1:
            self.size = val
        else:
            # TODO: (Atami) [2015/07/29]
            raise IndexError('index range 0 to 1 (got {})'.format(index))

    def __eq__(self, other):
        if isinstance(other, (GridSpec, )):
            return self.span == other.span
        return self.span == other

    def __ne__(self, other):
        return not self == other


class LayoutParams(object):
    """LayoutParams

    LayoutParams is a object.
    Responsibility:
    """
    def __init__(self, rowspec, colspec, left=0, top=0, right=0, bottom=0):
        """
        """
        self._row_spec = rowspec
        self._column_spec = colspec
        self._left_margin = left
        self._top_margin = top
        self._right_margin = right
        self._bottom_margin = bottom

    def get_row_spec(self, ):
        """SUMMARY

        get_row_spec()

        @Return:

        @Error:
        """
        return self._row_spec

    def set_row_spec(self, row_spec):
        """SUMMARY

        set_row_spec(row_spec)

        @Arguments:
        - `row_spec`:

        @Return:

        @Error:
        """
        self._row_spec = row_spec

    row_spec = property(get_row_spec, set_row_spec)

    def get_column_spec(self, ):
        """SUMMARY

        get_column_spec()

        @Return:

        @Error:
        """
        return self._column_spec

    def set_column_spec(self, col_spec):
        """SUMMARY

        set_column_spec(col_spec)

        @Arguments:
        - `col_spec`:

        @Return:

        @Error:
        """
        self._column_spec = col_spec

    column_spec = property(get_column_spec, set_column_spec)

    def get_left_margin(self, ):
        """SUMMARY

        get_left_margin()

        @Return:

        @Error:
        """
        return self._left_margin

    def set_left_margin(self, left):
        """SUMMARY

        set_left_margin(left)

        @Arguments:
        - `left`:

        @Return:

        @Error:
        """
        self._left_margin = left

    left = property(get_left_margin, set_left_margin)

    def get_top_margin(self, ):
        """SUMMARY

        get_top_margin()

        @Return:

        @Error:
        """
        return self._top_margin

    def set_top_margin(self, top):
        """SUMMARY

        set_top_margin(top)

        @Arguments:
        - `top`:

        @Return:

        @Error:
        """
        self._top_margin = top

    top = property(get_top_margin, set_top_margin)

    def get_right_margin(self, ):
        """SUMMARY

        get_right_margin()

        @Return:

        @Error:
        """
        return self._right_margin

    def set_right_margin(self, right):
        """SUMMARY

        set_right_margin(right)

        @Arguments:
        - `right`:

        @Return:

        @Error:
        """
        self._right_margin = right

    right = property(get_right_margin, set_right_margin)

    def get_bottom_margin(self, ):
        """SUMMARY

        get_bottom()

        @Return:

        @Error:
        """
        return self._bottom_margin

    def set_bottom_margin(self, bottom):
        """SUMMARY

        set_bottom_margin(bottom)

        @Arguments:
        - `bottom`:

        @Return:

        @Error:
        """
        self._bottom_margin = bottom

    bottom = property(get_bottom_margin, set_bottom_margin)

    def __eq__(self, other):
        if not isinstance(other, (GridLayout, )):
            return False
        if self.row_spec != other.row_spec:
            return False
        if self.column_spec != other.column_spec:
            return False
        return True

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return ((self.row_spec.span[0], self.column_spec.span[0]) <
                (other.row_spec.span[0], other.column_spec.span[0]))

    def __le__(self, other):
        return ((self.row_spec.span[0], self.column_spec.span[0]) <=
                (other.row_spec.span[0], other.column_spec.span[0]))

    def __gt__(self, other):
        return ((self.row_spec.span[0], self.column_spec.span[0]) >
                (other.row_spec.span[0], other.column_spec.span[0]))

    def __ge__(self, other):
        return ((self.row_spec.span[0], self.column_spec.span[0]) >=
                (other.row_spec.span[0], other.column_spec.span[0]))

    def __hash__(self):
        return hash((self.row_spec.span[0], self.column_spec.span[0]))


class GridLayout(LayoutItem):
    """GridLayout

    GridLayout is a LayoutItem.
    Responsibility:

            0     1     2     3
         +-----+-----+-----+-----+
         |     |     |     |     |
      0  | 0,0 | 0,1 | 0,2 | 0,3 |
         |     |     |     |     |
         +-----+-----+-----+-----+
         |     |     |     |     |
      1  | 1,0 | 1,1 | 1,2 | 1,3 |
         |     |     |     |     |
         +-----+-----+-----+-----+
         |     |     |     |     |
      2  | 2,0 | 2,1 | 2,2 | 2,3 |
         |     |     |     |     |
         +-----+-----+-----+-----+
    """
    def __init__(self, wspace=0, hspace=0):
        """

        @Arguments:
        - `rectangle`:
        - `rows`:
        - `cols`:
        """
        self._table = {}
        self._rows = 0
        self._columns = 0
        self._wspace = wspace
        self._hspace = hspace

    def get_rows(self, ):
        """SUMMARY

        get_rows()

        @Return:

        @Error:
        """
        return self._rows

    def set_rows(self, rows):
        """SUMMARY

        set_rows(rows)

        @Arguments:
        - `rows`:

        @Return:

        @Error:
        """
        self._rows = rows

    rows = property(get_rows, set_rows)

    def get_columns(self, ):
        """SUMMARY

        get_columns()

        @Return:

        @Error:
        """
        return self._columns

    def set_columns(self, cols):
        """SUMMARY

        set_columns(cols)

        @Arguments:
        - `cols`:

        @Return:

        @Error:
        """
        self._columns = cols

    columns = property(get_columns, set_columns)

    def get_layout_item(self, layoutparams):
        """SUMMARY

        get_layout_item(layoutparams)

        @Arguments:

        @Return:

        @Error:
        """
        return self._table[layoutparams]

    def set_layout_item(self, item, layoutparams):
        """SUMMARY

        set_layout_item(item, layoutparams)

        @Arguments:

        @Return:

        @Error:
        """
        self._table[layoutparams] = item
        self.set_rows(max(self._rows, layoutparams.get_row_spec().span[1] + 1))
        self.set_columns(
            max(self._columns, layoutparams.get_column_spec().span[1] + 1))

    def remove_layout_item(self, layoutparams):
        """SUMMARY

        remove_layout_item(layoutparams)

        @Arguments:
        - `rows`:
        - `cols`:

        @Return:

        @Error:
        """
        del self._table[layoutparams]

    def get_wspace(self, ):
        """SUMMARY

        get_wspace()

        @Return:

        @Error:
        """
        return self._wspace

    def set_wspace(self, wspace):
        """SUMMARY

        set_wspace(wspace)

        @Arguments:
        - `wspace`:

        @Return:

        @Error:
        """
        self._wspace = wspace

    wspace = property(get_wspace, set_wspace)

    def get_hspace(self, ):
        """SUMMARY

        get_hspace()

        @Return:

        @Error:
        """
        return self._hspace

    def set_hspace(self, hspace):
        """SUMMARY

        set_hspace(hspace)

        @Arguments:
        - `hspace`:

        @Return:

        @Error:
        """
        self._hspace = hspace

    hspace = property(get_hspace, set_hspace)

    def clear(self, ):
        """SUMMARY

        clear()

        @Return:

        @Error:
        """
        self._table.clear()

    def layout(self, rect):
        """SUMMARY

        layout()

        @Return:

        @Error:
        """
        rtable = rect.split_grid(self.rows, self.columns)
        for rects in rtable:
            spacing_horizon(rects, self._wspace)
        for rects in zip(*rtable):
            spacing_vertical(rects, self._hspace)

        cookies = []
        extend = cookies.extend
        for param, layout in self._table.items():
            row_span = param.get_row_spec().span
            col_span = param.get_column_spec().span
            rect = rtable[row_span[0]][col_span[0]]
            rect_span = rtable[row_span[1]][col_span[1]]
            newrect = rect.union(rect_span)
            newrect.set_x(newrect.get_x() + param.get_left_margin())
            newrect.set_y(newrect.get_y() + param.get_top_margin())
            newrect.set_width(newrect.get_width() + param.get_right_margin())
            newrect.set_height(newrect.get_height() + param.get_bottom_margin())
            extend(layout.layout(newrect))
        return cookies


class GridLayoutManager(object):
    """GridLayoutManager

    GridLayoutManager is a object.
    Responsibility:
    """
    def __init__(self, layout, params):
        """

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        self.layout = layout
        self.params = list(params)

    def get_layout(self, ):
        """SUMMARY

        get_layout()

        @Return:

        @Error:
        """
        return self.layout

    def set_layout(self, layout):
        """SUMMARY

        set_layout(layout)

        @Arguments:
        - `layout`:

        @Return:

        @Error:
        """
        self.layout = layout

    def add_param(self, param):
        """SUMMARY

        add_param(param)

        @Arguments:
        - `param`:

        @Return:

        @Error:
        """
        self.params.append(param)

    def remove_param(self, param):
        """SUMMARY

        remove_param(param)

        @Arguments:
        - `param`:

        @Return:

        @Error:
        """
        self.params.remove(param)

    def list_params(self, ):
        """SUMMARY

        list_params()

        @Return:

        @Error:
        """
        return self.params[:]

    def mapping(self, screen, items):
        """SUMMARY

        mapping(screen, items)

        @Arguments:
        - `screen`:
        - `items`:

        @Return:

        @Error:
        """
        self.layout.clear()
        for param, item in zip(self.params, items):
            self.layout.set_layout_item(item, param)
        return self.layout.layout(screen)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# grid.py ends here
