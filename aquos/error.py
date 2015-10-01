#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id: error.py 189 2014-05-17 09:44:59Z t1 $
# $Revision: 189 $
# $Date: 2014-05-17 18:44:59 +0900 (Sat, 17 May 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-05-17 18:44:59 +0900 (Sat, 17 May 2014) $
r""" error -- Error for aquos

$Revision: 189 $

"""


class LoginError(StandardError):
    r"""
    """

    def __init__(self, user, passwd):
        r"""

        Arguments:
        - `user`:
        - `passwd`:
        """
        self._user = user
        self._passwd = passwd



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# error.py ends here
