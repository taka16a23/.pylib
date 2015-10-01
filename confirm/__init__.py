#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id: __init__.py 229 2014-09-13 08:17:28Z t1 $
# $Revision: 229 $
# $Date: 2014-09-13 17:17:28 +0900 (Sat, 13 Sep 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-09-13 17:17:28 +0900 (Sat, 13 Sep 2014) $
r"""\
Name: __init__.py

2014/09/12: (v0.2.0) Add object ConsoleConfirm, GUIConfirm, Confirmer

"""


import sys as _sys
from confirm.confirmobj import ConsoleConfirm, GUIConfirm
from confirm.confirmer import Confirmer


__revision__ = "$Revision: 229 $"
__version__ = "0.2.0"


__all__ = ['confirm', 'yesno', 'wait_enter', 'yesnodialog', 'ConsoleConfirm',
           'GUIConfirm', 'Confirmer']


YES = ['y', 'Y', 'yes', 'YES']
NOP = ['n', 'N', 'no', 'NO']

def confirm(prompt='Confirm'):
    """Yes or No prompt."""
    prompt = '%s "y" or "n": ' % (prompt)
    yesnop = YES + NOP

    try:
        while 1:
            ans = raw_input(prompt)
            if not ans or ans not in yesnop:
                print "Set input " + ", ".join(yesnop)
                continue
            if ans in YES:
                return True
            if ans in NOP:
                return False
    except KeyboardInterrupt:
        print('KeyboardInterrupted!!')


def yesno(text='\rPlease enter yes/no[y/n]: '):
    """Yes No prompt.

    @Arguments:
    - `text`:

    @Return:
    yes = True
    no = False
    """
    while 1:
        try:
            _sys.stdout.write(text)
            query = raw_input().lower()
            if 'y' == query[0]:
                return True
            if 'n' == query[0]:
                return False
        except KeyboardInterrupt:
            print('KeyboardInterrupted!!')
            break

def wait_enter(text='\rPlease enter: '):
    """SUMMARY

    @Arguments:
    - `text`:

    @Return:
    """
    _sys.stdout.write(text)
    raw_input()
    return

def yesnodialog(title, message):
    """SUMMARY

    @Arguments:
    - `title`:
    - `message`:

    @Return:
    """
    import Tkinter
    import tkMessageBox
    root = Tkinter.Tk()
    root.withdraw()
    return tkMessageBox.askyesno(title, message)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
