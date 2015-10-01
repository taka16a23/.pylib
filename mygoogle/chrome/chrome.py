#!/usr/bin/env python
# -*- coding: utf-8 -*-
r""" chrome -- handling for google chrome.

Changelog:
inpremented iterator `ChromeMBParse`


"""
from mygoogle.chrome.utils import trim_url
from mygoogle.chrome.variables import BOOKMARK_PATH
from mygoogle.chrome.error import NoExistsFolderError

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__version__ = '0.3.0'


class ChromeBMBuffer(object):
    r"""
    """
    _notfound =- 1
    _alllines = None

    def __init__(self, bmpath=None):
        r"""

        @Arguments:
        - `bmpath`:
        """
        self._bmpath = bmpath or BOOKMARK_PATH
        self.current_line_num = 0
        self.loadfile()

    def loadfile(self, bmpath=None):
        r"""SUMMARY

        loadfile()

        @Return:
        """
        if bmpath:
            self._bmpath = bmpath
        with open(self._bmpath, 'r') as bmfile:
            self._alllines = bmfile.readlines()

    def reloadfile(self, ):
        r"""Ailias of self.loadfile()

        reloadfile()

        @Return:
        """
        self.loadfile()

    def seek_blockend(self):
        """Move initialize line.

        @Return: Nothing
        """
        while (not self.find_inline(']') and 0 != self.current_line_num):
            self.current_line_num -= 1

    def get_currentline(self, ):
        r"""SUMMARY

        get_currentline()

        @Return:
        """
        return self._alllines[self.current_line_num]

    def find_inline(self, str_):
        r"""SUMMARY

        find_inline(str_)

        @Arguments:
        - `str_`:

        @Return:
        bool
        """
        if self._notfound == self.get_currentline().find(str_):
            return False
        return True


class ChromeBMParse(ChromeBMBuffer):
    r"""
    """

    def __init__(self, name, bmpath=None):
        r"""

        @Arguments:
        - `name`:
        - `bmpath`:
        """
        ChromeBMBuffer.__init__(self, bmpath)
        self._name = name

    def getline_num(self):
        """Determine line number of name.

        @Arguments:

        - `name`: elements name

        @Return: line number
        """
        for num, line in enumerate(self._alllines):
            if '"name":' in line:
                trimed = line.split('"name":')[1].split('"')[1]
                if self._name == trimed:
                    self.current_line_num = num - 1
        if 0 == self.current_line_num:
            raise NoExistsFolderError(self._name)

    def __iter__(self):
        self.current_line_num = 0
        self.getline_num()
        self.seek_blockend()
        return self

    def next(self):
        """Parse urls"""
        operand = -1
        while operand < 0:
            self.current_line_num -= 1
            if self.find_inline('}'):
                operand -= 1
            if self.find_inline('{'):
                operand += 1
            if operand == -1:
                if self.find_inline('"url":'):
                    result = trim_url(self.get_currentline())
                    if result:
                        return result
        raise StopIteration


def test():
    pass


if __name__ == '__main__':
    test()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# chrome.py ends here
