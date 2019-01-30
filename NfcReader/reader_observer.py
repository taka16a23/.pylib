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

    def on_failed_before_started(self, reader, error):
        """This method will called when failed `on_before_started`.

        on_failed_before_started(reader)

        @Arguments:
        - `reader`: Reader object
        - `error`: type of Exception object

        @Return: None

        @Error:
        """

    def on_stopped(self, reader):
        """This method will called when Reader stopped.

        on_stopped(reader)

        @Arguments:
        - `reader`: Reader object

        @Return: None

        @Error:
        """

    def on_failed_stopped(self, reader, error):
        """This method will called when failed `on_stopped` method.

        on_failed_stopped(reader, error)

        @Arguments:
        - `reader`: Reader object
        - `error`: type of Exception object

        @Return: None

        @Error:
        """

    def on_startup(self, targets):
        """This method will called when wait connection.

        on_startup(targets)

        @Arguments:
        - `targets`: list of Target instance
        data of a remote card or device.

        @Return: None

        @Error:
        """

    def on_failed_startup(self, targets, error):
        """This method will called when failed `on_startup` method.

        on_failed_startup(targets, error)

        @Arguments:
        - `targets`: list of Target instance
        - `error`: type of Exception object

        @Return: None

        @Error:
        """

    def on_failed_connection(self, reader):
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
