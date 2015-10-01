#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: receiver.py 227 2014-09-13 08:15:46Z t1 $
# $Revision: 227 $
# $Date: 2014-09-13 17:15:46 +0900 (Sat, 13 Sep 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-09-13 17:15:46 +0900 (Sat, 13 Sep 2014) $
from abc import ABCMeta, abstractmethod


class Receiver:
    """Abstract class Receiver
    """
    __metaclass__ = ABCMeta

    # Operations
    @abstractmethod
    def set_received(self):
        raise NotImplementedError()

    @abstractmethod
    def get_received(self):
        raise NotImplementedError()

    @abstractmethod
    def issuccess(self):
        raise NotImplementedError()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# receiver.py ends here
