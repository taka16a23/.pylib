#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id: posix_ref.py 87 2013-11-30 07:34:05Z t1 $
# $Revision: 87 $
# $Date: 2013-11-30 16:34:05 +0900 (Sat, 30 Nov 2013) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2013-11-30 16:34:05 +0900 (Sat, 30 Nov 2013) $
""" posix_ref -- for posix reference

$Revision: 87 $

"""


__revision__ = '$Revision: 87 $'
__version__ = '0.1.0'

CMD = {'ln': '/bin/ln',
       'rm': '/bin/rm',
       'rmdir': '/bin/rmdir',
       'du': '/usr/bin/du',
       'rsync': '/usr/bin/rsync',
       'sshfs': '/usr/bin/sshfs',
       'umount': '/bin/umount',
       'runlevel': '/sbin/runlevel',
       'apt-get': '/usr/bin/apt-get',
       'google-chrome': '/usr/bin/google-chrome',
       'sudo': '/usr/bin/sudo'
       }



def test():
    pass


if __name__ == '__main__':
    test()


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# posix_ref.py ends here
