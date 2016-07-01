#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""screenshot -- DESCRIPTION

"""
from xcb import xproto

import Image


def screen_shot(display):
    r"""SUMMARY

    screen_shot(display)

    @Arguments:
    - `display`:

    @Return:

    @Error:
    """
    setup = display.get_setup()
    screen = setup.roots[0]
    width = screen.width_in_pixels
    height = screen.height_in_pixels
    root = screen.root
    output_format = xproto.ImageFormat.XYPixmap
    plane_mask = 2 ** 32 - 1
    reply = display.core.GetImage(
        output_format, root, 0, 0, width, height, plane_mask).reply()
    image_data = reply.data.buf()
    im = Image.frombuffer(
        "RGBX", (width, height), image_data, "raw", "BGRX").convert("RGB")
    with open('/tmp/tes.png') as f:
        im.save(f, format="png")



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# screenshot.py ends here
