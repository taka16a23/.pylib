#!/usr/bin/env python
# -*- coding: utf-8 -*-
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