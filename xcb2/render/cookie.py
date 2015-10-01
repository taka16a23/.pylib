#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: cookie.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""cookie -- DESCRIPTION

"""
from xcb import xcb


class QueryVersionCookie(xcb.Cookie):
    pass


class QueryPictFormatsCookie(xcb.Cookie):
    pass


class QueryPictIndexValuesCookie(xcb.Cookie):
    pass


class QueryFiltersCookie(xcb.Cookie):
    pass



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# cookie.py ends here
