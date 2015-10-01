#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""_client_x11 -- DESCRIPTION

"""
import subprocess as sbp
from mypcs._ssh.agent._client import SSHAgentClient


class SSHAgentClientX11(SSHAgentClient):
    """Class SSHAgentClientX11
    """
    # Attributes:

    # Operations
    def add_keys(self, paths, lifetime=None):
        """function add_key

        path: list
        lifetime: int

        returns
        """
        # TODO: (Atami) [2015/08/16]
        cmds = ['/usr/bin/ssh-add', ]
        if lifetime:
            cmds.extend(['-t', str(lifetime)])
        cmds.extend(paths)
        return sbp.call(cmds)

    def remove_key(self, paths):
        """function remove_key

        path:

        returns
        """
        cmds = ['/usr/bin/ssh-add', '-d']
        cmds.extend(paths)
        return sbp.call(cmds)

    def has_key(self, path):
        """function has_key

        path:

        returns bool
        """
        return path in self.list_keys()

    def list_keys(self):
        """function list_keys

        returns
        """
        proc = sbp.Popen(['/usr/bin/ssh-add', '-l'],
                         stdout=sbp.PIPE, stderr=sbp.PIPE)
        retcode = proc.wait()
        if retcode != 0:
            return []
        return [x.split(' ')[2] for x in proc.stdout.xreadlines() if x]

    def delete_all(self):
        """function delete_all

        returns
        """
        sbp.Popen(['/usr/bin/ssh-add', '-D'], stdout=sbp.PIPE, stderr=sbp.PIPE)

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
# _client_x11.py ends here
