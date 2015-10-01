#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py


"""
from task._manager import TaskManager
from task._manager_observer import TaskManagerObserver
from task._task import Task


__version__ = "0.0.1"


__all__ = ['TaskManager', 'TaskManagerObserver', 'Task', ]



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
