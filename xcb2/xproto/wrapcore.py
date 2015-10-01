#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""wrapcore -- DESCRIPTION

"""
from xcb2.xproto import ext
from xcb2.xobj import AtomIdentifier


class DummyMethod(object):
    r"""SUMMARY
    """

    def __init__(self, ):
        r"""
        """
        # KLUDGE: (Atami) [2014/05/11]
        # for flymake
        self.InternAtom                      = lambda *args, **kwargs: None
        self.InternAtomUnchecked             = lambda *args, **kwargs: None
        self.GetAtomName                     = lambda *args, **kwargs: None
        self.GetAtomNameUnchecked            = lambda *args, **kwargs: None
        self.AllocColor                      = lambda *args, **kwargs: None
        self.AllocColorUnchecked             = lambda *args, **kwargs: None
        self.AllocColorCells                 = lambda *args, **kwargs: None
        self.AllocColorCellsUnchecked        = lambda *args, **kwargs: None
        self.AllocColorPlanes                = lambda *args, **kwargs: None
        self.AllocColorPlanesUnchecked       = lambda *args, **kwargs: None
        self.AllocNamedColor                 = lambda *args, **kwargs: None
        self.AllocNamedColorUnchecked        = lambda *args, **kwargs: None
        self.AllowEvents                     = lambda *args, **kwargs: None
        self.AllowEventsChecked              = lambda *args, **kwargs: None
        self.Bell                            = lambda *args, **kwargs: None
        self.BellChecked                     = lambda *args, **kwargs: None
        self.ChangeActivePointerGrab         = lambda *args, **kwargs: None
        self.ChangeActivePointerGrabChecked  = lambda *args, **kwargs: None
        self.ChangeGC                        = lambda *args, **kwargs: None
        self.ChangeGCChecked                 = lambda *args, **kwargs: None
        self.ChageHosts                      = lambda *args, **kwargs: None
        self.ChageHostsChecked               = lambda *args, **kwargs: None
        self.ChangeKeyboardControl           = lambda *args, **kwargs: None
        self.ChangeKeyboardControlChecked    = lambda *args, **kwargs: None
        self.ChangeKeyboardMapping           = lambda *args, **kwargs: None
        self.ChangeKeyboardMappingChecked    = lambda *args, **kwargs: None
        self.ChangePointerControl            = lambda *args, **kwargs: None
        self.ChangePointerControlChecked     = lambda *args, **kwargs: None
        self.ChangeProperty                  = lambda *args, **kwargs: None
        self.ChangePropertyChecked           = lambda *args, **kwargs: None
        self.ChangeSaveSet                   = lambda *args, **kwargs: None
        self.ChangeSaveSetChecked            = lambda *args, **kwargs: None
        self.ChangeWindowAttributes          = lambda *args, **kwargs: None
        self.ChangeWindowAttributesChecked   = lambda *args, **kwargs: None
        self.CirculateWindow                 = lambda *args, **kwargs: None
        self.CirculateWindowChecked          = lambda *args, **kwargs: None
        self.ClearArea                       = lambda *args, **kwargs: None
        self.ClearAreaChecked                = lambda *args, **kwargs: None
        self.CloseFont                       = lambda *args, **kwargs: None
        self.CloseFontChecked                = lambda *args, **kwargs: None
        self.ConfigureWindow                 = lambda *args, **kwargs: None
        self.ConfigureWindowChecked          = lambda *args, **kwargs: None
        self.ConvertSelection                = lambda *args, **kwargs: None
        self.ConvertSelectionChecked         = lambda *args, **kwargs: None
        self.CopyArea                        = lambda *args, **kwargs: None
        self.CopyAreaChecked                 = lambda *args, **kwargs: None
        self.CopyColormapAndFree             = lambda *args, **kwargs: None
        self.CopyColormapAndFreeChecked      = lambda *args, **kwargs: None
        self.CopyGC                          = lambda *args, **kwargs: None
        self.CopyGCChecked                   = lambda *args, **kwargs: None
        self.CopyPlane                       = lambda *args, **kwargs: None
        self.CopyPlaneChecked                = lambda *args, **kwargs: None
        self.CreateColormap                  = lambda *args, **kwargs: None
        self.CreateColormapChecked           = lambda *args, **kwargs: None
        self.CreateCursor                    = lambda *args, **kwargs: None
        self.CreateCursorChecked             = lambda *args, **kwargs: None
        self.CreateGC                        = lambda *args, **kwargs: None
        self.CreateGCChecked                 = lambda *args, **kwargs: None
        self.CreateGlyphCursor               = lambda *args, **kwargs: None
        self.CreateGlyphCursorChecked        = lambda *args, **kwargs: None
        self.CreatePixmap                    = lambda *args, **kwargs: None
        self.CreatePixmapChecked             = lambda *args, **kwargs: None
        self.CreateWindow                    = lambda *args, **kwargs: None
        self.CreateWindowChecked             = lambda *args, **kwargs: None
        self.DeleteProperty                  = lambda *args, **kwargs: None
        self.DeletePropertyChecked           = lambda *args, **kwargs: None
        self.DestroySubwindows               = lambda *args, **kwargs: None
        self.DestroySubwindowsChecked        = lambda *args, **kwargs: None
        self.DestroyWindow                   = lambda *args, **kwargs: None
        self.DestroyWindowChecked            = lambda *args, **kwargs: None
        self.FillPoly                        = lambda *args, **kwargs: None
        self.FillPolyChecked                 = lambda *args, **kwargs: None
        self.ForceScreenSaver                = lambda *args, **kwargs: None
        self.ForceScreenSaverChecked         = lambda *args, **kwargs: None
        self.FreeColormap                    = lambda *args, **kwargs: None
        self.FreeColormapChecked             = lambda *args, **kwargs: None
        self.FreeColors                      = lambda *args, **kwargs: None
        self.FreeColorsChecked               = lambda *args, **kwargs: None
        self.FreeCursor                      = lambda *args, **kwargs: None
        self.FreeCursorChecked               = lambda *args, **kwargs: None
        self.FreeGC                          = lambda *args, **kwargs: None
        self.FreeGCChecked                   = lambda *args, **kwargs: None
        self.FreePixmap                      = lambda *args, **kwargs: None
        self.FreePixmapChecked               = lambda *args, **kwargs: None
        self.GetFontPath                     = lambda *args, **kwargs: None
        self.GetFontPathUnchecked            = lambda *args, **kwargs: None
        self.GetGeometry                     = lambda *args, **kwargs: None
        self.GetGeometryUnchecked            = lambda *args, **kwargs: None
        self.GetImage                        = lambda *args, **kwargs: None
        self.GetImageUnchecked               = lambda *args, **kwargs: None
        self.GetInputFocus                   = lambda *args, **kwargs: None
        self.GetInputFocusUnchecked          = lambda *args, **kwargs: None
        self.GetKeyboardControl              = lambda *args, **kwargs: None
        self.GetKeyboardControlUnchecked     = lambda *args, **kwargs: None
        self.GetKeyboardMapping              = lambda *args, **kwargs: None
        self.GetKeyboardMappingUnchecked     = lambda *args, **kwargs: None
        self.GetModifierMapping              = lambda *args, **kwargs: None
        self.GetModifierMappingUnchecked     = lambda *args, **kwargs: None
        self.GetMotionEvents                 = lambda *args, **kwargs: None
        self.GetMotionEventsUnchecked        = lambda *args, **kwargs: None
        self.GetPointerControl               = lambda *args, **kwargs: None
        self.GetPointerControlUnchecked      = lambda *args, **kwargs: None
        self.GetPointerMapping               = lambda *args, **kwargs: None
        self.GetPointerMappingUnchecked      = lambda *args, **kwargs: None
        self.GetProperty                     = lambda *args, **kwargs: None
        self.GetPropertyUnchecked            = lambda *args, **kwargs: None
        self.GetScreenSaver                  = lambda *args, **kwargs: None
        self.GetScreenSaverUnchecked         = lambda *args, **kwargs: None
        self.GetSelectionOwner               = lambda *args, **kwargs: None
        self.GetSelectionOwnerUnchecked      = lambda *args, **kwargs: None
        self.GetWindowAttributes             = lambda *args, **kwargs: None
        self.GetWindowAttributesUnchecked    = lambda *args, **kwargs: None
        self.GrabButton                      = lambda *args, **kwargs: None
        self.GrabButtonChecked               = lambda *args, **kwargs: None
        self.GrabKey                         = lambda *args, **kwargs: None
        self.GrabKeyChecked                  = lambda *args, **kwargs: None
        self.GrabKeyboard                    = lambda *args, **kwargs: None
        self.GrabKeyboardUnchecked           = lambda *args, **kwargs: None
        self.GrabPointer                     = lambda *args, **kwargs: None
        self.GrabPointerUnchecked            = lambda *args, **kwargs: None
        self.GrabServer                      = lambda *args, **kwargs: None
        self.GrabServerChecked               = lambda *args, **kwargs: None
        self.ImageText16                     = lambda *args, **kwargs: None
        self.ImageText16Checked              = lambda *args, **kwargs: None
        self.ImageText8                      = lambda *args, **kwargs: None
        self.ImageText8Checked               = lambda *args, **kwargs: None
        self.InstallColormap                 = lambda *args, **kwargs: None
        self.InstallColormapChecked          = lambda *args, **kwargs: None
        self.KillClient                      = lambda *args, **kwargs: None
        self.KillClientChecked               = lambda *args, **kwargs: None
        self.ListExtensions                  = lambda *args, **kwargs: None
        self.ListExtensionsUnchecked         = lambda *args, **kwargs: None
        self.ListFonts                       = lambda *args, **kwargs: None
        self.ListFontsUnchecked              = lambda *args, **kwargs: None
        self.ListFontsWithInfo               = lambda *args, **kwargs: None
        self.ListFontsWithInfoUnchecked      = lambda *args, **kwargs: None
        self.ListHosts                       = lambda *args, **kwargs: None
        self.ListHostsUnchecked              = lambda *args, **kwargs: None
        self.ListInstalledColormaps          = lambda *args, **kwargs: None
        self.ListInstalledColormapsUnchecked = lambda *args, **kwargs: None
        self.ListProperties                  = lambda *args, **kwargs: None
        self.ListPropertiesUnchecked         = lambda *args, **kwargs: None
        self.LookupColor                     = lambda *args, **kwargs: None
        self.LookupColorUnchecked            = lambda *args, **kwargs: None
        self.MapSubwindows                   = lambda *args, **kwargs: None
        self.MapSubwindowsChecked            = lambda *args, **kwargs: None
        self.MapWindow                       = lambda *args, **kwargs: None
        self.MapWindowChecked                = lambda *args, **kwargs: None
        self.NoOperation                     = lambda *args, **kwargs: None
        self.NoOperationChecked              = lambda *args, **kwargs: None
        self.OpenFont                        = lambda *args, **kwargs: None
        self.OpenFontChecked                 = lambda *args, **kwargs: None
        self.PolyArc                         = lambda *args, **kwargs: None
        self.PolyArcChecked                  = lambda *args, **kwargs: None
        self.PolyFillArc                     = lambda *args, **kwargs: None
        self.PolyFillArcChecked              = lambda *args, **kwargs: None
        self.PolyFillRectangle               = lambda *args, **kwargs: None
        self.PolyFillRectangleChecked        = lambda *args, **kwargs: None
        self.PolyLine                        = lambda *args, **kwargs: None
        self.PolyLineChecked                 = lambda *args, **kwargs: None
        self.PolyPoint                       = lambda *args, **kwargs: None
        self.PolyPointChecked                = lambda *args, **kwargs: None
        self.PolyRectangle                   = lambda *args, **kwargs: None
        self.PolyRectangleChecked            = lambda *args, **kwargs: None
        self.PolySegment                     = lambda *args, **kwargs: None
        self.PolySegmentChecked              = lambda *args, **kwargs: None
        self.PolyText16                      = lambda *args, **kwargs: None
        self.PolyText16Checked               = lambda *args, **kwargs: None
        self.PolyText8                       = lambda *args, **kwargs: None
        self.PolyText8Checked                = lambda *args, **kwargs: None
        self.PutImage                        = lambda *args, **kwargs: None
        self.PutImageChecked                 = lambda *args, **kwargs: None
        self.QueryBestSize                   = lambda *args, **kwargs: None
        self.QueryBestSizeUnchecked          = lambda *args, **kwargs: None
        self.QueryColors                     = lambda *args, **kwargs: None
        self.QueryColorsUnchecked            = lambda *args, **kwargs: None
        self.QueryExtension                  = lambda *args, **kwargs: None
        self.QueryExtensionUnchecked         = lambda *args, **kwargs: None
        self.QueryFont                       = lambda *args, **kwargs: None
        self.QueryFontUnchecked              = lambda *args, **kwargs: None
        self.QueryPointer                    = lambda *args, **kwargs: None
        self.QueryPointerUnchecked           = lambda *args, **kwargs: None
        self.QueryTextExtents                = lambda *args, **kwargs: None
        self.QueryTextExtentsUnchecked       = lambda *args, **kwargs: None
        self.QueryTree                       = lambda *args, **kwargs: None
        self.QueryTreeUnchecked              = lambda *args, **kwargs: None
        self.RecolorCursor                   = lambda *args, **kwargs: None
        self.RecolorCursorChecked            = lambda *args, **kwargs: None
        self.ReparentWindow                  = lambda *args, **kwargs: None
        self.ReparentWindowChecked           = lambda *args, **kwargs: None
        self.RotateProperties                = lambda *args, **kwargs: None
        self.RotatePropertiesChecked         = lambda *args, **kwargs: None
        self.SendEvent                       = lambda *args, **kwargs: None
        self.SendEventChecked                = lambda *args, **kwargs: None
        self.SetAccessControl                = lambda *args, **kwargs: None
        self.SetAccessControlChecked         = lambda *args, **kwargs: None
        self.SetClipRectangles               = lambda *args, **kwargs: None
        self.SetClipRectanglesChecked        = lambda *args, **kwargs: None
        self.SetCloseDownMode                = lambda *args, **kwargs: None
        self.SetCloseDownModeChecked         = lambda *args, **kwargs: None
        self.SetDashes                       = lambda *args, **kwargs: None
        self.SetDashesChecked                = lambda *args, **kwargs: None
        self.SetFontPath                     = lambda *args, **kwargs: None
        self.SetFontPathChecked              = lambda *args, **kwargs: None
        self.SetInputFocus                   = lambda *args, **kwargs: None
        self.SetInputFocusChecked            = lambda *args, **kwargs: None
        self.SetModifierMapping              = lambda *args, **kwargs: None
        self.SetModifierMappingUnchecked     = lambda *args, **kwargs: None
        self.SetPointerMapping               = lambda *args, **kwargs: None
        self.SetPointerMappingUnchecked      = lambda *args, **kwargs: None
        self.SetSelectionOwner               = lambda *args, **kwargs: None
        self.SetSelectionOwnerChecked        = lambda *args, **kwargs: None
        self.StoreColors                     = lambda *args, **kwargs: None
        self.StoreColorsChecked              = lambda *args, **kwargs: None
        self.StoreNamedColor                 = lambda *args, **kwargs: None
        self.StoreNamedColorChecked          = lambda *args, **kwargs: None
        self.TranslateCoordinates            = lambda *args, **kwargs: None
        self.TranslateCoordinatesUnchecked   = lambda *args, **kwargs: None
        self.UngrabButton                    = lambda *args, **kwargs: None
        self.UngrabButtonChecked             = lambda *args, **kwargs: None
        self.UngrabKey                       = lambda *args, **kwargs: None
        self.UngrabKeyChecked                = lambda *args, **kwargs: None
        self.UngrabKeyboard                  = lambda *args, **kwargs: None
        self.UngrabKeyboardChecked           = lambda *args, **kwargs: None
        self.UngrabPointer                   = lambda *args, **kwargs: None
        self.UngrabPointerChecked            = lambda *args, **kwargs: None
        self.UngrabServer                    = lambda *args, **kwargs: None
        self.UngrabServerChecked             = lambda *args, **kwargs: None
        self.UninstallColormap               = lambda *args, **kwargs: None
        self.UninstallColormapChecked        = lambda *args, **kwargs: None
        self.UnmapSubwindows                 = lambda *args, **kwargs: None
        self.UnmapSubwindowsChecked          = lambda *args, **kwargs: None
        self.UnmapWindow                     = lambda *args, **kwargs: None
        self.UnmapWindowChecked              = lambda *args, **kwargs: None
        self.WarpPointer                     = lambda *args, **kwargs: None
        self.WarpPointerChecked              = lambda *args, **kwargs: None


class WrapCore(DummyMethod):
    r"""SUMMARY
    """

    def __init__(self, connection):
        r"""

        @Arguments:
        - `connection`:
        """
        self.connection = connection

    def load(self, ):
        r"""SUMMARY

        load()

        @Return:
        """
        self.InternAtom = ext.InternAtom(self.connection)
        self.InternAtomUnchecked = ext.InternAtomUnchecked(self.connection)
        self.GetAtomName = ext.GetAtomName(self.connection)
        self.GetAtomNameUnchecked = ext.GetAtomNameUnchecked(self.connection)
        self.AllocColor = ext.AllocColor(self.connection)
        self.AllocColorUnchecked = ext.AllocColorUnchecked(self.connection)
        self.AllocColorCells = ext.AllocColorCells(self.connection)
        self.AllocColorCellsUnchecked = ext.AllocColorCellsUnchecked(self.connection)
        self.AllocColorPlanes = ext.AllocColorPlanes(self.connection)
        self.AllocColorPlanesUnchecked = ext.AllocColorPlanesUnchecked(self.connection)
        self.AllocNamedColor = ext.AllocNamedColor(self.connection)
        self.AllocNamedColorUnchecked = ext.AllocNamedColorUnchecked(self.connection)
        self.AllowEvents = ext.AllowEvents(self.connection)
        self.AllowEventsChecked = ext.AllowEventsChecked(self.connection)
        self.Bell = ext.Bell(self.connection)
        self.BellChecked = ext.BellChecked(self.connection)
        self.ChangeActivePointerGrab = ext.ChangeActivePointerGrab(self.connection)
        self.ChangeActivePointerGrabChecked = ext.ChangeActivePointerGrabChecked(self.connection)
        self.ChangeGC = ext.ChangeGC(self.connection)
        self.ChangeGCChecked = ext.ChangeGCChecked(self.connection)
        self.ChangeHosts = ext.ChangeHosts(self.connection)
        self.ChangeHostsChecked = ext.ChangeHostsChecked(self.connection)
        self.ChangeKeyboardControl = ext.ChangeKeyboardControl(self.connection)
        self.ChangeKeyboardControlChecked = ext.ChangeKeyboardControl(self.connection)
        self.ChangeKeyboardMapping = ext.ChangeKeyboardMapping(self.connection)
        self.ChangeKeyboardMappingChecked = ext.ChangeKeyboardMappingChecked(self.connection)
        self.ChangePointerControl = ext.ChangePointerControl(self.connection)
        self.ChangePointerControlChecked = ext.ChangePointerControlChecked(self.connection)
        self.ChangeProperty = ext.ChangeProperty(self.connection)
        self.ChangePropertyChecked = ext.ChangePropertyChecked(self.connection)
        self.ChangeSaveSet = ext.ChangeSaveSet(self.connection)
        self.ChangeSaveSetChecked = ext.ChangeSaveSetChecked(self.connection)
        self.ChangeWindowAttributes = ext.ChangeWindowAttributes(self.connection)
        self.ChangeWindowAttributesChecked = ext.ChangeWindowAttributesChecked(self.connection)
        self.CirculateWindow = ext.CirculateWindow(self.connection)
        self.CirculateWindowChecked = ext.CirculateWindowChecked(self.connection)
        self.ClearArea = ext.ClearArea(self.connection)
        self.ClearAreaChecked = ext.ClearAreaChecked(self.connection)
        self.CloseFont = ext.CloseFont(self.connection)
        self.CloseFontChecked = ext.CloseFontChecked(self.connection)
        self.ConfigureWindow = ext.ConfigureWindow(self.connection)
        self.ConfigureWindowChecked = ext.ConfigureWindowChecked(self.connection)
        self.ConvertSelection = ext.ConvertSelection(self.connection)
        self.ConvertSelectionChecked = ext.ConvertSelectionChecked(self.connection)
        self.CopyArea = ext.CopyArea(self.connection)
        self.CopyAreaChecked = ext.CopyAreaChecked(self.connection)
        self.CopyColormapAndFree = ext.CopyColormapAndFree(self.connection)
        self.CopyColormapAndFreeChecked = ext.CopyColormapAndFreeChecked(self.connection)
        self.CopyGC = ext.CopyGC(self.connection)
        self.CopyGCChecked = ext.CopyGCChecked(self.connection)
        self.CopyPlane = ext.CopyPlane(self.connection)
        self.CopyPlaneChecked = ext.CopyPlaneChecked(self.connection)
        self.CreateColormap = ext.CreateColormap(self.connection)
        self.CreateColormapChecked = ext.CreateColormapChecked(self.connection)
        self.CreateCursor = ext.CreateCursor(self.connection)
        self.CreateCursorChecked = ext.CreateCursorChecked(self.connection)
        self.CreateGC = ext.CreateGC(self.connection)
        self.CreateGCChecked = ext.CreateGCChecked(self.connection)
        self.CreateGlyphCursor = ext.CreateGlyphCursor(self.connection)
        self.CreateGlyphCursorChecked = ext.CreateGlyphCursorChecked(self.connection)
        self.CreatePixmap = ext.CreatePixmap(self.connection)
        self.CreatePixmapChecked = ext.CreatePixmapChecked(self.connection)
        self.CreateWindow = ext.CreateWindow(self.connection)
        self.CreateWindowChecked = ext.CreateWindowChecked(self.connection)
        self.DeleteProperty = ext.DeleteProperty(self.connection)
        self.DeletePropertyChecked = ext.DeletePropertyChecked(self.connection)
        self.DestroySubwindows = ext.DestroySubwindows(self.connection)
        self.DestroySubwindowsChecked = ext.DestroySubwindowsChecked(self.connection)
        self.DestroyWindow = ext.DestroyWindow(self.connection)
        self.DestroyWindowChecked = ext.DestroyWindowChecked(self.connection)
        self.FillPoly = ext.FillPoly(self.connection)
        self.FillPolyChecked = ext.FillPolyChecked(self.connection)
        self.ForceScreenSaver = ext.ForceScreenSaver(self.connection)
        self.ForceScreenSaverChecked = ext.ForceScreenSaverChecked(self.connection)
        self.FreeColormap = ext.FreeColormap(self.connection)
        self.FreeColormapChecked = ext.FreeColormapChecked(self.connection)
        self.FreeColors = ext.FreeColors(self.connection)
        self.FreeColorsChecked = ext.FreeColorsChecked(self.connection)
        self.FreeCursor = ext.FreeCursor(self.connection)
        self.FreeCursorChecked = ext.FreeCursorChecked(self.connection)
        self.FreeGC = ext.FreeGC(self.connection)
        self.FreeGCChecked = ext.FreeGCChecked(self.connection)
        self.FreePixmap = ext.FreePixmap(self.connection)
        self.FreePixmapChecked = ext.FreePixmapChecked(self.connection)
        self.GetFontPath = ext.GetFontPath(self.connection)
        self.GetFontPathUnchecked = ext.GetFontPathUnchecked(self.connection)
        self.GetGeometry = ext.GetGeometry(self.connection)
        self.GetGeometryUnchecked = ext.GetGeometryUnchecked(self.connection)
        self.GetImage = ext.GetImage(self.connection)
        self.GetImageUnchecked = ext.GetImageUnchecked(self.connection)
        self.GetInputFocus = ext.GetInputFocus(self.connection)
        self.GetInputFocusUnchecked = ext.GetInputFocusUnchecked(self.connection)
        self.GetKeyboardControl = ext.GetKeyboardControl(self.connection)
        self.GetKeyboardControlUnchecked = ext.GetKeyboardControlUnchecked(self.connection)
        self.GetKeyboardMapping = ext.GetKeyboardMapping(self.connection)
        self.GetKeyboardMappingUnchecked = ext.GetKeyboardMappingUnchecked(self.connection)
        self.GetModifierMapping = ext.GetModifierMapping(self.connection)
        self.GetModifierMappingUnchecked = ext.GetModifierMappingUnchecked(self.connection)
        self.GetMotionEvents = ext.GetMotionEvents(self.connection)
        self.GetMotionEventsUnchecked = ext.GetMotionEventsUnchecked(self.connection)
        self.GetPointerControl = ext.GetPointerControl(self.connection)
        self.GetPointerControlUnchecked = ext.GetPointerControlUnchecked(self.connection)
        self.GetPointerMapping = ext.GetPointerMapping(self.connection)
        self.GetPointerMappingUnchecked = ext.GetPointerMappingUnchecked(self.connection)
        self.GetProperty = ext.GetProperty(self.connection)
        self.GetPropertyUnchecked = ext.GetPropertyUnchecked(self.connection)
        self.GetScreenSaver = ext.GetScreenSaver(self.connection)
        self.GetScreenSaverUnchecked = ext.GetScreenSaverUnchecked(self.connection)
        self.GetSelectionOwner = ext.GetSelectionOwner(self.connection)
        self.GetSelectionOwnerUnchecked = ext.GetSelectionOwnerUnchecked(self.connection)
        self.GetWindowAttributes = ext.GetWindowAttributes(self.connection)
        self.GetWindowAttributesUnchecked = ext.GetWindowAttributesUnchecked(self.connection)
        self.GrabButton = ext.GrabButton(self.connection)
        self.GrabButtonChecked = ext.GrabButtonChecked(self.connection)
        self.GrabKey = ext.GrabKey(self.connection)
        self.GrabKeyChecked = ext.GrabKeyChecked(self.connection)
        self.GrabKeyboard = ext.GrabKeyboard(self.connection)
        self.GrabKeyboardUnchecked = ext.GrabKeyboardUnchecked(self.connection)
        self.GrabPointer = ext.GrabPointer(self.connection)
        self.GrabPointerUnchecked = ext.GrabPointerUnchecked(self.connection)
        self.GrabServer = ext.GrabServer(self.connection)
        self.GrabServerChecked = ext.GrabServerChecked(self.connection)
        self.ImageText16 = ext.ImageText16(self.connection)
        self.ImageText16Checked = ext.ImageText16Checked(self.connection)
        self.ImageText8 = ext.ImageText8(self.connection)
        self.ImageText8Checked = ext.ImageText8Checked(self.connection)
        self.InstallColormap = ext.InstallColormap(self.connection)
        self.InstallColormapChecked = ext.InstallColormapChecked(self.connection)
        self.KillClient = ext.KillClient(self.connection)
        self.KillClientChecked = ext.KillClientChecked(self.connection)
        self.ListExtensions = ext.ListExtensions(self.connection)
        self.ListExtensionsUnchecked = ext.ListExtensionsUnchecked(self.connection)
        self.ListFonts = ext.ListFonts(self.connection)
        self.ListFontsUnchecked = ext.ListFontsUnchecked(self.connection)
        self.ListFontsWithInfo = ext.ListFontsWithInfo(self.connection)
        self.ListFontsWithInfoUnchecked = ext.ListFontsWithInfoUnchecked(self.connection)
        self.ListHosts = ext.ListHosts(self.connection)
        self.ListHostsUnchecked = ext.ListHostsUnchecked(self.connection)
        self.ListInstalledColormaps = ext.ListInstalledColormaps(self.connection)
        self.ListInstalledColormapsUnchecked = ext.ListInstalledColormapsUnchecked(self.connection)
        self.ListProperties = ext.ListProperties(self.connection)
        self.ListPropertiesUnchecked = ext.ListPropertiesUnchecked(self.connection)
        self.LookupColor = ext.LookupColor(self.connection)
        self.LookupColorUnchecked = ext.LookupColorUnchecked(self.connection)
        self.MapSubwindows = ext.MapSubwindows(self.connection)
        self.MapSubwindowsChecked = ext.MapSubwindowsChecked(self.connection)
        self.MapWindow = ext.MapWindow(self.connection)
        self.MapWindowChecked = ext.MapWindowChecked(self.connection)
        self.NoOperation = ext.NoOperation(self.connection)
        self.NoOperationChecked = ext.NoOperationChecked(self.connection)
        self.OpenFont = ext.OpenFont(self.connection)
        self.OpenFontChecked = ext.OpenFontChecked(self.connection)
        self.PolyArc = ext.PolyArc(self.connection)
        self.PolyArcChecked = ext.PolyArcChecked(self.connection)
        self.PolyFillArc = ext.PolyFillArc(self.connection)
        self.PolyFillArcChecked = ext.PolyFillArcChecked(self.connection)
        self.PolyFillRectangle = ext.PolyFillRectangle(self.connection)
        self.PolyFillRectangleChecked = ext.PolyFillRectangleChecked(self.connection)
        self.PolyLine = ext.PolyLine(self.connection)
        self.PolyLineChecked = ext.PolyLineChecked(self.connection)
        self.PolyPoint = ext.PolyPoint(self.connection)
        self.PolyPointChecked = ext.PolyPointChecked(self.connection)
        self.PolyRectangle = ext.PolyRectangle(self.connection)
        self.PolyRectangleChecked = ext.PolyRectangleChecked(self.connection)
        self.PolySegment = ext.PolySegment(self.connection)
        self.PolySegmentChecked = ext.PolySegmentChecked(self.connection)
        self.PolyText16 = ext.PolyText16(self.connection)
        self.PolyText16Checked = ext.PolyText16Checked(self.connection)
        self.PolyText8 = ext.PolyText8(self.connection)
        self.PolyText8Checked = ext.PolyText8Checked(self.connection)
        self.PutImage = ext.PutImage(self.connection)
        self.PutImageChecked = ext.PutImageChecked(self.connection)
        self.QueryBestSize = ext.QueryBestSize(self.connection)
        self.QueryBestSizeUnchecked = ext.QueryBestSizeUnchecked(self.connection)
        self.QueryColors = ext.QueryColors(self.connection)
        self.QueryColorsUnchecked = ext.QueryColorsUnchecked(self.connection)
        self.QueryExtension = ext.QueryExtension(self.connection)
        self.QueryExtensionUnchecked = ext.QueryExtensionUnchecked(self.connection)
        self.QueryFont = ext.QueryFont(self.connection)
        self.QueryFontUnchecked = ext.QueryFontUnchecked(self.connection)
        self.QueryKeymap = ext.QueryKeymap(self.connection)
        self.QueryKeymap = ext.QueryKeymap(self.connection)
        self.QueryKeymapUnchecked = ext.QueryKeymapUnchecked(self.connection)
        self.QueryPointer = ext.QueryPointer(self.connection)
        self.QueryPointerUnchecked = ext.QueryPointerUnchecked(self.connection)
        self.QueryTextExtents = ext.QueryTextExtents(self.connection)
        self.QueryTextExtentsUnchecked = ext.QueryTextExtentsUnchecked(self.connection)
        self.QueryTree = ext.QueryTree(self.connection)
        self.QueryTreeUnchecked = ext.QueryTreeUnchecked(self.connection)
        self.RecolorCursor = ext.RecolorCursor(self.connection)
        self.RecolorCursorChecked = ext.RecolorCursorChecked(self.connection)
        self.ReparentWindow = ext.ReparentWindow(self.connection)
        self.ReparentWindowChecked = ext.ReparentWindowChecked(self.connection)
        self.RotateProperties = ext.RotateProperties(self.connection)
        self.RotatePropertiesChecked = ext.RotatePropertiesChecked(self.connection)
        self.SendEvent = ext.SendEvent(self.connection)
        self.SendEventChecked = ext.SendEventChecked(self.connection)
        self.SetAccessControl = ext.SetAccessControl(self.connection)
        self.SetAccessControlChecked = ext.SetAccessControlChecked(self.connection)
        self.SetClipRectangles = ext.SetClipRectangles(self.connection)
        self.SetClipRectanglesChecked = ext.SetClipRectanglesChecked(self.connection)
        self.SetCloseDownMode = ext.SetCloseDownMode(self.connection)
        self.SetCloseDownModeChecked = ext.SetCloseDownModeChecked(self.connection)
        self.SetDashes = ext.SetDashes(self.connection)
        self.SetDashesChecked = ext.SetDashesChecked(self.connection)
        self.SetFontPath = ext.SetFontPath(self.connection)
        self.SetFontPathChecked = ext.SetFontPathChecked(self.connection)
        self.SetInputFocus = ext.SetInputFocus(self.connection)
        self.SetInputFocusChecked = ext.SetInputFocusChecked(self.connection)
        self.SetModifierMapping = ext.SetModifierMapping(self.connection)
        self.SetModifierMappingUnchecked = ext.SetModifierMappingUnchecked(self.connection)
        self.SetPointerMapping = ext.SetPointerMapping(self.connection)
        self.SetPointerMappingUnchecked = ext.SetPointerMappingUnchecked(self.connection)
        self.SetScreenSaver = ext.SetScreenSaver(self.connection)
        self.SetScreenSaverChecked = ext.SetScreenSaverChecked(self.connection)
        self.SetSelectionOwner = ext.SetSelectionOwner(self.connection)
        self.SetSelectionOwnerChecked = ext.SetSelectionOwnerChecked(self.connection)
        self.StoreColors = ext.StoreColors(self.connection)
        self.StoreColorsChecked = ext.StoreColorsChecked(self.connection)
        self.StoreNamedColor = ext.StoreNamedColor(self.connection)
        self.StoreNamedColorChecked = ext.StoreNamedColorChecked(self.connection)
        self.TranslateCoordinates = ext.TranslateCoordinates(self.connection)
        self.TranslateCoordinatesUnchecked = ext.TranslateCoordinatesUnchecked(self.connection)
        self.UngrabButton = ext.UngrabButton(self.connection)
        self.UngrabButtonChecked = ext.UngrabButtonChecked(self.connection)
        self.UngrabKey = ext.UngrabKey(self.connection)
        self.UngrabKeyChecked = ext.UngrabKeyChecked(self.connection)
        self.UngrabKeyboard = ext.UngrabKeyboard(self.connection)
        self.UngrabKeyboardChecked = ext.UngrabKeyboardChecked(self.connection)
        self.UngrabPointer = ext.UngrabPointer(self.connection)
        self.UngrabPointerChecked = ext.UngrabPointerChecked(self.connection)
        self.UngrabServer = ext.UngrabServer(self.connection)
        self.UngrabServerChecked = ext.UngrabServerChecked(self.connection)
        self.UninstallColormap = ext.UninstallColormap(self.connection)
        self.UninstallColormapChecked = ext.UninstallColormapChecked(self.connection)
        self.UnmapSubwindows = ext.UnmapSubwindows(self.connection)
        self.UnmapSubwindowsChecked = ext.UnmapSubwindowsChecked(self.connection)
        self.UnmapWindow = ext.UnmapWindow(self.connection)
        self.UnmapWindowChecked = ext.UnmapWindowChecked(self.connection)
        self.WarpPointer = ext.WarpPointer(self.connection)
        self.WarpPointerChecked = ext.WarpPointerChecked(self.connection)
        # atomidentify
        self.atomidentify = AtomIdentifier(self.connection)

    def send_request(self, *args, **kwargs):
        r"""SUMMARY

        send_request(*args, **kwargs)

        @Arguments:
        - `args`:
        - `kwargs`:

        @Return:
        """
        return self.connection.rawconnection.core.send_request(*args, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# wrapcore.py ends here
