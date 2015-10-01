#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: debug.py 349 2015-08-04 22:35:27Z t1 $
# $Revision: 349 $
# $Date: 2015-08-05 07:35:27 +0900 (Wed, 05 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-05 07:35:27 +0900 (Wed, 05 Aug 2015) $

r"""debug -- DESCRIPTION

"""
from task import TaskManagerObserver
from daily2 import log


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
