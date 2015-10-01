#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
