#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: sshforwarder.py 259 2014-12-21 05:20:44Z t1 $
# $Revision: 259 $
# $Date: 2014-12-21 14:20:44 +0900 (Sun, 21 Dec 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-12-21 14:20:44 +0900 (Sun, 21 Dec 2014) $

"""
from '/usr/share/doc/python-paramiko/examples/forward.py.gz'

Sample script showing how to do local port forwarding over paramiko.

This script connects to the requested SSH server and sets up local port
forwarding (the openssh -L option) from a local port through a tunneled
connection to a destination reachable from the SSH server machine.
"""
import argparse
import getpass
import sys
import logging

from sshforward import _version
from sshforward.log import LOG
import sshportforward


SSH_PORT = 22
DEFAULT_PORT = 4000


def get_host_port(spec, default_port):
    "parse 'hostname:22' into a host and port, with the port optional"
    args = (spec.split(':', 1) + [default_port])[:2]
    args[1] = int(args[1])
    return args[0], args[1]


def _predef_options():
    parser = argparse.ArgumentParser(description="""\
    Set up a forward tunnel across an SSH server, using paramiko. A local port
    (given with -p) is forwarded across an SSH session to an address:port from
    the SSH server. This is similar to the openssh -L option.
    """)
    parser.add_argument('--version',
                        dest='version',
                        action='version',
                        version=_version.__version__,
                        help='Version Strings.')

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-v', '--verbose',
                       dest='verbose',
                       action='store_true',
                       default=False,
                       # (yas/expand-link "argparse_other_options" t)
                       help='A lot of messages.')

    group.add_argument('-q', '--quiet',
                       dest='quiet',
                       action='store_true',
                       default=False,
                       # (yas/expand-link "argparse_other_options" t)
                       help='squelch all informational output')

    parser.add_argument('-p', '--local-port',
                        action='store',
                        type=int,
                        dest='port',
                        default=DEFAULT_PORT,
                        help='local port to forward (default: {})'.format(
                            DEFAULT_PORT))

    parser.add_argument('-u', '--user',
                        action='store',
                        type=str,
                        dest='user',
                        default=getpass.getuser(),
                        help=('username for SSH authentication (default: {})'
                              .format(getpass.getuser())))

    parser.add_argument('-k', '--key',
                        action='store',
                        type=str,
                        dest='keyfile',
                        default=None,
                        help='private key file to use for SSH authentication')

    parser.add_argument('--no-key',
                        action='store_false',
                        dest='look_for_keys',
                        default=True,
                        help="don't look for or use a private key file")

    parser.add_argument('-P', '--password',
                        action='store_true',
                        dest='readpass',
                        default=False,
                        help=('read password (for key or password auth) '
                        'from stdin'))

    parser.add_argument('sshserver',
                        action='store',
                        type=str,
                        # (yas/expand-link "argparse_other_options" t)
                        metavar='ssh-server[:server_port]',
                        help='target ssh server. (default server_port: 22)')

    parser.add_argument('-r', '--remote',
                        action='store',
                        dest='remote',
                        type=str,
                        required=True,
                        metavar='host:port',
                        help='remote host and port to forward to')

    # (yas/expand-link "argparse_add_argument" t)
    return parser


def main():
    parser = _predef_options()
    opts = parser.parse_args()

    # verbose
    if opts.verbose and opts.quiet:
        parser.error(
            '("-v", "--verbose") and ("-q", "--quiet") exclusive options')
    if opts.verbose:
        LOG.setLevel(logging.DEBUG)
        LOG.debug('Debug mode.')
    if opts.quiet:
        LOG.setLevel(logging.ERROR)

    sshserver, sshport = get_host_port(opts.sshserver, SSH_PORT)
    target, targetport = get_host_port(opts.remote, SSH_PORT)

    password = None
    if opts.readpass:
        password = getpass.getpass('Enter SSH password: ')

    forwarder = sshportforward.PortForward(
        sshserver, target, sshport=sshport, user=opts.user, key=opts.keyfile)
    LOG.info('Connecting to ssh host {0}:{1} ...'.format(sshserver, sshport))
    LOG.info('Now forwarding port {0} to {1}:{2} ...'
             .format(opts.port, target, targetport))
    LOG.info('** C-c: Port forwarding will stop. **')

    try:
        forwarder.serve_forever(opts.port, targetport,
                                look_for_keys=opts.look_for_keys,
                                passwd=password)
    except Exception, err:
        LOG.error('*** Failed to connect to {0}:{1}: {3}'
                  .format(sshserver, sshport, err))
        sys.exit(1)
    except KeyboardInterrupt:
        LOG.info('C-c: Port forwarding stopped.')
        sys.exit(0)


if __name__ == '__main__':
    main()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# sshforward.py ends here
