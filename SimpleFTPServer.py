#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: SimpleFTPServer.py 155 2014-04-26 10:02:31Z t1 $
# $Revision: 155 $
# $Date: 2014-04-26 19:02:31 +0900 (Sat, 26 Apr 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-04-26 19:02:31 +0900 (Sat, 26 Apr 2014) $

##
## Change Log:
##
## 2013/11/22    Atami
##    Added: '-d', '--directory' options
##           set serving directory.

"""SimpleFTPServer -- Simple FTP Server

$ python -m SimpleFTPServer
"""

import argparse
import socket
import os

from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import ThreadedFTPServer
from pyftpdlib.authorizers import DummyAuthorizer


__revision__ = '$Revision: 155 $'
__version__ = '0.1.1'

LOCAL_IP = socket.gethostbyname(socket.gethostname())

def _options_maker():
    """SUMMARY

    @Return:
    """
    parser = argparse.ArgumentParser(description="""Simple FTP Server""")
    parser.add_argument('--version',
                        dest='version',
                        action='version',
                        version=__version__,
                        help='Version Strings.')

    parser.add_argument('-u', '--user',
                        dest='user',
                        action='store',
                        const=None,
                        default='user',
                        type=str,
                        choices=None,
                        required=False,
                        help='Set user name.')

    parser.add_argument('-p', '--passwd', '--password',
                        dest='password',
                        action='store',
                        const=None,
                        default='pass',
                        type=str,
                        choices=None,
                        required=False,
                        # (yas/expand-link "argparse_other_options" t)
                        help='Set password.')

    parser.add_argument('--port',
                        dest='port',
                        action='store',
                        const=None,
                        default=21,
                        type=int,
                        choices=None,
                        required=False,
                        # (yas/expand-link "argparse_other_options" t)
                        help='Set port num default as 21.')

    parser.add_argument('-d', '--directory',
                        dest='directory',
                        action='store',
                        nargs=1,
                        default=None,
                        type=str,
                        help='Serve directory.')

    # (yas/expand-link "argparse_add_argument" t)
    return parser


def _main():
    parser = _options_maker()
    opt = parser.parse_args()

    user = opt.user
    pass_ = opt.password

    if opt.directory:
        dir_ = opt.directory[0]
        if os.path.isdir(dir_):
            os.chdir(dir_)

    print('{0:#^40}'.format(' Serving Directory '))
    print(os.getcwd())
    print('')
    print('{0:#^40}'.format(''))
    print('USER="{0}", PASSWORD="{1}"'.format(user, pass_))
    print('')
    print('{0:#^40}'.format(' Do execute this! '))
    print('If you using windowsNT in local network.')
    print('"explorer ftp://{0}:{1}"'.format(LOCAL_IP, opt.port))
    print('')

    auth = DummyAuthorizer()

    auth.add_user(user, pass_, '.', perm='elradfmw')

    handler = FTPHandler
    handler.authorizer = auth

    address = ('0.0.0.0', opt.port)
    ftpd = ThreadedFTPServer(address, handler)
    ftpd.serve_forever()


if __name__ == '__main__':
    _main()


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# SimpleFTPServer.py ends here
