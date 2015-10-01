#!/usr/bin/env python
# -*- coding: utf-8 -*-
r""" cmds -- cmd informations for aquos.

"""



APART_NAMES = ['POWR', 'ITGD', 'ITVD', 'IAVD', 'IDEG', 'CBSD', 'CCSD', 'CTBD',
              'CHUP', 'CHDW', 'INP4', 'AVMD', 'VOLM', 'HPOS', 'VPOS', 'CLCK',
              'PHSE', 'WIDE', 'MUTE', 'ACSU', 'ACHA', 'OFTM']

__all__ = ['APART_NAMES', 'FORMATS', 'CMDS']


# make each command format and set check '?' command
CMDS = {}
FORMATS = {}
for cmd in APART_NAMES:
    FORMATS[cmd] = cmd + '{0: <4}\n'
    CMDS[cmd] = {'check': FORMATS.get(cmd).format('?')}
    CMDS[cmd]['format'] = FORMATS.get(cmd)

# POWR
# for key, Bpart in [('on', 1), ('off', 0)]:
    # CMDS['POWR'][key] = FORMATS.get('POWR').format(Bpart)

CMDS['POWR'] = {key: FORMATS.get('POWR').format(Bpart)
                for key, Bpart in (('on', 1), ('off', 0))}

CMDS['ITGD']['toggle'] = FORMATS.get('ITGD').format(' ')
CMDS['ITVD']['tv'] = FORMATS.get('ITVD').format(' ')

# IAVD
# for i in range(1, 6):
#     CMDS['IAVD'][i] = FORMATS.get('IAVD').format(i)
CMDS['IAVD'] = {i: FORMATS.get('IAVD').format(i) for i in range(1, 6)}


CMDS['IDEG']['toggle'] = FORMATS.get('IDEG').format(' ')
CMDS['CHUP']['up'] = FORMATS.get('CHUP').format(' ')
CMDS['CHDW']['down'] = FORMATS.get('CHDW').format(' ')

# INP4
# for key, Bpart in [('auto', 0), ('Dbus', 1), ('video', 4)]:
    # CMDS['INP4'][key] = FORMATS.get('INP4').format(Bpart)
CMDS['INP4'] = {key: FORMATS.get('INP4').format(Bpart)
                for key, Bpart in (('auto', 0), ('Dbus', 1), ('video', 4))}

# AVMD
CMDS['AVMD']['photo'] = 11
# for Bpart, key in enumerate(['toggle', 'standard', 'movie', 'game', 'avmemory',
#                      'static dynamic', 'dynamic', 'pc']):
#     CMDS['AVMD'][key] = FORMATS.get('AVMD').format(Bpart)
CMDS['AVMD'] = {key: FORMATS.get('AVMD').format(Bpart)
                for Bpart, key in enumerate(
                        ('toggle', 'standard', 'movie', 'game', 'avmemory',
                         'static dynamic', 'dynamic', 'pc'))}

# WIDE
# for Bpart, key in enumerate(['toggle', 'normal', 'smartzoom', 'wide4:3',
#                              'cinema', 'full', 'full1', 'full2', 'underscan',
#                              'dot_by_dot', 'wide16:9']):
#     CMDS['WIDE'][key] = FORMATS.get('WIDE').format(Bpart)
CMDS['WIDE'] = {key: FORMATS.get('WIDE').format(Bpart)
                for Bpart, key in enumerate(
                        ('toggle', 'normal', 'smartzoom', 'wide4:3', 'cinema',
                         'full', 'full1', 'full2', 'underscan', 'dot_by_dot',
                         'wide16:9'))}


# MUTE
# for Bpart, key in enumerate(['toggle', 'on', 'off']):
    # CMDS['MUTE'][key] = FORMATS.get('MUTE').format(Bpart)
CMDS['MUTE'] = {key: FORMATS.get('MUTE').format(Bpart)
                for Bpart, key in enumerate(('toggle', 'on', 'off'))}

# ACSU
# for Bpart, key in enumerate(['toggle', 'on', 'off', 'auto']):
    # CMDS['ACSU'][key] = FORMATS.get('ACSU').format(Bpart)
CMDS['ACSU'] = {key: FORMATS.get('ACSU').format(Bpart)
                for Bpart, key in enumerate(('toggle', 'on', 'off', 'auto'))}


CMDS['ACHA']['toggle'] = FORMATS.get('ACHA').format(' ')

# OFTM
# for Bpart, key in enumerate(['reset', '30min', '1h', '1h30min',
#                              '2h', '2h30min']):
#     CMDS['OFTM'][key] = FORMATS.get('OFTM').format(Bpart)
CMDS['OFTM'] = {key: FORMATS.get('OFTM').format(Bpart)
                for Bpart, key in enumerate(('reset', '30min', '1h',
                                             '1h30min', '2h', '2h30min'))}



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# cmds.py ends here
