#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: giin.py 440 2015-08-07 01:25:23Z t1 $
# $Revision: 440 $
# $Date: 2015-08-07 10:25:23 +0900 (Fri, 07 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-07 10:25:23 +0900 (Fri, 07 Aug 2015) $

"""\
Name: giin.py

"""
import argparse
import os
import sys
import urllib2
import urlparse
from collections import OrderedDict

import unicodecsv
from mygoogle.search import google_feeling_lucky
from lxmllib import lxml_soup, wikisoup
from .rss import feed_finder

from junk.abstract import Verbose as _Verbose


__revision__ = '$Revision: 440 $'
__version__ = '0.1.0'


## Exceptions
#
class NothingURLError(StandardError):
    pass

class BadUsage:
    pass

## Handle giin members info
#
class Giin(_Verbose):
    """
    """
    members = {}
    # FIXME: (Atami) [2013/04/13]
    # same reason of above
    partys = {u'自由民主': 'LDP',
              u'民主':     'DPJ',
              u'公明':     'Koumei',
              u'みんなの': 'Minna',}

    # TODO: (Atami) [2013/04/14]
    # add method for edit blow dictionary
    headers = OrderedDict([('syu_san',  u'衆参'),
                           ('name',     u'名前'),
                           ('kana',     u'ふりがな'),
                           ('party',    u'政党'),
                           ('location', u'選挙区'),
                           ('homepage', u'ホームページ'),
                           ('blog',     u'ブログ'),
                           ('twitter',  u'twitter'),
                           ('rss',      u'rss'),])

    def __init__(self, verbose=False):
        """
        """
        super(Giin, self).__init__(verbose=verbose)
        for parse in [SyuugiinParse(verbose=verbose),
                      SangiinParse(verbose=verbose)]:
            for el in parse:
                name = el[1].replace(u' ', '')
                party_name = el[3].replace(u' ', '')
                # make dictionary of name and object
                obj = globals()[self.partys.get(party_name, 'Other')]
                self.members[name] = obj(verbose=self._verbose, *el)

    def write_csv(self,
                  fname,
                  syu_san=True,
                  name=True,
                  kana=True,
                  party=True,
                  location=True,
                  homepage=True,
                  blog=True,
                  twitter=True,
                  rss=True,
                  header=True):
        """SUMMARY

        @Return:
        """
        if os.path.exists(fname):
            os.remove(fname)
        with open(fname, 'wb') as csvfile:
            writer = unicodecsv.writer(csvfile)
            # write header
            if header:
                # head = []
                # for key, value in self.headers.iteritems():
                    # if vars()[key]:
                        # head.append(value)
                # [value for key, value in self.headers.iteritems() if vars()[key]]
                writer.writerow([value for key, value in self.headers.iteritems()
                                 if vars()[key]])
            # write contents
            for member in self.members.itervalues():
                if self._verbose:
                    print(member.syu_san + ' ' +
                          member.name + ' ' + member.party)
                # lis = []
                # for key, v in self.headers.iteritems():
                    # if vars()[key]:
                        # lis.append(getattr(member, key))
                # [getattr(member, key) for key, v in self.headers.itervalues()
                 # if vars()[key]]
                try:
                    writer.writerow(
                        [getattr(member, key) for key, v in self.headers.itervalues()
                         if vars()[key]])
                except KeyboardInterrupt:
                    print('KeyboardInterrupted')
                    sys.exit(1)
                except:
                    continue


## class for parse members
#
class _ParseBase(_Verbose):
    """
    """
    # FIXME: (Atami) [2013/04/13]
    # can not auto make abbrev dictionary
    # can not grab from
    # 'http://www.shugiin.go.jp/index.nsf/html/index_kousei2.htm'

    party_abbrev = {u'自民':     u'自由民主',
                    u'民主':     u'民主',
                    u'維新':     u'日本維新の会',
                    u'公明':     u'公明',
                    u'みん':     u'みんなの',
                    u'みんなの': u'みんなの',
                    u'生活':     u'生活の',
                    u'共産':     u'日本共産',
                    u'み風':     u'みどりの風',
                    u'社民':     u'社会民主',
                    u'改革':     u'新党改革',
                    u'無':       u'無所属',
                    u'無所属':   u'無所属'}

    def __init__(self, verbose=False):
        """SUMMARY

        @Return:
        """
        super(_ParseBase, self).__init__(verbose=verbose)

    def _trim_name(self, str_):
        """Multiple space to just one space.

        'hello   world' to 'hello world'
        'hello　　world' to 'hello world'
        @Arguments:
        - `str_`:

        @Return:
        """
        new = str_.replace('\n', '')
        new = ' '.join(filter(None, str_.split(' ')))
        new = ' '.join(filter(None, new.split(u'　')))
        return new


