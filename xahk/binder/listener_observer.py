#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""listener_observer -- DESCRIPTION

"""


class ListenerObserver(object):
    """Class ListenerObserver
    """
    # Attributes:

    # Operations
    def on_registered_accelerator(self, accelerator, handler):
        """function on_registered_accelerator

        accelerator:
        cmd:

        returns
        """
        return None # should raise NotImplementedError()

    def on_unregistered_accelerator(self, accelerator):
        """function on_unregistered_accelerator

        accelerator:

        returns
        """
        return None # should raise NotImplementedError()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# listener_observer.py ends here
