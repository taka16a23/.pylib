#!/usr/bin/env python
# -*- coding: utf-8 -*-r"""\
Name: __main__.py

"""
import sys
import argparse
import re

from .explorer import explorer
from .pager import colorpager, normalpager

# for debug
import cgitb
cgitb.enable(format='text')


__version__ = '0.1.0'


def _predef_options():
    parser = argparse.ArgumentParser(description="""apropos""")
    parser.add_argument('--version',
                        dest='version',
                        action='version',
                        version=__version__,
                        help='Version Strings.')

    parser.add_argument('key',
                        action='store',
                        nargs=argparse.ONE_OR_MORE,
                        default=None,
                        help='Search key as regexp.')

    parser.add_argument('--color-normal',
                        dest='color_normal',
                        action='store_true',
                        default=False,
                        required=False,
                        # (yas/expand-link "argparse_other_options" t)
                        help='Normal print')

    parser.add_argument('--nosearch-name',
                        dest='nosearch_name',
                        action='store_false',
                        default=True,
                        required=False,
                        # (yas/expand-link "argparse_other_options" t)
                        help='Disable name search.')

    parser.add_argument('--search-file',
                        dest='search_file',
                        action='store_true',
                        default=False,
                        required=False,
                        # (yas/expand-link "argparse_other_options" t)
                        help='Enable search file')

    parser.add_argument('--search-definition',
                        dest='search_definition',
                        action='store_true',
                        default=False,
                        required=False,
                        # (yas/expand-link "argparse_other_options" t)
                        help='Enable search definition')

    parser.add_argument('--nosearch-summary',
                        dest='nosearch_summary',
                        action='store_false',
                        default=True,
                        required=False,
                        # (yas/expand-link "argparse_other_options" t)
                        help='Disable search summary')

    parser.add_argument('--search-doc',
                        dest='search_doc',
                        action='store_true',
                        default=False,
                        required=False,
                        # (yas/expand-link "argparse_other_options" t)
                        help='Enable search doc')

    # (yas/expand-link "argparse_add_argument" t)
    return parser

def _main():
    r"""Main function."""
    parser = _predef_options()
    opts = parser.parse_args()
    if not opts.key:
        parser.print_usage()
        return 1

    # set pager
    # if opts.color_normal:
    #     pager = normalpager
    # else:
    #     pager = colorpager
    pager = (opts.color_normal and normalpager or colorpager)

    keywords = '|'.join(opts.key)
    print('Search keywords "{}"\n\n'.format(keywords))
    explorer(key=keywords, pager=pager, inname=opts.nosearch_name,
             infile=opts.search_file, indef=opts.search_definition,
             insummary=opts.nosearch_summary, indoc=opts.search_doc)

    return 0


## Do Main!!
if __name__ == '__main__':
    sys.exit(_main())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __main__.py ends here
