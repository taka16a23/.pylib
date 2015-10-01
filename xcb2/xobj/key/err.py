#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""err -- DESCRIPTION

"""


class ConvertError(Exception):

    def __init__(self, obj):
        r"""

        @Arguments:
        - `obj`:
        """
        self._obj = obj

    def __repr__(self):
        return '{}, "{}"'.format(repr(self._obj), str(self._obj))

    def __str__(self):
        return repr(self)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# err.py ends here
