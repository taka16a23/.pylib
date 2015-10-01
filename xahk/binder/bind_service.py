#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: bind_service.py 463 2015-08-17 07:02:19Z t1 $
# $Revision: 463 $
# $Date: 2015-08-17 16:02:19 +0900 (Mon, 17 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-17 16:02:19 +0900 (Mon, 17 Aug 2015) $

r"""bind_service -- DESCRIPTION

"""
from xahk.binder.candidate_proxy_observer import CandidateProxyObserver
from xahk.binder.candidate_proxy import CandidateProxy


class BindService(CandidateProxyObserver):
    """Class BindService
    """
    # Attributes:
    def __init__(self, ):
        r"""
        """
        self._candidate_proxy = CandidateProxy()
        self._candidate_proxy.add_observer(self)
        self._is_serving = False

    # Operations
    def get_candidate_proxy(self):
        """function get_candidate_proxy

        returns
        """
        return self._candidate_proxy

    def set_candidate_proxy(self, proxy):
        """function set_candidate_proxy

        proxy:

        returns
        """
        self._candidate_proxy.remove_observer(self)
        self._candidate_proxy = proxy
        self._candidate_proxy.add_observer(self)
        self.update_listener()

    def list_candidates(self, ):
        r"""SUMMARY

        list_candidates()

        @Return:

        @Error:
        """
        return self._candidate_proxy.list_candidates()

    def entry_candidate(self, candidate, priority=5):
        """function entry_candidate

        candidate:

        returns
        """
        self._candidate_proxy.entry_candidate(candidate, priority)

    def withdraw_candidate(self, candidate):
        """function withdraw_candidate

        candidate:

        returns
        """
        self._candidate_proxy.withdraw_candidate(candidate)

    def has_candidate(self, candidate):
        """function has_candidate

        candidate:

        returns bool
        """
        return self._candidate_proxy.has_candidate(candidate)

    def counts_candidates(self):
        """function counts_candidates

        returns
        """
        return self._candidate_proxy.counts_candidates()

    def elect_candidates(self, window):
        """function elect_candidates

        window:

        returns
        """
        return self._candidate_proxy.elect_candidates(window)

    def on_changed_candidate(self):
        """function on_changed_candidate

        returns
        """
        self.update_listener()

    def update_listener(self):
        """function update_listener

        returns
        """
        raise NotImplementedError()

    def start_service(self):
        """function start_service

        returns bool
        """
        raise NotImplementedError()

    def stop_service(self):
        """function stop_service

        returns
        """
        raise NotImplementedError()

    def is_serving(self):
        """function is_serving

        returns
        """
        return self._is_serving



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# bind_service.py ends here
