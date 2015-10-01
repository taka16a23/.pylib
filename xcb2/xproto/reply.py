#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""reply -- DESCRIPTION

"""
from struct import unpack_from as _unpack_from

from xcb import xcb


class CHAR2B(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        _unpacked = _unpack_from('BB', parent, offset)
        self.byte1 = _unpacked[0]
        self.byte2 = _unpacked[1]


class POINT(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        _unpacked = _unpack_from('hh', parent, offset)
        self.x = _unpacked[0]
        self.y = _unpacked[1]


class RECTANGLE(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        _unpacked = _unpack_from('hhHH', parent, offset)
        self.x      = _unpacked[0]
        self.y      = _unpacked[1]
        self.width  = _unpacked[2]
        self.height = _unpacked[3]


class ARC(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        _unpacked = _unpack_from('hhHHhh', parent, offset)
        self.x      = _unpacked[0]
        self.y      = _unpacked[1]
        self.width  = _unpacked[2]
        self.height = _unpacked[3]
        self.angle1 = _unpacked[4]
        self.angle2 = _unpacked[5]


class FORMAT(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        _unpacked = _unpack_from('BBB5x', parent, offset)
        self.depth          = _unpacked[0]
        self.bits_per_pixel = _unpacked[1]
        self.scanline_pad   = _unpacked[2]


class VISUALTYPE(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        _unpacked = _unpack_from('IBBHIII4x', parent, offset)
        self.visual_id          = _unpacked[0]
        self._class             = _unpacked[1]
        self.bits_per_rgb_value = _unpacked[2]
        self.colormap_entries   = _unpacked[3]
        self.red_mask           = _unpacked[4]
        self.green_mask         = _unpacked[5]
        self.blue_mask          = _unpacked[6]


class DEPTH(xcb.Struct):
    def __init__(self, parent, offset):
        xcb.Struct.__init__(self, parent, offset)
        base = offset
        _unpacked = _unpack_from('BxH4x', parent, offset)
        self.depth       = _unpacked[0]
        self.visuals_len = _unpacked[1]
        offset += 8
        self.visuals = xcb.List(parent, offset, self.visuals_len, VISUALTYPE, 24)
        offset += len(self.visuals.buf())
        xcb._resize_obj(self, offset - base)


class SCREEN(xcb.Struct):
    def __init__(self, parent, offset):
        xcb.Struct.__init__(self, parent, offset)
        base = offset
        _unpacked = _unpack_from('IIIIIHHHHHHIBBBB', parent, offset)
        self.root                  = _unpacked[0]
        self.default_colormap      = _unpacked[1]
        self.white_pixel           = _unpacked[2]
        self.black_pixel           = _unpacked[3]
        self.current_input_masks   = _unpacked[4]
        self.width_in_pixels       = _unpacked[5]
        self.height_in_pixels      = _unpacked[6]
        self.width_in_millimeters  = _unpacked[7]
        self.height_in_millimeters = _unpacked[8]
        self.min_installed_maps    = _unpacked[9]
        self.max_installed_maps    = _unpacked[10]
        self.root_visual           = _unpacked[11]
        self.backing_stores        = _unpacked[12]
        self.save_unders           = _unpacked[13]
        self.root_depth            = _unpacked[14]
        self.allowed_depths_len    = _unpacked[15]
        offset += 40
        self.allowed_depths = xcb.List(
            parent, offset, self.allowed_depths_len, DEPTH, -1)
        offset += len(self.allowed_depths.buf())
        xcb._resize_obj(self, offset - base)


class SetupRequest(xcb.Struct):
    def __init__(self, parent, offset):
        xcb.Struct.__init__(self, parent, offset)
        base = offset
        _unpacked = _unpack_from('BxHHHH2x', parent, offset)
        self.byte_order                      = _unpacked[0]
        self.protocol_major_version          = _unpacked[1]
        self.protocol_minor_version          = _unpacked[2]
        self.authorization_protocol_name_len = _unpacked[3]
        self.authorization_protocol_data_len = _unpacked[4]
        offset += 12
        self.authorization_protocol_name = xcb.List(
            parent, offset, self.authorization_protocol_name_len, 'b', 1)
        offset += len(self.authorization_protocol_name.buf())
        offset += xcb.type_pad(1, offset)
        self.authorization_protocol_data = xcb.List(
            parent, offset, self.authorization_protocol_data_len, 'b', 1)
        offset += len(self.authorization_protocol_data.buf())
        xcb._resize_obj(self, offset - base)


class SetupFailed(xcb.Struct):
    def __init__(self, parent, offset):
        xcb.Struct.__init__(self, parent, offset)
        base = offset
        _unpacked = _unpack_from('BBHHH', parent, offset)
        self.status                 = _unpacked[0]
        self.reason_len             = _unpacked[1]
        self.protocol_major_version = _unpacked[2]
        self.protocol_minor_version = _unpacked[3]
        self.length                 = _unpacked[4]
        offset += 8
        self.reason = xcb.List(parent, offset, self.reason_len, 'b', 1)
        offset += len(self.reason.buf())
        xcb._resize_obj(self, offset - base)


class SetupAuthenticate(xcb.Struct):
    def __init__(self, parent, offset):
        xcb.Struct.__init__(self, parent, offset)
        base = offset
        _unpacked = _unpack_from('B5xH', parent, offset)
        self.status = _unpacked[0]
        self.length = _unpacked[1]
        offset += 8
        self.reason = xcb.List(parent, offset, (self.length * 4), 'b', 1)
        offset += len(self.reason.buf())
        xcb._resize_obj(self, offset - base)


class Setup(xcb.Struct):
    def __init__(self, parent, offset):
        xcb.Struct.__init__(self, parent, offset)
        base = offset
        _unpacked = _unpack_from('BxHHHIIIIHHBBBBBBBB4x', parent, offset)
        self.status                      = _unpacked[0]
        self.protocol_major_version      = _unpacked[1]
        self.protocol_minor_version      = _unpacked[2]
        self.length                      = _unpacked[3]
        self.release_number              = _unpacked[4]
        self.resource_id_base            = _unpacked[5]
        self.resource_id_mask            = _unpacked[6]
        self.motion_buffer_size          = _unpacked[7]
        self.vendor_len                  = _unpacked[8]
        self.maximum_request_length      = _unpacked[9]
        self.roots_len                   = _unpacked[10]
        self.pixmap_formats_len          = _unpacked[11]
        self.image_byte_order            = _unpacked[12]
        self.bitmap_format_bit_order     = _unpacked[13]
        self.bitmap_format_scanline_unit = _unpacked[14]
        self.bitmap_format_scanline_pad  = _unpacked[15]
        self.min_keycode                 = _unpacked[16]
        self.max_keycode                 = _unpacked[17]
        offset += 40
        self.vendor = xcb.List(parent, offset, self.vendor_len, 'b', 1)
        offset += len(self.vendor.buf())
        offset += xcb.type_pad(8, offset)
        self.pixmap_formats = xcb.List(
            parent, offset, self.pixmap_formats_len, FORMAT, 8)
        offset += len(self.pixmap_formats.buf())
        offset += xcb.type_pad(4, offset)
        self.roots = xcb.List(parent, offset, self.roots_len, SCREEN, -1)
        offset += len(self.roots.buf())
        xcb._resize_obj(self, offset - base)


class GetWindowAttributesReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        _unpacked = _unpack_from('xB2x4xIHBBIIBBBBIIIH2x', parent, offset)
        self.backing_store         = _unpacked[0]
        self.visual                = _unpacked[1]
        self._class                = _unpacked[2]
        self.bit_gravity           = _unpacked[3]
        self.win_gravity           = _unpacked[4]
        self.backing_planes        = _unpacked[5]
        self.backing_pixel         = _unpacked[6]
        self.save_under            = _unpacked[7]
        self.map_is_installed      = _unpacked[8]
        self.map_state             = _unpacked[9]
        self.override_redirect     = _unpacked[10]
        self.colormap              = _unpacked[11]
        self.all_event_masks       = _unpacked[12]
        self.your_event_mask       = _unpacked[13]
        self.do_not_propagate_mask = _unpacked[14]


class GetGeometryReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        _unpacked = _unpack_from('xB2x4xIhhHHH2x', parent, offset)
        self.depth        = _unpacked[0]
        self.root         = _unpacked[1]
        self.x            = _unpacked[2]
        self.y            = _unpacked[3]
        self.width        = _unpacked[4]
        self.height       = _unpacked[5]
        self.border_width = _unpacked[6]


class QueryTreeReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        _unpacked = _unpack_from('xx2x4xIIH14x', parent, offset)
        self.root         = _unpacked[0]
        self.parent       = _unpacked[1]
        self.children_len = _unpacked[2]
        offset += 32
        self.children = xcb.List(parent, offset, self.children_len, 'I', 4)


class InternAtomReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        _unpacked = _unpack_from('xx2x4xI', parent, offset)
        self.atom = _unpacked[0]


class GetAtomNameReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        _unpacked = _unpack_from('xx2x4xH22x', parent, offset)
        self.name_len = _unpacked[0]
        offset += 32
        self.name = xcb.List(parent, offset, self.name_len, 'b', 1)


class GetPropertyReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        _unpacked = _unpack_from('xB2x4xIII12x', parent, offset)
        self.format      = _unpacked[0]
        self.type        = _unpacked[1]
        self.bytes_after = _unpacked[2]
        self.value_len   = _unpacked[3]
        offset += 32
        self.value = xcb.List(
            parent, offset, (self.value_len * (self.format / 8)), 'B', 1)


class ListPropertiesReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.atoms_len,) = _unpack_from('xx2x4xH22x', parent, offset)
        offset += 32
        self.atoms = xcb.List(parent, offset, self.atoms_len, 'I', 4)


class GetSelectionOwnerReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.owner,) = _unpack_from('xx2x4xI', parent, offset)


class GrabPointerReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.status,) = _unpack_from('xB2x4x', parent, offset)


class GrabKeyboardReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.status,) = _unpack_from('xB2x4x', parent, offset)


class QueryPointerReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        _unpacked = _unpack_from('xB2x4xIIhhhhH2x', parent, offset)
        self.same_screen = _unpacked[0]
        self.root        = _unpacked[1]
        self.child       = _unpacked[2]
        self.root_x      = _unpacked[3]
        self.root_y      = _unpacked[4]
        self.win_x       = _unpacked[5]
        self.win_y       = _unpacked[6]
        self.mask        = _unpacked[7]


class TIMECOORD(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        _unpacked = _unpack_from('Ihh', parent, offset)
        self.time = _unpacked[0]
        self.x    = _unpacked[1]
        self.y    = _unpacked[2]


class GetMotionEventsReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.events_len,) = _unpack_from('xx2x4xI20x', parent, offset)
        offset += 32
        self.events = xcb.List(parent, offset, self.events_len, TIMECOORD, 8)


class TranslateCoordinatesReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        _unpacked = _unpack_from('xB2x4xIhh', parent, offset)
        self.same_screen = _unpacked[0]
        self.child       = _unpacked[1]
        self.dst_x       = _unpacked[2]
        self.dst_y       = _unpacked[3]


class GetInputFocusReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        _unpacked = _unpack_from('xB2x4xI', parent, offset)
        self.revert_to = _unpacked[0]
        self.focus     = _unpacked[1]


class QueryKeymapReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        offset += 8
        self.keys = xcb.List(parent, offset, 32, 'B', 1)


class FONTPROP(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        _unpacked = _unpack_from('II', parent, offset)
        self.name  = _unpacked[0]
        self.value = _unpacked[1]


class CHARINFO(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        _unpacked = _unpack_from('hhhhhH', parent, offset)
        self.left_side_bearing  = _unpacked[0]
        self.right_side_bearing = _unpacked[1]
        self.character_width    = _unpacked[2]
        self.ascent             = _unpacked[3]
        self.descent            = _unpacked[4]
        self.attributes         = _unpacked[5]


class QueryFontReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        offset += 8
        self.min_bounds = CHARINFO(parent, offset, 12)
        offset += 12
        offset += 4
        offset += xcb.type_pad(12, offset)
        self.max_bounds = CHARINFO(parent, offset, 12)
        offset += 12
        _unpacked = _unpack_from('4xHHHHBBBBhhI', parent, offset)
        self.min_char_or_byte2 = _unpacked[0]
        self.max_char_or_byte2 = _unpacked[1]
        self.default_char      = _unpacked[2]
        self.properties_len    = _unpacked[3]
        self.draw_direction    = _unpacked[4]
        self.min_byte1         = _unpacked[5]
        self.max_byte1         = _unpacked[6]
        self.all_chars_exist   = _unpacked[7]
        self.font_ascent       = _unpacked[8]
        self.font_descent      = _unpacked[9]
        self.char_infos_len    = _unpacked[10]
        offset += 24
        offset += xcb.type_pad(8, offset)
        self.properties = xcb.List(
            parent, offset, self.properties_len, FONTPROP, 8)
        offset += len(self.properties.buf())
        offset += xcb.type_pad(12, offset)
        self.char_infos = xcb.List(
            parent, offset, self.char_infos_len, CHARINFO, 12)


class QueryTextExtentsReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        _unpacked = _unpack_from('xB2x4xhhhhiii', parent, offset)
        self.draw_direction  = _unpacked[0]
        self.font_ascent     = _unpacked[1]
        self.font_descent    = _unpacked[2]
        self.overall_ascent  = _unpacked[3]
        self.overall_descent = _unpacked[4]
        self.overall_width   = _unpacked[5]
        self.overall_left    = _unpacked[6]
        self.overall_right   = _unpacked[7]


class STR(xcb.Struct):
    def __init__(self, parent, offset):
        xcb.Struct.__init__(self, parent, offset)
        base = offset
        (self.name_len,) = _unpack_from('B', parent, offset)
        offset += 1
        self.name = xcb.List(parent, offset, self.name_len, 'b', 1)
        offset += len(self.name.buf())
        xcb._resize_obj(self, offset - base)


class ListFontsReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.names_len,) = _unpack_from('xx2x4xH22x', parent, offset)
        offset += 32
        self.names = xcb.List(parent, offset, self.names_len, STR, -1)


class ListFontsWithInfoReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.name_len,) = _unpack_from('xB2x4x', parent, offset)
        offset += 8
        self.min_bounds = CHARINFO(parent, offset, 12)
        offset += 12
        offset += 4
        offset += xcb.type_pad(12, offset)
        self.max_bounds = CHARINFO(parent, offset, 12)
        offset += 12
        _unpacked = _unpack_from('4xHHHHBBBBhhI', parent, offset)
        self.min_char_or_byte2 = _unpacked[0]
        self.max_char_or_byte2 = _unpacked[1]
        self.default_char      = _unpacked[2]
        self.properties_len    = _unpacked[3]
        self.draw_direction    = _unpacked[4]
        self.min_byte1         = _unpacked[5]
        self.max_byte1         = _unpacked[6]
        self.all_chars_exist   = _unpacked[7]
        self.font_ascent       = _unpacked[8]
        self.font_descent      = _unpacked[9]
        self.replies_hint      = _unpacked[10]
        offset += 24
        offset += xcb.type_pad(8, offset)
        self.properties = xcb.List(
            parent, offset, self.properties_len, FONTPROP, 8)
        offset += len(self.properties.buf())
        offset += xcb.type_pad(1, offset)
        self.name = xcb.List(parent, offset, self.name_len, 'b', 1)


class GetFontPathReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.path_len,) = _unpack_from('xx2x4xH22x', parent, offset)
        offset += 32
        self.path = xcb.List(parent, offset, self.path_len, STR, -1)


class SEGMENT(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        _unpacked = _unpack_from('hhhh', parent, offset)
        self.x1 = _unpacked[0]
        self.y1 = _unpacked[1]
        self.x2 = _unpacked[2]
        self.y2 = _unpacked[3]


class GetImageReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        _unpacked = _unpack_from('xB2x4xI20x', parent, offset)
        self.depth  = _unpacked[0]
        self.visual = _unpacked[1]
        offset += 32
        self.data = xcb.List(parent, offset, (self.length * 4), 'B', 1)


class ListInstalledColormapsReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.cmaps_len,) = _unpack_from('xx2x4xH22x', parent, offset)
        offset += 32
        self.cmaps = xcb.List(parent, offset, self.cmaps_len, 'I', 4)


class AllocColorReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        _unpacked = _unpack_from('xx2x4xHHH2xI', parent, offset)
        self.red   = _unpacked[0]
        self.green = _unpacked[1]
        self.blue  = _unpacked[2]
        self.pixel = _unpacked[3]


class AllocNamedColorReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        _unpacked = _unpack_from('xx2x4xIHHHHHH', parent, offset)
        self.pixel        = _unpacked[0]
        self.exact_red    = _unpacked[1]
        self.exact_green  = _unpacked[2]
        self.exact_blue   = _unpacked[3]
        self.visual_red   = _unpacked[4]
        self.visual_green = _unpacked[5]
        self.visual_blue  = _unpacked[6]


class AllocColorCellsReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        _unpacked = _unpack_from('xx2x4xHH20x', parent, offset)
        self.pixels_len = _unpacked[0]
        self.masks_len  = _unpacked[1]
        offset += 32
        self.pixels = xcb.List(parent, offset, self.pixels_len, 'I', 4)
        offset += len(self.pixels.buf())
        offset += xcb.type_pad(4, offset)
        self.masks = xcb.List(parent, offset, self.masks_len, 'I', 4)


class AllocColorPlanesReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        _unpacked = _unpack_from('xx2x4xH2xIII8x', parent, offset)
        self.pixels_len = _unpacked[0]
        self.red_mask   = _unpacked[1]
        self.green_mask = _unpacked[2]
        self.blue_mask  = _unpacked[3]
        offset += 32
        self.pixels = xcb.List(parent, offset, self.pixels_len, 'I', 4)


class COLORITEM(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        _unpacked = _unpack_from('IHHHBx', parent, offset)
        self.pixel = _unpacked[0]
        self.red   = _unpacked[1]
        self.green = _unpacked[2]
        self.blue  = _unpacked[3]
        self.flags = _unpacked[4]


class RGB(xcb.Struct):
    def __init__(self, parent, offset, size):
        xcb.Struct.__init__(self, parent, offset, size)
        _unpacked = _unpack_from('HHH2x', parent, offset)
        self.red   = _unpacked[0]
        self.green = _unpacked[1]
        self.blue  = _unpacked[2]


class QueryColorsReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.colors_len,) = _unpack_from('xx2x4xH22x', parent, offset)
        offset += 32
        self.colors = xcb.List(parent, offset, self.colors_len, RGB, 8)


class LookupColorReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        _unpacked = _unpack_from('xx2x4xHHHHHH', parent, offset)
        self.exact_red    = _unpacked[0]
        self.exact_green  = _unpacked[1]
        self.exact_blue   = _unpacked[2]
        self.visual_red   = _unpacked[3]
        self.visual_green = _unpacked[4]
        self.visual_blue  = _unpacked[5]


class QueryBestSizeReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        _unpacked = _unpack_from('xx2x4xHH', parent, offset)
        self.width  = _unpacked[0]
        self.height = _unpacked[1]


class QueryExtensionReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.present, self.major_opcode, self.first_event, self.first_error,) = _unpack_from('xx2x4xBBBB', parent, offset)


class ListExtensionsReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.names_len,) = _unpack_from('xB2x4x24x', parent, offset)
        offset += 32
        self.names = xcb.List(parent, offset, self.names_len, STR, -1)


class GetKeyboardMappingReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.keysyms_per_keycode,) = _unpack_from('xB2x4x24x', parent, offset)
        offset += 32
        self.keysyms = xcb.List(parent, offset, self.length, 'I', 4)


class GetKeyboardControlReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        _unpacked = _unpack_from('xB2x4xIBBHH2x', parent, offset)
        self.global_auto_repeat = _unpacked[0]
        self.led_mask           = _unpacked[1]
        self.key_click_percent  = _unpacked[2]
        self.bell_percent       = _unpacked[3]
        self.bell_pitch         = _unpacked[4]
        self.bell_duration      = _unpacked[5]
        offset += 20
        self.auto_repeats = xcb.List(parent, offset, 32, 'B', 1)


class GetPointerControlReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        _unpacked = _unpack_from('xx2x4xHHH18x', parent, offset)
        self.acceleration_numerator   = _unpacked[0]
        self.acceleration_denominator = _unpacked[1]
        self.threshold                = _unpacked[2]


class GetScreenSaverReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        _unpacked = _unpack_from('xx2x4xHHBB18x', parent, offset)
        self.timeout         = _unpacked[0]
        self.interval        = _unpacked[1]
        self.prefer_blanking = _unpacked[2]
        self.allow_exposures = _unpacked[3]


class HOST(xcb.Struct):
    def __init__(self, parent, offset):
        xcb.Struct.__init__(self, parent, offset)
        base = offset
        _unpacked = _unpack_from('BxH', parent, offset)
        self.family      = _unpacked[0]
        self.address_len = _unpacked[1]
        offset += 4
        self.address = xcb.List(parent, offset, self.address_len, 'B', 1)
        offset += len(self.address.buf())
        xcb._resize_obj(self, offset - base)


class ListHostsReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        _unpacked = _unpack_from('xB2x4xH22x', parent, offset)
        self.mode      = _unpacked[0]
        self.hosts_len = _unpacked[1]
        offset += 32
        self.hosts = xcb.List(parent, offset, self.hosts_len, HOST, -1)


class SetPointerMappingReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.status,) = _unpack_from('xB2x4x', parent, offset)


class GetPointerMappingReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.map_len,) = _unpack_from('xB2x4x24x', parent, offset)
        offset += 32
        self.map = xcb.List(parent, offset, self.map_len, 'B', 1)


class SetModifierMappingReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.status,) = _unpack_from('xB2x4x', parent, offset)


class GetModifierMappingReply(xcb.Reply):
    def __init__(self, parent, offset=0):
        xcb.Reply.__init__(self, parent, offset)
        (self.keycodes_per_modifier,) = _unpack_from('xB2x4x24x', parent, offset)
        offset += 32
        self.keycodes = xcb.List(
            parent, offset, (self.keycodes_per_modifier * 8), 'B', 1)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# reply.py ends here
