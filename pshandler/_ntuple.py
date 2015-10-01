#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""_common -- DESCRIPTION

"""
import sys as _sys
from collections import namedtuple

# _handler.ProcessHandler.memory_info()
if _sys.platform.startswith("linux"):
    PSMEM = namedtuple('PSMEM', 'rss vms shared text lib data dirty')
elif _sys.platform.startswith("win32"):
    PSMEM = namedtuple(
        'PSMEM', ['num_page_faults', 'peak_wset', 'wset', 'peak_paged_pool',
                  'paged_pool', 'peak_nonpaged_pool', 'nonpaged_pool',
                  'pagefile', 'peak_pagefile', 'private'])
elif _sys.platform.startswith("darwin"):
    PSMEM = namedtuple('PSMEM', ['rss', 'vms', 'pfaults', 'pageins'])
elif _sys.platform.startswith("freebsd"):
    PSMEM = namedtuple('PSMEM', ['rss', 'vms', 'text', 'data', 'stack'])
elif _sys.platform.startswith("sunos"):
    PSMEM = namedtuple('PSMEM', ['rss', 'vms'])

# _handler.ProcessHandler.cpu_times()
PSCpuTimes = namedtuple('PSCpuTimes', ['user', 'system'])
# _handler.ProcessHandler.open_files()
PSOpenFile = namedtuple('PSOpenFile', ['path', 'fd'])
# _handler.ProcessHandler.threads()
PSThread = namedtuple('PSThread', ['id', 'user_time', 'system_time'])
# _handler.ProcessHandler.uids()
PSUIDs = namedtuple('PSUIDs', ['real', 'effective', 'saved'])
# _handler.ProcessHandler.gids()
PSGIDs = namedtuple('PSGIDs', ['real', 'effective', 'saved'])
# _handler.ProcessHandler.io_counters()
PSIO = namedtuple('PSIO', ['read_count', 'write_count',
                           'read_bytes', 'write_bytes'])
# _handler.ProcessHandler.ionice()
PSIONice = namedtuple('PSIONice', ['ioclass', 'value'])
# _handler.ProcessHandler.ctx_switches()
# PSCTXSW = namedtuple('PSCTXSW', ['voluntary', 'involuntary'])

# _handler.ProcessHandler.connections()
PSCONN = namedtuple('PSCONN', ['fd', 'family', 'type',
                               'local_addr', 'remote_addr', 'status'])



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _common.py ends here
