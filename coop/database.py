#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: database.py 485 2015-09-29 03:10:26Z t1 $
# $Revision: 485 $
# $Date: 2015-09-29 12:10:26 +0900 (Tue, 29 Sep 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-09-29 12:10:26 +0900 (Tue, 29 Sep 2015) $

r"""database -- DESCRIPTION

"""
from coop.database_interface import CoopDatabaseInterface


class CoopDatabase(CoopDatabaseInterface):
    r"""CoopDatabase

    CoopDatabase is a CoopDatabaseInterface.
    Responsibility:
    """

    def iter_goods(self, ):
        r"""SUMMARY

        iter_goods()

        @Return:

        @Error:
        """

    def list_goods(self, ):
        r"""SUMMARY

        list_goods()

        @Return:

        @Error:
        """

    def register_goods(self, goods):
        r"""SUMMARY

        register_goods(goods)

        @Arguments:
        - `goods`:

        @Return:

        @Error:
        """

    def unregister_goods(self, goods):
        r"""SUMMARY

        unregister_goods(goods)

        @Arguments:
        - `goods`:

        @Return:

        @Error:
        """

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
# database.py ends here
