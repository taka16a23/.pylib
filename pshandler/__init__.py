#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: __init__.py 307 2015-02-07 03:48:46Z t1 $
# $Revision: 307 $
# $Date: 2015-02-07 12:48:46 +0900 (Sat, 07 Feb 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-02-07 12:48:46 +0900 (Sat, 07 Feb 2015) $

r"""Name: __init__.py


"""
__revision__ = "$Revision: 307 $"
__version__ = "0.0.1"

__all__ = [ ]


import sys as _sys

from pshandler import _status as status
from pshandler import _conn as conn
from pshandler._handler import ProcessHandler, Popen
from pshandler._func import list_pids, list_process, get_boot_time
from pshandler._err import (Error,
                            NoSuchProcess,
                            AccessDenied,
                            Timeout)


if _sys.platform.startswith(('linux')):
    IOPRIO_CLASS_NONE = 0
    IOPRIO_CLASS_RT = 1
    IOPRIO_CLASS_BE = 2
    IOPRIO_CLASS_IDLE = 3

elif _sys.platform.startswith(('win32')):
    from psutil import (ABOVE_NORMAL_PRIORITY_CLASS,
                        BELOW_NORMAL_PRIORITY_CLASS,
                        HIGH_PRIORITY_CLASS,
                        IDLE_PRIORITY_CLASS,
                        NORMAL_PRIORITY_CLASS,
                        REALTIME_PRIORITY_CLASS)
    from psutil import CONN_DELETE_TCB
    try:
        # Linux >= 2.6.36
        from psutil import (RLIM_INFINITY,
                            RLIMIT_AS,
                            RLIMIT_CORE,
                            RLIMIT_CPU,
                            RLIMIT_DATA,
                            RLIMIT_FSIZE,
                            RLIMIT_LOCKS,
                            RLIMIT_MEMLOCK,
                            RLIMIT_NOFILE,
                            RLIMIT_NPROC,
                            RLIMIT_RSS,
                            RLIMIT_STACK)
    except ImportError as _err:
        pass
    try:
        from psutil import RLIMIT_MSGQUEUE
    except ImportError:
        pass
    try:
        from psutil import RLIMIT_NICE
    except ImportError:
        pass
    try:
        from psutil import RLIMIT_RTPRIO
    except ImportError:
        pass
    try:
        from psutil import RLIMIT_RTTIME
    except ImportError:
        pass
    try:
        from psutil import RLIMIT_SIGPENDING
    except ImportError:
        pass

elif _sys.platform.startswith(('sunos')):
    from psutil import CONN_IDLE, CONN_BOUND

else:
    raise NotImplementedError(
        'platform {} is not supported'.format(_sys.platform))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
