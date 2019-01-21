#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""dakoku -- DESCRIPTION

"""
import requests
from reader_observer import ReaderObserverAbstract


class Dakoku(ReaderObserverAbstract):
    """Dakoku

    Dakoku is a object.
    Responsibility:
    """
    # temporary
    URL = '192.168.0.2/dakoku/dakoku'

    class ReturnCode(object):
        """ReturnCode

        ReturnCode is a object.
        Responsibility:
        """
        SUCCESS = '100'
        FAILED = '200'
        IDM_NOT_EXISTS = '201'

    def on_released(self, tag):
        """SUMMARY

        on_released(tag)

        @Arguments:
        - `tag`:

        @Return:

        @Error:
        """
        self.dakoku(tag.identifier.encode("hex").upper())

    def dakoku(self, idm):
        """SUMMARY

        dakoku(idm)

        @Arguments:
        - `idm`:

        @Return:

        @Error:
        """
        # require
        print('DEBUG-1-dakoku.py')
        print(idm)
        # do
        params = {'idm': idm,}
        # response = requests.get(self.URL, params=params)
        print('DEBUG-2-dakoku.py')
        # print(response)
        # if response.ok == False:
            # pass
        # if response.text == Dakoku.ReturnCode.SUCCESS:
            # pass
        # ensure



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# dakoku.py ends here
