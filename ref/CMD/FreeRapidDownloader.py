#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id: FreeRapidDownloader.py 87 2013-11-30 07:34:05Z t1 $
# $Revision: 87 $
# $Date: 2013-11-30 16:34:05 +0900 (Sat, 30 Nov 2013) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2013-11-30 16:34:05 +0900 (Sat, 30 Nov 2013) $
""" FreeRapidDownloader -- for FreeRapidDownloader's info

$Revision: 87 $

"""


# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__revision__ = '$Revision: 87 $'
__version__ = '0.1.0'

FRD = {
    'binname': 'frd.jar',
    'binpath': '/media/portable/system/FRDPortable/App/FreeRapidDownloader/frd.jar',
    'proxy_path': ('/media/portable/system/FRDPortable/'
                    'App/FreeRapidDownloader/proxy.txt'),
       }


def test():
    pass


if __name__ == '__main__':
    test()


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# FreeRapidDownloader.py ends here
