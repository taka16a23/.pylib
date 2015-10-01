#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id: __init__.py 445 2015-08-07 01:26:31Z t1 $
# $Revision: 445 $
# $Date: 2015-08-07 10:26:31 +0900 (Fri, 07 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-07 10:26:31 +0900 (Fri, 07 Aug 2015) $
r"""\
Name: __init__.py


"""


__revision__ = "$Revision: 445 $"
__version__ = "0.1.0"

__all__ = [ '' ]


import os as _os
import urllib2 as _urllib2

import lxml.html as _lxhtml

from portable import DRIVE as _DRIVE


PROXY = {'speed': 'http://www.cybersyndrome.net/plr5.html',
         'anonymous': 'http://www.cybersyndrome.net/pla5.html',
         }

proxy_file = _DRIVE + '\\system\\FRDPortable\\proxy.txt'


def parse_pxurl(url):
    """Generator for get proxy list from url.

    Arguments:
    - `url`:
    """
    html = _urllib2.urlopen(url).read()
    root = _lxhtml.fromstring(html)
    anchors = root.xpath('//a')
    for anchor in anchors:
        if type(anchor.text) == str:
            if '.' in anchor.text and ':' in anchor.text:
                yield anchor.text


def _main():
    # force delete
    _os.remove(proxy_file)
    lis = parse_pxurl(PROXY['anonymous'])
    with open(proxy_file, 'w') as f:
        f.write('\n'.join(lis))

if __name__ == '__main__':
    _main()




# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
