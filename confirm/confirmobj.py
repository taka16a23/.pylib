#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: confirmobj.py 229 2014-09-13 08:17:28Z t1 $
# $Revision: 229 $
# $Date: 2014-09-13 17:17:28 +0900 (Sat, 13 Sep 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-09-13 17:17:28 +0900 (Sat, 13 Sep 2014) $

r"""confirm -- DESCRIPTION

"""
from abc import ABCMeta, abstractmethod
from userinput import UserInputer, ConsoleUserInput
import Tkinter
import tkMessageBox


class Confirm(object):
    r"""Confirm

    Confirm is a object.
    Responsibility:
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def confirm(self, ):
        raise NotImplementedError()


class ConsoleConfirm(Confirm):
    r"""ConsoleConfirm

    ConsoleConfirm is a Confirm.
    Responsibility:
    """
    def __init__(self, prompt=None, acceptables=None, disacceptables=None):
        r"""

        @Arguments:
        - `prompt`:
        - `acceptables`:
        - `disacceptables`:
        """
        self._prompt = prompt or 'Confirm y or n: '
        self._acceptables = acceptables or ['y', 'yes']
        self._disacceptables = disacceptables or ['n', 'no']

    def _input(self, ):
        r"""SUMMARY

        _input()

        @Return:

        @Error:
        """
        string = UserInputer(ConsoleUserInput(self._prompt)).input()
        return string.lower()

    def confirm(self, ):
        r"""SUMMARY

        confirm()

        @Return:

        @Error:
        """
        got = self._input()
        if got in self._acceptables:
            return True
        if got in self._disacceptables:
            return False
        return None

    def get_prompt(self, ):
        r"""SUMMARY

        get_prompt()

        @Return:

        @Error:
        """
        return self._prompt

    def set_prompt(self, prompt):
        r"""SUMMARY

        set_prompt(prompt)

        @Arguments:
        - `prompt`:

        @Return:

        @Error:
        """
        self._prompt = prompt

    def get_acceptables(self, ):
        r"""SUMMARY

        get_acceptables()

        @Return:

        @Error:
        """
        return self._acceptables

    def set_acceptables(self, acceptables):
        r"""SUMMARY

        set_acceptables(acceptables)

        @Arguments:
        - `acceptables`:

        @Return:

        @Error:
        """
        self._acceptables = acceptables

    def get_disacceptables(self, ):
        r"""SUMMARY

        get_disacceptables()

        @Return:

        @Error:
        """
        return self._disacceptables

    def set_disacceptables(self, disacceptables):
        r"""SUMMARY

        set_disacceptables(disacceptables)

        @Arguments:
        - `disacceptables`:

        @Return:

        @Error:
        """
        self._disacceptables = disacceptables


class GUIConfirm(Confirm):
    r"""GUIConfirm

    GUIConfirm is a Confirm.
    Responsibility:
    """
    def __init__(self, title=None, msg=None):
        r"""

        @Arguments:
        - `title`:
        - `msg`:
        """
        self._title = title or 'Confirm'
        self._msg = msg or 'Confirm'

    def confirm(self, ):
        r"""SUMMARY

        confirm()

        @Return:

        @Error:
        """
        root = Tkinter.Tk()
        root.withdraw()
        return tkMessageBox.askyesno(self._title, self._msg)

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



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# confirm.py ends here