class SyuugiinParse(_ParseBase):
    """Generator for parse 衆議院議員 infomation list from 'www.shugiin.go.jp'.

    @Return: [syu-san, name, kana, party, location]
    example2 [syuugiin, 山田太郎, やまだたろう, 政党, 東京?区]
    """
    giin = u'(衆)'

    urls = [
     'http://www.shugiin.go.jp/itdb_annai.nsf/html/statics/syu/1giin.htm',
     'http://www.shugiin.go.jp/itdb_annai.nsf/html/statics/syu/2giin.htm',
     'http://www.shugiin.go.jp/itdb_annai.nsf/html/statics/syu/3giin.htm',
     'http://www.shugiin.go.jp/itdb_annai.nsf/html/statics/syu/4giin.htm',
     'http://www.shugiin.go.jp/itdb_annai.nsf/html/statics/syu/5giin.htm',
     'http://www.shugiin.go.jp/itdb_annai.nsf/html/statics/syu/6giin.htm',
     'http://www.shugiin.go.jp/itdb_annai.nsf/html/statics/syu/7giin.htm',
     'http://www.shugiin.go.jp/itdb_annai.nsf/html/statics/syu/8giin.htm',
     'http://www.shugiin.go.jp/itdb_annai.nsf/html/statics/syu/9giin.htm',
     'http://www.shugiin.go.jp/itdb_annai.nsf/html/statics/syu/10giin.htm']


    def __iter__(self):
        for url in self.urls:
            doc = lxml_soup(url, wait=2, verbose=self._verbose)
            table = doc.xpath('//table')[2]

            # appending infomation
            for tr in table[1:]:
                info = []
                info.append(self.giin)
                font = tr.xpath('td/tt')
                for i in range(4):
                    # 0 = name, 1 = kana, 2 = party, 3 = location
                    str_ = font[i].text_content()
                    if not str_:
                        str_ = ''
                    else:
                        str_ = self._trim_name(str_)
                        # trim "君"
                        if 0 == i and str_.endswith(u'君'):
                            str_ = str_[:-1]
                        # reference of true party name from abbrev.
                        elif 2 == i:
                            str_ = str_.replace(u' ', '')
                            str_ = self.party_abbrev.get(str_, str_)
                    info.append(str_)
                yield info


class SangiinParse(_ParseBase):
    """
    """
    giin = u'(参)'
    url = 'http://www.sangiin.go.jp/japanese/joho1/kousei/giin/183/giin.htm'

    def __iter__(self):
        doc = lxml_soup(self.url, verbose=self._verbose)
        table = doc.xpath('//*[@id="ContentsBox"]/table[2]')[0]

        for tr in table[1:]:
            info = []
            # first element
            info.append(self.giin)
            td = tr.xpath('td')

            for i in range(4):
                str_ = td[i].text_content()
                if not str_:
                    str_ = ''
                else:
                    str_ = self._trim_name(str_)
                    # name
                    if 0 == i:
                        finded = str_.find('[')
                        if -1 != finded:
                            # trim string after '['
                            str_ = str_[:finded]
                    # party
                    elif 2 == i:
                        str_ = str_.replace(' ', '')
                        str_ = self.party_abbrev.get(str_, str_)
                info.append(str_)
            yield info


