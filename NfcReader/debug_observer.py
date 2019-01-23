#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""debug_observer -- debug reader observer

"""
import logging

from NfcReader.reader_observer import ReaderObserverAbstract


LOG = logging.getLogger('NfcReader')


class DebugReader(ReaderObserverAbstract):
    """DebugReader

    DebugReader is a object.
    Responsibility:
    """

    def on_before_started(self, reader):
        """SUMMARY

        on_before_started(reader)

        @Arguments:
        - `reader`:

        @Return:

        @Error:
        """
        LOG.debug('on_before_started')

    def on_startup(self, targets):
        """SUMMARY

        on_startup(targets)

        @Arguments:
        - `targets`:

        @Return:

        @Error:
        """
        LOG.debug('on_startup')

    def on_failed(self, reader):
        """SUMMARY

        on_failed(reader)

        @Arguments:
        - `reader`:

        @Return:

        @Error:
        """
        LOG.debug('on_failed')

    def on_released(self, tag):
        """SUMMARY

        on_released(tag)

        @Arguments:
        - `tag`:

        @Return:

        @Error:
        """
        LOG.debug('on_released')

    def on_stopped(self, reader):
        """SUMMARY

        on_stopped(reader)

        @Arguments:
        - `reader`:

        @Return:

        @Error:
        """
        LOG.debug('on_stopped')



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# debug_observer.py ends here
