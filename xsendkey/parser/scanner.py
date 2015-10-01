#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: scanner.py 277 2015-01-28 23:57:11Z t1 $
# $Revision: 277 $
# $Date: 2015-01-29 08:57:11 +0900 (Thu, 29 Jan 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-01-29 08:57:11 +0900 (Thu, 29 Jan 2015) $

r"""subscanner -- DESCRIPTION

"""
from collections import deque
from abc import ABCMeta, abstractmethod

from xsendkey.parser.token import Token, TokenType
from xsendkey.parser import err


BEHAVE = {'down': 'press',
          'up': 'release',
          'd': 'press',
          'u': 'release',
          }


class DispatchArguments(object):
    r"""DispatchArguments

    DispatchArguments is a object.
    Responsibility:
    """
    def __init__(self, ):
        r"""

        @Arguments:
        - `tokens`:
        """
        self.digits = list()
        self.words = list()

    def _dispatch(self, token):
        r"""SUMMARY

        _dispatch(digits, words)

        @Arguments:
        - `digits`:
        - `words`:

        @Return:

        @Error:
        """
        if token.isdigit():
            self.digits.append(token)
        else:
            self.words.append(token.lower())

    def dispatch(self, tokens):
        r"""SUMMARY

        dispatch()

        @Return:

        @Error:
        """
        for token in tokens:
            self._dispatch(token)

    def get_digits(self, ):
        r"""SUMMARY

        get_digits()

        @Return:

        @Error:
        """
        return self.digits

    def get_words(self, ):
        r"""SUMMARY

        get_words()

        @Return:

        @Error:
        """
        return self.words


class SubScannerAbstract(object):
    r"""SubScannerAbstract

    SubScannerAbstract is a object.
    Responsibility:
    """
    __metaclass__ = ABCMeta

    def __init__(self, tokens):
        r"""

        @Arguments:
        - `tokens`:
        """
        self._tokens = tokens

    @abstractmethod
    def scan_line(self, line):
        pass

    def clear(self, ):
        r"""SUMMARY

        clear()

        @Return:

        @Error:
        """
        self._tokens.clear()

    def get_tokens(self, ):
        r"""SUMMARY

        get_tokens()

        @Return:

        @Error:
        """
        return self._tokens

    def append(self, token):
        r"""SUMMARY

        append(token)

        @Arguments:
        - `token`:

        @Return:

        @Error:
        """
        if not isinstance(token, (Token, )):
            # TODO: (Atami) [2015/01/27]
            raise StandardError()
        self._tokens.append(token)

    def extend(self, tokens):
        r"""SUMMARY

        extend(tokens)

        @Arguments:
        - `tokens`:

        @Return:

        @Error:
        """
        for token in tokens:
            if not isinstance(token, (Token, )):
                # TODO: (Atami) [2015/01/27]
                raise StandardError()
        self._tokens.extend(tokens)


class KeyArgumentsScanner(SubScannerAbstract):
    r"""KeyArgumentsScanner

    KeyArgumentsScanner is a ScannerAbstract.
    Responsibility:
    """
    def scan_line(self, line):
        r"""SUMMARY

        scan_line(line)

        @Arguments:
        - `line`:

        @Return:

        @Error:
        """
        self.scan_list(line.split())

    def scan_list(self, list_):
        r"""SUMMARY

        scan_list(list_)

        @Arguments:
        - `list_`:

        @Return:

        @Error:
        """
        arguments = DispatchArguments()
        arguments.dispatch(list_)
        self.scan_digits(arguments.get_digits())
        self.scan_words(arguments.get_words())

    def scan_digits(self, digits):
        r"""SUMMARY

        scan_digits(digits)

        @Arguments:
        - `digits`:

        @Return:

        @Error:
        """
        if len(digits) not in (0, 1):
            # TODO: (Atami) [2015/01/27]
            raise err.XSKSyntaxError()
        if len(digits):
            self.append_repeat(digits[0])

    def scan_words(self, words):
        r"""SUMMARY

        scan_words(words)

        @Arguments:
        - `words`:

        @Return:

        @Error:
        """
        if len(words) not in (0, 1):
            # TODO: (Atami) [2015/01/27]
            raise err.XSKSyntaxError()
        if len(words):
            self.append_behave(words[0])

    def append_repeat(self, repeat):
        r"""SUMMARY

        append_repeat(repeat)

        @Arguments:
        - `repeat`:

        @Return:

        @Error:
        """
        self.append(Token(TokenType.repeat, repeat))

    def append_behave(self, behave):
        r"""SUMMARY

        append_behave(behave)

        @Arguments:
        - `behave`:

        @Return:

        @Error:
        """
        self.append(Token(TokenType.behave, behave))


