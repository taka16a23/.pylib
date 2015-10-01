#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: cacheatom.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""cacheatom -- DESCRIPTION

"""
from xcb2.xobj.atom.atompair import AtomPair


__all__ = ['CacheAtomPair', 'DisplayCacheAtomPair', 'GlobalCacheAtoms']


class CacheAtomPair(dict):
    r"""SUMMARY
    """

    def dual_add(self, atompair):
        r"""SUMMARY

        _dual_add(atompair)

        @Arguments:
        - `atompair`:

        @Return:
        """
        self[str(atompair)] = atompair
        self[int(atompair)] = atompair

    def __setitem__(self, key, value):
        r"""SUMMARY

        __setitem__(key, value)

        @Arguments:
        - `key`:
        - `value`:

        @Return:
        """
        if not isinstance(value, AtomPair):
            # TODO: (Atami) [2014/05/08]
            raise StandardError('type error')
        super(CacheAtomPair, self).__setitem__(key, value)


class DisplayCacheAtomPair(dict):
    r"""SUMMARY
    """
    _class = CacheAtomPair

    def get(self, display):
        r"""SUMMARY

        get(display)

        @Arguments:
        - `display`:

        @Return:
        """
        return self[display]

    def __getitem__(self, key):
        r"""SUMMARY

        __getitem__(key)()

        @Return:
        """
        if not key in self:
            self[key] = self._class()
        return super(DisplayCacheAtomPair, self).__getitem__(key)


class GlobalCacheAtoms(object):
    r"""SUMMARY
    """
    displaymap = DisplayCacheAtomPair()

    @staticmethod
    def getcaches(display=''):
        r"""SUMMARY

        get(display='')

        @Arguments:
        - `display`:

        @Return:
        """
        return GlobalCacheAtoms.displaymap.get(display)

    @staticmethod
    def getatom(cachekey, display=''):
        r"""SUMMARY

        getatom(cachekey)

        @Arguments:
        - `cachekey`:

        @Return:
        """
        return GlobalCacheAtoms.getcaches(display).get(cachekey, None)

    @staticmethod
    def add(atompair, display=''):
        r"""SUMMARY

        add(atompair, display='')

        @Arguments:
        - `atompair`:
        - `display`:

        @Return:
        """
        GlobalCacheAtoms.getcaches(display).dual_add(atompair)

    @staticmethod
    def iscached(cachekey, display=''):
        r"""SUMMARY

        iscached(cachekey)

        @Arguments:
        - `cachekey`:

        @Return:
        """
        if isinstance(cachekey, AtomPair):
            cachekey = int(cachekey)
        return cachekey in GlobalCacheAtoms.getcaches(display)

    @staticmethod
    def clearall():
        r"""SUMMARY

        clearall()

        @Return:
        """
        GlobalCacheAtoms.displaymap.clear()

    @staticmethod
    def clear(display=''):
        r"""SUMMARY

        clear(display='')

        @Arguments:
        - `display`:

        @Return:
        """
        GlobalCacheAtoms.getcaches(display).clear()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# cacheatom.py ends here
