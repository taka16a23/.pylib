#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: _client.py 468 2015-08-19 05:49:01Z t1 $
# $Revision: 468 $
# $Date: 2015-08-19 14:49:01 +0900 (Wed, 19 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-19 14:49:01 +0900 (Wed, 19 Aug 2015) $

r"""_client -- DESCRIPTION

"""


class SSHAgentClient(object):
    """Class SSHAgentClient
    """
    # Operations
    def add_keys(self, paths, lifetime=None):
        """function add_key

        path:
        lifetime: int

        returns
        """
        return None # should raise NotImplementedError()

    def remove_key(self, path):
        """function remove_key

        path:

        returns
        """
        return None # should raise NotImplementedError()

    def has_key(self, path):
        """function has_key

        path:

        returns bool
        """
        return None # should raise NotImplementedError()

    def list_keys(self):
        """function list_keys

        returns
        """
        return None # should raise NotImplementedError()

    def delete_all(self):
        """function delete_all

        returns
        """
        return None # should raise NotImplementedError()

    def lock_agent(self):
        """function lock_agent

        returns
        """
        return None # should raise NotImplementedError()

    def unock_agent(self):
        """function unock_agent

        returns
        """
        return None # should raise NotImplementedError()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _client.py ends here