class ClickScanner(SubScannerAbstract):
    r"""ClickScanner

    ClickScanner is a SubScannerAbstract.
    Responsibility:
    """
    buttons = {'left': 'LButton',
               'right': 'RButton',
               'middle': 'MButton',
               'wheelup': 'WheelUp',
               'wheeldown': 'WheelDown',
               'l': 'LButton',
               'r': 'RButton',
               'm': 'MButton',
               'wu': 'WheelUp',
               'wd': 'WheelDown',
    }

    def scan_line(self, line):
        r"""SUMMARY

        scan_line(line)

        @Arguments:
        - `line`:

        @Return:

        @Error:
        """
        self.scan_list(line.replace('Click', '').split())

    def scan_list(self, list_):
        r"""SUMMARY

        scan_list(list_)

        @Arguments:
        - `list_`:

        @Return:

        @Error:
        """
        arguments = DispatchArguments()
        arguments.dispatch(list_)
        self.scan_words(arguments.get_words())
        self.scan_digits(arguments.get_digits())

    def scan_words(self, words):
        r"""SUMMARY

        scan_words(words)

        @Arguments:
        - `words`:

        @Return:

        @Error:
        """
        if 2 < len(words):
            # TODO: (Atami) [2015/01/27]
            raise err.XSKSyntaxError()
        button = 'left'
        for word in words:
            wrd = word.lower()
            if wrd in self.buttons:
                button = wrd
            elif wrd in BEHAVE:
                self.append_behave(BEHAVE.get(wrd))
            else:
                # TODO: (Atami) [2015/01/27]
                raise err.XSKSyntaxError()
        self.append_button(self.buttons.get(button))

    def scan_digits(self, digits):
        r"""SUMMARY

        scan_digits(digits)

        @Arguments:
        - `digits`:

        @Return:

        @Error:
        """
        dlen = len(digits)
        if 3 < dlen:
            # TODO: (Atami) [2015/01/27]
            raise err.XSKSyntaxError()
        if dlen in (2, 3):
            self.append_point(digits[0], digits[1])
        if 1 == dlen:
            self.append_repeat(digits[0])
        if 3 == dlen:
            self.append_repeat(digits[2])

    def append_repeat(self, repeat):
        r"""SUMMARY

        append_repeat(repeat)

        @Arguments:
        - `repeat`:

        @Return:

        @Error:
        """
        self.append(Token(TokenType.repeat, repeat))

    def append_behave(self, behave):
        r"""SUMMARY

        append_behave(behave)

        @Arguments:
        - `behave`:

        @Return:

        @Error:
        """
        self.append(Token(TokenType.behave, behave))

    def append_button(self, button):
        r"""SUMMARY

        append_button(button)

        @Arguments:
        - `button`:

        @Return:

        @Error:
        """
        self.append(Token(TokenType.button, button))

    def append_point(self, x, y):
        r"""SUMMARY

        append_point(x, y)

        @Arguments:
        - `x`:
        - `y`:

        @Return:

        @Error:
        """
        self.append(Token(TokenType.point, (x, y)))


