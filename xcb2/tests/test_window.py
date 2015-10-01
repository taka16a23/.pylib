#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: test_window.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""Name: test_window.py

['skipTest', ]

['assertAlmostEqual', 'assertAlmostEquals', 'assertApproximates',
 'assertDictContainsSubset', 'assertDictEqual', 'assertEndsWith', 'assertEqual',
 'assertEquals', 'assertFalse', 'assertGreater', 'assertGreaterEqual',
 'assertIdentical', 'assertIn', 'assertIs', 'assertIsInstance', 'assertIsNone',
 'assertIsNot', 'assertIsNotInstance', 'assertIsNotNone', 'assertItemsEqual',
 'assertLess', 'assertLessEqual', 'assertListEqual', 'assertMethodsMatch',
 'assertMultiLineEqual', 'assertNotAlmostEqual', 'assertNotAlmostEquals',
 'assertNotApproximates', 'assertNotEndsWith', 'assertNotEqual',
 'assertNotEquals', 'assertNotIdentical', 'assertNotIn', 'assertNotIsInstance',
 'assertNotRegexpMatches', 'assertNotStartsWith', 'assertRaises',
 'assertRaisesRegexp', 'assertRegexpMatches', 'assertSequenceEqual',
 'assertSetEqual', 'assertStartsWith', 'assertTrue', 'assertTupleEqual', ]

['failIf', 'failIfAlmostEqual', 'failIfApproximates', 'failIfEndsWith',
 'failIfEqual', 'failIfIdentical', 'failIfIn', 'failIfIs', 'failIfIsInstance',
 'failIfStartsWith', 'failUnless', 'failUnlessAlmostEqual',
 'failUnlessApproximates', 'failUnlessEndsWith', 'failUnlessEqual',
 'failUnlessIdentical', 'failUnlessIn', 'failUnlessIs', 'failUnlessIsInstance',
 'failUnlessMethodsMatch', 'failUnlessRaises', 'failUnlessRaisesRegexp',
 'failUnlessStartsWith', 'failureException', ]

