#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""easy -- DESCRIPTION

"""
from easygui import passwordbox
from getpasswd.getter.abstract import PassGetter


class EasyGUIPassGetter(PassGetter):
    r"""EasyGUIPassGetter

    EasyGUIPassGetter is a PassGetter.
    Responsibility:
    """
    def __init__(self, title='Input password', default='',
                 image=None, root=None):
        r"""

        @Arguments:
        - `title`:
        - `default`:
        - `image`:
        - `root`:
        """
        self._title = title
        self._default = default
        self._image = image
        self._root = root

    def gettitle(self, ):
        r"""SUMMARY

        gettitle()

        @Return:

        @Error:
        """
        return self._title

    def settitle(self, title='Input password'):
        r"""SUMMARY

        settitle(title='Input password')

        @Arguments:
        - `title`:

        @Return:

        @Error:
        """
        self._title = title

    def getdefault(self, ):
        r"""SUMMARY

        getdefault()

        @Return:

        @Error:
        """
        return self._default

    def setdefault(self, default=''):
        r"""SUMMARY

        setdefault(default='')

        @Arguments:
        - `default`:

        @Return:

        @Error:
        """
        self._default = default

    def getimage(self, ):
        r"""SUMMARY

        getimage()

        @Return:

        @Error:
        """
        return self._image

    def setimage(self, image=None):
        r"""SUMMARY

        setimage(image=None)

        @Arguments:
        - `image`:

        @Return:

        @Error:
        """
        self._image = image

    def getroot(self, ):
        r"""SUMMARY

        getroot()

        @Return:

        @Error:
        """
        return self._root

    def setroot(self, root=None):
        r"""SUMMARY

        setroot(root=None)

        @Arguments:
        - `root`:

        @Return:

        @Error:
        """
        self._root = root

    def getpass(self, prompt='Password: '):
        r"""SUMMARY

        getpass(prompt='Password: ')

        @Arguments:
        - `prompt`:

        @Return:

        @Error:
        """
        return passwordbox(msg=prompt, title=self._title, default=self._default,
                           image=self._image, root=self._root)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# easy.py ends here