class ButtonScanner(SubScannerAbstract):
    r"""ButtonScanner

    ButtonScanner is a ScannerAbstract.
    Responsibility:
    """
    buttons = {'lbutton': 'LButton',
               'rbutton': 'RButton',
               'mbutton': 'MButton',
               'wheelup': 'WheelUp',
               'wheeldown': 'WheelDown',
               'lclick': 'LButton',
               'rclick': 'RButton',
               'mclick': 'MButton',
               'wup': 'WheelUp',
               'wdown': 'WheelDown',
               }

    def scan_line(self, line):
        r"""SUMMARY

        scan_line(line)

        @Arguments:
        - `line`:

        @Return:

        @Error:
        """
        self.scan_list(line.split())

    def scan_list(self, list_):
        r"""SUMMARY

        scan_list(list_)

        @Arguments:
        - `list_`:

        @Return:

        @Error:
        """
        arguments = DispatchArguments()
        arguments.dispatch(list_)
        self.scan_words(arguments.get_words())
        self.scan_digits(arguments.get_digits())

    def scan_words(self, words):
        r"""SUMMARY

        scan_words(words)

        @Arguments:
        - `words`:

        @Return:

        @Error:
        """
        if 2 < len(words):
            # TODO: (Atami) [2015/01/27]
            raise err.XSKSyntaxError()
        for word in words:
            wrd = word.lower()
            if wrd in self.buttons:
                self.append_button(self.buttons.get(wrd))
            elif wrd in BEHAVE:
                self.append_behave(BEHAVE.get(wrd))
            else:
                # TODO: (Atami) [2015/01/27]
                raise err.XSKSyntaxError()

    def scan_digits(self, digits):
        r"""SUMMARY

        scan_digits(digits)

        @Arguments:
        - `digits`:

        @Return:

        @Error:
        """
        dlen = len(digits)
        if 3 < dlen:
            # TODO: (Atami) [2015/01/27]
            raise err.XSKSyntaxError()
        if dlen in (2, 3):
            self.append_point(digits[0], digits[1])
        if 1 == dlen:
            self.append_repeat(digits[0])
        if 3 == dlen:
            self.append_repeat(digits[2])

    def append_button(self, button):
        r"""SUMMARY

        append_button(button)

        @Arguments:
        - `button`:

        @Return:

        @Error:
        """
        self.append(Token(TokenType.button, button))

    def append_behave(self, behave):
        r"""SUMMARY

        append_behave(behave)

        @Arguments:
        - `behave`:

        @Return:

        @Error:
        """
        self.append(Token(TokenType.behave, behave))

    def append_repeat(self, repeat):
        r"""SUMMARY

        append_repeat(repeat)

        @Arguments:
        - `repeat`:

        @Return:

        @Error:
        """
        self.append(Token(TokenType.repeat, repeat))

    def append_point(self, x, y):
        r"""SUMMARY

        append_point(x, y)

        @Arguments:
        - `x`:
        - `y`:

        @Return:

        @Error:
        """
        self.append(Token(TokenType.point, (x, y)))


#### for scan ASC, SYM, UNI, KEY arguments.
##
class ArgumentsScanner(SubScannerAbstract):
    r"""ArgumentsScanner

    ArgumentsScanner is a object.
    Responsibility:
    """
    def scan_line(self, line):
        r"""SUMMARY

        scan_line(line)

        @Arguments:
        - `line`:

        @Return:

        @Error:
        """
        self.scan_list(line.split())

    def scan_list(self, list_):
        r"""SUMMARY

        scan_list(list_)

        @Arguments:
        - `list_`:

        @Return:

        @Error:
        """
        arguments = DispatchArguments()
        arguments.dispatch(list_)
        self.scan_digits(arguments.get_digits())
        self.scan_words(arguments.get_words())

    def scan_digits(self, digits):
        r"""SUMMARY

        scan_digits(digits)

        @Arguments:
        - `digits`:

        @Return:

        @Error:
        """
        dgts = list(digits)
        if 2 <= len(dgts):
            # TODO: (Atami) [2015/01/27]
            raise err.XSKSyntaxError('')
        if 1 == len(dgts):
            self.append_repeat(dgts[0])

    def append_repeat(self, repeat):
        r"""SUMMARY

        append_repeat(repeat)

        @Arguments:
        - `repeat`:

        @Return:

        @Error:
        """
        self.append(Token(TokenType.repeat, repeat))

    def scan_words(self, words):
        r"""SUMMARY

        scan_words(words)

        @Arguments:
        - `words`:

        @Return:

        @Error:
        """
        wds = list(words)
        if 2 <= len(wds):
            # TODO: (Atami) [2015/01/27]
            raise err.XSKSyntaxError('')
        if 1 == len(wds):
            self.append_behave(wds[0])

    def append_behave(self, behave):
        r"""SUMMARY

        append_behave(behave)

        @Arguments:
        - `behave`:

        @Return:

        @Error:
        """
        self.append(Token(TokenType.behave, behave))


