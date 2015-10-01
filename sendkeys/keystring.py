#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: keystring.py 173 2014-05-03 07:51:01Z t1 $
# $Revision: 173 $
# $Date: 2014-05-03 16:51:01 +0900 (Sat, 03 May 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-05-03 16:51:01 +0900 (Sat, 03 May 2014) $

r"""keystring -- DESCRIPTION

"""
from sendkeys.core import SendKeys
from sendkeys.code import KeyAbstract


class KeyString(KeyAbstract):
    r"""SUMMARY
    """

    def to_keycode(self, ):
        r"""SUMMARY

        to_keycode()

        @Return:
        """
        analyzed = list(SendKeys(self._data, display=self.display))
        if len(analyzed) != 1:
            # TODO: (Atami) [2014/04/28]
            raise StandardError(analyzed)
        return analyzed[0].code



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# keystring.py ends here
