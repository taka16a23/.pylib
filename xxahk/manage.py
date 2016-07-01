#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""manage -- DESCRIPTION

"""
from xahk.events.loop import EventLoop
from xahk.x11.display import Display

from .chrome import *
from .emacs import *
from .libre_calc import *
from .thunar import *
from .control_runcher import *
from .global_move import *
from .sendaddress import *
from .restart import *
from .always_on_top import *
from .close import *
from .debug import *

DebugKeyBindServiceObserver()


try:
    EventLoop.get_instance(Display()).start_loop()
except KeyboardInterrupt:
    pass



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# manage.py ends here
