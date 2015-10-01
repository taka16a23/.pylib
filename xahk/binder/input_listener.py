#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""input_listener -- DESCRIPTION

"""
from observer import Observable


class InputListener(Observable):
    """Class InputListener
    """
    # Attributes:
    def __init__(self, ):
        r"""
        """
        Observable.__init__(self)
        self._binding = {} # (<Accelerator, handler>)

    # Operations
    def register_accelerator(self, accelerator, handler):
        """function register_accelerator

        accelerator:
        handler:

        returns
        """
        self._binding[accelerator] = handler
        self._register_accelerator_impl([accelerator])
        self._notify_regisetered_accelerator(accelerator, handler)

    def register_accelerators(self, accelerator_map):
        """function register_accelerators

        accelerator_map:

        returns
        """
        self._register_accelerator_impl(accelerator_map.keys())
        for accelerator, handler in accelerator_map.iteritems():
            self._binding[accelerator] = handler
            self._notify_regisetered_accelerator(accelerator, handler)

    def _notify_regisetered_accelerator(self, accelerator, handler):
        r"""SUMMARY

        _notify_regisetered_accelerator(Accelerator, handler)

        @Arguments:
        - `Accelerator`:
        - `handler`:

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_registered_accelerator(accelerator, handler)

    def unregister_accelerator(self, accelerator):
        """function unregister_accelerator

        accelerator:

        returns
        """
        if accelerator in self._binding:
            del self._binding[accelerator]
        self._unregister_accelerator_impl([accelerator])
        self._notify_unregistered_accelerator(accelerator)

    def clear_accelerators(self):
        """function clear_accelerators

        returns
        """
        self._unregister_accelerator_impl(self.list_accelerators())
        for accelerator in self.list_accelerators():
            self._notify_unregistered_accelerator(accelerator)
        self._binding.clear()

    def _notify_unregistered_accelerator(self, accelerator):
        r"""SUMMARY

        _notify_unregistered_accelerator(accelerator)

        @Arguments:
        - `accelerator`:

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_unregistered_accelerator(accelerator)

    def list_accelerators(self):
        """function list_accelerators

        returns
        """
        return self._binding.keys()

    def list_handlers(self):
        """function list_handlers

        returns
        """
        return self._binding.values()

    def iteritems(self):
        """function iteritems

        returns
        """
        return self._binding.iteritems()

    def items(self):
        """function items

        returns
        """
        return self._binding.items()

    def _register_accelerator_impl(self, accelerator):
        """function register_accelerator_impl

        accelerator:

        returns
        """
        pass

    def _unregister_accelerator_impl(self, accelerator):
        """function unregister_accelerator_impl

        accelerator:

        returns
        """
        pass



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# input_listener.py ends here
