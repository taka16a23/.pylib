#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: vlc_converters.py 485 2015-09-29 03:10:26Z t1 $
# $Revision: 485 $
# $Date: 2015-09-29 12:10:26 +0900 (Tue, 29 Sep 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-09-29 12:10:26 +0900 (Tue, 29 Sep 2015) $

r"""Name: vlc_converters.py


"""

import sys
import os
import argparse
import subprocess as sbp
from pathhandler import PathHandler


# for debug
import cgitb
cgitb.enable(format='text')


__revision__ = '$Revision: 485 $'
__version__ = '0.0.1'


def check_directory(directory):
    r"""SUMMARY

    check_directory(directory)

    @Arguments:
    - `directory`:

    @Return:

    @Error:
    """
    pth = PathHandler(directory)
    if not pth.exists():
        print('path not exists')
        sys.exit(1)
    if not pth.isdir():
        print('{} not directory'.format(str(pth)))
        sys.exit(1)

def make_finished_directry(directory):
    r"""SUMMARY

    make_finished_directry(directory)

    @Arguments:
    - `directory`:

    @Return:

    @Error:
    """
    pth = PathHandler(directory)
    finpath = pth.join('finished')

    if finpath.exists() and not finpath.isdir():
        print('finished path is not directory')
        sys.exit(1)
    if finpath.isdir():
        return finpath
    finpath.mkdir(777)
    return finpath


def make_newpath(fpath, dstpath):
    r"""SUMMARY

    make_newpath(dstpath)

    @Arguments:
    - `dstpath`:

    @Return:

    @Error:
    """
    return dstpath.join(fpath.get_basename())

def convert(fpath, newf):
    r"""SUMMARY

    convert(fpath, dstpath)

    @Arguments:
    - `fpath`:
    - `dstpath`:

    @Return:

    @Error:
    """
    return sbp.check_call(['/usr/bin/vlc', '--no-repeat', '--no-loop',
                    '--sout-avcodec-strict=-2', '-I', 'dummy', str(fpath),
                    r"--sout=#transcode{width=720, height=480, vcodec=h264,"
                    r" acodec=mp4a,channels=2}:standard{access=file,mux=mp4,dst="
                    + str(newf) + r"}",
                    r'vlc://quit'])

def move_source(fpath, dest):
    r"""SUMMARY

    move_source(fpath)

    @Arguments:
    - `fpath`:

    @Return:

    @Error:
    """
    name, ext = dest.join(fpath.get_basename()).splitext()
    fpath.move(name + '.old' + ext)


def _predef_options():
    parser = argparse.ArgumentParser(description="""""")
    parser.add_argument('--version',
                        dest='version',
                        action='version',
                        version=__version__,
                        help='Version Strings.')
    parser.add_argument(dest='dir',
                        action='store',
                        type=str,
                        # (yas-expand-link "argparse_other_options" t)
                        help='directory')
    # (yas-expand-link "argparse_add_argument" t)
    return parser

def _main():
    r"""Main function."""
    parser = _predef_options()
    opts = parser.parse_args()
    # parser.print_usage()
    check_directory(opts.dir)
    sources = PathHandler(opts.dir)
    dstdir = make_finished_directry(opts.dir)
    try:
        for fpath in sources.listdir():
            if not fpath.isfile():
                continue
            newf = make_newpath(fpath, dstdir)
            if convert(fpath, newf) == 0:
                move_source(fpath, dstdir)
    except KeyboardInterrupt:
        if newf.exists():
            newf.remove()
        return -1
    return os.EX_OK

if __name__ == '__main__':
    sys.exit(_main())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# vlc_converters.py ends here
