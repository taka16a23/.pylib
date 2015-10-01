#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: database_interface.py 485 2015-09-29 03:10:26Z t1 $
# $Revision: 485 $
# $Date: 2015-09-29 12:10:26 +0900 (Tue, 29 Sep 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-09-29 12:10:26 +0900 (Tue, 29 Sep 2015) $

r"""database_interface -- DESCRIPTION

"""
from abc import ABCMeta, abstractmethod


class CoopDatabaseInterface(object):
    r"""CoopDatabaseInterface

    CoopDatabaseInterface is a object.
    Responsibility:
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def iter_goods(self, ):
        r"""SUMMARY

        iter_goods()

        @Return:

        @Error:
        """

    @abstractmethod
    def list_goods(self, ):
        r"""SUMMARY

        list_goods()

        @Return:

        @Error:
        """

    @abstractmethod
    def register_goods(self, goods):
        r"""SUMMARY

        register_goods(goods)

        @Arguments:
        - `goods`:

        @Return:

        @Error:
        """

    @abstractmethod
    def unregister_goods(self, goods):
        r"""SUMMARY

        unregister_goods(goods)

        @Arguments:
        - `goods`:

        @Return:

        @Error:
        """

    @abstractmethod
    def register_goods_many(self, goods_list):
        r"""SUMMARY

        register_goods_many(goods_list)

        @Arguments:
        - `goods_list`:

        @Return:

        @Error:
        """



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# database_interface.py ends here
