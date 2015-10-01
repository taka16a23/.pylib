#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: gmail_database.py 349 2015-08-04 22:35:27Z t1 $
# $Revision: 349 $
# $Date: 2015-08-05 07:35:27 +0900 (Wed, 05 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-05 07:35:27 +0900 (Wed, 05 Aug 2015) $

r"""gmail_database -- DESCRIPTION

"""
import time
import imaplib
from email import message_from_string
from email.utils import parsedate
from datetime import datetime

from dotavoider import dotavoid

from diary.database import DiaryDatabase
from diary.note import DiaryNote


class GmailDiaryDatabase(DiaryDatabase):
    """Class GmailDiaryDatabase
    """
    ACCOUNT = 'taka16daily@gmail.com'
    PASSWORD = 'xwwrheownfdkbmao'

    # Attributes:
    def __init__(self, ):
        r"""
        """
        self._imap = imaplib.IMAP4_SSL('imap.gmail.com')
        self._imap.login(self.ACCOUNT, self.PASSWORD)
        self._imap.select('inbox')

    # Operations
    def _search(self, command):
        r"""SUMMARY

        _search(command)

        @Arguments:
        - `command`:

        @Return:

        @Error:
        """
        typ, data = self._imap.search(None, command)
        if typ != 'OK':
            # TODO: (Atami) [2015/08/01]
            raise StandardError()
        if not data:
            return []
        return data[0].split()

    def _fetchs(self, ids):
        r"""SUMMARY

        _fetchs(ids)

        @Arguments:
        - `ids`:

        @Return:

        @Error:
        """
        def get_text(mail):
            if mail.is_multipart():
                text = ''
                for mil in mail.get_payload():
                    text += get_text(mil)
                return text
            else:
                return mail.get_payload()

        results, append = dotavoid([], 'append')
        typ, data = self._imap.fetch(','.join(ids), 'RFC822')
        if not typ == 'OK':
            return results
        for dat in data:
            if not isinstance(dat, (tuple, )):
                continue
            mail = message_from_string(dat[1])
            date = datetime.fromtimestamp(
                time.mktime(parsedate(mail.get('Date'))))
            append(DiaryNote(date, get_text(mail)))
        return results

    def list_notes(self):
        """function iter_notes

        returns iter
        """
        return self._fetchs(self._search('ALL'))

    def list_by_date(self, date):
        """function list_by_date

        date:

        returns
        """
        return self._fetchs(
            self._search('(ON "{}")'.format(date.strftime('%d-%b-%Y'))))

    def list_by_month(self, month):
        """function list_by_month

        month:

        returns
        """
        return [n for n in self.list_notes() if n.date.month == month]

    def list_by_day(self, day):
        """function list_by_day

        day:

        returns
        """
        return [n for n in self.list_notes() if n.date.day == day]

    def list_by_date_range(self, start, end):
        """function list_by_date_range

        start:
        end:

        returns
        """
        return self._fetchs(self._search('(since "{}" before "{}")'.format(
                start.strftime('%d-%b-%Y'), end.strftime('%d-%b-%Y'))))

    def list_by_search_text(self, regexp):
        """function list_by_search_text

        regexp: re.compile

        returns
        """
        # TODO: (Atami) [2015/08/01]
        # search(None, 'CHARSET', 'UTF-8', 'ALL', 'TEXT', '餃子') to fail
        results, append = dotavoid([], 'append')
        for note in self.list_notes():
            if regexp.search(note.text) is None:
                continue
            append(note)
        return results

    def close(self):
        """function close

        returns
        """
        self._imap.close()
        self._imap.logout()

    def __del__(self):
        # Do not imprement "raise"!!
        self.close()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# gmail_database.py ends here
