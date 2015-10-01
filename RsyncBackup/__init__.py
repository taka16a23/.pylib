#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id$
# $Revision$
# $Date$
# $Author$
# $LastChangedBy$
# $LastChangedDate$
r"""\
Name: __init__.py


"""


from .local import LinkDestLocalBackup
from .remote import LinkDestRemoteBackup


# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__revision__ = '$Revision$'
__version__ = '0.1.0'


def _test():
    pass


if __name__ == '__main__':
    _test()


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# RsyncBackup.py ends here
