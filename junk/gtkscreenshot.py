#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id: gtkscreenshot.py 419 2015-08-07 00:26:04Z t1 $
# $Revision: 419 $
# $Date: 2015-08-07 09:26:04 +0900 (Fri, 07 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-07 09:26:04 +0900 (Fri, 07 Aug 2015) $
""" gtkscreenshot -- screenshot

$Revision: 419 $

"""


# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')

import gtk.gdk

__revision__ = '$Revision: 419 $'
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
