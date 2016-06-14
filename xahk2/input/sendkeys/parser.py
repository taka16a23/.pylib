#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""parser -- DESCRIPTION

"""
from xahk2.input.sendkeys.token import Tokenizer


class Parser(object):
    r"""Parser

    Parser is a object.
    Responsibility:
    """
    def __init__(self, analyzer):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        self._analyzer = analyzer

    def compile(self, string):
        r"""SUMMARY

        compile(string)

        @Arguments:
        - `string`:

        @Return:

        @Error:
        """
        for token in Tokenizer(string):
            self._analyzer.analyze(token)
        return self._analyzer.list_expressions()

    def parse(self, string):
        r"""SUMMARY

        parse(string)

        @Arguments:
        - `string`:

        @Return:

        @Error:
        """
        expressions = self.compile(string)
        for exp in expressions:
            exp.interpret()

    def clear(self, ):
        r"""SUMMARY

        clear()

        @Return:

        @Error:
        """
        self._analyzer.clear()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# parser.py ends here
