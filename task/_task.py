#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: _task.py 350 2015-08-04 22:36:15Z t1 $
# $Revision: 350 $
# $Date: 2015-08-05 07:36:15 +0900 (Wed, 05 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-05 07:36:15 +0900 (Wed, 05 Aug 2015) $

r"""_task -- DESCRIPTION

"""
from abc import ABCMeta, abstractmethod


class Task(object):
    r"""Task

    Task is a object.
    Responsibility:
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def is_ready(self, ):
        r"""SUMMARY

        is_ready()

        @Return:

        @Error:
        """

    @abstractmethod
    def execute(self, ):
        r"""SUMMARY

        execute()

        @Return:

        @Error:
        """



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _task.py ends here
