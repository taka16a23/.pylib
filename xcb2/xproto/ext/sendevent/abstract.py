#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: abstract.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""abstract -- a parts of xcb2

"""
from cStringIO import StringIO as _StringIO
from struct import pack as _pack

from xcb2.xproto.ext.abstract import CoreSubMethodAbstract


class EventAbstract(CoreSubMethodAbstract):
    r"""SUMMARY
    """

    _mask = ''
    _code = ''

    def _getbinary(self, propagate, destination, detail, sequence_number,
                   time, root, window, child, root_x, root_y, event_x, event_y,
                   state, samescreen):
        r"""SUMMARY

        _getbinary(propagate, destination, detail, sequence_number,
        time, root, window, child, root_x, root_y, event_x, event_y,
        state, samescreen)

        @Arguments:
        - `propagate`:
        - `destination`:
        - `detail`:
        - `sequence_number`:
        - `time`:
        - `root`:
        - `window`:
        - `child`:
        - `root_x`:
        - `root_y`:
        - `event_x`:
        - `event_y`:
        - `state`:
        - `samescreen`:

        @Return:
        """
        buf = _StringIO()
        buf.write(_pack('=xB2xI', propagate, destination))
        buf.write(self._mask)
        buf.write(self._code)
        buf.write(_pack('B', detail))
        buf.write(_pack('H', sequence_number)) # why 'BH4I5HBx' fmt LengthError
        buf.write(_pack('4I5HBx', time, root, window, child,
                        root_x, root_y,
                        event_x, event_y, state, samescreen))
        return buf.getvalue()

    def __call__(self, propagate, destination, detail, sequence_number,
                 time, root, window, child, root_x, root_y, event_x, event_y,
                 state, samescreen):
        r"""SUMMARY

        __call__(propagate, destination, detail, sequence_number,
        time, root, window, child, root_x, root_y, event_x, event_y, state,
        samescreen)

        @Arguments:
        - `propagate`:
        - `destination`:
        - `detail`:
        - `sequence_number`:
        - `time`:
        - `root`:
        - `window`:
        - `child`:
        - `root_x`:
        - `root_y`:
        - `event_x`:
        - `event_y`:
        - `state`:
        - `samescreen`:

        @Return:
        """
        return self._parent.request(
            self._getbinary(propagate, destination, detail, sequence_number,
                 time, root, window, child, root_x, root_y, event_x, event_y,
                 state, samescreen))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# abstract.py ends here
