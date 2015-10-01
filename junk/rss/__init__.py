#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""\
Name: __init__.py


"""



import types as _types


from lxmllib import lxml_soup as _lxml_soup

__version__ = '0.1.0'


__all__ = [ '' ]


def feed_finder(url, cache=True, verbose=False):
    """SUMMARY

    @Arguments:
    - `doc`:

    @Return:
    """
    assert type(url) is _types.StringType, "'url' is must be a strings"


    doc = _lxml_soup(url, cache, verbose=verbose)
    el = doc.xpath('//link[@rel="alternate"][contains(@type, "rss")'
                   ' or contains(@type, "atom") or contains(@type, "rdf")]')
    feed_link = []
    if el:
        feed_link += [e.attrib['href'] for e in el]
        # for e in el:
        #     feed_link.append(e.attrib['href'])
    else:
        extensions = ['.rss', '.xml', '.rdf']
        a = doc.xpath('//a')
        for el in a:
            link = ''
            try:
                if el.attrib.has_key('href'):
                    link = el.attrib['href']
            except KeyError:
                continue
            feed_link += [link for ext in extensions if link and link.endswith(ext)]
            # for ext in extensions:
            #     if link and link.endswith(ext):
            #         feed_link.append(link)
    return feed_link




# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
