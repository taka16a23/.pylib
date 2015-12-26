#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __main__.py

"""
import sys
import os
import argparse
import datetime
from dateutil.relativedelta import relativedelta

from colorama import Fore, Style

from holiday import japan, __version__, international_name


HOLIDAYS_CLASSES = {'japan': japan.JapaneseDay,}


def _predef_options():
    parser = argparse.ArgumentParser(description="""""")
    parser.add_argument('--version',
                        dest='version',
                        action='version',
                        version=__version__,
                        help='Version Strings.')
    parser.add_argument('--country',
                        dest='country',
                        action='store',
                        default='japan',
                        type=str,
                        # (yas/expand-link "argparse_other_options" t)
                        help='Show elected nations holidays.\n"japan"')
    parser.add_argument('--lang', '--language',
                        dest='lang',
                        action='store',
                        default='en',
                        type=str,
                        # (yas/expand-link "argparse_other_options" t)
                        help='Printable languages.\n"en", "ja"')
    parser.add_argument('-y', '--year',
                        dest='year',
                        action='store',
                        default=datetime.datetime.now().year,
                        type=int,
                        # (yas/expand-link "argparse_other_options" t)
                        help="Show year's holidays.(default this year)")
    parser.add_argument('--end',
                        dest='end',
                        action='store',
                        default=None,
                        type=int,
                        # (yas/expand-link "argparse_other_options" t)
                        help='Show while end of year.')
    parser.add_argument('--coloring-next',
                        dest='coloring_next',
                        action='store_true',
                        default=False,
                        help='Coloring next holiday.')
    # (yas/expand-link "argparse_add_argument" t)
    return parser


def print_holidays(holidays, colors=None):
    r"""SUMMARY

    print_holidays(holidays)

    @Arguments:
    - `holidays`:

    @Return:

    @Error:
    """
    colors_dates = colors or []
    dates = holidays
    dates.sort()
    for date in dates:
        if date in colors_dates:
            print(Fore.RED + unicode(date) + u' ' + unicode(date.get_name()) +
                  Style.RESET_ALL)
        else:
            print(u'{} {}'.format(date, date.get_name()))


def _main():
    r"""Main function."""
    parser = _predef_options()
    opts = parser.parse_args()
    # country
    holidays_cls = HOLIDAYS_CLASSES.get(opts.country, None)
    if holidays_cls is None:
        parser.print_usage()
        return "{} is not supported country.".format(opts.country)
    international_name.set_default_lang(opts.lang)
    day = holidays_cls(opts.year, 1, 1)
    # period
    if opts.end is None:
        end = day + relativedelta(years=1)
    else:
        end = datetime.date(opts.end + 1, 1, 1) - datetime.timedelta(1)
    # get
    results = day.between_holidays(end)
    next_dates = []
    if opts.coloring_next:
        date = holidays_cls.today().next_holiday()
        if not date is None:
            next_dates.append(date)
    # print
    print_holidays(results, next_dates)
    return os.EX_OK

if __name__ == '__main__':
    sys.exit(_main())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __main__.py ends here
