#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""binder -- DESCRIPTION

"""
from xahk.bind.candidate import Candidate, Priority
from xahk.wm.window_spec import WindowAnySpec
from xahk.bind.key.service import KeyBindService
from xahk.utils.singleton import SingletonMeta


class KeyBinder(object):
    r"""KeyBinder

    KeyBinder is a object.
    Responsibility:
    """
    def __init__(self, spec, start=True, priority=Priority.Normal):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        self.candidate = Candidate(spec, priority=priority)
        self._service = KeyBindService()
        if start:
            self.start()

    def get_display(self, ):
        r"""SUMMARY

        get_display()

        @Return:

        @Error:
        """
        return self._service.get_display()

    display = property(get_display)

    def get_window_spec(self, ):
        r"""SUMMARY

        get_window_spec()

        @Return:

        @Error:
        """
        return self.candidate.get_window_spec()

    def set_window_spec(self, spec):
        r"""SUMMARY

        set_window_spec(spec)

        @Arguments:
        - `spec`:

        @Return:

        @Error:
        """
        self.candidate.set_window_spec(spec)

    spec = property(get_window_spec, set_window_spec)

    def get_priority(self, ):
        r"""SUMMARY

        get_priority()

        @Return:

        @Error:
        """
        return self.candidate.get_priority()

    def set_priority(self, priority):
        r"""SUMMARY

        set_priority(priority)

        @Arguments:
        - `priority`:

        @Return:

        @Error:
        """
        self.candidate.set_priority(priority)

    priority = property(get_priority, set_priority)

    def list_accelerators(self, ):
        r"""SUMMARY

        list_accelerators()

        @Return:

        @Error:
        """
        return self.candidate.list_accelerators()

    def bind(self, accelerator, handler):
        r"""SUMMARY

        bind(accelerator, handler)

        @Arguments:
        - `accelerator`:
        - `handler`:

        @Return:

        @Error:
        """
        self.candidate.register(accelerator, handler)
        if self.is_starting():
            self._service.reload()

    def unbind(self, accelerator):
        r"""SUMMARY

        unbind(accelerator)

        @Arguments:
        - `accelerator`:

        @Return:

        @Error:
        """
        self.candidate.unregister(accelerator)
        if self.is_starting():
            self._service.reload()

    def start(self, ):
        r"""SUMMARY

        start()

        @Return:

        @Error:
        """
        if self.is_starting():
            return
        self._service.add_candidate(self.candidate)

    def stop(self, ):
        r"""SUMMARY

        stop()

        @Return:

        @Error:
        """
        if not self.is_starting():
            return
        self._service.remove_candidate(self.candidate)

    def is_starting(self, ):
        r"""SUMMARY

        is_starting()

        @Return:

        @Error:
        """
        return self._service.has_candidate(self.candidate)


class GlobalKeyBinder(KeyBinder):
    r"""GlobalKeyBinder

    GlobalKeyBinder is a KeyBinder.
    Responsibility:
    """
    __metaclass__ = SingletonMeta

    def __init__(self, ):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        KeyBinder.__init__(self, WindowAnySpec(), priority=Priority.Low)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# binder.py ends here
