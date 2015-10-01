#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""_manager -- DESCRIPTION

"""
from observer import Observable
from PickleSelf import PickleSelf


class TaskManager(PickleSelf, Observable):
    r"""TaskManager

    TaskManager is a PickleSelf, Observable.
    Responsibility:
    """
    def __init__(self, path):
        r"""

        @Arguments:
        - `path`:
        """
        PickleSelf.__init__(self, path)
        Observable.__init__(self)
        self._tasks = []
        self._index = 0

    def add_task(self, task):
        r"""SUMMARY

        add_task(task)

        @Arguments:
        - `task`:

        @Return:

        @Error:
        """
        self._tasks.append(task)
        self._notify_changed_tasks()

    def remove_task(self, task):
        r"""SUMMARY

        remove_task(task)

        @Arguments:
        - `task`:

        @Return:

        @Error:
        """
        self._tasks.remove(task)
        self._notify_changed_tasks()

    def has_task(self, task):
        r"""SUMMARY

        has_task(task)

        @Arguments:
        - `task`:

        @Return:

        @Error:
        """
        return task in self._tasks

    def clear_tasks(self, ):
        r"""SUMMARY

        clear_tasks()

        @Return:

        @Error:
        """
        self._tasks[:] = []
        self._notify_changed_tasks()

    def list_tasks(self, ):
        r"""SUMMARY

        list_tasks()

        @Return:

        @Error:
        """
        return self._tasks[:] # return new list

    def is_empty_tasks(self, ):
        r"""SUMMARY

        is_empty_tasks()

        @Return:

        @Error:
        """
        return bool(self._tasks)

    def start(self, ):
        r"""SUMMARY

        start()

        @Return:

        @Error:
        """
        if self.is_pickled():
            self._notify_resuming_tasks()
            obj = self.load_pickle()
            return obj.process_tasks()
        self._index = 0
        self.process_tasks()

    @property
    def current_task(self, ):
        r"""SUMMARY

        _current_task()

        @Return:

        @Error:
        """
        if self._index < len(self._tasks):
            return self._tasks[self._index]
        return None

    def process_tasks(self, ):
        r"""SUMMARY

        process_tasks()

        @Return:

        @Error:
        """
        while self.current_task:
            self._notify_before_task()
            if self.current_task.is_ready():
                self.current_task.execute()
            self._notify_after_task()
            self._index += 1
            self.dump_pickle()
        self.remove_pickle()
        self._notify_completed_tasks()

    def _notify_resuming_tasks(self, ):
        r"""SUMMARY

        _notify_resuming_tasks()

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_resuming_task(self)

    def _notify_before_task(self, ):
        r"""SUMMARY

        _notify_before_task()

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_before_task(self.current_task)

    def _notify_after_task(self, ):
        r"""SUMMARY

        _notify_after_task()

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_after_task(self.current_task)

    def _notify_completed_tasks(self, ):
        r"""SUMMARY

        _notify_completed_tasks()

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_completed_tasks(self)

    def _notify_changed_tasks(self, ):
        r"""SUMMARY

        _notify_changed_tasks()

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_changed_tasks(self)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _manager.py ends here
