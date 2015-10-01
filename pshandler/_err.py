#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: _err.py 307 2015-02-07 03:48:46Z t1 $
# $Revision: 307 $
# $Date: 2015-02-07 12:48:46 +0900 (Sat, 07 Feb 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-02-07 12:48:46 +0900 (Sat, 07 Feb 2015) $

r"""_err -- DESCRIPTION

borrow from psutil

"""


class Error(Exception):
    r"""Error

    Error is a Exception.
    Responsibility:
    """


class NoSuchProcess(Error):
    r"""NoSuchProcess

    NoSuchProcess is a Error.
    Responsibility:
    """
    def __init__(self, pid, name=None, msg=None):
        Error.__init__(self)
        self.pid = pid
        self.name = name
        self.msg = msg
        if msg is None:
            if name:
                details = "(pid=%s, name=%s)" % (self.pid, repr(self.name))
            else:
                details = "(pid=%s)" % self.pid
            self.msg = "process no longer exists " + details

    def __str__(self):
        return self.msg


class AccessDenied(Error):
    r"""AccessDenied

    AccessDenied is a Error.
    Responsibility:
    """
    def __init__(self, pid=None, name=None, msg=None):
        Error.__init__(self)
        self.pid = pid
        self.name = name
        self.msg = msg
        if msg is None:
            if (pid is not None) and (name is not None):
                self.msg = "(pid=%s, name=%s)" % (pid, repr(name))
            elif (pid is not None):
                self.msg = "(pid=%s)" % self.pid
            else:
                self.msg = ""

    def __str__(self):
        return self.msg


class Timeout(Error):
    r"""Timeout

    Timeout is a Error.
    Responsibility:
    """
    def __init__(self, seconds, pid=None, name=None):
        Error.__init__(self)
        self.seconds = seconds
        self.pid = pid
        self.name = name
        self.msg = "timeout after %s seconds" % seconds
        if (pid is not None) and (name is not None):
            self.msg += " (pid=%s, name=%s)" % (pid, repr(name))
        elif (pid is not None):
            self.msg += " (pid=%s)" % self.pid

    def __str__(self):
        return self.msg



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _err.py ends here
