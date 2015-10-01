#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: cls.py 136 2014-04-05 08:42:53Z t1 $
# $Revision: 136 $
# $Date: 2014-04-05 17:42:53 +0900 (Sat, 05 Apr 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-04-05 17:42:53 +0900 (Sat, 05 Apr 2014) $

r"""cls -- DESCRIPTION

"""

import sys as _sys
import os as _os

from predicate import functions


# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__revision__ = '$Revision: 136 $'
__version__ = '0.1.0'


class Predicate(object):
    r"""SUMMARY
    """

    def __init__(self, obj):
        r"""

        @Arguments:
        - `obj`:
        """
        self._obj = obj

    def isInstance(self, ):
        r"""SUMMARY

        isInstance()

        @Return:
        """
        return functions.isInstance(self._obj)

    def isMappingType(self, ):
        r"""SUMMARY

        isMappingType()

        @Return:
        """
        return functions.isMappingType(self._obj)

    def isNumberType(self, ):
        r"""SUMMARY

        isNumberType()

        @Return:
        """
        return functions.isNumberType(self._obj)

    def isSequenceType(self, ):
        r"""SUMMARY

        isSequenceType()

        @Return:
        """
        return functions.isSequenceType(self._obj)

    def isabstract(self, ):
        r"""SUMMARY

        isabstract()

        @Return:
        """
        return functions.isabstract(self._obj)

    def isboolean(self, ):
        r"""SUMMARY

        isboolean()

        @Return:
        """
        return functions.isboolean(self._obj)

    def isbuiltin(self, ):
        r"""SUMMARY

        isbuiltin()

        @Return:
        """
        return functions.isbuiltin(self._obj)

    def isbuiltinmethod(self, ):
        r"""SUMMARY

        isbuitinmethod()

        @Return:
        """
        return functions.isbuiltinmethod(self._obj)

    def iscallable(self, ):
        r"""SUMMARY

        iscallable()

        @Return:
        """
        return functions.iscallable(self._obj)

    def isclass(self, ):
        r"""SUMMARY

        isclass()

        @Return:
        """
        return functions.isclass(self._obj)

    def iscode(self, ):
        r"""SUMMARY

        iscode()

        @Return:
        """
        return functions.iscode(self._obj)

    def isdatadescriptor(self, ):
        r"""SUMMARY

        isdatadescriptor()

        @Return:
        """
        return functions.isdatadescriptor(self._obj)

    def isdict(self, ):
        r"""SUMMARY

        isdict()

        @Return:
        """
        return functions.isdict(self._obj)

    def isdictproxy(self, ):
        r"""SUMMARY

        isdictproxy()

        @Return:
        """
        return functions.isdictproxy(self._obj)

    def isellipsis(self, ):
        r"""SUMMARY

        issellipsis()

        @Return:
        """
        return functions.isellipsis(self._obj)

    def isfile(self, ):
        r"""SUMMARY

        isfile()

        @Return:
        """
        return functions.isfile(self._obj)

    def isfloat(self, ):
        r"""SUMMARY

        isfloat()

        @Return:
        """
        return functions.isfloat(self._obj)

    def isframe(self, ):
        r"""SUMMARY

        isframe()

        @Return:
        """
        return functions.isframe(self._obj)

    def isfunction(self, ):
        r"""SUMMARY

        isfunction()

        @Return:
        """
        return functions.isfunction(self._obj)

    def isgenerator(self, ):
        r"""SUMMARY

        isgenerator()

        @Return:
        """
        return functions.isgenerator(self._obj)

    def isgeneratorfunction(self, ):
        r"""SUMMARY

        isgeneratorfunction()

        @Return:
        """
        return functions.isgeneratorfunction(self._obj)

    def isglobalvariable(self, ):
        r"""SUMMARY

        isglobalvariable()

        @Return:
        """
        return functions.isglobalvariable(self._obj)

    def isint(self, ):
        r"""SUMMARY

        isint()

        @Return:
        """
        return functions.isint(self._obj)

    def islambda(self, ):
        r"""SUMMARY

        islambda()

        @Return:
        """
        return functions.islambda(self._obj)

    def islist(self, ):
        r"""SUMMARY

        islist()

        @Return:
        """
        return functions.islist(self._obj)

    def islocalvariable(self, ):
        r"""SUMMARY

        islocalvariable()

        @Return:
        """
        return functions.islocalvariable(self._obj)

    def islong(self, ):
        r"""SUMMARY

        islong()

        @Return:
        """
        return functions.islong(self._obj)

    def ismemberdescriptor(self, ):
        r"""SUMMARY

        ismemberdescriptor()

        @Return:
        """
        return functions.ismemberdescriptor(self._obj)

    def ismethod(self, ):
        r"""SUMMARY

        ismethod()

        @Return:
        """
        return functions.ismethod(self._obj)

    def ismodule(self, ):
        r"""SUMMARY

        ismodule()

        @Return:
        """
        return functions.ismodule(self._obj)

    def isnegative(self, ):
        r"""SUMMARY

        isnegative()

        @Return:
        """
        return functions.isnegative(self._obj)

    def isnone(self, ):
        r"""SUMMARY

        isnone()

        @Return:
        """
        return functions.isnone(self._obj)

    def isnotimplemented(self, ):
        r"""SUMMARY

        isnotimplemented()

        @Return:
        """
        return functions.isnotimplemented(self._obj)

    def isobject(self, ):
        r"""SUMMARY

        isobject()

        @Return:
        """
        return functions.isobject(self._obj)

    def ispositive(self, ):
        r"""SUMMARY

        ispositive()

        @Return:
        """
        return functions.ispositive(self._obj)

    def isroutine(self, ):
        r"""SUMMARY

        isroutine()

        @Return:
        """
        return functions.isroutine(self._obj)

    def isslice(self, ):
        r"""SUMMARY

        isslice()

        @Return:
        """
        return functions.isslice(self._obj)

    def isstring(self, ):
        r"""SUMMARY

        isstring()

        @Return:
        """
        return functions.isstring(self._obj)

    def isstrings(self, ):
        r"""SUMMARY

        isstrings()

        @Return:
        """
        return functions.isstrings(self._obj)

    def istraceback(self, ):
        r"""SUMMARY

        istraceback()

        @Return:
        """
        return functions.istraceback(self._obj)

    def istuple(self, ):
        r"""SUMMARY

        istuple()

        @Return:
        """
        return functions.istuple(self._obj)

    def istype(self, ):
        r"""SUMMARY

        istype()

        @Return:
        """
        return functions.istype(self._obj)

    def isunboundmethod(self, ):
        r"""SUMMARY

        isunboundmethod()

        @Return:
        """
        return functions.isunboundmethod(self._obj)

    def isunicode(self, ):
        r"""SUMMARY

        isunicode()

        @Return:
        """
        return functions.isunicode(self._obj)

    def isvariable(self, ):
        r"""SUMMARY

        isvariable()

        @Return:
        """
        return functions.isvariable(self._obj)

    def isxrange(self, ):
        r"""SUMMARY

        isxrange()

        @Return:
        """
        return functions.isxrange(self._obj)

    def iszero(self, ):
        r"""SUMMARY

        iszero()

        @Return:
        """
        return functions.iszero(self._obj)

    def isiterable(self, ):
        r"""SUMMARY

        isiterable()

        @Return:
        """
        return functions.isiterable(self._obj)


def _test():
    r"""Test function."""
    return _os.EX_OK

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# cls.py ends here
