#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import errno

import nfc

from NfcReader.observable import Observable
from NfcReader.reader_observer import ReaderObserverAbstract

LOG = logging.getLogger('NfcReader')


class Reader(Observable):
    """Felica Reader

    Reader is a object.
    Responsibility: Read IDm
    """
    def __init__(self, interval=None, wait_release=True):
        # Initialize for observer
        Observable.__init__(self)
        self._clf = None

        # set interval time for each connect
        if interval is not None:
            interval = float(interval)
        self._interval = interval

        # wait release when connected
        self.is_wait_release = bool(wait_release)

        # connect 用にオプション作成
        # options for reader/writer
        self._rdwr_options = {'on-connect': self._on_rdwr_connect,
                              'on-startup': self._on_rdwr_startup,
                              'on-release': self._on_rdwr_release,
                              'interval': self._interval,
        }
        self.on_create()

    def add_observer(self, observer):
        """Add ReaderObserverAbstract observer.

        add_observer(observer)

        @Arguments:
        - `observer`: ReaderObserverAbstract

        @Return: None

        @Error: TypeError if observer not ReaderObserverAbstract.

        Overrided Observer.add_observer
        """
        if not isinstance(observer, (ReaderObserverAbstract, )):
            raise TypeError(
                'TypeError: observer argument require ReaderObserverAbstract. got({})'
                .format(observer))
        super(Reader, self).add_observer(observer)

    def on_create(self, ):
        """Called on Constracted.

        on_create()

        @Return: None

        @Error:
        """

    # override
    def add_observer(self, observer):
        """Add observer for Reader.

        add_observer(observer)

        @Arguments:
        - `observer`: Require instance of ReaderObserverAbstract

        @Return: None

        @Error:
        """
        # require
        if isinstance(observer, (ReaderObserverAbstract, )) is False:
            raise ValueError('observer must be ReaderObserverAbstract type. got({})'
                             .format(type(observer)))
        # do
        super(Reader, self).add_observer(observer)

    def get_interval(self, ):
        """Get interval value.

        get_interval()

        @Return: None or float

        @Error:
        """
        return self._interval

    def set_interval(self, interval):
        """Set interval value at Reader each connection.

        set_interval(interval)

        @Arguments:
        - `interval`: float value.

        @Return: None

        @Error:
        TypeError: raise error if not float type.
        ValueError: raise error if value less than 0.
        """
        # require
        if interval is None:
            self._interval = None
            return
        if isinstance(interval, (float, )) is not False:
            raise TypeError('type of interval is not float. got({})'.format(type(interval)))
        if interval < 0:
            raise ValueError('interval not accept less than 0. got({})'.format(interval))

        # do
        self._interval = interval

    ## notifer for observer
    def _notify_before_started(self, ):
        """Notify to register observers on before Reader start loop.

        _notify_before_started()

        @Return: None

        @Error:

        Require method on_before_started.
        Path this object.
        """
        for observer in self._observers:
            observer.on_before_started(self)

    def _notify_startup(self, targets):
        """Notify to register observers on Reader before each connect.

        _notify_startup(targets)

        @Arguments:
        - `targets`: Target

        @Return: None

        @Error:
        """
        for observer in self._observers:
            observer.on_startup(targets)

    def _notify_failed_connection(self, ):
        """Notify to register observers on Reader fail to read tag.

        _notify_failed()

        @Return: None

        @Error:
        """
        for observer in self._observers:
            observer.on_failed_connection(self)

    def _notify_touched(self, tag):
        """Notify to register observers when a remote tag has been activated.

        _notify_touched(tag)

        observer object require on_touched method

        @Arguments:
        - `tag`: `nfc.tag.Tag` object

        @Return: None

        @Error:
        """
        for observer in self._observers:
            observer.on_touched(tag)

    def _notify_released(self, tag):
        """Notify to register observers when release cards.

        _notify_released(tag)

        observer object require on_released method

        @Arguments:
        - `tag`: nfc.tag.Tag

        @Return: None

        @Error:
        """
        for observer in self._observers:
            observer.on_released(tag)

    def _notify_stopped(self, ):
        """Notify to register observers when end of Reader looping.

        _notify_stopped()

        @Return: None

        @Error:
        """
        for observer in self._observers:
            observer.on_stopped(self)

    ############################################################################

    ## options for reader/writer
    #
    def _on_rdwr_connect(self, tag):
        """Callback rdwr method for on-connect.

        _on_rdwr_connect(tag)

        @Arguments:
        - `tag`: nfc.tag.Tag

        @Return: Bool: Wait until release card if return value is True.

        @Error:
        """
        self._notify_touched(tag)
        # Wait until release card if return value is True.
        return self.is_wait_release

    def _on_rdwr_startup(self, targets):
        """Callback rdwr method for on-startup.

        _on_rdwr_startup(targets)

        @Arguments:
        - `targets`: list of Target object.

        @Return: None

        @Error:
        """
        # do
        self._notify_startup(targets)

        # ensure
        return targets

    def _on_rdwr_release(self, tag):
        """Callback rdwr method for on-release.

        _on_rdwr_release(tag)

        @Arguments:
        - `tag`: nfc.tag.Tag

        @Return: None

        @Error:
        """
        self._notify_released(tag)
        return True

    def _create_clf(self, ):
        """Create ContactlessFrontend instance.

        Use usb path.

        _create_clf()

        @Return: None

        @Error:
        """
        try:
            self._clf = nfc.ContactlessFrontend('usb')
        except IOError as error:
            if error.errno == errno.ENODEV:
                LOG.info('no contactless reader found on usb')
            elif error.errno == errno.EACCES:
                LOG.info('access denied for device with path usb')
            elif error.errno == errno.EBUSY:
                LOG.info("the reader on usb is busy")
            else:
                LOG.debug(repr(error) + "when trying usb")
            raise SystemExit(-1)

    def _close_clf(self, ):
        """Call ContactlessFrontend.close().

        _close_clf()

        @Return: None

        @Error:
        """
        # require
        if self._clf is None:
            return

        # do
        self._clf.close()
        self._clf = None

    def _run(self, ):
        """Run Reader connection.

        _run()

        @Return: None

        @Error:
        """
        self._create_clf()
        try:
            # _rdwr_options is callback function dictionary
            if self._clf.connect(rdwr=self._rdwr_options) != True:
                self._notify_failed_connection()
        finally:
            self._close_clf()

    def run(self, ):
        """Interface for Reader run connection.

        run()

        @Return: None

        @Error:
        """
        self._notify_before_started()

        while 1:
            try:
                self._run()
            except KeyboardInterrupt as error:
                LOG.info('KeyboardInterrupted!!')
                self._close_clf()
                break

        self._notify_stopped()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# reader.py ends here
