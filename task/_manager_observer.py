#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