"""
from mocker import *
from struct import pack
import xcb2, xcb2.render, xcb2.xproto
from xcb2.xobj.window.window import Window
from xcb2.xproto.reply import GetWindowAttributesReply
from xcb2.xproto import CW, EventMask, BadWindow


def simple_teswindow2():
    r"""SUMMARY

    simple_teswindow()

    @Return:
    """
    CON = xcb2.connect()
    CON.render = CON(xcb2.render.key)
    setup = CON.get_setup()
    root = setup.roots[0].root
    depth = setup.roots[0].root_depth
    visual = setup.roots[0].root_visual
    white = setup.roots[0].white_pixel

    window = CON.generate_id()

    CON.core.CreateWindow(depth, window, root,
                          0, 0, 640, 480, 0,
                          xcb2.xproto.WindowClass.InputOutput,
                          visual,
                          xcb2.xproto.CW.BackPixel, [white])
    CON.flush()
    return window


class TestWindow(MockerTestCase):
    """2014/06/06"""
    @classmethod
    def setUpClass(cls):
        cls.conn = xcb2.connect()

    def setUp(self):
        self.window = simple_teswindow2()
        self.Window = Window(self.conn, self.window)
        self.conn.flush()
        self.mocker.replay()

    def test_pack(self):
        expect = pack('I', self.window)
        got = self.Window.pack()
        self.assertEqual(expect, got,
                         msg='Failed: Window.pack expect: \{}, got: \{}'
                         .format(repr(expect), repr(got)))

    def test_get_attributes(self, ):
        attr = self.Window.get_attributes()
        self.assertIsInstance(
            attr, GetWindowAttributesReply,
            msg='Failed: Window.get_attributes expect: {}, got: {}'
            .format(GetWindowAttributesReply, attr))
        self.assertEqual(
            0, attr.all_event_masks,
            msg='Failed: Window.get_attributes expect: \{}, got: \{}'
            .format(0, attr.all_event_masks))

    def test_set_attributes(self, ):
        attr = self.Window.get_attributes()
        self.assertEqual(
            0, attr.all_event_masks,
            msg='Failed: Window.get_attributes expect: \{}, got: \{}'
            .format(0, attr.all_event_masks))
        self.Window.change_attributes(CW.EventMask, [EventMask.FocusChange])
        self.conn.flush()
        mask = self.Window.get_attributes().all_event_masks
        self.assertTrue(mask & EventMask.FocusChange)
        self.assertFalse(mask & EventMask.KeyPress)

    def test_destroy(self, ):
        self.conn.core.MapWindowChecked(self.window).check() # check exist
        self.Window.destroy()
        self.conn.flush()
        with self.assertRaises(BadWindow):
            self.conn.core.MapWindowChecked(self.window).check()

    def test_destroy_subwindow(self, ):
        self.skipTest('how to make subwindow')

    def test_save_set(self, ):
        self.skipTest('')

    def test_reparent(self, ):
        self.skipTest('')

    def test_map(self, ):
        self.Window.map()

    def test_map_sub_windows(self, ):
        self.Window.map_sub_windows()

    def test_unmap(self, ):
        self.Window.map()
        self.Window.unmap()

    def test_unmap_sub_windows(self, ):
        self.Window.unmap_sub_windows()

    def test_configure(self, ):
        self.skipTest('')

    def test_curculate(self, ):
        self.skipTest('')

    def test_raise_window(self, ):
        self.skipTest('')

    def test_query_tree(self, ):
        self.skipTest('')

    def test_query_recursive_tree(self, ):
        self.skipTest('')

    def test_change_property(self, ):
        self.skipTest('')

    def test_delete_property(self, ):
        self.skipTest('')

    def test_get_property(self, ):
        self.skipTest('')

    def test_list_properties(self, ):
        self.skipTest('')

    def test_set_selection_owner(self, ):
        self.skipTest('')

    def test_convert_selection(self, ):
        self.skipTest('')

    def test_send_event(self, ):
        self.skipTest('')

    def test_grab_pointer(self, ):
        self.skipTest('')

    def test_grab_button(self, ):
        self.skipTest('')

    def test_ungrab_button(self, ):
        self.skipTest('')

    def test_grab_keyboard(self, ):
        self.skipTest('')

    def test_ungrab_keyboard(self, ):
        self.skipTest('')

    def test_grab_key(self, ):
        self.skipTest('')

    def test_ungrab_key(self, ):
        self.skipTest('')

    def test_query_pointer(self, ):
        self.skipTest('')

    def test_get_motion_events(self, ):
        self.skipTest('')

    def test_translate_coords(self, ):
        self.skipTest('')

    def test_warp_pointer(self, ):
        self.skipTest('')

    def test_set_input_focus(self, ):
        self.skipTest('')

    def test_clear_area(self, ):
        self.skipTest('')

    def test_create_colormap(self, ):
        self.skipTest('')

    def test_list_installed_colormaps(self, ):
        self.skipTest('')

    def test_rotate_properties(self, ):
        self.skipTest('')

    def test_set_wm_name(self, ):
        self.skipTest('')

    def test_get_wm_name(self, ):
        self.skipTest('')

    def test_set_wm_icon_name(self, ):
        self.skipTest('')

    def test_set_wm_class(self, ):
        self.skipTest('')

    def test_get_wm_class(self, ):
        self.skipTest('')

    def test_set_wm_transient_for(self, ):
        self.skipTest('')

    def test_get_wm_transient_for(self, ):
        self.skipTest('')

    def test_set_wm_protocols(self, ):
        self.skipTest('')

    def test_get_wm_protocols(self, ):
        self.skipTest('')

    def test_set_wm_colormap_windows(self, ):
        self.skipTest('')

    def test_get_wm_colormap_windows(self, ):
        self.skipTest('')

    def test_set_wm_client_machine(self, ):
        self.skipTest('')

    def test_get_wm_client_machine(self, ):
        self.skipTest('')

    def test_set_wm_normal_hints(self, ):
        self.skipTest('')

    def test_get_wm_normal_hints(self, ):
        self.skipTest('')

    def test_set_wm_hints(self, ):
        self.skipTest('')

    def test_get_wm_hints(self, ):
        self.skipTest('')

    def test_set_wm_state(self, ):
        self.skipTest('')

    def test_get_wm_state(self, ):
        self.skipTest('')

    def test_set_wm_icon_size(self, ):
        self.skipTest('')

    def test_get_wm_icon_size(self, ):
        self.skipTest('')

    def test_set_net_wm_name(self, ):
        self.skipTest('')

    def test_get_net_wm_name(self, ):
        self.skipTest('')

    def test_set_net_wm_state(self, ):
        self.skipTest('')

    def test_get_net_wm_state(self, ):
        self.skipTest('')

    def test_set_net_wm_pid(self, ):
        self.skipTest('')

    def test_get_net_wm_pid(self, ):
        self.skipTest('')

    def test_set_net_wm_allowed_actions(self, ):
        self.skipTest('')

    def test_get_net_wm_allowed_actions(self, ):
        self.skipTest('')

    def test_set_net_supported(self, ):
        self.skipTest('')

    def test_get_net_supported(self, ):
        self.skipTest('')

    def test_set_net_wm_icon(self, ):
        self.skipTest('')

    def test_get_net_wm_icon(self, ):
        self.skipTest('')

    def test_set_net_wm_icon_geometry(self, ):
        self.skipTest('')

    def test_get_net_wm_icon_geometry(self, ):
        self.skipTest('')

    def test_set_net_wm_user_time(self, ):
        self.skipTest('')

    def test_get_net_wm_user_time(self, ):
        self.skipTest('')

    def test_set_net_wm_user_time_window(self, ):
        self.skipTest('')

    def test_get_net_wm_user_time_window(self, ):
        self.skipTest('')

    def test_set_net_wm_window_type(self, ):
        self.skipTest('')

    def test_get_net_wm_window_type(self, ):
        self.skipTest('')

    def test_set_net_workarea(self, ):
        self.skipTest('')

    def test_get_net_workarea(self, ):
        self.skipTest('')

    def tearDown(self):
        self.conn.core.DestroyWindow(self.window)
        self.conn.flush()

    @classmethod
    def tearDownClass(cls, ):
        # cls.conn.core.DestroyWindow(cls.window)
        cls.conn.disconnect()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_window.py ends here
