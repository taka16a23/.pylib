#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: listener_observer.py 339 2015-07-23 18:01:26Z t1 $
# $Revision: 339 $
# $Date: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $

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
