#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""_pickleself -- DESCRIPTION

"""
import cPickle

from pathhandler import PathHandler


class PickleSelf(object):
    r"""PickleSelf

    PickleSelf is a object.
    Responsibility:
    """
    def __init__(self, path, protocol=0):
        r"""

        @Arguments:
        - `path`:
        """
        self._path = PathHandler(path)
        self._protocol = protocol

    def get_path(self, ):
        r"""SUMMARY

        get_path()

        @Return:

        @Error:
        """
        return self._path

    def set_path(self, path):
        r"""SUMMARY

        set_path(path)

        @Arguments:
        - `path`:

        @Return:

        @Error:
        """
        self._path = PathHandler(path)

    path = property(get_path, set_path)

    def get_protocol(self, ):
        r"""SUMMARY

        get_protocol()

        @Return:

        @Error:
        """
        return self._protocol

    def set_protocol(self, protocol):
        r"""SUMMARY

        set_protocol(protocol)

        @Arguments:
        - `protocol`:

        @Return:

        @Error:
        """
        self._protocol = protocol

    protocol = property(get_protocol, set_protocol)

    def load_pickle(self, ):
        r"""SUMMARY

        load_pickle()

        @Return:

        @Error:
        """
        with self.path.open('rb') as fobj:
            return cPickle.load(fobj)

    def is_pickled(self, ):
        r"""SUMMARY

        is_pickled()

        @Return:

        @Error:
        """
        return self.path.exists()

    def dump_pickle(self, ):
        r"""SUMMARY

        dump_pickle()

        @Return:

        @Error:
        """
        with self.path.open('wb') as fobj:
            cPickle.dump(self, fobj, self.protocol)

    def remove_pickle(self, ):
        r"""SUMMARY

        remove_pickle()

        @Return:

        @Error:
        """
        if self.is_pickled():
            self.path.remove()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _pickleself.py ends here
