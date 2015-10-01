#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: biteventmask.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""biteventmask -- DESCRIPTION

"""
from struct import pack as _pack

from bitflag import BitFlagAbstract, BitFlag32


class BitEventMask(BitFlagAbstract):
    r"""SUMMARY
    """

    def __init__(self, mask=0):
        r"""

        @Arguments:
        - `mask`:
        """
        self.flags = BitFlag32(mask)

    def pack(self, ):
        r"""SUMMARY

        pack()

        @Return:
        """
        return _pack('I', self.flags)

    def clear(self, ):
        r"""SUMMARY

        clear()

        @Return:
        """
        self.flags.clear()

    def set_keypress(self, ):
        r"""Set keypress bit event mask.

        set_keypress()

        @Return:
        None
        """
        self.flags.set1()

    def reset_keypress(self, ):
        r"""Reset keypress bit event mask.

        reset_keypress()

        @Return:
        None
        """
        self.flags.reset1()

    def iskeypress(self, ):
        r"""Check is flaged keypress bit event mask.

        iskeypress()

        @Return:
        (bool)
        """
        return self.flags.isflaged1()

    def set_keyrelease(self, ):
        r"""Set keyrelease bit event mask.

        set_keyrelease()

        @Return:
        None
        """
        self.flags.set2()

    def reset_keyrelease(self, ):
        r"""Reset keyrelease bit event mask.

        reset_keyrelease()

        @Return:
        None
        """
        self.flags.reset2()

    def iskeyrelease(self, ):
        r"""Check is flaged keyrelease bit event mask.

        iskeyrelease()

        @Return:
        (bool)
        """
        return self.flags.isflaged2()


    def set_buttonpress(self, ):
        r"""Set buttonpress bit event mask.

        set_buttonpress()

        @Return:
        None
        """
        self.flags.set3()

    def reset_buttonpress(self, ):
        r"""Reset buttonpress bit event mask.

        reset_buttonpress()

        @Return:
        None
        """
        self.flags.reset3()

    def isbuttonpress(self, ):
        r"""Check is flaged buttonpress bit event mask.

        isbuttonpress()

        @Return:
        (bool)
        """
        return self.flags.isflaged3()

    def set_buttonrelease(self, ):
        r"""Set buttonrelease bit event mask.

        set_buttonrelease()

        @Return:
        None
        """
        self.flags.set4()

    def reset_buttonrelease(self, ):
        r"""Reset buttonrelease bit event mask.

        reset_buttonrelease()

        @Return:
        None
        """
        self.flags.reset4()

    def isbuttonrelease(self, ):
        r"""Check is flaged buttonrelease bit event mask.

        isbuttonrelease()

        @Return:
        (bool)
        """
        return self.flags.isflaged4()

    def set_enterwindow(self, ):
        r"""Set enterwindow bit event mask.

        set_enterwindow()

        @Return:
        None
        """
        self.flags.set5()

    def reset_enterwindow(self, ):
        r"""Reset enterwindow bit event mask.

        reset_enterwindow()

        @Return:
        None
        """
        self.flags.reset5()

    def isenterwindow(self, ):
        r"""Check is flaged enterwindow bit event mask.

        isenterwindow()

        @Return:
        (bool)
        """
        return self.flags.isflaged5()

    def set_leavewindow(self, ):
        r"""Set leavewindow bit event mask.

        set_leavewindow()

        @Return:
        None
        """
        self.flags.set6()

    def reset_leavewindow(self, ):
        r"""Reset leavewindow bit event mask.

        reset_leavewindow()

        @Return:
        None
        """
        self.flags.reset6()

    def isleavewindow(self, ):
        r"""Check is flaged leavewindow bit event mask.

        isleavewindow()

        @Return:
        (bool)
        """
        return self.flags.isflaged6()

    def set_pointermotion(self, ):
        r"""Set pointermotion bit event mask.

        set_pointermotion()

        @Return:
        None
        """
        self.flags.set7()

    def reset_pointermotion(self, ):
        r"""Reset pointermotion bit event mask.

        reset_pointermotion()

        @Return:
        None
        """
        self.flags.reset7()

    def ispointermotion(self, ):
        r"""Check is flaged pointermotion bit event mask.

        ispointermotion()

        @Return:
        (bool)
        """
        return self.flags.isflaged7()

    def set_pointermotionhint(self, ):
        r"""Set pointermotionhint bit event mask.

        set_pointermotionhint()

        @Return:
        None
        """
        self.flags.set8()

    def reset_pointermotionhint(self, ):
        r"""Reset pointermotionhint bit event mask.

        reset_pointermotionhint()

        @Return:
        None
        """
        self.flags.reset8()

    def ispointermotionhint(self, ):
        r"""Check is flaged pointermotionhint bit event mask.

        ispointermotionhint()

        @Return:
        (bool)
        """
        return self.flags.isflaged8()

    def set_button1motion(self, ):
        r"""Set button1motion bit event mask.

        set_button1motion()

        @Return:
        None
        """
        self.flags.set9()

    def reset_button1motion(self, ):
        r"""Reset button1motion bit event mask.

        reset_button1motion()

        @Return:
        None
        """
        self.flags.reset9()

    def isbutton1motion(self, ):
        r"""Check is flaged button1motion bit event mask.

        isbutton1motion()

        @Return:
        (bool)
        """
        return self.flags.isflaged9()

    def set_button2motion(self, ):
        r"""Set button2motion bit event mask.

        set_button2motion()

        @Return:
        None
        """
        self.flags.set10()

    def reset_button2motion(self, ):
        r"""Reset button2motion bit event mask.

        reset_button2motion()

        @Return:
        None
        """
        self.flags.reset10()

    def isbutton2motion(self, ):
        r"""Check is flaged button2motion bit event mask.

        isbutton2motion()

        @Return:
        (bool)
        """
        return self.flags.isflaged10()

    def set_button3motion(self, ):
        r"""Set button3motion bit event mask.

        set_button3motion()

        @Return:
        None
        """
        self.flags.set11()

    def reset_button3motion(self, ):
        r"""Reset button3motion bit event mask.

        reset_button3motion()

        @Return:
        None
        """
        self.flags.reset11()

    def isbutton3motion(self, ):
        r"""Check is flaged button3motion bit event mask.

        isbutton3motion()

        @Return:
        (bool)
        """
        return self.flags.isflaged11()

    def set_button4motion(self, ):
        r"""Set button4motion bit event mask.

        set_button4motion()

        @Return:
        None
        """
        self.flags.set12()

    def reset_button4motion(self, ):
        r"""Reset button4motion bit event mask.

        reset_button4motion()

        @Return:
        None
        """
        self.flags.reset12()

    def isbutton4motion(self, ):
        r"""Check is flaged button4motion bit event mask.

        isbutton4motion()

        @Return:
        (bool)
        """
        return self.flags.isflaged12()

    def set_button5motion(self, ):
        r"""Set button5motion bit event mask.

        set_button5motion()

        @Return:
        None
        """
        self.flags.set13()

    def reset_button5motion(self, ):
        r"""Reset button5motion bit event mask.

        reset_button5motion()

        @Return:
        None
        """
        self.flags.reset13()

    def isbutton5motion(self, ):
        r"""Check is flaged button5motion bit event mask.

        isbutton5motion()

        @Return:
        (bool)
        """
        return self.flags.isflaged13()

    def set_buttonmotion(self, ):
        r"""Set buttonmotion bit event mask.

        set_buttonmotion()

        @Return:
        None
        """
        self.flags.set14()

    def reset_buttonmotion(self, ):
        r"""Reset buttonmotion bit event mask.

        reset_buttonmotion()

        @Return:
        None
        """
        self.flags.reset14()

    def isbuttonmotion(self, ):
        r"""Check is flaged buttonmotion bit event mask.

        isbuttonmotion()

        @Return:
        (bool)
        """
        return self.flags.isflaged14()

    def set_keymapstate(self, ):
        r"""Set keymapstate bit event mask.

        set_keymapstate()

        @Return:
        None
        """
        self.flags.set15()

    def reset_keymapstate(self, ):
        r"""Reset keymapstate bit event mask.

        reset_keymapstate()

        @Return:
        None
        """
        self.flags.reset15()

    def iskeymapstate(self, ):
        r"""Check is flaged keymapstate bit event mask.

        iskeymapstate()

        @Return:
        (bool)
        """
        return self.flags.isflaged15()

    def set_exposure(self, ):
        r"""Set exposure bit event mask.

        set_exposure()

        @Return:
        None
        """
        self.flags.set16()

    def reset_exposure(self, ):
        r"""Reset exposure bit event mask.

        reset_exposure()

        @Return:
        None
        """
        self.flags.reset16()

    def isexposure(self, ):
        r"""Check is flaged exposure bit event mask.

        isexposure()

        @Return:
        (bool)
        """
        return self.flags.isflaged16()

    def set_visibilitychange(self, ):
        r"""Set visibilitychange bit event mask.

        set_visibilitychange()

        @Return:
        None
        """
        self.flags.set17()

    def reset_visibilitychange(self, ):
        r"""Reset visibilitychange bit event mask.

        reset_visibilitychange()

        @Return:
        None
        """
        self.flags.reset17()

    def isvisibilitychange(self, ):
        r"""Check is flaged visibilitychange bit event mask.

        isvisibilitychange()

        @Return:
        (bool)
        """
        return self.flags.isflaged17()

    def set_structurenotify(self, ):
        r"""Set structurenotify bit event mask.

        set_structurenotify()

        @Return:
        None
        """
        self.flags.set18()

    def reset_structurenotify(self, ):
        r"""Reset structurenotify bit event mask.

        reset_structurenotify()

        @Return:
        None
        """
        self.flags.reset18()

    def isstructurenotify(self, ):
        r"""Check is flaged structurenotify bit event mask.

        isstructurenotify()

        @Return:
        (bool)
        """
        return self.flags.isflaged18()

    def set_resizeredirect(self, ):
        r"""Set resizeredirect bit event mask.

        set_resizeredirect()

        @Return:
        None
        """
        self.flags.set19()

    def reset_resizeredirect(self, ):
        r"""Reset resizeredirect bit event mask.

        reset_resizeredirect()

        @Return:
        None
        """
        self.flags.reset19()

    def isresizeredirect(self, ):
        r"""Check is flaged resizeredirect bit event mask.

        isresizeredirect()

        @Return:
        (bool)
        """
        return self.flags.isflaged19()

    def set_substructurenotify(self, ):
        r"""Set substructurenotify bit event mask.

        set_substructurenotify()

        @Return:
        None
        """
        self.flags.set20()

    def reset_substructurenotify(self, ):
        r"""Reset substructurenotify bit event mask.

        reset_substructurenotify()

        @Return:
        None
        """
        self.flags.reset20()

    def issubstructurenotify(self, ):
        r"""Check is flaged substructurenotify bit event mask.

        issubstructurenotify()

        @Return:
        (bool)
        """
        return self.flags.isflaged20()

    def set_substructureredirect(self, ):
        r"""Set substructureredirect bit event mask.

        set_substructureredirect()

        @Return:
        None
        """
        self.flags.set21()

    def reset_substructureredirect(self, ):
        r"""Reset substructureredirect bit event mask.

        reset_substructureredirect()

        @Return:
        None
        """
        self.flags.reset21()

    def issubstructureredirect(self, ):
        r"""Check is flaged substructureredirect bit event mask.

        issubstructureredirect()

        @Return:
        (bool)
        """
        return self.flags.isflaged21()

    def set_focuschange(self, ):
        r"""Set focuschange bit event mask.

        set_focuschange()

        @Return:
        None
        """
        self.flags.set22()

    def reset_focuschange(self, ):
        r"""Reset focuschange bit event mask.

        reset_focuschange()

        @Return:
        None
        """
        self.flags.reset22()

    def isfocuschange(self, ):
        r"""Check is flaged focuschange bit event mask.

        isfocuschange()

        @Return:
        (bool)
        """
        return self.flags.isflaged22()

    def set_propertychange(self, ):
        r"""Set propertychange bit event mask.

        set_propertychange()

        @Return:
        None
        """
        self.flags.set23()

    def reset_propertychange(self, ):
        r"""Reset propertychange bit event mask.

        reset_propertychange()

        @Return:
        None
        """
        self.flags.reset23()

    def ispropertychange(self, ):
        r"""Check is flaged propertychange bit event mask.

        ispropertychange()

        @Return:
        (bool)
        """
        return self.flags.isflaged23()

    def set_colormapchange(self, ):
        r"""Set colormapchange bit event mask.

        set_colormapchange()

        @Return:
        None
        """
        self.flags.set24()

    def reset_colormapchange(self, ):
        r"""Reset colormapchange bit event mask.

        reset_colormapchange()

        @Return:
        None
        """
        self.flags.reset24()

    def iscolormapchange(self, ):
        r"""Check is flaged colormapchange bit event mask.

        iscolormapchange()

        @Return:
        (bool)
        """
        return self.flags.isflaged24()

    def set_ownergrabbutton(self, ):
        r"""Set ownergrabbutton bit event mask.

        set_ownergrabbutton()

        @Return:
        None
        """
        self.flags.set25()

    def reset_ownergrabbutton(self, ):
        r"""Reset ownergrabbutton bit event mask.

        reset_ownergrabbutton()

        @Return:
        None
        """
        self.flags.reset25()

    def isownergrabbutton(self, ):
        r"""Check is flaged ownergrabbutton bit event mask.

        isownergrabbutton()

        @Return:
        (bool)
        """
        return self.flags.isflaged25()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# biteventmask.py ends here
