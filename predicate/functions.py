#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""functions -- DESCRIPTION

"""
import sys as _sys
from inspect import (ismodule, isclass, ismethod, isfunction, iscode,
                     isabstract, isbuiltin, isdatadescriptor, isframe,
                     isgenerator, isgeneratorfunction, ismemberdescriptor,
                     isroutine, istraceback)
from operator import isMappingType, isNumberType, isSequenceType
import types as _types
from types import (NoneType, TypeType, ObjectType, IntType, LongType, FloatType,
                   BooleanType, ComplexType, StringType, UnicodeType,
                   StringTypes, BufferType, TupleType, ListType, DictType,
                   FunctionType, LambdaType, CodeType, GeneratorType, ClassType,
                   UnboundMethodType, InstanceType, MethodType,
                   BuiltinFunctionType, BuiltinMethodType, ModuleType, FileType,
                   XRangeType, TracebackType, FrameType, SliceType,
                   EllipsisType, DictProxyType, NotImplementedType,
                   GetSetDescriptorType, MemberDescriptorType, )

from collections import Iterable as _Iterable # for isiterable

__all__ = ['ismodule', 'isclass', 'ismethod', 'isfunction', 'iscode',
           'isabstract', 'isbuiltin', 'isdatadescriptor', 'isframe',
           'isgenerator', 'isgeneratorfunction', 'ismemberdescriptor',
           'isroutine', 'istraceback', 'iscallable', 'isMappingType',
           'isNumberType', 'isSequenceType', 'isglobalvariable',
           'islocalvariable', 'isvariable', 'ispositive', 'isnegative',
           'iszero', 'islist', 'isnone', 'istype', 'isobject', 'isint',
           'islong', 'isfloat', 'isboolean', 'isstring', 'isstrings',
           'isunicode', 'istuple', 'isdict', 'islambda', 'isunboundmethod',
           'isInstance', 'isbuiltinmethod', 'isfile', 'isxrange', 'isslice',
           'isellipsis', 'isdictproxy', 'isnotimplemented', 'isiterable',
           'ispython3', 'ispython2']

__version__ = '0.1.0'


def isglobalvariable(name):
    r"""Predicate name is global variables.

    @Arguments:
    - `name`: string of variables name

    @Return:
    boolean

    isglobalvariable(name)
    """
    # TODO: (Atami) [2014/04/02]
    return name in globals()


def islocalvariable(name, localvar=locals()):
    r"""Predicate name is local variables.

    @Arguments:
    - `name`: string of variables name
    - `localvar`: parent local variables

    @Return:
    boolean

    islocalvariable(name)
    """
    # TODO: (Atami) [2014/04/02]
    return name in localvar


def isvariable(name, localvar=locals()):
    r"""Predicate name is variables name.

    @Arguments:
    - `name`: string of variables name
    - `localvar`: parent local variables

    @Return:
    boolean

    isvariable(name, localvar=locals())
    """
    # TODO: (Atami) [2014/04/02]
    globalvar = globals()
    globalvar.update(localvar)
    return name in globalvar


def ispositive(num):
    r"""Predicate num is greater than 0.

    @Arguments:
    - `num`:

    @Return:

    ispositive(num)
    """
    return 0 < num


def isnegative(num):
    r"""Predicate num is lower than 0.

    @Arguments:
    - `num`:

    @Return:

    isnegative(num)
    """
    return num < 0


def iszero(num):
    r"""Predicate num is 0.

    @Arguments:
    - `num`:

    @Return:

    iszero(num)
    """
    return num == 0


def islist(obj):
    r"""Predicate object is list type.

    @Arguments:
    - `obj`: object

    @Return:
    boolean

    islist(obj)

    >>> islist([])
    True
    """
    return isinstance(obj, ListType)


def isnone(obj):
    r"""Predicate object is None type.

    @Arguments:
    - `obj`: object

    @Return:
    boolean

    isNone(obj)

    >>> isnone(None)
    True
    """
    return isinstance(obj, NoneType)


def istype(obj):
    r"""Predicate object is type type.

    @Arguments:
    - `obj`: object

    @Return:
    boolean

    istype(obj)

    >>> istype(type)
    True
    """
    return isinstance(obj, TypeType)


def isobject(obj):
    r"""Predicate object is Object type.

    @Arguments:
    - `obj`: object

    @Return:
    boolean

    isobject(obj)

    >>> isobject(object)
    True
    """
    return isinstance(obj, ObjectType)


def isint(obj):
    r"""Predicate int_ is Int type.

    @Arguments:
    - `obj`: integer

    @Return:
    boolean

    isint(obj)

    >>> isint(1)
    True
    """
    return isinstance(obj, IntType)


def islong(obj):
    r"""Predicate num is Long type.

    @Arguments:
    - `obj`: integer

    @Return:
    boolean

    islong(obj)

    >>> islong(10000000000)
    True
    >>> islong(10L)
    True
    """
    return isinstance(obj, LongType)


def isfloat(obj):
    r"""Predicate float_ is Float type.

    @Arguments:
    - `obj`: object

    @Return:
    boolean

    isfloat(obj)

    >>> isfloat(1.1)
    True
    """
    return isinstance(obj, FloatType)


def isboolean(obj):
    r"""Predicate args is Boolean type.

    @Arguments:
    - `obj`: object

    @Return:
    boolean

    isboolean(obj)

    >>> isboolean(False)
    True
    """
    return isinstance(obj, BooleanType)


def isstring(obj):
    r"""Predicate obj is String type.

    @Arguments:
    - `obj`: object

    @Return:
    boolean

    isstring(obj)

    >>> isstring('hello')
    True
    """
    return isinstance(obj, StringType)


def isstrings(obj):
    r"""Predicate obj is Strings type.

    @Arguments:
    - `obj`: object

    @Return:
    boolean

    isstrings(obj)

    >>> isstrings('hello')
    True
    >>> isstrings(u'あ')
    True
    """
    # return type(obj) in StringTypes
    return isinstance(obj, StringTypes)


def isunicode(obj):
    r"""Predicate obj is Unicode type.

    @Arguments:
    - `obj`: object

    @Return:
    boolean

    isunicode(obj)

    >>> isunicode(u'あ')
    True
    """
    return isinstance(obj, UnicodeType)


def istuple(obj):
    r"""Predicate obj is Tuple type.

    @Arguments:
    - `obj`: object

    @Return:
    boolean

    istuple(obj)

    >>> istuple(('',))
    True
    """
    return isinstance(obj, TupleType)


def isdict(obj):
    r"""Predicate obj is Dict type.

    @Arguments:
    - `obj`: object

    @Return:
    boolean

    isdict(obj)

    >>> isdict({})
    True
    """
    return isinstance(obj, DictType)


def islambda(obj):
    r"""Predicate obj is Lambda type.

    @Arguments:
    - `obj`: object

    @Return:
    boolean

    islambda(obj)

    >>> islambda(lambda :None)
    True
    """
    return isinstance(obj, LambdaType)


def isunboundmethod(obj):
    r"""Predicate obj is Unbound Method type.

    @Arguments:
    - `obj`: object

    @Return:
    boolean

    isunboundmethod(obj)

    >>> class Tes():
    ...     def _m(self): pass
    >>> isunboundmethod(Tes._m)
    True
    """
    return isinstance(obj, UnboundMethodType)


def isInstance(obj):
    r"""Predicate obj is Instance type.

    @Arguments:
    - `obj`: object

    @Return:
    boolean

    isInstance(obj)

    >>> class Tes(): pass
    >>> _x = Tes()
    >>> isInstance(_x)
    True
    """
    return isinstance(obj, InstanceType)


def isbuiltinmethod(obj):
    r"""Predicate obj is Builtin Method type.

    @Arguments:
    - `obj`: object

    @Return:
    boolean

    isbuiltinmethod(obj)

    >>> isbuiltinmethod([].append)
    True
    """
    return isinstance(obj, BuiltinMethodType)


def isfile(obj):
    r"""Predicate obj is File type.

    isfile(obj)

    @Arguments:
    - `obj`: object

    @Return:
    boolean

    >>> isfile(open('/tmp/test.txt', 'w'))
    True
    """
    return isinstance(obj, FileType)


def isxrange(obj):
    r"""Predicate obj is Xrange type.

    @Arguments:
    - `obj`: object

    @Return:
    boolean

    isxrange(obj)

    >>> isxrange(xrange(1))
    True
    """
    return isinstance(obj, XRangeType)


def isslice(obj):
    r"""Predicate obj is Slice type.

    isslice(obj)

    @Arguments:
    - `obj`: object

    @Return:
    boolean

    >>> isslice(slice(0))
    True
    """
    return isinstance(obj, SliceType)


def isellipsis(obj):
    r"""Predicate obj is Ellipsis type.

    @Arguments:
    - `obj`: object

    @Return:
    boolean

    isellipsis(obj)

    >>> isellipsis(Ellipsis)
    True
    """
    return isinstance(obj, EllipsisType)


def isdictproxy(obj):
    r"""Predicate obj is Dict Proxy type.

    @Arguments:
    - `obj`: object

    @Return:
    boolean

    isdictproxy(obj)

    >>> isdictproxy(type.__dict__)
    True
    """
    return isinstance(obj, DictProxyType)


def isnotimplemented(obj):
    r"""Predicate obj is NotImplemented type.

    @Arguments:
    - `obj`: object

    @Return:
    boolean

    isnotimplemented(obj)

    >>> isnotimplemented(NotImplemented)
    True
    """
    return isinstance(obj, NotImplementedType)


def iscallable(obj):
    r"""SUMMARY

    iscallable(obj)

    @Arguments:
    - `obj`:

    @Return:
    """
    return hasattr(obj, '__call__')


def ispython2():
    r"""SUMMARY

    ispython2()

    @Return:
    """
    return 2 == _sys.version_info.major


def ispython3():
    r"""SUMMARY

    ispython3()

    @Return:
    """
    return 3 == _sys.version_info.major


def isiterable(obj):
    r"""SUMMARY

    isiterable(obj)

    @Arguments:
    - `obj`:

    @Return:
    """
    return isinstance(obj, _Iterable)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# functions.py ends here
