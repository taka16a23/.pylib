#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""\
Name: __main__.py

"""

import os as _os
import sys
import argparse
from .__init__ import path_checker, Overview, my_epydoc
import tempfile

# for debug
import cgitb
cgitb.enable(format='text')


__version__ = '0.1.0'


def _predef_options():
    parser = argparse.ArgumentParser(description=""" """)
    parser.add_argument('--version',
                        dest='version',
                        action='version',
                        version=__version__,
                        help='Version Strings.')
    parser.add_argument('file',
                        action='store',
                        help='File name.')
                        # (yas/expand-link "argparse_add_argument")
    # (yas/expand-link "argparse_add_argument" t)
    return parser

def _main():
    r"""Main function."""
    parser = _predef_options()
    opts = parser.parse_args()
    target = _os.path.abspath(_os.path.normcase(opts.file))
    path_checker(target)
    # parser.print_usage()

    tmpdir = tempfile.mkdtemp()

    # if _os.path.isfile(target):
    #     dst_dir = _os.path.splitext(target)[0]
    # elif _os.path.isdir(target):
    #     dst_dir = target
    dst_dir = tmpdir

    # dst_dir
    # set files directory, if target is a file.
    # set as it, if target is a directory.
    # make destination directory
    # if _os.path.isfile(target) and not _os.path.exists(dst_dir):
        # _os.mkdir(dst_dir)

    view = Overview(target, dst_dir)
    # pyreverse
    # my_pyreverse(target, dst_dir)
    # my_pyreverse(target, dst_dir, detail=False)
    view.pyreverse()

    # epydoc
    my_epydoc(target, dst_dir)
    view.epydoc()

    # doxygen
    # orig_dir = _os.getcwd()
    # try:
        # my_doxygen(target, dst_dir)
    # finally:
        # _os.chdir(orig_dir)
    view.doxygen()


    return 0

if __name__ == '__main__':
    sys.exit(_main())


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __main__.py ends here
