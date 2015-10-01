#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" ps -- process for windows

"""


__version__ = "0.1.0"

import win32com.client


def find_process(name):
    objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
    objSWbemServices = objWMIService.ConnectServer(".", "root\cimv2")
    colItems = objSWbemServices.ExecQuery(
         "Select * from Win32_Process where Caption = '{0}'".format(name))
    return len(colItems)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# ps.py ends here
