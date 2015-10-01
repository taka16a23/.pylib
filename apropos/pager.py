#!/usr/bin/env python
# -*- coding: utf-8 -*-

r""" pager -- print result for apropos.

"""
import os as _os
import sys as _sys

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__version__ = '0.1.0'


def normalpager(key, dic, **flags):
    r"""SUMMARY

    @Arguments:
    - `key`:
    - `dic`:

    @Return:
    """
    fmt = '{0:<10} : {1}'.format
    print('\n{0:*<50}'.format(''))
    print(fmt('name', str(dic['name'])))
    try:
        types = str(dic['type']).split("type ")[1].split('>')[0].replace("'", "")
        print(fmt('type', types))
    except IndexError:
        pass
    print(fmt('definition', str(dic['definition'])))
    print(fmt('file', str(dic['file'])))
    print(fmt('summary', str(dic['summary'])))
    if flags.get('indoc', False):
        print(fmt('doc', str(dic['doc'])))


def colorpager(key, dic, **flags):
    r"""SUMMARY

    @Arguments:
    - `key`:
    - `dic`:
    - `** flags`:

    @Return:
    """
    from colorama import Fore, Style, init
    init(autoreset=True)

    def makeanotation(str_, regexp, color):
        r"""SUMMARY

        @Arguments:
        - `str_`:
        - `regexp`:
        - `color`:

        @Return:
        """
        newstr = str_
        for match in regexp.finditer(str_):
            try:
                newstr = (str_[:match.start()] + color +
                          str_[match.start():match.end()] + Fore.RESET +
                          str_[match.end():])
            except TypeError:
                pass
        return newstr

    fmt = (Style.BRIGHT + Fore.GREEN + '   {0:<10}' + ': ' +
           Fore.RESET + Style.NORMAL + '{1}')

    # name
    print('\n{0:*<50}'.format(''))
    print((Style.BRIGHT + Fore.CYAN + '* ' + Fore.RESET +
           makeanotation(str(dic['name']), key, Fore.RED) + Style.NORMAL))
    # type
    try:
        types = str(dic['type']).split("type ")[1].split('>')[0].replace("'", "")
        if 'function' == types:
            types = Style.BRIGHT + Fore.CYAN + types + Style.NORMAL
        elif 'classobj' == types:
            types = Style.BRIGHT + Fore.YELLOW + types.split('obj')[0] + Style.NORMAL
        elif 'type' == types:
            types = Style.BRIGHT + Fore.MAGENTA + types + Style.NORMAL
        print(fmt.format('type', types))
    except IndexError:
        pass

    # definition
    print(fmt.format('definition', str(dic['definition'])))
    # file
    print(fmt.format('file', makeanotation(str(dic['file']), key, Fore.RED)))
    # summary
    print(fmt.format('summary', makeanotation(str(dic['summary']), key, Fore.RED)))
    # doc
    if flags.get('indoc', False):
        print(fmt.format('doc', makeanotation(str(dic['doc']), key, Fore.RED)))



def _test():
    r"""Test function."""
    return 0

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# pager.py ends here
