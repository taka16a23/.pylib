#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: charsym.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

"""Charsym
"""


import keysymdef


class Charsym(unicode):
    """Class Charsym
    """
    # Attributes:
    def __init__(self, char):
        r"""

        @Arguments:
        - `char`:
        """
        if 1 != len(char):
            raise StandardError()
        unicode.__init__(self, char, 'utf-8')

    # Operations
    def to_sym(self):
        """function to_sym

        returns
        """
        return keysymdef.CharToSym.char_to_sym(self)

    def __repr__(self):
        """function __repr__

        returns
        """
        return '{0.__class__.__name__}("{1}")'.format(
            self, self.encode('utf-8'))

    def __int__(self):
        """function __int__

        returns int
        """
        return int(self.to_sym())

    def __long__(self):
        """function __long__

        returns long
        """
        return long(self.to_sym())

    def __hex__(self):
        """function __hex__

        returns hex
        """
        return hex(self.to_sym())

    def __eq__(self, other):
        """function __eq__

        other:

        returns bool
        """
        if isinstance(other, unicode):
            return super(Charsym, self).__eq__(other)
        return super(Charsym, self).__eq__(other)

    def __ne__(self, other):
        """function __ne__

        other:

        returns bool
        """
        return not self == other

    def __lt__(self, other):
        """function __lt__

        other:

        returns bool
        """
        return self.to_sym() > other

    def __le__(self, other):
        """function __le__

        other:

        returns bool
        """
        return self.to_sym() >= other

    def __gt__(self, other):
        """function __gt__

        other:

        returns bool
        """
        return self.to_sym() < other

    def __ge__(self, other):
        """function __ge__

        other:

        returns bool
        """
        return self.to_sym() <= other



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# charsym.py ends here
