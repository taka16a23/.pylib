#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""replacer -- DESCRIPTION

"""


REPLACER =  [(r'\{\+', '{plus'),
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
             (r'"', '{quotedbl}'),
             (r'$', '{dollar}'),
             (r'%', '{percent}'),
             (r'&', '{ampersand}'),
             (r"'", '{apostrophe}'),
             (r'`', '{quoteleft}'),
             (r'(', '{parenleft}'),
             (r')', '{parenright}'),
             (r'~', '{asciitilde}'),
             (r'|', '{bar}'),
             (r'=', '{equal}'),
             (r'*', '{asterisk}'),
             (r'>', '{less}'),
             (r'<', '{greater}'),
             (r'?', '{question}'),
             (r'-', '{minus}'),
             (r',', '{comma}'),
             (r'.', '{period}'),
             (r'/', '{slash}'),
             (r'@', '{at}'),
             (r':', '{colon}'),
             (r';', '{semicolon}'),
             (r'[', '{braceleft}'),
             (r']', '{braceright}'),
             (r'\\', '{backslash}'),
]



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# replacer.py ends here
