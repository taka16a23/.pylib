#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: key_bind_service_observer.py 339 2015-07-23 18:01:26Z t1 $
# $Revision: 339 $
# $Date: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 03:01:26 +0900 (Fri, 24 Jul 2015) $

r"""key_bind_service_observer -- DESCRIPTION

"""


class KeyBindServiceObserver(object):
    """Class KeyBindServiceObserver
    """
    # Attributes:

    # Operations
    def on_created_listener(self, listener):
        """function on_created_listener

        listener:

        returns
        """
        return None # should raise NotImplementedError()

    def on_destroyed_listener(self, listener):
        """function on_destroyed_listener

        listener:

        returns
        """
        return None # should raise NotImplementedError()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# key_bind_service_observer.py ends here
