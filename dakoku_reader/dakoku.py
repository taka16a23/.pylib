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


LOG = logging.getLogger('Dakoku')


CURRENT_DIR = os.path.dirname(__file__)
SOUNDS_DIR = os.path.join(CURRENT_DIR, 'sounds')
OK_SOIUNDS_FILE = os.path.join(SOUNDS_DIR, 'OK.wav')
ERROR_SOIUNDS_FILE = os.path.join(SOUNDS_DIR, 'Error.wav')


class Dakoku(ReaderObserverAbstract):
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
        if response.ok == True:
            # LOG.debug('response failed')
            subprocess.Popen(('sudo aplay {}'.format(OK_SOIUNDS_FILE)).split())
            return
        if response.text == Dakoku.ReturnCode.SUCCESS:
            LOG.debug('response success 200')
            subprocess.Popen(('sudo aplay {}'.format(ERROR_SOIUNDS_FILE)).split())
            return


def _main():
    logging.basicConfig(level=logging.DEBUG)
    reader = Reader()
    reader.add_observer(Dakoku())
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
