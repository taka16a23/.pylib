#!/usr/bin/env python
# -*- coding: utf-8 -*-r"""\
r"""
Name: search.py


"""


import urlparse as _urlparse
from lxmllib import lxml_soup as _lxml_soup


__version__ = "0.1.0"


url = 'http://www.google.com/search?hl=ja&q=%(query)s&num=1'

def google_feeling_lucky(query, verbose=False):
    """SUMMARY

    @Arguments:
    - `query`:

    @Return:
    """
    query = query.encode('utf-8')
    if verbose:
        print(query)
    search_url = (url % vars())
    search_url = search_url.replace(' ', '+').replace('　', '+')
    print(search_url)
    soup = _lxml_soup(search_url, wait=10)
    try:
        link = soup.xpath('//*[@class="r"]/a')[0].attrib['href']
        link = _filter_result(link)
    except IndexError:
        link = ''
    return link

def _filter_result(link):
    try:

        # Valid results are absolute URLs not pointing to a Google domain
        # like images.google.com or googleusercontent.com
        o = _urlparse.urlparse(link, 'http')
        if o.netloc and 'google' not in o.netloc:
            return link

        # Decode hidden URLs.
        if link.startswith('/url?'):
            link = _urlparse.parse_qs(o.query)['q'][0]

            # Valid results are absolute URLs not pointing to a Google domain
            # like images.google.com or googleusercontent.com
            o = _urlparse.urlparse(link, 'http')
            if o.netloc and 'google' not in o.netloc:
                return link

    # Otherwise, or on error, return None.
    except Exception:
        pass
    return None



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# search.py ends here
