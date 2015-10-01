#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: parse.py 277 2015-01-28 23:57:11Z t1 $
# $Revision: 277 $
# $Date: 2015-01-29 08:57:11 +0900 (Thu, 29 Jan 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-01-29 08:57:11 +0900 (Thu, 29 Jan 2015) $

r"""parse -- DESCRIPTION

"""
from xsendkey.parser.scanner import Scanner
from xsendkey.parser.analyze import Analyze


class Parse(object):
    r"""Parse

    Parse is a object.
    Responsibility:
    """
    def __init__(self, xinputs=None):
        r"""

        @Arguments:
        - `inputs`:
        """
        self._xinputs = xinputs or []

    def parse(self, line, display=None):
        r"""SUMMARY

        parse(line, display=None)

        @Arguments:
        - `line`:
        - `display`:

        @Return:

        @Error:
        """
        analyzer = Analyze()
        scanner = Scanner()
        scanner.scan_line(line)
        analyzer.analyze_tokens(scanner.get_tokens(), display)
        self._xinputs.extend(analyzer.get_expressions().interpret())

    def get_xinputs(self, ):
        r"""SUMMARY

        get_xinputs()

        @Return:

        @Error:
        """
        return self._xinputs



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# parse.py ends here