class ASCScanner(SubScannerAbstract):
    r"""ASCScanner

    ASCScanner is a SubScannerAbstract.
    Responsibility:
    """
    def scan_line(self, line):
        r"""SUMMARY

        scan_line(line)

        @Arguments:
        - `line`:

        @Return:

        @Error:
        """
        self.scan_list(line.replace('ASC', '').split())

    def scan_list(self, list_):
        r"""SUMMARY

        scan_list(list_)

        @Arguments:
        - `list_`:

        @Return:

        @Error:
        """
        tokens = deque(list_)
        if len(tokens) <= 0 or 2 < len(tokens):
            # TODO: (Atami) [2015/01/27]
            raise err.XSKSyntaxError()
        self.append_code(tokens.popleft())
        ArgumentsScanner(self._tokens).scan_list(tokens)

    def append_code(self, code):
        r"""SUMMARY

        append_code(code)

        @Arguments:
        - `code`:

        @Return:

        @Error:
        """
        self.append(Token(TokenType.code, code))


class SYMScanner(SubScannerAbstract):
    r"""SYMScanner

    SYMScanner is a SubScannerAbstract.
    Responsibility:
    """
    def scan_line(self, line):
        r"""SUMMARY

        scan_line(line)

        @Arguments:
        - `line`:

        @Return:

        @Error:
        """
        self.scan_list(line.replace('SYM', '').split())

    def scan_list(self, list_):
        r"""SUMMARY

        scan_list(list_)

        @Arguments:
        - `list_`:

        @Return:

        @Error:
        """
        tokens = deque(list_)
        if len(tokens) <= 0 or 2 < len(tokens):
            # TODO: (Atami) [2015/01/27]
            raise err.XSKSyntaxError()
        self.append_sym(tokens.popleft())
        ArgumentsScanner(self._tokens).scan_list(tokens)

    def append_sym(self, sym):
        r"""SUMMARY

        append_sym(sym)

        @Arguments:
        - `sym`:

        @Return:

        @Error:
        """
        self.append(Token(TokenType.sym, sym))


class UNIScanner(SubScannerAbstract):
    r"""UNIScanner

    UNIScanner is a SubScannerAbstract.
    Responsibility:
    """
    def scan_line(self, line):
        r"""SUMMARY

        scan_line(line)

        @Arguments:
        - `line`:

        @Return:

        @Error:
        """
        self.scan_list(line.replace('UNI', '').split())

    def scan_list(self, list_):
        r"""SUMMARY

        scan_list(list_)

        @Arguments:
        - `list_`:

        @Return:

        @Error:
        """
        tokens = deque(list_)
        if len(tokens) <= 0 or 2 < len(tokens):
            # TODO: (Atami) [2015/01/27]
            raise err.XSKSyntaxError()
        self.append_unicode(tokens.popleft())
        ArgumentsScanner(self._tokens).scan_list(tokens)

    def append_unicode(self, unicode_):
        r"""SUMMARY

        append_unicode(unicode_)

        @Arguments:
        - `unicode_`:

        @Return:

        @Error:
        """
        self.append(Token(TokenType.unicode, unicode_))


class KeyScanner(SubScannerAbstract):
    r"""KeyScanner

    KeyScanner is a SubScannerAbstract.
    Responsibility:
    """
    def scan_line(self, line):
        r"""SUMMARY

        scan_line(line)

        @Arguments:
        - `line`:

        @Return:

        @Error:
        """
        self.scan_list(line.split())

    def scan_list(self, list_):
        r"""SUMMARY

        scan_list(list_)

        @Arguments:
        - `list_`:

        @Return:

        @Error:
        """
        tokens = deque(list_)
        if len(tokens) <= 0 or 2 < len(tokens):
            # TODO: (Atami) [2015/01/27]
            raise err.XSKSyntaxError()
        self.append_name(tokens.popleft())
        ArgumentsScanner(self._tokens).scan_list(tokens)

    def append_name(self, name):
        r"""SUMMARY

        append_name(name)

        @Arguments:
        - `name`:

        @Return:

        @Error:
        """
        self.append(Token(TokenType.name, name))


