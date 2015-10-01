#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: __init__.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""Name: __init__.py


"""
import struct
import xcb, xcb.xproto
import xcb.render

NAME = 'TestName'
WMCLASS = 'testclass\x00TestClass\x00'

def simple_teswindow():
    r"""SUMMARY

    simple_teswindow()

    @Return:
    """
    con = xcb.connect()
    con.render = con(xcb.render.key)

    setup = con.get_setup()
    root = setup.roots[0].root
    depth = setup.roots[0].root_depth
    visual = setup.roots[0].root_visual
    white = setup.roots[0].white_pixel

    window = con.generate_id()

    con.core.CreateWindow(depth, window, root,
                          0, 0, 640, 480, 0,
                          xcb.xproto.WindowClass.InputOutput,
                          visual,
                          xcb.xproto.CW.BackPixel | xcb.xproto.CW.EventMask,
                          [white, xcb.xproto.EventMask.Exposure |
                           xcb.xproto.EventMask.KeyPress])
    xa_wm_name = con.core.InternAtom(
        False, len('WM_NAME'), 'WM_NAME').reply().atom
    xa_net_wm_name = con.core.InternAtom(
        False, len('_NET_WM_NAME'), '_NET_WM_NAME').reply().atom
    xa_wmclass = con.core.InternAtom(
        False, len('WM_CLASS'), 'WM_CLASS').reply().atom
    xa_utf8_string = con.core.InternAtom(
        False, len('UTF8_STRING'), 'UTF8_STRING').reply().atom

    xa_net_wm_window_type = con.core.InternAtom(
        False, len('_NET_WM_WINDOW_TYPE'), '_NET_WM_WINDOW_TYPE').reply().atom
    xa_normal = con.core.InternAtom(
        False, len('_NET_WM_WINDOW_TYPE_NORMAL'),
        '_NET_WM_WINDOW_TYPE_NORMAL').reply().atom
    xa_atom = con.core.InternAtom(False, len('ATOM'), 'ATOM').reply().atom
    xa_string = con.core.InternAtom(False, len('STRING'), 'STRING').reply().atom

    con.core.ChangeProperty(xcb.xproto.PropMode.Replace, window,
                            xa_net_wm_name, xa_utf8_string, 8, len(NAME), NAME)

    con.core.ChangeProperty(
        xcb.xproto.PropMode.Replace, window, xa_wmclass, xa_string,
        8, len(WMCLASS), WMCLASS)

    data = struct.pack('I', xa_normal)

    con.core.ChangeProperty(
        xcb.xproto.PropMode.Replace, window, xa_net_wm_window_type,
        xa_atom, 32, 1, data)
    con.core.MapWindow(window)
    con.flush()
    return window



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
