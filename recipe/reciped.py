#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: reciped.py 404 2015-08-06 21:17:12Z t1 $
# $Revision: 404 $
# $Date: 2015-08-07 06:17:12 +0900 (Fri, 07 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-07 06:17:12 +0900 (Fri, 07 Aug 2015) $

r"""reciped -- DESCRIPTION

ref. http://georgik.sinusgear.com/2011/01/07/how-to-dump-post-request-with-python/


"""
import sys
import os

from SimpleHTTPServer import SimpleHTTPRequestHandler
import BaseHTTPServer
from recipe._recipe import Recipe

import logging
from logging.handlers import RotatingFileHandler
from excepthook._logging import LoggingExceptionHook

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__revision__ = '$Revision: 404 $'
__version__ = '0.1.0'


###############################################################################
# output log file
LOGNAME = 'reciped.log'
LOGDIR = '/var/log'
LOGPATH = os.path.join(LOGDIR, LOGNAME)
_RH = RotatingFileHandler(LOGPATH, 'a', 1024*50, 3)
_RH.setLevel(logging.INFO)
_RH.setFormatter(logging.Formatter(
    '%(asctime)s;%(name)s;%(module)s %(funcName)s(%(lineno)d);%(levelname)s;'
    '\n   %(message)s'))

# console
_CH = logging.StreamHandler()
_CH.setLevel(logging.INFO)

LOG = logging.getLogger('reciped')
LOG.setLevel(logging.INFO)
LOG.addHandler(_RH)
LOG.addHandler(_CH)

# exception
LoggingExceptionHook(LOG)


class ServerHandler(SimpleHTTPRequestHandler):
    r"""SUMMARY
    """

    def do_GET(self, ):
        r"""SUMMARY

        do_GET()

        @Return:
        """
        LOG.info(self.headers)
        SimpleHTTPRequestHandler.do_GET(self)

    def log_message(self, fmt, *args):
        LOG.info('[{}] {} - {}'.format(self.log_date_time_string(),
                                       self.client_address[0],
                                       fmt%args))


def reciped():
    r"""SUMMARY

    reciped()

    @Return:
    """
    os.chdir(Recipe().basedir)
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class(('', 8000), ServerHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    return 0

if __name__ == '__main__':
    sys.exit(reciped())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# reciped.py ends here
