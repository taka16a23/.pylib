#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: func.py 351 2015-08-05 21:00:40Z t1 $
# $Revision: 351 $
# $Date: 2015-08-06 06:00:40 +0900 (Thu, 06 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-06 06:00:40 +0900 (Thu, 06 Aug 2015) $

r"""func -- DESCRIPTION

"""
import sys as _sys

from getpasswd.core import GetPasswd
from getpasswd.getter import * # must int


if  _sys.stdout.isatty():
    GETPASSWD = GetPasswd()
elif 'WXPassGetter' in globals():
    GETPASSWD = GetPasswd(WXPassGetter())
else:
    GETPASSWD = GetPasswd(EasyGUIPassGetter())


def confirm_passwd(prompt1='Passwrod: ', prompt2='Confirm: '):
    r"""SUMMARY

    confirm_passwd(prompt1='Passwrod: ', prompt2='Confirm: ')

    @Arguments:
    - `prompt`:
    - `prompt2`:
    - `times`:

    @Return:

    @Error:
    """
    pass1 = GETPASSWD(prompt1)
    if pass1 == GETPASSWD(prompt2):
        return pass1



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# func.py ends here
