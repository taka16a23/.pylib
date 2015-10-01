#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: backup.py 468 2015-08-19 05:49:01Z t1 $
# $Revision: 468 $
# $Date: 2015-08-19 14:49:01 +0900 (Wed, 19 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-19 14:49:01 +0900 (Wed, 19 Aug 2015) $

r"""backup -- DESCRIPTION

"""
from . import abstract
from . import data


class MyBackup(abstract.MyPath):
    r"""MyBackup

    MyBackup is a abstract.MyPath.
    Responsibility:
    """
    root = data.MyData()

    def get_root(self, ):
        r"""SUMMARY

        get_root()

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
        return self.get_path()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# backup.py ends here
