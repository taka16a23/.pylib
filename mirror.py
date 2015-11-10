#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""mirror -- Rsync mirroring for king server.
"""

# for debug
# import cgitb as _cgitb
# _cgitb.enable(format='text')

import sys
import os
import argparse

# from king import King
from ref import CMD
from junk.abstract import Verbose
from mypath import MyArchive
import subprocess as sbp


__version__ = '0.1.0'


class MountError(StandardError):
    r"""
    """

    def __init__(self, path):
        r"""

        @Arguments:
        - `path`:
        """
        self._path = path


class DataMirror(Verbose):
    """
    """
    _debug_opts = ['--dry-run']

    _default_opts = ['--compress', '--delete', '--force', '--update',
                     '--rsync-path="sudo rsync"']

    _archive_opts = ['--recursive', '--links', '--perms', '--times', '--group',
                     '--owner', '--devices', '--specials']

    _exclude_opts = ['/data/.backup/*',
                     '/data/.repository',
                     '/data/repository',
                     '/data/www',
                     '/data/tmp',
                     'lost+found',
                     # for safety
                     '/boot',
                     '/dev',
                     '/home',
                     '/lost+found',
                     '/mnt',
                     '/public',
                     '/run',
                     '/selinux',
                     '/srv',
                     '/tmp',
                     '/var',
                     '/bin',
                     '/etc',
                     '/lib',
                     '/media',
                     '/proc',
                     '/root',
                     '/sbin',
                     '/share',
                     '/sys',
                     '/usr',
                     ]

    def __init__(self, verbose=True, debug=False):
        """
        """
        super(DataMirror, self).__init__(verbose=verbose)
        if self._verbose:
            self._default_opts.append('--verbose')
        self._debug = debug
        if not self._debug:
            self._debug_opts = ['']

    def _pave_server(self):
        """SUMMARY

        @Return:
        """
        MyArchive().pave()
        sbp.check_call(('wol', '--silent'))
        # with King() as ki:
        #     if not ki.ismount():
        #         raise ki.MountError('Data is not mounted.')

    def _execute(self, cmdline):
        """SUMMARY

        @Arguments:

        - `cmdline`:

        @Return:
        """
        if self._verbose:
            print(' '.join(cmdline))
        os.system(' '.join(cmdline))

    @property
    def cmdline(self):
        """SUMMARY

        @Return:
        """
        return ([CMD.get('rsync')] + self._debug_opts +
                self._default_opts + self._archive_opts + self._exclude_opts)

    def push(self):
        """SUMMARY

        @Return:
        """
        self._pave_server()
        if self._verbose and self._debug:
            print('{0:*^30}'.format('DEBUG --dry-run'))
        local_remote = ['/data', 'ki:/']
        self._execute([CMD.get('rsync')] + self._debug_opts +
                      self._default_opts + self._archive_opts +
                      ['--exclude=' + x for x in self._exclude_opts] +
                      ['-e /usr/bin/ssh'] +
                      local_remote)

    def pull(self):
        """SUMMARY

        @Return:
        """
        self._pave_server()
        if self._verbose and self._debug:
            print('{0:*^30}'.format('DEBUG --dry-run'))
        remote_local = ['ki:/data', '/']
        self._execute([CMD.get('rsync')] + self._debug_opts +
                      self._default_opts + self._archive_opts +
                      ['--exclude=' + x for x in self._exclude_opts] +
                      ['-e ssh'] +
                      remote_local)


def mirror_ni():
    """SUMMARY

    @Return:
    """
    pass


def _options_maker():
    parser = argparse.ArgumentParser(description="""Mirror with king server.""")
    parser.add_argument('--version',
                        dest='version',
                        action='version',
                        version=__version__,
                        help='Version Strings.')
    parser.add_argument('-d', '--dry-run',
                        dest='dryrun',
                        action='store_true',
                        default=False,
                        required=False,
                        # (yas/expand-link "argparse_other_options" t)
                        help='Rsync with --dry-run option.')

    parser.add_argument('-s', '--silent',
                        dest='silent',
                        action='store_false',
                        default=True,
                        required=False,
                        # (yas/expand-link "argparse_other_options" t)
                        help='No verbose mode.')

    parser.add_argument('--pull-only',
                        dest='pull_only',
                        action='store_true',
                        default=False,
                        required=False,
                        # (yas/expand-link "argparse_other_options" t)
                        help='Rsync pull only.')

    parser.add_argument('--push-only',
                        dest='push_only',
                        action='store_true',
                        default=False,
                        required=False,
                        # (yas/expand-link "argparse_other_options" t)
                        help='Rsync push only.')

    parser.add_argument('--pull-push',
                        dest='pull_push',
                        action='store_true',
                        default=False,
                        required=False,
                        # (yas/expand-link "argparse_other_options" t)
                        help='Rsync pull and push')

    parser.add_argument('--push-pull',
                        dest='push_pull',
                        action='store_true',
                        default=False,
                        required=False,
                        # (yas/expand-link "argparse_other_options" t)
                        help='Rsync push and pull.')

    parser.add_argument('--halt',
                        dest='halt',
                        action='store_true',
                        default=False,
                        required=False,
                        # (yas/expand-link "argparse_other_options" t)
                        help='Halt remote machine after finished.')

# (yas/expand-link "argparse_add_argument" t)
    return parser


def _main():
    parser = _options_maker()
    opt = parser.parse_args()

    m = DataMirror(verbose=opt.silent, debug=opt.dryrun)

    if opt.pull_push:
        try:
            m.pull()
        except KeyboardInterrupt:
            sys.exit('KeyboardInterrupted')
        m.push()
    elif opt.push_pull:
        try:
            m.push()
        except KeyboardInterrupt:
            sys.exit('KeyboardInterrupted')
        m.pull()
    elif opt.pull_only:
        m.pull()
    elif opt.push_only:
        m.push()
    else:
        parser.print_usage()

    if opt.halt:
        sbp.check_call(('kihalt'))
        # with King() as ki:
            # ki.halt()


if __name__ == '__main__':
    _main()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# mirror.py ends here
