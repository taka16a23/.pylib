#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""reader -- dakoku reader

"""
import sys as _sys
import logging

import nfc
import errno

from observable import Observable
from dakoku import Dakoku
from reader_observer import ReaderObserverAbstract

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


LOG = logging.getLogger('dakoku')


class Reader(Observable):
    """Reader

    Reader is a object.
    Responsibility: Read IDm
    """
    def __init__(self, interval=None):
        """
        オブザーバー用に初期化
        """
        Observable.__init__(self)
        self._clf = None

        self._interval = interval

        # connect 用にオプション作成
        # options for reader/writer
        self._rdwr_options = {'on-connect': self._on_rdwr_connect,
                              'on-startup': self._on_rdwr_startup,
                              'on-release': self._on_rdwr_release,
                              'interval': self._interval,
        }
        self.on_create()

    def on_create(self, ):
        """インスタンス作成時に呼ばれる

        on_create()

        @Return:
        None

        @Error:
        """

    # override
    def add_observer(self, observer):
        """add observer for Reader

        add_observer(observer)

        @Arguments:
        - `observer`:

        @Return:

        @Error:
        """
        # require
        if isinstance(observer, (ReaderObserverAbstract, )) is False:
            raise ValueError('observer must be ReaderObserverAbstract type. got({})'
                             .format(type(observer)))
        # do
        super(Reader, self).add_observer(observer)

    def get_interval(self, ):
        """SUMMARY

        get_interval()

        @Return:

        @Error:
        """
        return self._interval

    def set_interval(self, interval):
        """SUMMARY

        set_interval(interval)

        @Arguments:
        - `interval`:

        @Return:

        @Error:
        """
        # require
        if interval is None:
            self._interval = None
            return

        if isinstance(interval, (float, )) is not False:
            raise ValueError('type of interval is not float. got({})'.format(type(interval)))
        if interval < 0:
            raise ValueError('interval not accept less than 0. got({})'.format(interval))

        # do
        self._interval = interval

    ## オブザーバー通知用
    #
    def _notify_before_started(self, ):
        """SUMMARY

        _notify_before_started()

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_before_started(self)

    def _notify_startup(self, targets):
        """SUMMARY

        _notify_startup(targets)

        @Arguments:
        - `targets`:

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_startup(targets)

    def _notify_success(self, tag):
        """tag取得成功時に登録されているリスナーオブジェクトに通知

        @Arguments:
        - `tag`: nfc.tag.Tag

        @Return:
        None

        _notify_success()

        @Error:
        """
        for observer in self._observers:
            observer.on_success(tag)

    def _notify_failed(self, ):
        """tag取得失敗時に登録されているリスナーオブジェクトに通知

        _notify_failed()

        @Return:
        None

        @Error:
        """
        for observer in self._observers:
            observer.on_failed(self)

    def _notify_released(self, tag):
        """SUMMARY

        _notify_released(tag)

        @Arguments:
        - `tag`: nfc.tag.Tag

        @Return:

        @Error:
        """
        for observer in self._observers:
            observer.on_released(tag)

    def _notify_stopped(self, ):
        """実行終了時に登録されているリスナーオブジェクトに通知

        _notify_stopped()

        @Return:
        None

        @Error:
        """
        for observer in self._observers:
            observer.on_stopped(self)

    #####################################################

    ## options for reader/writer
    #
    def _on_rdwr_connect(self, tag):
        """rdwrのon-connect用コールバックメソッド

        _on_rdwr_connect(tag)

        @Arguments:
        - `tag`: nfc.tag.Tag

        @Return: True カードを離すまで待機する

        @Error:
        """
        print('DEBUG-1-reader.py')

        for observer in self._observers:
            observer.on_released(tag)

        # True で返すとカードを離すまで待機
        return True

    def _on_rdwr_startup(self, targets):
        """SUMMARY

        _on_rdwr_startup(targets)

        @Arguments:
        - `targets`:

        @Return:

        @Error:
        """
        # do
        self._notify_startup(targets)

        # ensure
        return targets

    def _on_rdwr_release(self, tag):
        """SUMMARY

        _on_rdwr_release(tag)

        @Arguments:
        - `tag`: nfc.tag.Tag

        @Return:

        @Error:
        """
        # do
        self._notify_released(tag)

        return True

    def _create_clf(self, ):
        """SUMMARY

        _create_clf()

        @Return:

        @Error:
        """
        # do
        try:
            self._clf = nfc.ContactlessFrontend('usb')
        except IOError as error:
            if error.errno == errno.ENODEV:
                # TODO: (Atami) [2018/05/04]
                pass
            elif error.errno == errno.EACCES:
                # TODO: (Atami) [2018/05/04]
                pass
            elif error.errno == errno.EBUSY:
                # TODO: (Atami) [2018/05/04]
                pass
            else:
                # TODO: (Atami) [2018/05/04]
                pass

    def _close_clf(self, ):
        """SUMMARY

        _close_clf()

        @Return:

        @Error:
        """
        # require
        if self._clf is None:
            return

        # do
        self._clf.close()
        self._clf = None

    def _run(self, ):
        """SUMMARY

        _run()

        @Return:

        @Error:
        """
        self._notify_before_started()

        loop = True
        while loop:
            self._create_clf()
            try:
                # _rdwr_options is callback function dictionary
                tag = self._clf.connect(rdwr=self._rdwr_options)
            finally:
                self._close_clf()

        self._notify_stopped()

    def run(self, ):
        """打刻リーダー実装処理

        run()

        @Return:
        None

        @Error:
        """
        try:
            self._run()
        except KeyboardInterrupt as error:
            LOG.info('KeyboardInterrupted!!')
            self._close_clf()


def _main():
    reader = Reader()
    reader.add_observer(Dakoku())
    reader.run()
    return 0

if __name__ == '__main__':
    _sys.exit(_main())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# reader.py ends here