## Partys class hold each members info
#
class _Party(_Verbose):
    """Abstract base class.
    """
    def __init__(self,
                  syu_san,
                  name,
                  kana,
                  party,
                  location,
                  homepage=None,
                  blog=None,
                  twitter=None,
                  rss=None,
                  verbose=False):
        """
        Arguments:
        - `syu_san`: 衆議院(syuugiin) or 参議院(sangiin)
        - `name`: name
        - `kana`: 読みがな
        - `party`: Political party
        - `location`: Electoral district
        - `homepage`: url of homepage
        - `blog`: url of blog
        - `twitter`: url of twitter
        - `rss`: url of rss
        """
        self.syu_san = syu_san
        self.name = name
        self.kana = kana
        self.party = party
        self.location = location
        self._homepage = homepage
        self._blog = blog
        self._twitter = twitter
        self._rss = rss
        self._verbose = verbose

    wikiurl = 'http://ja.wikipedia.org/wiki/'

    @property
    def homepage(self):
        """Return homepages url.

        @Return: string of url.
        """
        if not self._homepage:
            self._homepage = ''
            self._set_homepage()
        return self._homepage

    @property
    def blog(self):
        """Return blogs url.

        @Return: string of url.
        """
        if not self._blog:
            self._blog = ''
            if not self._homepage:
                self._set_homepage()
            self._set_blog()
        return self._blog

    @property
    def twitter(self):
        """Return twitters url.

        @Return: string of url.
        """
        if not self._twitter:
            self._twitter = ''
            if not self._homepage:
                self._set_homepage()
            self._set_twitter()
        return self._twitter

    @property
    def rss(self):
        """Return homepages url.

        @Return: string of url.
        """
        if not self._rss:
            self._rss = ''
            if not self._homepage:
                self._set_homepage()
            try:
                self._set_rss()
            except KeyboardInterrupt:
                print('KeyboardInterrupted')
                sys.exit(1)
            except:
                pass
        return self._rss

    def _set_homepage(self):
        """SUMMARY

        @Return:
        """
        def wikiparse(query, verbose=False):
            """SUMMARY

            @Return:
            """
            homepage = ''

            try:
                soup = wikisoup(query, verbose=verbose)
            except (urllib2.HTTPError, urllib2.URLError):
                return False

            if hasattr(soup, 'xpath'):
                table = soup.xpath('//*[@class="infobox"]')
            if 1 <= len(table):
                table = table[0]

            site_str = [
                # '公式サイト'
                u'\xe5\x85\xac\xe5\xbc\x8f\xe3\x82\xb5\xe3\x82\xa4\xe3\x83\x88',
                # 'ウェブサイト'
                u'\xe3\x82\xa6\xe3\x82\xa7\xe3\x83\x96\xe3\x82\xb5\xe3\x82\xa4\xe3\x83\x88']

            for tr in table:
                if (len(tr) > 0 and hasattr(tr[0], 'text') and tr[0].text in site_str):
                    homepage = tr[1].xpath('a')[0].attrib['href']
            return homepage

        querys = [self.name.replace(' ', ''), self.name + u'_(政治家)']
        for query in querys:
            result = wikiparse(query, verbose=self._verbose)
            if result:
                self._homepage = result
                if self._verbose:
                    print('Homepage: ' + result)
                break

        if self._homepage == '':
            self._set_alt_homepage()

    def _set_alt_homepage(self):
        """SUMMARY

        @Return:
        """
        pass

    def _set_blog(self):
        """SUMMARY

        @Return:
        """
        pass

    def _set_twitter(self):
        """SUMMARY

        @Return:
        """
        pass

    def _set_rss(self):
        """SUMMARY

        @Return:
        """
        def set_rss(url, verbose=False):
            """SUMMARY

            @Arguments:

            - `verbose`:

            @Return:
            """
            url = url.encode('utf-8')
            def defrag_rss_url(url):
                """SUMMARY

                @Return:
                """
                parse = urlparse.urlparse(url)
                if not parse.netloc:
                    return urlparse.urljoin(self._homepage, url)
                return url

            rss_links = feed_finder(url)
            if rss_links:
                parse = urlparse.urlparse(url)
                self._rss = defrag_rss_url(rss_links[0])
                if self._verbose:
                    print('RSS: ' + self._rss)

        if self._blog:
            set_rss(self._blog, verbose=self._verbose)

        if not self._rss and self._homepage:
            set_rss(self._homepage, verbose=self._verbose)


class LDP(_Party):
    """
    """
    url = 'www.jimin.jp'

    def _set_alt_homepage(self):
        """SUMMARY

        @Return:
        """
        query = ' '.join(['site:' + self.url, self.name.replace(u' ', '')])

        try:
            url = google_feeling_lucky(query, verbose=self._verbose)
            doc = lxml_soup(url, verbose=self._verbose)
            homepage_a_tag = doc.xpath('//*[@class="homepage start"]/p/a')
            self._homepage = homepage_a_tag[0].attrib['href']
        except KeyboardInterrupt:
            print('KeyboardInterrupted')
            sys.exit(1)
        except:
            pass

        try:
            blog_a_tag = doc.xpath('//*[@class="blog"]/p/a')
            self._blog = blog_a_tag[0].attrib['href']
        except KeyboardInterrupt:
            print('KeyboardInterrupted')
            sys.exit(1)
        except:
            pass

        try:
            twitter_a_tag = doc.xpath('//*[@class="twitter"]/p/a')
            self._twitter = twitter_a_tag[0].attrib['href']
        except KeyboardInterrupt:
            print('KeyboardInterrupted')
            sys.exit(1)
        except:
            pass


