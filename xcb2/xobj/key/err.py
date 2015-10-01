#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: err.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

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
