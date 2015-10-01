#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id: __init__.py 136 2014-04-05 08:42:53Z t1 $
# $Revision: 136 $
# $Date: 2014-04-05 17:42:53 +0900 (Sat, 05 Apr 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-04-05 17:42:53 +0900 (Sat, 05 Apr 2014) $
r"""\
Name: __init__.py

inspect:
  `ismodule', `isclass', `ismethod', `ismethoddescriptor', `isdatadescriptor',
  `isfunction', `isgeneratorfunction', `isgenerator', `istraceback',
  `isframe', `iscode', `isbuiltin', `isroutine', `isabstract', `getmembers'

operator:
  `isCallable', `isMappingType', `isNumberType', `isSequenceType'


"""
from predicate.functions import *
from predicate.cls import Predicate

__revision__ = "$Revision: 136 $"
__version__ = "0.1.0"



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
