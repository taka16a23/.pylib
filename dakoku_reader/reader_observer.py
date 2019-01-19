#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""reader_observer -- DESCRIPTION

"""


class ReaderObserverAbstract(object):
    """ReaderObserverAbstract

    ReaderObserverAbstract is a object.
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

    def on_startup(self, targets):
        """SUMMARY

        on_startup(targets)

        @Arguments:
        - `targets`:

        @Return:

        @Error:
        """

    def on_failed(self, reader):
        """SUMMARY

        on_failed(reader)

        @Arguments:
        - `reader`:

        @Return:

        @Error:
        """

    def on_released(self, tag):
        """SUMMARY

        on_released(tag)

        @Arguments:
        - `tag`:

        @Return:

        @Error:
        """

    def on_stopped(self, reader):
        """SUMMARY

        on_stopped(reader)

        @Arguments:
        - `reader`:

        @Return:

        @Error:
        """



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# reader_observer.py ends here
