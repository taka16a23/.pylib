#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""accelerators -- DESCRIPTION

"""
from xahk.input.mouse import Mouse as _Mouse
from xahk.bind.accelerator import Accelerator as _Accelerator


LEFT_ACCELERATOR = _Accelerator(_Mouse.Button.Index.Left)
MIDDLE_ACCELERATOR = _Accelerator(_Mouse.Button.Index.Middle)
RIGHT_ACCELERATOR = _Accelerator(_Mouse.Button.Index.Right)
WHEELUP_ACCELERATOR = _Accelerator(_Mouse.Button.Index.WheelUp)
WHEELDOWN_ACCELERATOR = _Accelerator(_Mouse.Button.Index.WheelDown)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# accelerators.py ends here
