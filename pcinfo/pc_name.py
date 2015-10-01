#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: pc_name.py 483 2015-09-19 22:10:00Z t1 $
# $Revision: 483 $
# $Date: 2015-09-20 07:10:00 +0900 (Sun, 20 Sep 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-09-20 07:10:00 +0900 (Sun, 20 Sep 2015) $

r"""pc_name -- DESCRIPTION

"""
import sys as _sys
import os as _os
from socket import gethostname


__revision__ = '$Revision: 483 $'
__version__ = '0.1.0'


def pc_name():
    r"""SUMMARY

    pc_name()

    @Return:
    """
    return gethostname()


def _test():
    r"""Test function."""
    return _os.EX_OK

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# pc_name.py ends here
