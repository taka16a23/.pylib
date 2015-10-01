#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: abstract.py 285 2015-01-29 00:12:29Z t1 $
# $Revision: 285 $
# $Date: 2015-01-29 09:12:29 +0900 (Thu, 29 Jan 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-01-29 09:12:29 +0900 (Thu, 29 Jan 2015) $

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
