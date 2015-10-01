#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: bitmask.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""bitmask -- DESCRIPTION

"""
from struct import pack as _pack

from bitflag import BitFlagAbstract, BitFlag8


class BitConfigWindow(BitFlagAbstract):
    r"""SUMMARY
    """

    def __init__(self, mask=0):
        r"""

        @Arguments:
        - `mask`:
        """
        self.flags = BitFlag8(mask)

    def pack(self, ):
        r"""SUMMARY

        pack()

        @Return:
        """
        return _pack('I', self.flags)

    def set_x(self, ):
        r"""SUMMARY

        set_x()

        @Return:
        """
        self.flags.set1()

    def reset_x(self, ):
        r"""SUMMARY

        reset_x()

        @Return:
        """
        self.flags.reset1()

    def isx(self, ):
        r"""SUMMARY

        isx()

        @Return:
        """
        return self.flags.isflaged1()

    def set_y(self, ):
        r"""SUMMARY

        set_x()

        @Return:
        """
        self.flags.set2()

    def reset_y(self, ):
        r"""SUMMARY

        reset_x()

        @Return:
        """
        self.flags.reset2()

    def isy(self, ):
        r"""SUMMARY

        isx()

        @Return:
        """
        return self.flags.isflaged2()

    def set_width(self, ):
        r"""SUMMARY

        set_x()

        @Return:
        """
        self.flags.set3()

    def reset_width(self, ):
        r"""SUMMARY

        reset_x()

        @Return:
        """
        self.flags.reset3()

    def iswidth(self, ):
        r"""SUMMARY

        isx()

        @Return:
        """
        return self.flags.isflaged3()

    def set_height(self, ):
        r"""SUMMARY

        set_x()

        @Return:
        """
        self.flags.set4()

    def reset_height(self, ):
        r"""SUMMARY

        reset_x()

        @Return:
        """
        self.flags.reset4()

    def isheight(self, ):
        r"""SUMMARY

        isx()

        @Return:
        """
        return self.flags.isflaged4()

    def set_borderwidth(self, ):
        r"""SUMMARY

        set_x()

        @Return:
        """
        self.flags.set5()

    def reset_borderwidth(self, ):
        r"""SUMMARY

        reset_x()

        @Return:
        """
        self.flags.reset5()

    def isborderwidth(self, ):
        r"""SUMMARY

        isx()

        @Return:
        """
        return self.flags.isflaged5()

    def set_sibling(self, ):
        r"""SUMMARY

        set_x()

        @Return:
        """
        self.flags.set6()

    def reset_sibling(self, ):
        r"""SUMMARY

        reset_x()

        @Return:
        """
        self.flags.reset6()

    def issibling(self, ):
        r"""SUMMARY

        isx()

        @Return:
        """
        return self.flags.isflaged6()

    def set_stackmode(self, ):
        r"""SUMMARY

        set_x()

        @Return:
        """
        self.flags.set7()

    def reset_stackmode(self, ):
        r"""SUMMARY

        reset_x()

        @Return:
        """
        self.flags.reset7()

    def isstackmode(self, ):
        r"""SUMMARY

        isx()

        @Return:
        """
        return self.flags.isflaged7()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# bitmask.py ends here
