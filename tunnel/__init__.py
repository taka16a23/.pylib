#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id$
# $Revision$
# $Date$
# $Author$
# $LastChangedBy$
# $LastChangedDate$
"""\
Name: __init__.py


"""


import os as _os

if 'nt' == _os.name:
    from nt_tunnel import Tunneling, TunnelError

elif 'posix' == _os.name:
    from posix_tunnel import Tunneling, TunnelError, Tunnel


__revision__ = "$Revision$"
__version__ = "0.1.1"



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
