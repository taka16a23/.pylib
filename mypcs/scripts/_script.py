#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: _script.py 464 2015-08-17 07:02:48Z t1 $
# $Revision: 464 $
# $Date: 2015-08-17 16:02:48 +0900 (Mon, 17 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-17 16:02:48 +0900 (Mon, 17 Aug 2015) $

r"""_script -- DESCRIPTION

"""
from abc import ABCMeta, abstractmethod


class Script(object):
    """Abstract class Script
    """
    __metaclass__ = ABCMeta

    # Operations
    @abstractmethod
    def execute_script(self, shell):
        """function execute_script

        shell:

        returns
        """
        raise NotImplementedError()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _script.py ends here
