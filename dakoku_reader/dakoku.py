#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""dakoku -- DESCRIPTION

"""
import requests


class Dakoku(object):
    """Dakoku

    Dakoku is a object.
    Responsibility:
    """
    URL = '192.168.0.2/dakoku/dakoku'

    class ReturnCode(object):
        """ReturnCode

        ReturnCode is a object.
        Responsibility:
        """
        SUCCESS = '100'
        FAILED = '200'
        IDM_NOT_EXISTS = '201'

    def dakoku(self, idm):
        """SUMMARY

        dakoku(idm)

        @Arguments:
        - `idm`:

        @Return:

        @Error:
        """
        # require
        print(idm)
        # do
        params = {'idm': idm,}
        response = requests.get(self.URL, params=params)
        print(response)
        if response.ok == False:
            pass
        if response.text == Dakoku.ReturnCode.SUCCESS:
            pass
        # ensure



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# dakoku.py ends here
