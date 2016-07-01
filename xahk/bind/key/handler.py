#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""handler -- DESCRIPTION

"""


class KeyEventHandler(object):
    r"""KeyEventHandler

    KeyEventHandler is a object.
    Responsibility:
    """
    def on_key_event(self, event):
        r"""SUMMARY

        name()

        @Return:

        @Error:
        """
        if event.is_pressed():
            self.on_key_press(event)
        else:
            self.on_key_release(event)

    def on_key_press(self, event):
        r"""SUMMARY

        on_key_press(event)

        @Arguments:
        - `event`:

        @Return:

        @Error:
        """

    def on_key_release(self, event):
        r"""SUMMARY

        on_key_release()

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
