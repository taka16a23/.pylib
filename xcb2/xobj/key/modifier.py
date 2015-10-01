#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: modifier.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $


class Modifier(int):
    """Class Modifier
    """
    # Attributes:

    # Operations
    def __repr__(self):
        return '{0.__class__.__name__}({0})'.format(self)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# modifier.py ends here
