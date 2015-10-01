#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: candidate_proxy.py 339 2015-07-23 18:01:26Z t1 $
# $Revision: 339 $
# $Date: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $

r"""candidate_proxy -- DESCRIPTION

"""
from observer import Observable

from xahk.binder.candidate_observer import CandidateObserver


class CandidateProxy(Observable, CandidateObserver):
    """Class CandidateProxy
    """
    # Attributes:
    def __init__(self, ):
        r"""
        """
        Observable.__init__(self)
        self._candidates = [] # ([(num, candidate),])

    # Operations
    def build_listener(self, window, listener):
        """function build_listener

        window:
        listener:

        returns
        """
        for candidate in self.elect_candidates(window):
            candidate.build_listener(listener)

    def entry_candidate(self, candidate, priority=5):
        """function entry_candidate

        candidate:
        priority: int

        returns
        """
        if self.has_candidate(candidate):
            # TODO: (Atami) [2015/07/04]
            raise StandardError()
        self._candidates.append((priority, candidate))
        candidate.add_observer(self)
        self._candidates.sort()
        self._notify_changed_candidate()

    def withdraw_candidate(self, candidate):
        """function withdraw_candidate

        candidate:

        returns
        """
        for pri, cand in self._candidates[:]:
            if cand == candidate:
                self._candidates.remove((pri, cand))
                cand.remove_observer(self)
                self._notify_changed_candidate()

    def has_candidate(self, candidate):
        """function has_candidate

        candidate:

        returns
        """
        return candidate in self.list_candidates()

    def counts_candidates(self):
        """function counts_candidates

        returns int
        """
        return len(self._candidates)

    def elect_candidates(self, window):
        """function elect_candidates

        window:

        returns
        """
        return [x for x in self.list_candidates() if x.is_satisfied(window)]

    def get_priority(self, candidate):
        """function get_priority

        candidate:

        returns
        """
        return None # should raise NotImplementedError()

    def list_candidates(self):
        """function list_candidates

        returns
        """
        return [x for _, x in self._candidates]

    def on_changed_candidate_member(self, candidate):
        """function on_changed_candidate_member

        returns
        """
        self._notify_changed_candidate()

    def _notify_changed_candidate(self):
        """function notify_changed_candidate

        returns
        """
        for observer in self._observers:
            observer.on_changed_candidate()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# candidate_proxy.py ends here
