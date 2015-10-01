#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: replacer.py 277 2015-01-28 23:57:11Z t1 $
# $Revision: 277 $
# $Date: 2015-01-29 08:57:11 +0900 (Thu, 29 Jan 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-01-29 08:57:11 +0900 (Thu, 29 Jan 2015) $

r"""replacer -- DESCRIPTION

"""
from orderedreplace.replace import OrderedReplace as _OrderedReplace


REPLACER = _OrderedReplace(
    # list for ordered
    [(r'\{\+', '{plus'),
     (r'\\\+', '{plus}'),
     (r'\{\!', '{exclam'),
     (r'\\\!', '{exclam}'),
     (r'\{\#', '{numbersign'),
     (r'\\\#', '{numbersign}'),
     (r'\{\^', '{asciicircum'),
     (r'\\\^', '{asciicircum}'),
     (r'\{\_', '{underscore'),
     (r'\_', '{underscore}'),
     (r'\{\}\}', '{bracketright}'),
     (r'\{\}\ ', '{bracketright '),
     (r'\{\{\}', '{bracketleft}'),
     (r'\{\{\ ', '{bracketleft '),
     # ('{{', '{bracketleft}' ),
     (r'\\\{', '{bracketleft}'),
     (r'\\\}', '{bracketright}'),
     (r'\"', '{quotedbl}'),
     (r'\$', '{dollar}'),
     (r'\%', '{percent}'),
     (r'\&', '{ampersand}'),
     (r"\'", '{apostrophe}'),
     (r'\`', '{quoteleft}'),
     (r'\(', '{parenleft}'),
     (r'\)', '{parenright}'),
     (r'\~', '{asciitilde}'),
     (r'\|', '{bar}'),
     (r'\=', '{equal}'),
     (r'\*', '{asterisk}'),
     (r'\>', '{less}'),
     (r'\<', '{greater}'),
     (r'\?', '{question}'),
     (r'\-', '{minus}'),
     (r'\,', '{comma}'),
     (r'\.', '{period}'),
     (r'\/', '{slash}'),
     (r'\@', '{at}'),
     (r'\:', '{colon}'),
     (r'\;', '{semicolon}'),
     (r'\[', '{braceleft}'),
     (r'\]', '{braceright}'),
     (r'\\', '{backslash}'),
 ])



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# replacer.py ends here
