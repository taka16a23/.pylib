#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id: __init__.py 87 2013-11-30 07:34:05Z t1 $
# $Revision: 87 $
# $Date: 2013-11-30 16:34:05 +0900 (Sat, 30 Nov 2013) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2013-11-30 16:34:05 +0900 (Sat, 30 Nov 2013) $
r""" DiskUsage -- Disk usage

$Revision: 87 $

"""


# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')

import os as _os
import collections

__revision__ = '$Revision: 87 $'
__version__ = '0.1.0'


_ntuple_diskusage = collections.namedtuple('usage', 'total used free')

def disk_usage(path):
    st = _os.statvfs(path)
    free = st.f_bavail * st.f_frsize
    total = st.f_blocks * st.f_frsize
    used = (st.f_blocks - st.f_bfree) * st.f_frsize
    return _ntuple_diskusage(total, used, free)

def bytes2human(n):
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i+1)*10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n


def test():
    pass


if __name__ == '__main__':
    test()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
