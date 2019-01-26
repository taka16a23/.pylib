#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ReaderObserverAbstract(object):
    """ReaderObserverAbstract

    ReaderObserverAbstract is a object.
    Responsibility: Observe nfc Reader.
    """

    def on_before_started(self, reader):
        """This method will called at before Reader startup.

        on_before_started(reader)

        @Arguments:
        - `reader`: Reader object

        @Return: None

        @Error:
        """

    def on_stopped(self, reader):
        """This method will called at Reader stopped.

        on_stopped(reader)

        @Arguments:
        - `reader`: Reader object

        @Return: None

        @Error:
        """

    def on_startup(self, targets):
        """This method will called at each startup Reader.

        on_startup(targets)

        @Arguments:
        - `targets`: list of Target class
        data of a remote card or device.

        @Return: None

        @Error:
        """

    def on_failed(self, reader):
        """This method will called at failed Reader get tag.

        on_failed(reader)

        @Arguments:
        - `reader`: Reader object

        @Return: None

        @Error:
        """

    def on_touched(self, tag):
        """This method will called at card touch.

        on_touched(tag)

        @Arguments:
        - `tag`: Tag object

        @Return: None

        @Error:
        """

    def on_released(self, tag):
        """This method will called at card release.

        on_released(tag)

        @Arguments:
        - `tag`: Tag object

        @Return: None

        @Error:
        """



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# reader_observer.py ends here
