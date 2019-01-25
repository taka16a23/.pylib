#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""BaseBuilder -- DESCRIPTION

"""
from .IBuilder import IBuilder
from argparse import ArgumentParser



class BaseBuilder(IBuilder):
    """BaseBuilder

    BaseBuilder is a IBuilder.
    Responsibility:
    """
    def build(self, parser):
        """base build

        build(parser)

        @Arguments:
        - `parser`:

        @Return:

        @Error:
        """
        if not isinstance(parser, (ArgumentParser, )):
            raise TypeError('parser required argparse.ArgumentParser.got({})'
                            .format(type(parser)))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# BaseBuilder.py ends here
