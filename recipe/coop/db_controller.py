#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""db_controller -- DESCRIPTION

"""
from abc import ABCMeta, abstractmethod


class CoopDatabaseControllerInterface(object):
    r"""CoopDatabaseControllerInterface

    CoopDatabaseControllerInterface is a object.
    Responsibility:
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def update_database(self, ): pass
    @abstractmethod
    def is_latest(self, ): pass


class CoopDatabaseController(CoopDatabaseControllerInterface):
    r"""CoopDatabaseController

    CoopDatabaseController is a CoopDatabaseControllerInterface.
    Responsibility:
    """



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# db_controller.py ends here
