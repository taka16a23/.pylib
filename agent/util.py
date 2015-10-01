#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: util.py 261 2014-12-27 06:38:46Z t1 $
# $Revision: 261 $
# $Date: 2014-12-27 15:38:46 +0900 (Sat, 27 Dec 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-12-27 15:38:46 +0900 (Sat, 27 Dec 2014) $

r"""util -- DESCRIPTION

"""
import os as _os
import paramiko as _paramiko


if 'nt' == _os.name:
    from nt_agent import add_keys
elif 'posix' == _os.name:
    from posix_agent import add_keys
else:
    raise NotImplementedError('not supported {.name} environment'.format(_os))


class AgentUtils(object):
    """
    """
    def __init__(self, kagi, kagiMD5):
        r"""SUMMARY

        __init__(kagi, kagiMD5)

        @Arguments:
        - `kagi`:
        - `kagiMD5`:

        @Return:
        """
        self.kagi = kagi
        self.kagiMD5 = kagiMD5

    def haskeyring(self):
        """Check key in agent.
        """
        return self._haskeyring(self.kagiMD5)

    def _haskeyring(self, md5):
        """Check key in agent.
        """
        keys = self.get_keys()
        if not keys:
            return False
        return (md5 in [x.get_fingerprint() for x in keys])

    def get_keys(self):
        """summary
        """
        return _paramiko.Agent().get_keys()

    def add_keys(self):
        """summary
        """
        add_keys(self.kagi)





# For Emacs
# Local Variables:
# coding: utf-8
# End:
# util.py ends here
