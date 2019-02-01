#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""debug_dakoku_observer -- DESCRIPTION

"""


from dakoku_reader.dakoku_observer import DakokuObserver


class DebugDakokuObserver(DakokuObserver):
    """DebugDakokuObserver

    DebugDakokuObserver is a DakokuObserver.
    Responsibility:
    """
    def on_before_dakoku(self, ):
        """SUMMARY

        on_before_dakoku()

        @Return:

        @Error:
        """
        print('on before dakoku')

    def on_success(self, response):
        """SUMMARY

        on_success()

        @Return:

        @Error:
        """
        print('on success')

    def on_failed_connection(self, ):
        """SUMMARY

        on_failed_connection()

        @Return:

        @Error:
        """
        print('on failed connection')

    def on_failed_dakoku(self, response):
        """SUMMARY

        @Arguments:
        - `response`:

        @Return:

        on_failed_dakoku()

        @Error:
        """
        print('on failed dakoku')

    def on_released(self, ):
        """SUMMARY

        on_released()

        @Return:

        @Error:
        """
        print('on released')



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# debug_dakoku_observer.py ends here
