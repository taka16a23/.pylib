#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
