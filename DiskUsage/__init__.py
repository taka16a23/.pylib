#!/usr/bin/env python
# -*- coding: utf-8 -*-
r""" DiskUsage -- Disk usage

"""


# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')

import os as _os
import collections

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
