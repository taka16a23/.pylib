#!/usr/bin/env python
# -*- coding: utf-8 -*-

r"""debug -- DESCRIPTION

"""
from task import TaskManagerObserver
from weekly2 import log


class LoggingTaskManager(TaskManagerObserver):
    r"""LoggingTaskManager

    LoggingTaskManager is a TaskManagerObserver.
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
        log.LOG.info('{0} {1} {0}'.format('=' * 20, 'Resuming!!'))
        log.LOG.debug(
            'Current Task {0.__class__.__name__}'.format(manager.current_task))

    def on_before_task(self, task):
        r"""SUMMARY

        on_before_task(task)

        @Arguments:
        - `task`:

        @Return:

        @Error:
        """
        log.LOG.info('Taking {0.__class__.__name__}'.format(task))

    def on_after_task(self, task):
        r"""SUMMARY

        on_after_task(task)

        @Arguments:
        - `task`:

        @Return:

        @Error:
        """
        log.LOG.debug('Finished {0.__class__.__name__}'.format(task))

    def on_completed_tasks(self, manager):
        r"""SUMMARY

        on_completed_tasks(manager)

        @Arguments:
        - `manager`:

        @Return:

        @Error:
        """
        log.LOG.debug('Completed Tasks')

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
# debug.py ends here
