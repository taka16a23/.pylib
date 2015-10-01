#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""error -- DESCRIPTION

"""


class BitFlagError(StandardError):
    r"""SUMMARY
    """


class BitFlagValueError(BitFlagError, ValueError):
    r"""SUMMARY
    """


class BitLengthError(BitFlagValueError):
    r"""SUMMARY
    """



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# error.py ends here
