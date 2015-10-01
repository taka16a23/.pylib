#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: formatter.py 390 2015-08-06 15:47:02Z t1 $
# $Revision: 390 $
# $Date: 2015-08-07 00:47:02 +0900 (Fri, 07 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-07 00:47:02 +0900 (Fri, 07 Aug 2015) $

r"""formatter -- DESCRIPTION

"""
from colorama import Fore, Style, Back

__all__ = ['BRIGHT', 'FOREWHITE', 'FOREBLACK', 'FOREBLUE', 'FORECYAN',
           'FORERED', 'FOREMAGENTA', 'FOREGREEN', 'FOREYELLOW', 'BACKWHITE',
           'BACKBLACK', 'BACKBLUE', 'BACKCYAN', 'BACKRED', 'BACKMAGENTA',
           'BACKGREEN', 'BACKYELLOW', 'RESET_ALL', 'FOREWHITE_RESET',
           'FOREBLACK_RESET', 'FOREBLUE_RESET', 'FORECYAN_RESET',
           'FORERED_RESET', 'FOREMAGENTA_RESET', 'FOREGREEN_RESET',
           'FOREYELLOW_RESET', 'BACKWHITE_RESET', 'BACKBLACK_RESET',
           'BACKBLUE_RESET', 'BACKCYAN_RESET', 'BACKRED_RESET',
           'BACKMAGENTA_RESET', 'BACKGREEN_RESET', 'BACKYELLOW_RESET']

BRIGHT            = (Style.BRIGHT + '{}').format

FOREWHITE         = (Fore.WHITE + '{}').format
FOREBLACK         = (Fore.BLACK + '{}').format
FOREBLUE          = (Fore.BLUE + '{}').format
FORECYAN          = (Fore.CYAN + '{}').format
FORERED           = (Fore.RED + '{}').format
FOREMAGENTA       = (Fore.MAGENTA + '{}').format
FOREGREEN         = (Fore.GREEN + '{}').format
FOREYELLOW        = (Fore.YELLOW + '{}').format

BACKWHITE         = (Back.WHITE + '{}').format
BACKBLACK         = (Back.BLACK + '{}').format
BACKBLUE          = (Back.BLUE + '{}').format
BACKCYAN          = (Back.CYAN + '{}').format
BACKRED           = (Back.RED + '{}').format
BACKMAGENTA       = (Back.MAGENTA + '{}').format
BACKGREEN         = (Back.GREEN + '{}').format
BACKYELLOW        = (Back.YELLOW + '{}').format

RESET_ALL         = ('{}' + Style.RESET_ALL).format

FOREWHITE_RESET   = RESET_ALL(FOREWHITE('{}')).format
FOREBLACK_RESET   = RESET_ALL(FOREBLACK('{}')).format
FOREBLUE_RESET    = RESET_ALL(FOREBLUE('{}')).format
FORECYAN_RESET    = RESET_ALL(FORECYAN('{}')).format
FORERED_RESET     = RESET_ALL(FORERED('{}')).format
FOREMAGENTA_RESET = RESET_ALL(FOREMAGENTA('{}')).format
FOREGREEN_RESET   = RESET_ALL(FOREGREEN('{}')).format
FOREYELLOW_RESET  = RESET_ALL(FOREYELLOW('{}')).format

BACKWHITE_RESET   = RESET_ALL(BACKWHITE('{}')).format
BACKBLACK_RESET   = RESET_ALL(BACKBLACK('{}')).format
BACKBLUE_RESET    = RESET_ALL(BACKBLUE('{}')).format
BACKCYAN_RESET    = RESET_ALL(BACKCYAN('{}')).format
BACKRED_RESET     = RESET_ALL(BACKRED('{}')).format
BACKMAGENTA_RESET = RESET_ALL(BACKMAGENTA('{}')).format
BACKGREEN_RESET   = RESET_ALL(BACKGREEN('{}')).format
BACKYELLOW_RESET  = RESET_ALL(BACKYELLOW('{}')).format



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# formatter.py ends here
