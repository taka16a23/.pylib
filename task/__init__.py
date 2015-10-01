#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: __init__.py 350 2015-08-04 22:36:15Z t1 $
# $Revision: 350 $
# $Date: 2015-08-05 07:36:15 +0900 (Wed, 05 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-05 07:36:15 +0900 (Wed, 05 Aug 2015) $

r"""Name: __init__.py


"""
from task._manager import TaskManager
from task._manager_observer import TaskManagerObserver
from task._task import Task


__revision__ = "$Revision: 350 $"
__version__ = "0.0.1"


__all__ = ['TaskManager', 'TaskManagerObserver', 'Task', ]



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
