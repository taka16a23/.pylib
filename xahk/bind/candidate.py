#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""candidate -- DESCRIPTION

"""
from abc import ABCMeta, abstractmethod
from enum import IntEnum


class Priority(IntEnum):
    r"""Priority

    Priority is a IntEnum.
    Responsibility:
    """
    Low = -20
    Minor = -10
    Normal = 0
    Medium = 10
    High = 20


class CandidateInterface(object):
    r"""CandidateInterface

    CandidateInterface is a object.
    Responsibility:
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def can_bind_window(self, window):
        r"""SUMMARY

        can_bind_window(window)

        @Arguments:
        - `window`: WindowClientListener

        @Return:

        @Error:
        """

    @abstractmethod
    def build_binder(self, binder):
        r"""SUMMARY

        build_binder(binder)

        @Arguments:
        - `binder`:

        @Return:

        @Error:
        """


class Candidate(CandidateInterface):
    """Class Candidate

    candidate for binding service
    """
    # Attributes:
    def __init__(self, spec, priority=Priority.Normal):
        r"""

        @Arguments:
        - `spec`:
        """
        self.spec = spec
        self.priority = priority
        self._accelerator_map = {}

    # Operations
    def get_window_spec(self, ):
        r"""SUMMARY

        get_window_spec()

        @Return:

        @Error:
        """
        return self.spec

    def set_window_spec(self, spec):
        r"""SUMMARY

        set_window_spec(spec)

        @Arguments:
        - `spec`:

        @Return:

        @Error:
        """
        self.spec = spec

    def get_priority(self, ):
        r"""SUMMARY

        get_priority()

        @Return:

        @Error:
        """
        return self.priority

    def set_priority(self, priority):
        r"""SUMMARY

        set_priority(priority)

        @Arguments:
        - `priority`:

        @Return:

        @Error:
        """
        self.priority = priority

    def can_bind_window(self, window):
        """function can_bind_window

        @Arguments:
        - `window`: WindowClientListener

        @Return:

        window:

        """
        return self.spec.is_satisfied_window(window)

    def build_binder(self, binder):
        """function build_listener

        listener:

        returns
        """
        cookies = []
        extend = cookies.extend
        for accelerator, handler in self._accelerator_map.iteritems():
            extend(binder.bind(accelerator, handler))
        return cookies

    def register(self, accelerator, handler):
        """function register_candidate_accelerator

        accelerator:
        handler:

        returns
        """
        # TODO: (Atami) [2015/07/04]
        # raise error if already exists
        self._accelerator_map[accelerator] = handler

    def unregister(self, accelerator):
        """function unregister_candidate_accelerator

        accelerator:

        returns
        """
        del self._accelerator_map[accelerator]

    def is_registered(self, accelerator):
        """function is_registered_candidate_accelerator

        accelerator:

        returns bool
        """
        return accelerator in self._accelerator_map

    def list_accelerators(self, ):
        r"""SUMMARY

        list_accelerators()

        @Return:

        @Error:
        """
        return self._accelerator_map.keys()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# candidate.py ends here
