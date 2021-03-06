#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""__main__ -- DESCRIPTION

"""

import argparse
import sys as _sys
import os as _os

from pypimirror import mirror


# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__version__ = '0.1.0'


def _predef_options():
    parser = argparse.ArgumentParser(description=""" """)
    parser.add_argument('--version',
                        dest='version',
                        action='version',
                        version=__version__,
                        help='Version Strings.')
    parser.add_argument(dest='target',
                        action='store',
                        type=str,
                        help='A lot of messages.')
    # (yas/expand-link "argparse_add_argument" t)
    return parser


def _main():
    parser = _predef_options()
    opts = parser.parse_args()
    mirror(opts.target)
    # parser.print_usage()
    return _os.EX_OK

if __name__ == '__main__':
    _sys.exit(_main())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __main__.py ends here
