#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: abstract.py 244 2014-12-21 05:15:27Z t1 $
# $Revision: 244 $
# $Date: 2014-12-21 14:15:27 +0900 (Sun, 21 Dec 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-12-21 14:15:27 +0900 (Sun, 21 Dec 2014) $

r"""_getter -- DESCRIPTION

"""
from abc import ABCMeta, abstractmethod


class PassGetter(object):
    r"""PassGetter

    PassGetter is a object.
    Responsibility:
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def getpass(self, prompt='Password: '):
        pass





# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _getter.py ends here
