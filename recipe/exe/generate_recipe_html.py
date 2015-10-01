#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: generate_recipe_html.py 448 2015-08-07 02:54:21Z t1 $
# $Revision: 448 $
# $Date: 2015-08-07 11:54:21 +0900 (Fri, 07 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-07 11:54:21 +0900 (Fri, 07 Aug 2015) $

r"""Name: generate_recipe_html.py

"""
import argparse
from t1.dateutil import now_weekday

import sys
import os

from recipe.menu2 import MenuManager
from recipe.menu2.common import DEFAULT_DIR
from pathhandler import PathHandler

import logging
from path import Path
from logging.handlers import RotatingFileHandler

__revision__ = '$Revision: 448 $'
__version__ = '0.0.1'

###############################################################################
LOG = logging.getLogger('generate_recipe_html')
LOG.setLevel(logging.INFO)

# output log file
LOGPATH = Path('/var/log/generate_recipe_html.log')
_RH = RotatingFileHandler(unicode(LOGPATH), 'a', 1024*50, 2)
_RH.setLevel(logging.INFO)
_RH.setFormatter(logging.Formatter(
    '%(asctime)s;%(name)s;%(module)s %(funcName)s(%(lineno)d);%(levelname)s;'
    '\n   %(message)s'))
LOG.addHandler(_RH)

# console
if sys.stdout.isatty():
    _CH = logging.StreamHandler()
    _CH.setLevel(logging.INFO)
    LOG.addHandler(_CH)


# exception
def logging_handle_exceptions(excls, value, trcbck):
    r"""Handling exception hook.

    sys.excepthook = logging_handle_exceptions
    """
    import traceback
    if issubclass(excls, KeyboardInterrupt):
        sys.__excepthook__(excls, value, trcbck)
        return
    errortype = 'Error type: {}'.format(excls)
    valuetxt = 'Uncaught exception: {0}'.format(str(value))
    trcbcktxt = ''.join(traceback.format_tb(trcbck))
    LOG.exception('\n'.join([errortype, valuetxt, trcbcktxt]))

sys.excepthook = logging_handle_exceptions
###############################################################################
LOG.debug('logging started')


# gen html
HTML_TEMPLATE = """
<html>
 <head>
   <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
   <title>献立</title>
 </head>
 <body>
   <h1><b>献立</b></h1><br>
   {}
</body></html>
"""


def _main():
    tags = []
    menus = MenuManager(DEFAULT_DIR).list_exists_menus()
    menus.sort(key=lambda key: key.get_date())
    for menu in menus:
        tags.append(menu.generate_html_tag())
    path = PathHandler(DEFAULT_DIR).get_dirname().join('index.html')
    if path.exists():
        LOG.info('will remove {}'.format(unicode(path)))
        path.remove()
    with path.open('wb') as fobj:
        LOG.info('writing {}'.format(fobj.name))
        fobj.write(HTML_TEMPLATE.format(''.join(tags)))
    return os.EX_OK


def _predef_options():
    parser = argparse.ArgumentParser(description=""" """)
    parser.add_argument('--version',
                        dest='version',
                        action='version',
                        version=__version__,
                        help='Version Strings.')
    parser.add_argument('--force',
                        dest='force',
                        action='store_true',
                        default=False,
                        required=False,
                        # (yas/expand-link "argparse_other_options" t)
                        help='A lot of messages.')
    # (yas/expand-link "argparse_add_argument" t)
    return parser


parser = _predef_options()
opts = parser.parse_args()

weekday = now_weekday()
if weekday.is_friday() or opts.force:
    sys.exit(_main())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# generate_recipe_html.py ends here
