#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id: evolution.py 87 2013-11-30 07:34:05Z t1 $
# $Revision: 87 $
# $Date: 2013-11-30 16:34:05 +0900 (Sat, 30 Nov 2013) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2013-11-30 16:34:05 +0900 (Sat, 30 Nov 2013) $
""" evolution -- for evolution's informations

$Revision: 87 $

"""


# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__revision__ = '$Revision: 87 $'
__version__ = '0.1.0'

EVOLUTION = {
    'name': 'evolution',
    'bin': 'evolution',
    'binpath': '/usr/bin/evolution',
    'mailformat': 'mailto:%(mailto)s?cc=%(cc)s&subject=%(subject)s&body=%(body)s'
    }

EVELEMENT = {'mailto': '',
             'subject': '',
             'cc': '',
             'body': '',
             'attched': ''}


# full format
EVOLUTION.setdefault(
    'fmailformat', '{0} "{1}"'.format(
        EVOLUTION.get('binpath'), EVOLUTION.get('mailformat')))


def test():
    pass


if __name__ == '__main__':
    test()


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# evolution.py ends here
