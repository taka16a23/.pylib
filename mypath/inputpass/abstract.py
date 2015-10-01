#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: abstract.py 263 2014-12-27 06:39:30Z t1 $
# $Revision: 263 $
# $Date: 2014-12-27 15:39:30 +0900 (Sat, 27 Dec 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-12-27 15:39:30 +0900 (Sat, 27 Dec 2014) $

r"""abstract -- DESCRIPTION

"""
from abc import ABCMeta, abstractmethod



class InputPass(object):
    r"""InputPass

    InputPass is a object.
    Responsibility:
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def input(self, ):
        pass

    @abstractmethod
    def set_prompt(self, msg):
        pass



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# abstract.py ends here
