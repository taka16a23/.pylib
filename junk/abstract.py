#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id: abstract.py 421 2015-08-07 00:28:38Z t1 $
# $Revision: 421 $
# $Date: 2015-08-07 09:28:38 +0900 (Fri, 07 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-07 09:28:38 +0900 (Fri, 07 Aug 2015) $
""" abstract -- abstract

$Revision: 421 $

"""
import cPickle

__revision__ = '$Revision: 421 $'
__version__ = '0.1.0'


class Verbose(object):
    """Abstract for verbose mode."""

    def __init__(self, verbose=False):
        self._verbose = verbose

    def verbose_on(self, verbose=False):
        """Turn on verbose mode."""
        self._verbose = True
        if verbose:
            print('Truned On verbose mode')

    def verbose_off(self, verbose=False):
        """Turn off verbose mode."""
        self._verbose = False
        if verbose:
            print('Truned Off verbose mode')

    def _ifverbose(self, *args):
        """SUMMARY

        @Arguments:

        - `*args`:

        @Return:
        """
        if self._verbose:
            for v in args:
                print(v)


class SavePickle(object):
    r"""
    """

    def __init__(self, filepath):
        r"""SUMMARY

        __init__(basedir)

        @Arguments:
        - `basedir`:

        @Return:
        """
        self.pickle_file = filepath

    def save_pickle(self, ):
        r"""SUMMARY

        save()

        @Return:
        """
        with open(self.pickle_file, 'wb') as fobj:
            cPickle.dump(self, fobj, cPickle.HIGHEST_PROTOCOL)


def pickle_resume(filepath):
    return cPickle.load(open(filepath, 'rb'))




def test():
    pass


if __name__ == '__main__':
    test()


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# abstract.py ends here
