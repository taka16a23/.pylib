#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: candidate.py 339 2015-07-23 18:01:26Z t1 $
# $Revision: 339 $
# $Date: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $

r"""candidate -- DESCRIPTION

"""
from observer import Observable


class Candidate(Observable):
    """Class Candidate
    """
    # Attributes:
    def __init__(self, spec):
        r"""

        @Arguments:
        - `spec`:
        """
        Observable.__init__(self)
        self.spec = spec
        self._accelerator_map = {}

    # Operations
    def is_satisfied(self, window):
        """function is_satisfied

        window:

        returns
        """
        return self.spec.is_satisfied(window)

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

    def build_listener(self, listener):
        """function build_listener

        listener:

        returns
        """
        listener.register_accelerators(self._accelerator_map)

    def register(self, accelerator, handler):
        """function register_candidate_accelerator

        accelerator:
        handler:

        returns
        """
        # TODO: (Atami) [2015/07/04]
        # raise error if already exists
        self._accelerator_map[accelerator] = handler
        self._notify_changed_accelerator()

    def unregister(self, accelerator):
        """function unregister_candidate_accelerator

        accelerator:

        returns
        """
        del self._accelerator_map[accelerator]
        self._notify_changed_accelerator()

    def is_registered(self, accelerator):
        """function is_registered_candidate_accelerator

        accelerator:

        returns bool
        """
        return accelerator in self._accelerator_map

    def _notify_changed_accelerator(self, ):
        r"""SUMMARY

        _notify_changed_accelerator()

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_changed_candidate_member(self)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# candidate.py ends here
