#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: _manager_observer.py 350 2015-08-04 22:36:15Z t1 $
# $Revision: 350 $
# $Date: 2015-08-05 07:36:15 +0900 (Wed, 05 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-05 07:36:15 +0900 (Wed, 05 Aug 2015) $

r"""_manager_observer -- DESCRIPTION

"""


class TaskManagerObserver(object):
    r"""TaskManagerObserver

    TaskManagerObserver is a object.
    Responsibility:
    """
    def on_resuming_task(self, manager):
        r"""SUMMARY

        on_resuming_task(manager)

        @Arguments:
        - `manager`:

        @Return:

        @Error:
        """

    def on_before_task(self, task):
        r"""SUMMARY

        on_before_task(task)

        @Arguments:
        - `task`:

        @Return:

        @Error:
        """

    def on_after_task(self, task):
        r"""SUMMARY

        on_after_task(task)

        @Arguments:
        - `task`:

        @Return:

        @Error:
        """

    def on_completed_tasks(self, manager):
        r"""SUMMARY

        on_completed_tasks(manager)

        @Arguments:
        - `manager`:

        @Return:

        @Error:
        """

    def on_changed_tasks(self, manager):
        r"""SUMMARY

        on_changed_tasks(manager)

        @Arguments:
        - `manager`:

        @Return:

        @Error:
        """



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _manager_observer.py ends here
