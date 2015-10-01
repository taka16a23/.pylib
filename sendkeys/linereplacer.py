#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: linereplacer.py 173 2014-05-03 07:51:01Z t1 $
# $Revision: 173 $
# $Date: 2014-05-03 16:51:01 +0900 (Sat, 03 May 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-05-03 16:51:01 +0900 (Sat, 03 May 2014) $

r"""linereplacer -- DESCRIPTION

"""
from collections import OrderedDict

from sendkeys.display import KeymapDisplay
from sendkeys.tokenize import Tokenize


REPLACE_MAP = OrderedDict([('{+'  , '{plus'          ),
                           ('\\+' , '{plus}'         ),
                           ('{!'  , '{exclam'        ),
                           ('\\!' , '{exclam}'       ),
                           ('{#'  , '{numbersign'    ),
                           ('\\#' , '{numbersign}'   ),
                           ('{^'  , '{asciicircum'   ),
                           ('\\^' , '{asciicircum}'  ),
                           ('{_'  , '{underscore'    ),
                           ('\\_' , '{underscore}'   ),
                           ('{}}' , '{bracketright}' ),
                           ('{} ' , '{bracketright ' ),
                           ('{{}' , '{bracketleft}'  ),
                           ('{{ ' , '{bracketleft '  ),
                           # ('{{'  , '{bracketleft}'  ),
                           ('\\{' , '{bracketleft}'  ),
                           ('\\}' , '{bracketright}' ),
                           ('\"'  , '{quotedbl}'     ),
                           ('$'   , '{dollar}'       ),
                           ('%'   , '{percent}'      ),
                           ('&'   , '{ampersand}'    ),
                           ("'"   , '{apostrophe}'   ),
                           ('`'   , '{quoteleft}'    ),
                           ('('   , '{parenleft}'    ),
                           (')'   , '{parenright}'   ),
                           ('~'   , '{asciitilde}'   ),
                           ('|'   , '{bar}'          ),
                           ('='   , '{equal}'        ),
                           ('*'   , '{asterisk}'     ),
                           ('>'   , '{less}'         ),
                           ('<'   , '{greater}'      ),
                           ('?'   , '{question}'     ),
                           ('-'   , '{minus}'        ),
                           (','   , '{comma}'        ),
                           ('.'   , '{period}'       ),
                           ('/'   , '{slash}'        ),
                           ('@'   , '{at}'           ),
                           (':'   , '{colon}'        ),
                           (';'   , '{semicolon}'    ),
                           ('['   , '{braceleft}'    ),
                           (']'   , '{braceright}'   ),
                           ('\\'  , '{backslash}'    ),
                           ])


class LineReplacer(KeymapDisplay):
    r"""SUMMARY
    """
    _maps = REPLACE_MAP

    def __init__(self, line, display=None):
        r"""

        @Arguments:
        - `line`:
        - `maps`:
        """
        KeymapDisplay.__init__(self, display)
        self.line = line

    def get_tokenize(self, ):
        r"""SUMMARY

        get_tokenize()

        @Return:
        """
        return Tokenize(self, self.display)

    def replace(self, ):
        r"""SUMMARY

        replaced()

        @Return:
        """
        line = self.line
        for key in self._maps.keys():
            if key in line:
                line = line.replace(key, self._maps[key])
        return line

    def __iter__(self, ):
        return iter(self.replace())

    def __repr__(self, ):
        return "{0.__class__.__name__}('{0.line}')".format(self)

    def __str__(self, ):
        return self.replace()

    def __call__(self, ):
        return self.replace()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# linereplacer.py ends here
