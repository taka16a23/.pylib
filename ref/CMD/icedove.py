#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id: icedove.py 439 2015-08-07 01:25:08Z t1 $
# $Revision: 439 $
# $Date: 2015-08-07 10:25:08 +0900 (Fri, 07 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-07 10:25:08 +0900 (Fri, 07 Aug 2015) $
r""" icedove -- for icedove's informations

$Revision: 439 $

"""

import sys as _sys
import subprocess as _sbp

from junk.mypsutil import psexists as _psexists
import wm
import predicate

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__revision__ = '$Revision: 439 $'
__version__ = '0.1.0'

NAME = 'icedove'
BIN = 'icedove'
BINPATH = '/usr/bin/icedove'
MAILOPT = '-compose'

ICE_ELEMENT = {'to': '',
               'cc': '',
               'subject': '',
               'body': '',
               'attachment': ''}

HTML_FORMAT = 1
TEXT_FORMAT = 2

class IcedoveMail(object):
    r"""
    """
    binpath = BINPATH
    opt = MAILOPT
    to = []
    cc = []
    bcc = []
    subject = ''
    body = ''
    format = ''
    attachment = []

    def __init__(self, to=[], cc=[], bcc=[], subject='', body='',
                 format='', attachment=[]):
        r"""

        @Arguments:
        - `to`:
        - `cc`:
        - `subject`:
        - `body`:
        - `attachment`:
        """
        self.set_to(to)
        self.set_cc(cc)
        self.set_bcc(bcc)
        self.subject = subject
        self.body = body
        self.format = format
        self.set_attachment(attachment)

    def __repr__(self, ):
        r"""SUMMARY

        @Return:

        __repr__()
        """
        str_ = []
        append = str_.append
        fmt = '{0:<11}: {1}'.format
        append(fmt('to', self.to))
        append(fmt('cc', self.cc))
        append(fmt('bcc', self.bcc))
        append(fmt('subject', self.subject))
        append(fmt('body', self.body))
        append(fmt('format', self.format))
        append(fmt('attachment', self.attachment))
        return '\n'.join(str_)

    def send(self, ):
        r"""SUMMARY

        send()

        @Return:
        """
        pass

    def getcmdline(self, ):
        r"""SUMMARY

        getcmdline()

        @Return:
        """
        return ' '.join(self.getcmdtuple())

    def getcmdtuple(self, ):
        r"""SUMMARY

        getcmdtuple()

        @Return:
        """
        return (self.binpath, self.opt, self.getcomposed())

    def getcomposed(self, ):
        r"""SUMMARY

        getcmdline()

        @Return:
        """
        args = []
        append = args.append
        if self.to:
            append(u"to='{0}'".format(','.join(self.to)))
        if self.cc:
            append(u"cc='{0}'".format(','.join(self.cc)))
        if self.bcc:
            append(u"bcc='{0}'".format(','.join(self.bcc)))
        if self.subject:
            append(u"subject='{0}'".format(self.subject))
        if self.body:
            append(u"body='{0}'".format(self.body))
        if self.format:
            append(u"format={0}".format(self.format))
        if self.attachment:
            append(u"attachment='{0}'".format(','.join(self.attachment)))
        return u'"{0}"'.format(','.join(args))

    def set_to(self, to_list):
        r"""SUMMARY

        set_to(to_list)

        @Arguments:
        - `to_list`:

        @Return:
        """
        if predicate.isstring(to_list):
            to_list = [to_list]
        if not (predicate.islist(to_list) or predicate.istuple(to_list)):
        # if not type(to_list) in (predicate.ListType, predicate.TupleType):
            raise ValueError('to_list must be List, Tuple or String type.')
        if self.to:
            self.to.extend(to_list)
        else:
            self.to = to_list

    def set_cc(self, cc_list):
        r"""SUMMARY

        set_cc(cc_list)

        @Arguments:
        - `cc_list`:

        @Return:
        """
        if predicate.isstring(cc_list):
            cc_list = [cc_list]
        if not (predicate.islist(cc_list) or predicate.istuple(cc_list)):
        # if not type(cc_list) in (predicate.ListType, predicate.TupleType):
            raise ValueError('cc_list must be List or String type.')
        if self.cc:
            self.cc.extend(cc_list)
        else:
            self.cc = cc_list

    def set_bcc(self, bcc_list):
        r"""SUMMARY

        set_cc(cc_list)

        @Arguments:
        - `cc_list`:

        @Return:
        """
        if predicate.isstring(bcc_list):
            bcc_list = [bcc_list]
        if not (predicate.islist(bcc_list) or predicate.istuple(bcc_list)):
        # if not type(bcc_list) in (predicate.ListType, predicate.TupleType):
            raise ValueError('cc_list must be List or String type.')
        if self.bcc:
            self.bcc.extend(bcc_list)
        else:
            self.bcc = bcc_list

    def set_subject(self, text):
        r"""SUMMARY

        set_subject(text)

        @Arguments:
        - `text`:

        @Return:
        """
        if not isinstance(text, (str, unicode)):
            raise ValueError('text must be String type.')
        self.subject = text

    def set_body(self, text):
        r"""SUMMARY

        set_body(text)

        @Arguments:
        - `text`:

        @Return:
        """
        if not isinstance(text, (str, unicode)):
            raise ValueError('text must be String type.')
        self.body = text

    def set_htmlformat(self, ):
        r"""SUMMARY

        set_htmlformat()

        @Return:
        """
        self.format = HTML_FORMAT

    def set_textformat(self, ):
        r"""SUMMARY

        set_textformat()

        @Return:
        """
        self.format = TEXT_FORMAT

    def set_attachment(self, attachments):
        r"""SUMMARY

        @Arguments:
        - `attachments`:

        @Return:

        set_attachment()
        """
        if predicate.isstring(attachments):
            attachments = [attachments]
        if not (predicate.islist(attachments) or predicate.istuple(attachments)):
        # if not type(attachments) in (predicate.ListType, predicate.TupleType):
            raise ValueError('to_list must be List, Tuple or String type.')
        if self.attachment:
            self.attachment.extend(attachments)
        else:
            self.attachment = attachments


def mailformat_maker(elt):
    r"""SUMMARY

    @Arguments:
    - `elt`:

    @Return:
    """
    return "{}".format(','.join(
        ["{0}='{1}'".format(key, val) for key, val in elt.iteritems() if val]))


def run():
    r"""SUMMARY

    @Return:
    """
    from sh import icedove
    icedove(_bg=True)
    # if not _psexists(BIN):
        # _sbp.Popen((BINPATH, ))


def move():
    r"""SUMMARY

    @Return:
    """
    if wm.WinWait(sec=180).win(klass='Icedove'):
        win = wm.getwin(klass='Icedove')
    if win.ismaximize():
        win.reset_maximize()
    win.move(x=0, y=0)
    win.maximize()
    return win


def _test():
    r"""Test function."""
    return 0

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# icedove.py ends here
