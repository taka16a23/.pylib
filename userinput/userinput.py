#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: userinput.py 357 2015-08-05 21:41:46Z t1 $
# $Revision: 357 $
# $Date: 2015-08-06 06:41:46 +0900 (Thu, 06 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-06 06:41:46 +0900 (Thu, 06 Aug 2015) $

from abc import ABCMeta, abstractmethod
from easygui import enterbox

from .safeinput import safeinput


class UserInput(object):
    """Abstract class UserInput
    """
    __metaclass__ = ABCMeta

    # Operations
    @abstractmethod
    def input(self):
        """function input

        returns string
        """
        raise NotImplementedError()


class CommandlineUserInput(UserInput):
    """Class CommandlineUserInput
    """
    # Attributes:
    def __init__(self, cmdline):
        r"""

        @Arguments:
        - `username`:
        """
        self._cmdline = cmdline

    # Operations
    def input(self):
        """function input

        returns string
        """
        return self.getcmdline()

    def setcmdline(self, cmdline):
        """function setusername

        username: string

        returns void
        """
        self._cmdline = cmdline

    def getcmdline(self):
        """function getusername

        returns string
        """
        return self._cmdline


class ConsoleUserInput(UserInput):
    """Class ConsoleUserInput
    """
    # Attributes:
    def __init__(self, prompt):
        r"""

        @Arguments:
        - `prompt`:
        """
        self._prompt = prompt

    # Operations
    def input(self):
        """function input

        returns string
        """
        return safeinput(self._prompt)

    def setprompt(self, prompt):
        """function setprompt

        prompt: string

        returns void
        """
        self._prompt = prompt

    def getprompt(self):
        """function getprompt

        returns string
        """
        return self._prompt


class FileUserInput(UserInput):
    """Class FileUserInput
    """
    # Attributes:
    def __init__(self, path):
        r"""

        @Arguments:
        - `path`:
        """
        self._path = path

    # Operations
    def input(self):
        """function input

        returns string
        """
        fileobj = open(self._path, 'r')
        string = fileobj.readline().replace('\n', '')
        fileobj.close()
        return string

    def setpath(self, path):
        """function setpath

        path: string

        returns void
        """
        self._path = path

    def getpath(self):
        """function getpath

        returns string
        """
        return self._path


class GUIUserInput(UserInput):
    """Class GUIUserInput
    """
    # Attributes:
    def __init__(self, msg=None, title=None, default=None):
        r"""

        @Arguments:
        - `msg`:
        - `title`:
        - `text`:
        """
        self._msg = msg or 'Enter text'
        self._title = title or 'Input Box'
        self._default = default or ''

    # Operations
    def input(self):
        """function input

        returns string
        """
        return enterbox(msg=self._msg, title=self._title, default=self._default)

    def get_msg(self, ):
        r"""SUMMARY

        get_msg()

        @Return:

        @Error:
        """
        return self._msg

    def set_msg(self, msg):
        r"""SUMMARY

        set_msg(msg)

        @Arguments:
        - `msg`:

        @Return:

        @Error:
        """
        self._msg = msg

    def get_title(self, ):
        r"""SUMMARY

        get_title()

        @Return:

        @Error:
        """
        return self._title

    def set_title(self, title):
        r"""SUMMARY

        set_title(title)

        @Arguments:
        - `title`:

        @Return:

        @Error:
        """
        self._title = title

    def get_default(self, ):
        r"""SUMMARY

        get_default()

        @Return:

        @Error:
        """
        return self._default

    def set_default(self, default):
        r"""SUMMARY

        set_default(default)

        @Arguments:
        - `default`:

        @Return:

        @Error:
        """
        self._default = default



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# userinput.py ends here
