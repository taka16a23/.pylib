#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: redirect.py 92 2013-12-07 10:20:05Z t1 $
# $Revision: 92 $
# $Date: 2013-12-07 19:20:05 +0900 (Sat, 07 Dec 2013) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2013-12-07 19:20:05 +0900 (Sat, 07 Dec 2013) $

r"""redirect -- a part of sysutil

Redirect sys.stdout and sys.stderr
"""

import sys
import cStringIO
from contextlib import contextmanager

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__revision__ = '$Revision: 92 $'
__version__ = '0.1.0'

@contextmanager
def with_mute():
    r"""Context redirecting sys.stdout, sys.stderr.

    >>> import sys
    >>> with with_mute():
    ...     print('dummyprint')
    ...     sys.stderr.write('dummyprint')
    >>> print('recovered stdout')
    recovered stdout
    """
    _stdout, _stderr = sys.stdout, sys.stderr
    sys.stdout, sys.stderr = cStringIO.StringIO(), cStringIO.StringIO()
    yield
    sys.stdout, sys.stderr = _stdout, _stderr

@contextmanager
def with_nostdout():
    r"""Context redirecting sys.stdout, sys.stderr.

    >>> with with_nostdout():
    ...     print('dummyprint')
    >>> print('recoverd stdout')
    recoverd stdout
    """
    _stdout = sys.stdout
    sys.stdout = cStringIO.StringIO()
    yield
    sys.stdout = _stdout

@contextmanager
def with_nostderr():
    r"""Context redirecting sys.stderr.

    >>> with with_nostderr():
    ...     sys.stderr.write('dummyprint')
    """
    _stderr = sys.stderr
    sys.stderr = cStringIO.StringIO()
    yield
    sys.stderr = _stderr


def mute(func):
    r"""Decorator of redirecting sys.stdout, sys.stderr.

    >>> @mute
    ... def dummyfunc():
    ...     print('dummyprint')
    ...     sys.stderr.write('dummyprint')
    >>> dummyfunc()

    >>> print('recovered stdout')
    recovered stdout
    """
    def wrapped(*args, **kwargs):
        """Wrapper."""
        try:
            _stdout, _stderr = sys.stdout, sys.stderr
            sys.stdout, sys.stderr = cStringIO.StringIO(), cStringIO.StringIO()
            return func(*args, **kwargs)
        finally:
            sys.stdout, sys.stderr = _stdout, _stderr
    return wrapped


def mute_stdout(func):
    r"""Decorator of redirecting sys.stdout.

    >>> @mute_stdout
    ... def dummyfunc():
    ...     print('dummyprint')
    >>> dummyfunc()

    >>> print('recovered stdout')
    recovered stdout
    """
    def wrapped(*args, **kwargs):
        """Wrapper."""
        try:
            _stdout = sys.stdout
            sys.stdout = cStringIO.StringIO()
            return func(*args, **kwargs)
        finally:
            sys.stdout = _stdout
    return wrapped


def mute_stderr(func):
    r"""Decorator of redirecting sys.stderr.

    >>> import sys
    >>> @mute_stderr
    ... def dummyfunc():
    ...     sys.stderr.write('dummyprint')
    >>> dummyfunc()

    """
    def wrapped(*args, **kwargs):
        """Wrapper."""
        try:
            _stderr = sys.stderr
            sys.stderr = cStringIO.StringIO()
            return func(*args, **kwargs)
        finally:
            sys.stderr = _stderr
    return wrapped


def redirect(stdout=sys.stdout, stderr=sys.stderr):
    """Decorator of redirect sys.stdout, sys.stderr.

    @Arguments:
    - `stdout`: redirect to standard output.
    - `stderr`: redirect to standard error.

    @Examples
    @redirect(stdout=StringIO(), stderr=StringIO())
    def foo():
        print('hello')

    >>> import sys
    >>> from cStringIO import StringIO
    >>> @redirect(stdout=StringIO(), stderr=StringIO())
    ... def dummyfunc():
    ...     print('dummyprint')
    ...     sys.stdout.write('dummyprint')
    >>> dummyfunc()

    >>> print('recoverd stdout')
    recoverd stdout
    """

    def wrap(func):
        """Wrapper."""
        def newf(*args, **kwargs):
            """Make new function."""
            _stdout, _stderr = sys.stdout, sys.stderr
            sys.stdout, sys.stderr = stdout, stderr
            try:
                return func(*args, **kwargs)
            finally:
                sys.stdout, sys.stderr = _stdout, _stderr
        return newf
    return wrap



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# redirect.py ends here
