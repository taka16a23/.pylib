#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: sendevent.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""sendevent -- DESCRIPTION

"""
import xcb4.xobj.pieces as pieces


class KeyPress(object):
    r"""KeyPress

    KeyPress is a object.
    Responsibility:
    """
    def __init__(self, propagate, destination, detail, sequence_number, time,
                 root, window, child, rootpoint, eventpoint, state, samescreen):
        r"""

        @Arguments:
        - `propagate`:
        - `destination`:
        - `detail`:
        - `sequence_number`:
        - `time`:
        - `root`:
        - `window`:
        - `child`:
        - `rootpoint`:
        - `eventpoint`:
        - `state`:
        - `samescreen`:
        """
        self._propagate = propagate
        self._destination = destination
        self._sequence_number = sequence_number
        self._time = time
        self._root = root
        self._window = window
        self._child = child
        self._rootpoint = rootpoint
        self._eventpoint = eventpoint
        self._samescreen = samescreen
        self._key = pieces.XKey(detail, state)

    def get_detail(self, ):
        r"""SUMMARY

        get_detail()

        @Return:

        @Error:
        """
        return self._key.get_code()

    def set_detail(self, detail):
        r"""SUMMARY

        set_detail(detail)

        @Arguments:
        - `detail`:

        @Return:

        @Error:
        """
        self._key.set_code(detail)

    detail = property(get_detail, set_detail)

    def get_state(self, ):
        r"""SUMMARY

        get_state()

        @Return:

        @Error:
        """
        return self._key.get_modifiers()

    def set_state(self, state):
        r"""SUMMARY

        set_state(state)

        @Arguments:
        - `state`:

        @Return:

        @Error:
        """
        self._key.set_modifiers(state)

    state = property(get_state, set_state)




# For Emacs
# Local Variables:
# coding: utf-8
# End:
# sendevent.py ends here
