#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""error -- a parts of chrome

"""

import sys as _sys
import os as _os

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


class ChromeError(StandardError):
    r"""For chrome StandardError."""
    pass


class NoExistsFolderError(ChromeError):
    """Not Exist Folder in Bookmarks."""

    def __init__(self, name):
        self._name = name

    def __str__(self, ):
        return 'Not exists bookmarks folder "{}"'.format(self._name)


def _test():
    r"""Test function."""
    return _os.EX_OK

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# error.py ends here
