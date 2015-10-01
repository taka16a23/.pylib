#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id: setup.py 87 2013-11-30 07:34:05Z t1 $
# $Revision: 87 $
# $Date: 2013-11-30 16:34:05 +0900 (Sat, 30 Nov 2013) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2013-11-30 16:34:05 +0900 (Sat, 30 Nov 2013) $

from distutils.core import setup
import py2exe

option = {'compressed'   : 1,
          'optimize'     : 2,
          'bundle_files' : 1}


setup(
    options = {'py2exe': option},
    windows = [{'script': 'ki_client.pyw',
                'icon_resources': [(1, 'server.ico')]}],

    zipfile = None)
