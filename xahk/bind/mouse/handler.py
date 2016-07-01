#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""handler -- DESCRIPTION

"""


class MouseEventHandler(object):
    r"""MouseEventHandler

    MouseEventHandler is a object.
    Responsibility:
    """
    def on_button_event(self, event):
        r"""SUMMARY

        name()

        @Return:

        @Error:
        """
        if event.is_pressed():
            self.on_button_press(event)
            return
        self.on_button_release(event)

    def on_button_press(self, event):
        r"""SUMMARY

        on_button_press(event)

        @Arguments:
        - `event`:

        @Return:

        @Error:
        """

    def on_button_release(self, event):
        r"""SUMMARY

        on_button_release()

        @Return:

        @Error:
        """

    def __str__(self):
        return '{0.__class__.__name__}'.format(self)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# handler.py ends here