class DPJ(_Party):
    """
    """
    url = 'www.dpj.or.jp'

    def _set_alt_homepage(self):
        """SUMMARY

        @Return:
        """
        query = ' '.join(['site:' + self.url, self.name.replace(u' ', '')])
        try:
            url = google_feeling_lucky(query, verbose=self._verbose)
            doc = lxml_soup(url, verbose=self._verbose)
            table = doc.xpath('//*[@id="member-content"]/div[2]/table')[0]
            for i, tr in enumerate(table.xpath('//tr')):
                if u'ホームページ' == tr.xpath('//th')[i].text_content():
                    self._homepage = tr.xpath('//a')[i].attrib['href']
        except KeyboardInterrupt:
            print('KeyboardInterrupted')
            sys.exit(1)
        except:
            pass


class Koumei(_Party):
    """
    """
    url = 'www.komei.or.jp'

    def _set_alt_homepage(self):
        """SUMMARY

        @Return:
        """
        query = ' '.join(['site:' + self.url, self.name.replace(u' ', '')])
        try:
            url = google_feeling_lucky(query, verbose=self._verbose)
            doc = lxml_soup(url, verbose=self._verbose)
            table = doc.xpath('//*[@id="main-inner"]/div/div[2]/table')[0]
            for li in table.xpath('//li'):
                if u'公式ホームページ' == li.text_content():
                    self._homepage = li[0].attrib['href']
        except KeyboardInterrupt:
            print('KeyboardInterrupted')
            sys.exit(1)
        except:
            pass


class Minna(_Party):
    """
    """
    url = 'www.your-party.jp'

    def _set_alt_homepage(self):
        """SUMMARY

        @Return:
        """
        query = ' '.join(['site:' + self.url, self.name.replace(u' ', '')])
        try:
            url = google_feeling_lucky(query, verbose=self._verbose)
            doc = lxml_soup(url, verbose=self._verbose)
            table = doc.xpath('//*[@class="career-table"]')[0]
            for tr in table.xpath('//tr'):
                for th in tr.xpath('//th'):
                    if u'ホームページ' == th.text_content():
                        self._homepage = th.getnext()[0].attrib['href']

        except KeyboardInterrupt:
            print('KeyboardInterrupted')
            sys.exit(1)
        except:
            pass


class Kyousan(_Party):
    """
    """
    url = 'www.jcp.or.jp'

    def _set_alt_homepage(self):
        """SUMMARY

        @Return:
        """
        query = ' '.join(['site:' + self.url, self.name.replace(u' ', '')])
        try:
            url = google_feeling_lucky(query, verbose=self._verbose)
            doc = lxml_soup(url, verbose=self._verbose)

        except KeyboardInterrupt:
            print('KeyboardInterrupted')
            sys.exit(1)
        except:
            pass


class Other(_Party):
    pass


def _gui():
    """SUMMARY

    @Return:
    """
    pass


def _main():
    parser = argparse.ArgumentParser(description="""
    List up lawmakers info.""")
    parser.add_argument('--version',
                        dest='version',
                        action='version',
                        version=__version__,
                        help='Version Strings.')

    parser.add_argument('-v', '--verbose',
                        dest='verbose',
                        action='store_true',
                        default=False,
                        required=False,
                        # (yas/expand-link "argparse_other_options" t)
                        help='A lot of messages.')

    parser.add_argument('-c', '--csv',
                        dest='csv',
                        action='store',
                        # nargs=1,
                        const=None,
                        type=str,
                        required=False,
                        # (yas/expand-link "argparse_other_options" t)
                        help='Write to csv')

    # (yas/expand-link "argparse_add_argument" t)
    opt = parser.parse_args()
    try:
        if 1 == len(sys.argv):
            _gui()
            return

        if opt.csv:
            gi = Giin(verbose=opt.verbose)
            gi.write_csv(opt.csv)

    except BadUsage:
        parser.print_help()

if __name__ == '__main__':
    _main()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# giin.py ends here
