#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: __init__.py 342 2015-07-24 05:07:32Z t1 $
# $Revision: 342 $
# $Date: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-07-24 14:07:32 +0900 (Fri, 24 Jul 2015) $

r"""Name: __init__.py


"""
from xcb import xcb
from xcb.xcb import (CAPI, ExtensionException, Response,
                     ConnectException, ExtensionKey, Struct, _add_core,
                     Connection, Iterator, Union, _add_ext,
                     Cookie, List, VoidCookie, _resize_obj,
                     CopyFromParent, NONE, X_PROTOCOL, #connect,
                     CurrentTime, NoSymbol, X_PROTOCOL_REVISION, popcount,
                     Error, Protobj, X_TCP_PORT, type_pad,
                     Event, ProtocolException,
                     Exception, Reply,
                     Extension, Request, )

from xcb2.xproto import connect # not error
from xcb2.display import Display


__revision__ = "$Revision: 342 $"
__version__ = "0.1.0"

__all__ = [  ]



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
