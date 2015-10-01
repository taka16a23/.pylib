#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""notifier -- DESCRIPTION

"""
import notify2
from task import TaskManagerObserver


STARRED_ICON_PATH = '/usr/share/icons/gnome/24x24/status/starred.png'
WARNING_ICON_PATH = '/usr/share/icons/gnome/24x24/status/dialog-warning.png'
ERROR_ICON_PATH = '/usr/share/icons/gnome/24x24/status/dialog-error.png'


class Notifier(TaskManagerObserver):
    r"""Notifier

    Notifier is a object.
    Responsibility:
    """
    def __init__(self, timeout=3000):
        r"""

        @Arguments:
        - `timeout`:
        """
        TaskManagerObserver.__init__(self)
        self._timeout = timeout

    def on_resuming_task(self, manager):
        r"""SUMMARY

        on_resuming_task(manager)

        @Arguments:
        - `manager`:

        @Return:

        @Error:
        """
        notify2.init('Task')
        notif = notify2.Notification('Resuming {}'.format('Daily2'),
                                     'Current {0.__class__.__name__}'
                                     .format(manager.current_task),
                                     WARNING_ICON_PATH)
        notif.set_timeout(self._timeout)
        notif.show()

    def on_before_task(self, task):
        r"""SUMMARY

        on_before_task(task)

        @Arguments:
        - `task`:

        @Return:

        @Error:
        """
        if not task.is_ready():
            return
        notify2.init('Task')
        notif = notify2.Notification('{0.__class__.__name__}'.format(task),
                                     '', STARRED_ICON_PATH)
        notif.set_timeout(self._timeout)
        notif.show()

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
        notify2.init('Task')
        notif = notify2.Notification('Completed {}'.format('Daily2'),
                                     'Current {0.__class__.__name__}'
                                     .format(manager.current_task),
                                     STARRED_ICON_PATH)
        notif.set_timeout(self._timeout)
        notif.show()

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
# notifier.py ends here