class SubScanner(SubScannerAbstract):
    r"""SubScanner

    SubScanner is a ScannerAbstract.
    Responsibility:

    Scan in curly brace "{ASC 100}" => Token(type=code, value="100")

    """
    buttons = tuple(ButtonScanner.buttons.keys())

    def scan_line(self, line):
        r"""SUMMARY

        scan_line(line)

        @Arguments:
        - `line`:

        @Return:

        @Error:
        """
        if line.startswith(('ASC')):
            sscanner = ASCScanner(self._tokens)
        elif line.startswith(('SYM')):
            sscanner = SYMScanner(self._tokens)
        elif line.startswith(('UNI')):
            sscanner = UNIScanner(self._tokens)
        elif line.startswith(('Click')):
            sscanner = ClickScanner(self._tokens)
        elif line.lower().startswith(self.buttons):
            sscanner = ButtonScanner(self._tokens)
        else:
            sscanner = KeyScanner(self._tokens)
        sscanner.scan_line(line)


## Main Scanner
#
class CurlyState(object):
    r"""CurlyState

    CurlyState is a object.
    Responsibility:
    """
    def __init__(self, substring='', incurly=False):
        r"""
        """
        self._substr = substring
        self._incurly = incurly

    def get_substr(self, ):
        r"""SUMMARY

        get_substr()

        @Return:

        @Error:
        """
        return self._substr

    def set_substr(self, substr=''):
        r"""SUMMARY

        set_substr(substr='')

        @Arguments:
        - `substr`:

        @Return:

        @Error:
        """
        self._substr = substr

    def clear(self, ):
        r"""SUMMARY

        clear()

        @Return:

        @Error:
        """
        self._substr = ''

    def add_substr(self, substring):
        r"""SUMMARY

        add_substr(substring)

        @Arguments:
        - `substring`:

        @Return:

        @Error:
        """
        self._substr += substring

    def incurly(self, ):
        r"""SUMMARY

        incurly()

        @Return:

        @Error:
        """
        return self._incurly

    def set_incurly(self, bool_):
        r"""SUMMARY

        set_incurly(bool_)

        @Arguments:
        - `bool_`:

        @Return:

        @Error:
        """
        self._incurly = bool(bool_)


class Scanner(object):
    r"""Scanner

    Scanner is a object.
    Responsibility:
    """
    def __init__(self, ):
        r"""
        """
        self._tokens = deque()

    def get_tokens(self, ):
        r"""SUMMARY

        get_tokens()

        @Return:

        @Error:
        """
        return self._tokens

    def clear(self, ):
        r"""SUMMARY

        clear()

        @Return:

        @Error:
        """
        self._tokens.clear()

    def scan_line(self, line):
        r"""SUMMARY

        scan_line(line)

        @Arguments:
        - `line`:

        @Return:

        @Error:
        """
        curlystate = {}
        curlystate['substr'], curlystate['incurly'] = '', False
        for char in line:
            self._tokenize(char, curlystate)

    def _tokenize(self, char, curlystate):
        r"""SUMMARY

        _tokenize(char, curlystate)

        @Arguments:
        - `char`:
        - `curlystate`:

        @Return:

        @Error:
        """
        if char == '}':
            subscan = SubScanner(self._tokens)
            subscan.scan_line(curlystate['substr'])
            curlystate['incurly'] = False
            curlystate['substr'] = '' # clear substring
        elif curlystate['incurly']:
            curlystate['substr'] += char
        elif char == '{':
            curlystate['incurly'] = True
        elif char in ('+', '^', '!', '#'):
            self.append_modifier(char)
        elif char == '\0':
            self.append_endmarker()
        else:
            self.append_char(char)

    def append(self, token):
        r"""SUMMARY

        append(token)

        @Arguments:
        - `token`:

        @Return:

        @Error:
        """
        if not isinstance(token, (Token, )):
            # TODO: (Atami) [2015/01/27]
            raise StandardError()
        self._tokens.append(token)

    def append_modifier(self, mod):
        r"""SUMMARY

        append_modifier(mod)

        @Arguments:
        - `mod`:

        @Return:

        @Error:
        """
        self.append(Token(TokenType.modifier, mod))

    def append_endmarker(self, ):
        r"""SUMMARY

        append_endmarker()

        @Return:

        @Error:
        """
        self.append(Token(TokenType.endmarker))

    def append_char(self, char):
        r"""SUMMARY

        append_char(char)

        @Arguments:
        - `char`:

        @Return:

        @Error:
        """
        self.append(Token(TokenType.char, char))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# subscanner.py ends here
