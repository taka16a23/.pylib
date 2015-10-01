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


class GetGeometryCookie(xcb.Cookie):
    pass


class QueryTreeCookie(xcb.Cookie):
    pass


class InternAtomCookie(xcb.Cookie):
    pass


class GetAtomNameCookie(xcb.Cookie):
    pass


class GetPropertyCookie(xcb.Cookie):
    pass


class ListPropertiesCookie(xcb.Cookie):
    pass


class GetSelectionOwnerCookie(xcb.Cookie):
    pass


class GrabPointerCookie(xcb.Cookie):
    pass


class GrabKeyboardCookie(xcb.Cookie):
    pass



class QueryPointerCookie(xcb.Cookie):
    pass


class GetMotionEventsCookie(xcb.Cookie):
    pass


class TranslateCoordinatesCookie(xcb.Cookie):
    pass


class GetInputFocusCookie(xcb.Cookie):
    pass


class QueryKeymapCookie(xcb.Cookie):
    pass


class QueryFontCookie(xcb.Cookie):
    pass


class QueryTextExtentsCookie(xcb.Cookie):
    pass


class ListFontsCookie(xcb.Cookie):
    pass


class ListFontsWithInfoCookie(xcb.Cookie):
    pass


class GetFontPathCookie(xcb.Cookie):
    pass


class GetImageCookie(xcb.Cookie):
    pass


class ListInstalledColormapsCookie(xcb.Cookie):
    pass


class AllocColorCookie(xcb.Cookie):
    pass


class AllocNamedColorCookie(xcb.Cookie):
    pass


class AllocColorCellsCookie(xcb.Cookie):
    pass


class AllocColorPlanesCookie(xcb.Cookie):
    pass


class QueryColorsCookie(xcb.Cookie):
    pass


class LookupColorCookie(xcb.Cookie):
    pass


class QueryBestSizeCookie(xcb.Cookie):
    pass


class QueryExtensionCookie(xcb.Cookie):
    pass


class ListExtensionsCookie(xcb.Cookie):
    pass


class GetKeyboardMappingCookie(xcb.Cookie):
    pass


class GetKeyboardControlCookie(xcb.Cookie):
    pass


class GetPointerControlCookie(xcb.Cookie):
    pass


class GetScreenSaverCookie(xcb.Cookie):
    pass


class GetWindowAttributesCookie(xcb.Cookie):
    pass


class ListHostsCookie(xcb.Cookie):
    pass


class SetPointerMappingCookie(xcb.Cookie):
    pass


class GetPointerMappingCookie(xcb.Cookie):
    pass


class SetModifierMappingCookie(xcb.Cookie):
    pass


class GetModifierMappingCookie(xcb.Cookie):
    pass



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# cookie.py ends here
