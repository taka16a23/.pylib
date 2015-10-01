#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: archive.py 305 2015-02-07 03:47:58Z t1 $
# $Revision: 305 $
# $Date: 2015-02-07 12:47:58 +0900 (Sat, 07 Feb 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-02-07 12:47:58 +0900 (Sat, 07 Feb 2015) $

r"""archive -- DESCRIPTION

"""
from . import abstract
from . import data


class MyArchive(abstract.MyPath):
    r"""MyArchive

    MyArchive is a abstract.MyPath.
    Responsibility:
    """
    root = data.MyData()

    def get_root(self, ):
        r"""SUMMARY

        getroot()

        @Return:

        @Error:
        """
        return self.root

    def get_path(self, ):
        r"""SUMMARY

        get_path()

        @Return:

        @Error:
        """
        return self.get_root().get_path().join('archive')

    def isexists(self, ):
        r"""SUMMARY

        isexists()

        @Return:

        @Error:
        """
        return self.get_path().exists()

    def pave(self, ):
        r"""SUMMARY

        pave()

        @Return:

        @Error:
        """
        self.get_root().pave()
        path = self.get_path()
        if not path.exists():
            path.mkdir()

    def __str__(self):
        return str(self.get_path())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# archive.py ends here
