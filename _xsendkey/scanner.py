#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""scanner -- DESCRIPTION

"""
from orderedreplace import OrderedReplace

import strpointer
import subscanner
from xsendkey.token import TokenType, Token
from xcb2.xobj.key import Modifier, Namesym, Charsym
import xsend


REPLACES = [(r'\{\+'   ,'{plus'         ),
            (r'\\\+'   ,'{plus}'        ),
            (r'\{\!'   ,'{exclam'       ),
            (r'\\\!'   ,'{exclam}'      ),
            (r'\{\#'   ,'{numbersign'   ),
            (r'\\\#'   ,'{numbersign}'  ),
            (r'\{\^'   ,'{asciicircum'  ),
            (r'\\\^'   ,'{asciicircum}' ),
            (r'\{\_'   ,'{underscore'   ),
            (r'\_'     ,'{underscore}'  ),
            (r'\{\}\}' ,'{bracketright}'),
            (r'\{\}\ ' ,'{bracketright '),
            (r'\{\{\}' ,'{bracketleft}' ),
            (r'\{\{\ ' ,'{bracketleft ' ),
            # ('{{'    ,'{bracketleft}' ),
            (r'\\\{'   ,'{bracketleft}' ),
            (r'\\\}'   ,'{bracketright}'),
            (r'\"'     ,'{quotedbl}'    ),
            (r'\$'     ,'{dollar}'      ),
            (r'\%'     ,'{percent}'     ),
            (r'\&'     ,'{ampersand}'   ),
            (r"\'"     ,'{apostrophe}'  ),
            (r'\`'     ,'{quoteleft}'   ),
            (r'\('     ,'{parenleft}'   ),
            (r'\)'     ,'{parenright}'  ),
            (r'\~'     ,'{asciitilde}'  ),
            (r'\|'     ,'{bar}'         ),
            (r'\='     ,'{equal}'       ),
            (r'\*'     ,'{asterisk}'    ),
            (r'\>'     ,'{less}'        ),
            (r'\<'     ,'{greater}'     ),
            (r'\?'     ,'{question}'    ),
            (r'\-'     ,'{minus}'       ),
            (r'\,'     ,'{comma}'       ),
            (r'\.'     ,'{period}'      ),
            (r'\/'     ,'{slash}'       ),
            (r'\@'     ,'{at}'          ),
            (r'\:'     ,'{colon}'       ),
            (r'\;'     ,'{semicolon}'   ),
            (r'\['     ,'{braceleft}'   ),
            (r'\]'     ,'{braceright}'  ),
            (r'\\'     ,'{backslash}'   ),
            ]


class Scanner(object):
    r"""Scanner

    Scanner is a object.
    Responsibility:
    """
    modmap = {'+': TokenType.shift, # shift
              '^': TokenType.control, # control
              '!': TokenType.alt, # alt
              '#': TokenType.hiper, # hiper
              }

    _replacer = OrderedReplace(REPLACES)

    def __init__(self, line):
        r"""

        @Arguments:
        - `text`:
        """
        self._line = strpointer.StringPointer(self._replacer.replace(line))
        self._subscanner = None

    def get_token(self, char):
        r"""SUMMARY

        get_char_token(char)

        @Arguments:
        - `char`:

        @Return:

        @Error:
        """
        # Modifier
        token = self.modmap.get(char, None)
        if token is not None:
            return Token(token)
        # Char
        key = Charsym(char).to_sym().to_key()
        return Token(TokenType.key, xsend.KeySend(key))

    def iscurlyleft(self, index):
        r"""SUMMARY

        iscurlystart(index)

        @Arguments:
        - `index`:

        @Return:

        @Error:
        """
        return '{' == self._line[index]

    def next_curlyright(self, index):
        r"""SUMMARY

        next_curlyright(index)

        @Arguments:
        - `index`:

        @Return:

        @Error:
        """
        indx = index
        while self._line[indx] != '}':
            indx += 1
        return indx

    def next_index(self, index):
        r"""SUMMARY

        next_index()

        @Return:

        @Error:
        """
        start = index
        char = self._line[start]
        if '{' == char:
            return self.next_curlyright(start)
        if '}' == char:
            return None
        return start + 1

    def __iter__(self):
        self._line.setindex(0)
        self._subscanner = None
        return self

    def next(self, ):
        if self._subscanner is not None:
            if self._subscanner.hasnext():
                return self._subscanner.next()
            else:
                self._subscanner = None
        if self._line.getpoint() is None:
            raise StopIteration()
        start = self._line.getindex()
        end = self.next_index(start)
        if end is None:
            raise SyntaxError()
        increment = end - start
        phrase = self._line[start:end]
        if '{' in phrase:
            phrase = phrase.replace('{', '').replace('}', '')
            self._subscanner = iter(subscanner.Subscanner(phrase))
            self._line += increment + 1
            return self._subscanner.next()
        self._line += increment
        return self.get_token(phrase)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# scanner.py ends here
