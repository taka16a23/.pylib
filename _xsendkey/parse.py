#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: parse.py 298 2015-01-29 00:24:54Z t1 $
# $Revision: 298 $
# $Date: 2015-01-29 09:24:54 +0900 (Thu, 29 Jan 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-01-29 09:24:54 +0900 (Thu, 29 Jan 2015) $

r"""parse -- DESCRIPTION

"""
import scanner
from .token import TokenType
from . import expression as exp


class Parser(object):
    r"""Parser

    Parser is a object.
    Responsibility:
    """
    def __init__(self, text):
        r"""

        @Arguments:
        - `text`:
        """
        self._scanner = scanner.Scanner(text)
        self._stack = []

        self.__iter = None
        self.__token = None

    def parse(self, ):
        r"""SUMMARY

        parse(text)

        @Arguments:
        - `text`:

        @Return:

        @Error:
        """
        self.__iter = iter(self._scanner)
        self.analyse()
        return self._stack

    def analyse(self, ):
        r"""SUMMARY

        analyse()

        @Return:

        @Error:
        """

        return

    def _next_token(self, ):
        r"""SUMMARY

        _next_token()

        @Return:

        @Error:
        """
        try:
            self.__token = self.__iter.next()
        except StopIteration:
            self.__token = None

    def expression(self, ):
        r"""SUMMARY

        expression()

        @Return:

        @Error:
        """
        self._stack = []
        self.__iter = iter(self._scanner)
        self.__token = self.__iter.next()
        while 1:
            if self.__token == TokenType.shift:
                self.__token = self.__iter.next()
                self._stack.append(exp.ShiftModifierExpression(self.term()))
            elif self.__token == TokenType.alt:
                self.__token = self.__iter.next()
                self._stack.append(exp.AltModifierExpression(self.term()))
            elif self.__token == TokenType.control:
                self._stack.append(exp.ControlModifierExpression(self.term()))


    def term(self, ):
        r"""SUMMARY

        term()

        @Return:

        @Error:
        """
        if self.__token == TokenType.key:
            return exp.KeyExpression(self.__token.getvalue())
        if self.__token == TokenType.button:
            return exp.ButtonExpression(self.__token.getvalue())
        if self.__token == TokenType.repeat:
            return exp.ButtonExpression(self.__token.getvalue())
        # TODO: (Atami) [2014/10/31]
        raise StandardError()


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# parse.py ends here
