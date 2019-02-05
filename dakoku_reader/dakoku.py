#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""dakoku -- DESCRIPTION

"""
import sys as _sys
import logging
import os
import subprocess

import requests

from NfcReader.reader_observer import ReaderObserverAbstract
from NfcReader.reader import Reader
from NfcReader.debug_observer import DebugReader

from dakoku_reader.observable import Observable
from dakoku_reader.debug_dakoku_observer import DebugDakokuObserver


LOG = logging.getLogger('Dakoku')


CURRENT_DIR = os.path.dirname(__file__)
SOUNDS_DIR = os.path.join(CURRENT_DIR, 'sounds')
OK_SOIUNDS_FILE = os.path.join(SOUNDS_DIR, 'OK.wav')
ERROR_SOIUNDS_FILE = os.path.join(SOUNDS_DIR, 'Error.wav')


class Dakoku(ReaderObserverAbstract, Observable):
    """Dakoku

    Dakoku is a object.
    Responsibility:
    """
    # temporary
    URL = 'http://192.168.0.2/dakoku/dakoku'

    class ReturnCode(object):
        """ReturnCode

        ReturnCode is a object.
        Responsibility:
        """
        SUCCESS = '100'
        FAILED = '200'
        IDM_NOT_EXISTS = '201'

    def __init__(self, ):
        Observable.__init__(self)

    def on_before_dakoku(self, ):
        """SUMMARY

        on_before_dakoku()

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_before_dakoku()

    def notify_success(self, response):
        """SUMMARY

        @Arguments:
        - `response`:

        @Return:

        notify_success()

        @Error:
        """
        for observer in self._observers:
            observer.on_success(response)

    def notify_failed_connection(self, ):
        """SUMMARY

        notify_failed_connection()

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_failed_connection()

    def notify_failed_dakoku(self, response):
        """SUMMARY

        @Arguments:
        - `response`:

        @Return:

        notify_failed_dakoku()

        @Error:
        """
        for observer in self._observers:
            observer.on_failed_dakoku(response)

    def notify_on_released(self, ):
        """SUMMARY

        notify_on_released()

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_released()

    def on_touched(self, tag):
        """SUMMARY

        on_touched(tag)

        @Arguments:
        - `tag`:

        @Return:

        @Error:
        """
        self.dakoku(tag.identifier.encode("hex").upper())

    def on_released(self, tag):
        """SUMMARY

        on_released(tag)

        @Arguments:
        - `tag`:

        @Return:

        @Error:
        """
        self.notify_on_released()

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
        try:
            response = requests.get(self.URL, params=params)
        except requests.exceptions.ConnectionError:
            self.notify_failed_connection()
        if response.ok:
            self.notify_success(response)
            return
        if not response.ok:
            self.notify_failed_dakoku(response)
            return


def _main():
    logging.basicConfig(level=logging.DEBUG)
    reader = Reader()
    dakoku = Dakoku()
    dakoku.add_observer(DebugDakokuObserver())
    reader.add_observer(dakoku)
    reader.add_observer(DebugReader())
    reader.run()
    return 0

if __name__ == '__main__':
    _sys.exit(_main())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# dakoku.py ends here
