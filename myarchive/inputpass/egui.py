#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: egui.py 285 2015-01-29 00:12:29Z t1 $
# $Revision: 285 $
# $Date: 2015-01-29 09:12:29 +0900 (Thu, 29 Jan 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-01-29 09:12:29 +0900 (Thu, 29 Jan 2015) $

r"""easygui -- DESCRIPTION

"""
import easygui
from . import abstract


class EasyGUIInputPass(abstract.InputPass):
    r"""EasyGUIInputPass

    EasyGUIInputPass is a abstract.InputPass.
    Responsibility:
    """
    def __init__(self, prompt='Password: ', title='', default='',
                 image=None, root=None):
        r"""

        @Arguments:
        - `prompt`:
        - `title`:
        - `default`:
        - `image`:
        - `root`:
        """
        self._prompt = prompt
        self._title = title
        self._default = default
        self._image = image
        self._root = root

    def set_prompt(self, msg):
        r"""SUMMARY

        set_prompt(msg)

        @Arguments:
        - `msg`:

        @Return:

        @Error:
        """
        self._prompt = msg

    def get_prompt(self, ):
        r"""SUMMARY

        get_prompt()

        @Return:

        @Error:
        """
        return self._prompt

    def set_title(self, title):
        r"""SUMMARY

        set_title(title)

        @Arguments:
        - `title`:

        @Return:

        @Error:
        """
        self._title = title

    def get_title(self, ):
        r"""SUMMARY

        get_title()

        @Return:

        @Error:
        """
        return self._title

    def set_image(self, image=None):
        r"""SUMMARY

        set_image(image=None)

        @Arguments:
        - `image`:

        @Return:

        @Error:
        """
        self._image = image

    def get_image(self, ):
        r"""SUMMARY

        get_image()

        @Return:

        @Error:
        """
        return self._image

    def set_root(self, root=None):
        r"""SUMMARY

        set_root(root=None)

        @Arguments:
        - `root`:

        @Return:

        @Error:
        """
        self._root = root

    def get_root(self, ):
        r"""SUMMARY

        get_root()

        @Return:

        @Error:
        """
        return self._root

    def input(self, ):
        r"""SUMMARY

        input()

        @Return:

        @Error:
        """
        return easygui.passwordbox(
            msg=self._prompt, title=self._title, default=self._default,
            image=self._image, root=self._root)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# easygui.py ends here
