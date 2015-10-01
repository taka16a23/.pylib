#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""resize -- DESCRIPTION

"""


def spacing_horizon(rects, space):
    r"""SUMMARY

    spacing_horizon(rects, space)

    @Arguments:
    - `rects`:
    - `space`:

    @Return:

    @Error:

    +---------------+-+----------------+-+----------------+
    | Rectangle1    | | Rectangle2     | | Rectangle3     |
    |               | |                | |                |
    |               | |                | |                |
    |           <---| |--->        <---| |--->            |
    |               | |                | |                |
    |               | |                | |                |
    |               | |                | |                |
    +---------------+-+----------------+-+----------------+
    """
    if len(rects) <= 1:
        return
    for rect in rects:
        rect.set_width(rect.get_width() - space * 2)
    rects[-1].set_x(rects[-1].get_x() + space * 2) # Rectangle3 move to right
    for rct in rects[1:-1]:
        rct.set_x(rct.get_x() + space)
    return rects


def spacing_vertical(rects, space):
    r"""SUMMARY

    spacing_vertical(rects, space)

    @Arguments:
    - `rects`:
    - `space`:

    @Return:

    @Error:
    """
    if len(rects) <= 1:
        return
    rects[-1].set_y(rects[-1].get_y() + space * 2)
    for rect in rects:
        rect.set_height(rect.get_height() - space * 2)
    for rct in rects[1:-1]:
        rct.set_y(rct.get_y() + space)
    return rects



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# resize.py ends here
