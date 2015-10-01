#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" evolution -- for evolution's informations


"""


# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


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
