#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: __main__.py 460 2015-08-10 16:51:55Z t1 $
# $Revision: 460 $
# $Date: 2015-08-11 01:51:55 +0900 (Tue, 11 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-11 01:51:55 +0900 (Tue, 11 Aug 2015) $

r"""Name: __main__.py

"""
import sys
import os
import argparse
import datetime
from colorama import Fore, Style

from holiday import JapanHolidays, Period, __version__


HOLIDAYS_CLASSES = {'japan': JapanHolidays,}


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
    dates = holidays.keys()
    dates.sort()
    for date in dates:
        if date in colors_dates:
            print(Fore.RED + unicode(date) + u' ' + unicode(holidays[date]) +
                  Style.RESET_ALL)
        else:
            print(u'{} {}'.format(date, holidays[date]))


def _main():
    r"""Main function."""
    parser = _predef_options()
    opts = parser.parse_args()
    # country
    holidays_cls = HOLIDAYS_CLASSES.get(opts.country, None)
    if holidays_cls is None:
        parser.print_usage()
        return "{} is not supported country.".format(opts.country)
    holidays = holidays_cls(lang=opts.lang)
    # period
    start = datetime.date(opts.year, 1, 1)
    end = datetime.date(opts.year + 1, 1, 1) - datetime.timedelta(1)
    if not opts.end is None:
        end = datetime.date(opts.end + 1, 1, 1) - datetime.timedelta(1)
    # get
    results = holidays.between_holidays(Period(start, end))
    next_dates = []
    if opts.coloring_next:
        today = datetime.datetime.today()
        date, _ = holidays.get_next(today.date())
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
