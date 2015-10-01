#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: resource.py 306 2015-02-07 03:48:07Z t1 $
# $Revision: 306 $
# $Date: 2015-02-07 12:48:07 +0900 (Sat, 07 Feb 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-02-07 12:48:07 +0900 (Sat, 07 Feb 2015) $

r"""resource -- DESCRIPTION

"""
import wxcb.xobj.display as _display
import wxcb.xobj.rid as _rid
import wxcb.conn


class Resource(object):
    r"""Resource

    Resource is a object.
    Responsibility:
    """
    def __init__(self, rid, display=None):
        r"""

        @Arguments:
        - `rid`:
        - `display`:
        """
        self._rid = _rid.Id(rid)
        self._display = _display.Display(display)

    def get_display(self, ):
        r"""SUMMARY

        get_display()

        @Return:

        @Error:
        """
        return self._display

    def set_display(self, display):
        r"""SUMMARY

        set_display(display)

        @Arguments:
        - `display`:

        @Return:

        @Error:
        """
        self._display.set(display)

    display = property(get_display, set_display)

    def get_id(self, ):
        r"""SUMMARY

        get_id()

        @Return:

        @Error:
        """
        return self._rid

    def set_id(self, id_):
        r"""SUMMARY

        set_id(id_)

        @Arguments:
        - `id_`:

        @Return:

        @Error:
        """
        self._rid.set(id_)

    id = property(get_id, set_id)

    def __int__(self):
        return self._rid

    def __cmp__(self, other):
        """
        self < other return -1
        self > other return 1
        self == other return 0
        """
        if isinstance(other, (self.__class__, )):
            return cmp(self._rid, other.get_id())
        return cmp(self._rid, other)

    def __hash__(self, ):
        return self._rid

    def __repr__(self):
        return '{0.__class__.__name__}(id={0.id})'.format(self)

    def __str__(self, ):
        return '{0.__class__.__name__}(id={0.id})'.format(self)

    def kill_client(self, ):
        r"""SUMMARY

        kill_client()

        @Return:
        """
        return self.id.kill_client(self.display)

    def flush(self, ):
        r"""SUMMARY

        flush()

        @Return:

        @Error:
        """
        self.display.flush()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# resource.py ends here
