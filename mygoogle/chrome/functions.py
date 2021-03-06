#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""functions -- a parts of chrome functions

"""
import sh
import predicate

from mygoogle.chrome import ChromeBMParse


__all__ = ['get_urls', 'run', 'open_folder']



def get_urls(name):
    """SUMMARY

    @Arguments:
    - `name`:

    @Return:
    """
    return list(ChromeBMParse(name))


# @singledispatch
def run(url, options=None):
    r"""SUMMARY

    run(url, options=[])

    @Arguments:
    - `url`:
    - `options`:

    @Return:
    """
    # if isinstance(url, (list, )):
        # url = ' '.join(url)
    options = options or []
    if not predicate.islist(options):
        raise ValueError('Must be list {}'.format(options))
    sh.google_chrome(url, options, _bg=True)


def open_folder(folder_name, options=None, reverse=False):
    r"""SUMMARY

    open_folder(folder_name, options=[])

    @Arguments:
    - `folder_name`:
    - `options`:

    @Return:
    """
    options = options or []
    lis = list(ChromeBMParse(folder_name))
    if reverse:
        lis.reverse()
    run(lis, options=options)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# functions.py ends here
