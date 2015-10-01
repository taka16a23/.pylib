#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""\
Name: __init__.py


"""


from time import sleep
import os as _os
import urllib2 as _urllib2
import tempfile as _tempfile
import datetime as _datetime
import contextlib as _contextlib
import urlparse as _urlparse

import lxml.html as lxhtml
from sleep_progress import sleep_progress as _sleep_progress


__version__ = '0.1.0'


__all__ = [ '' ]


def _get_html_filename(url):
    """SUMMARY

    @Arguments:
    - `url`:

    @Return:
    """
    if url.endswith('/'):
        url = url[:-1]
    name = url.split('/')[-1]
    if 'index.html' == name:
        netloc = _urlparse.urlsplit(url).netloc
        name = netloc + '.' + name
    return name


def lxml_soup(url, wait=0, cache=True, verbose=False):
    """SUMMARY

    @Arguments:
    - `url`:
    - `cache`:

    @Return:
    """
    # val = URLValidator(verify_exists=False)
    # try:
        # val(url)
    # except ValidationError, e:
        # print(e)

    if not url:
        return

    parse = _urlparse.urlparse(url)
    tmpdir = _os.path.join(_tempfile.gettempdir(), 'urllib_cache', parse.netloc)

    if not _os.path.exists(tmpdir):
        _os.makedirs(tmpdir)
    name = _get_html_filename(url)
    if not name:
        import string
        import random
        name = ''.join(random.sample(string.lowercase, 5))
    fname = _os.path.join(tmpdir, name)

    if _os.path.exists(fname) and 0 == _os.path.getsize(fname):
        _os.remove(fname)

    if _os.path.exists(fname):
        mtime = _datetime.datetime.fromtimestamp(_os.path.getmtime(fname))
        yesterday = _datetime.datetime.now() - _datetime.timedelta(1)
        obsoluted = mtime < yesterday
    else:
        obsoluted = False

    if not _os.path.exists(fname) or obsoluted or cache is False:
        # force delete
        try:
            _os.remove(fname)
        except OSError:
            pass

        with open(fname, 'w') as f:
            opener = _urllib2.build_opener()
            agent_str = (u'Mozilla/5.0 (X11; Linux i686) '
                         'AppleWebKit/537.31 (KHTML, like Gecko) '
                         'Chrome/26.0.1410.63 Safari/537.31')
            opener.addheaders = [('User-agent', agent_str)]
            if verbose:
                _sleep_progress(wait)
            else:
                sleep(wait)
            if verbose:
                print('Accessing: ' + url)
            with _contextlib.closing(opener.open(url)) as page:
                try:
                    f.write(page.read())
                except IOError, err:
                    print('IOError errorno: [%d]' % err.errno)
                    return False
    if verbose:
        print('Reading: ' + fname)
    with open(fname, 'r') as file_:
        html = file_.read()
    return lxhtml.fromstring(html)


wikija = 'http://ja.wikipedia.org/wiki/'

def wikisoup(query, wait=10, verbose=False):
    """SUMMARY

    @Arguments:
    - `query`:

    @Return:
    """
    url = wikija + query
    doc = lxml_soup(url.encode('utf-8'), wait=wait, verbose=verbose)
    return doc



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
