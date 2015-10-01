#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: __init__.py 443 2015-08-07 01:26:03Z t1 $
# $Revision: 443 $
# $Date: 2015-08-07 10:26:03 +0900 (Fri, 07 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-07 10:26:03 +0900 (Fri, 07 Aug 2015) $

r"""Name: __init__.py


"""
import pyutmp


__revision__ = "$Revision: 443 $"
__version__ = "0.0.1"

__all__ = ['RunLevel', 'get_runlvl_utmp', ]


def get_runlvl_utmp():
    r"""SUMMARY

    get_runlvl_utmp()

    @Return:

    @Error:
    """
    for utmp in pyutmp.UtmpFile():
        if utmp.ut_type == 'RUN_LVL':
            return utmp
    return None


class RunLevel(object):
    r"""RunLevel

    RunLevel is a object.
    Responsibility:
    """
    def __init__(self, ):
        r"""

        @Arguments:
        - `previous`:
        - `current`:
        """
        utmp = get_runlvl_utmp()
        if utmp is None:
            # TODO: (Atami) [2015/08/07]
            raise StandardError('unknown: utmp error')
        prev = utmp.ut_pid / 256
        if prev == 0:
            self.previous = 'N'
        else:
            self.previous = '{0:c}'.format(prev)
        self.current = '{0:c}'.format(utmp.ut_pid % 256)

    def get_previous_level(self, ):
        r"""SUMMARY

        get_previous_level()

        @Return:

        @Error:
        """
        return self.previous

    def get_current_level(self, ):
        r"""SUMMARY

        get_current_level()

        @Return:

        @Error:
        """
        return self.current



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
