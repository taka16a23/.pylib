#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" gtkscreenshot -- screenshot


"""


# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')

import gtk.gdk

__version__ = '0.1.0'


def screanshot(path):
    """SUMMARY

    @Arguments:
    - `path`:

    @Return:
    """
    w = gtk.gdk.get_default_root_window()
    sz = w.get_size()
    pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
    pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
    if (pb != None):
        pb.save(path,"png")



def test():
    pass


if __name__ == '__main__':
    test()


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# gtkscreenshot.py ends here
