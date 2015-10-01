#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: _handler2.py 485 2015-09-29 03:10:26Z t1 $
# $Revision: 485 $
# $Date: 2015-09-29 12:10:26 +0900 (Tue, 29 Sep 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-09-29 12:10:26 +0900 (Tue, 29 Sep 2015) $

r"""_handler2 -- DESCRIPTION

"""
import re
import os as _os
import io

import path
import pathlib as _pathlib

from pathhandler._interface import PathHandlerAbstract


# Adapter Pattern
# third party "path.Path", "pathlib.Path" の interface が変更されたら
# ここを修正する。


class PathHandler(PathHandlerAbstract, unicode):
    r"""PathHandler

    PathHandler is a PathHandlerAbstract, str.
    Responsibility:
    """
    def __init__(self, pth):
        r"""

        @Arguments:
        - `pth`:
        """
        unicode.__init__(self, pth)
        self._path = path.Path(pth)

    # Operations
    @classmethod
    def from_cwd(cls):
        """SUMMARY

        @Arguments:
        - `cls`:

        @Return: PathHandler
        """
        return cls(_os.getcwd())

    def chmod(self, mode):
        """Change the access permissions of a file.

        @Arguments:
        - `mode`:

        @Return: None
        """
        self._path.chmod(mode)

    def chown(self, uid, gid):
        """SUMMARY

        @Arguments:
        - `uid`:
        - `gid`:

        @Return: None
        """
        self._path.chown(uid, gid)

    def copy(self, dst):
        """SUMMARY

        @Arguments:
        - `dst`:

        @Return: PathHandler
        """
        return PathHandler(unicode(self._path.copy2(dst)))

    def copytree(self, dst, symlinks=False, ignore=None):

        r"""SUMMARY

        @Arguments:
        - `dst`:
        - `symlinks`:
        - `ignore`:

        @Return: None

        copytree(dst, symlinks=False, ignore=None)

        @Error:
        """
        self._path.copytree(dst, symlinks=symlinks, ignore=ignore)

    def copymode(self, dst):
        """SUMMARY

        @Arguments:
        - `dst`:

        @Return: None
        """
        self._path.copymode(dst)

    def copystat(self, dst):
        """SUMMARY

        @Arguments:
        - `dst`:

        @Return: None
        """
        self._path.copystat(dst)

    def exists(self):
        """SUMMARY

        @Return: bool
        """
        return self._path.exists()

    def expanduser(self):
        """SUMMARY

        @Return: PathHandler
        """
        return PathHandler(self._path.expanduser())

    def expandvars(self):
        """SUMMARY

        @Return: PathHandler

        """
        return PathHandler(self._path.expandvars())

    def get_absolute(self):
        """SUMMARY

        @Return: PathHandler
        """
        return PathHandler(self._path.abspath())

    absolute = property(get_absolute)

    def get_atime(self):
        """SUMMARY

        @Return: float
        """
        return self._path.getatime()

    atime = property(get_atime)

    def get_basename(self):
        """SUMMARY

        @Return: PathHandler
        """
        return PathHandler(self._path.basename())

    basename = property(get_basename)

    def get_conf(self, name):
        """SUMMARY

        @Arguments:
        - `name`:

        @Return: int
        """
        return self._path.pathconf(name)

    def get_ctime(self):
        """SUMMARY

        @Return: float
        """
        return self._path.getctime()

    ctime = property(get_ctime)

    def get_drive(self):
        """SUMMARY

        @Return: PathHandler
        """
        return PathHandler(self._path.drive)

    drive = property(get_drive)

    def get_dirname(self):
        """SUMMARY

        @Return: PathHandler
        """
        return PathHandler(self._path.dirname())

    dirname = property(get_dirname)

    def get_extension(self):
        """SUMMARY

        @Return: str
        """
        return unicode(self._path.ext)

    ext = property(get_extension)

    def get_mtime(self):
        """SUMMARY

        @Return: float
        """
        return self._path.getmtime()

    mtime = property(get_mtime)

    def get_normal(self):
        """SUMMARY

        @Return: PathHandler
        """
        return PathHandler(self._path.normpath())

    normal = property(get_normal)

    def get_size(self):
        """SUMMARY

        @Return: long
        """
        return self._path.getsize()

    size = property(get_size)

    def get_stat(self, ):
        """SUMMARY

        @Return: posix.stat_result
        """
        return self._path.stat()

    stat = property(get_stat)

    def get_stem(self):
        """SUMMARY

        @Return: str
        """
        return _pathlib.Path(str(self)).stem

    stem = property(get_stem)

    def get_root(self):
        """SUMMARY

        @Return: str
        """
        return PathHandler(_pathlib.Path(str(self)).root)

    root = property(get_root)

    def get_relative(self, start='.'):
        """SUMMARY

        @Arguments:
        - `start`:

        @Return: PathHandler
        """
        return PathHandler(self._path.relpath(start))

    def isabsolute(self):
        """SUMMARY

        @Return: bool
        """
        return self._path.isabs()

    def isdir(self):
        """SUMMARY

        @Return: bool
        """
        return self._path.isdir()

    def isfifo(self):
        """SUMMARY

        @Return: bool
        """
        return _pathlib.Path(str(self)).is_fifo()

    def isfile(self):
        """SUMMARY

        @Return: bool
        """
        return self._path.isfile()

    def ismount(self):
        """SUMMARY

        @Return: bool
        """
        return self._path.ismount()

    def issymlink(self):
        """SUMMARY

        @Return: bool
        """
        return self._path.islink()

    def join(self, pth):
        """SUMMARY

        @Arguments:
        - `path`:

        @Return: PathHandler
        """
        return PathHandler(_os.path.join(self._path, pth))

    def listdir(self, pattern=None):
        """SUMMARY

        @Arguments:
        - `pattern`:

        @Return: list
        """
        regexp = re.compile(pattern or '')
        return [PathHandler(x) for x in self._path.listdir()
                if not regexp.search(x) is None]

    def link(self, pth):
        """SUMMARY

        @Arguments:
        - `path`:

        @Return: PathHandler
        """
        return PathHandler(self._path.symlink(pth))

    def mkdir(self, mode, parents=False):
        """SUMMARY

        @Argumentins:
        - `mode`: (int)
        - `parents`:

        @Return: None
        """
        if parents:
            self._path.makedirs(mode)
            return
        self._path.mkdir(mode)

    def move(self, dst):
        """SUMMARY

        @Arguments:
        - `dst`:

        @Return: PathHandler
        """
        return PathHandler(unicode(self._path.move(dst)))

    def open(self, mode='r', buffering=-1, encoding=None, errors=None,
             newline=None, closefd=True):
        """SUMMARY

        @Arguments:
        - `mode`:
        - `buffering`
        - `**kwargs`:

        @Return: file
        """
        return io.open(self._path, mode=mode, buffering=buffering,
                       encoding=encoding, errors=errors, newline=newline,
                       closefd=closefd)

    def readlink(self):
        """SUMMARY

        @Return: PathHandler
        """
        return PathHandler(_os.readlink(self._path))

    def remove(self):
        """SUMMARY

        @Return: None
        """
        if self.isdir():
            self._path.rmtree()
            return
        self._path.remove()

    def rename(self, new, force=False):
        """SUMMARY

        @Arguments:
        - `new`:
        - `force`:

        @Return: PathHandler
        """
        return PathHandler(self._path.rename(new))

    def samefile(self, other):
        """SUMMARY

        @Arguments:
        - `other`:

        @Return: bool
        """
        return self._path.samefile(other)

    def splitdrive(self):
        """SUMMARY

        @Return: tuple
        """
        return tuple(PathHandler(x) for x in self._path.splitdrive())

    def splitext(self):
        """SUMMARY

        @Return: tuple
        """
        pth, ext = self._path.splitext()
        return PathHandler(pth), ext

    def touch(self):
        """SUMMARY

        @Return: PathHandler
        """
        return PathHandler(self._path.touch())

    def unlink(self):
        """SUMMARY

        @Return: None
        """
        self._path.unlink()

    def walk(self):
        """SUMMARY

        @Return: iterator
        """
        for pth in self._path.walk():
            yield PathHandler(pth)

    def with_name(self, name):
        """SUMMARY

        @Arguments:
        - `name`:

        @Return: PathHandler
        """
        return PathHandler(unicode(_pathlib.Path(str(self)).with_name(name)))

    def with_ext(self, suffix):
        """SUMMARY

        @Arguments:
        - `suffix`:

        @Return: PathHandler
        """
        return PathHandler(
            unicode(_pathlib.Path(str(self)).with_suffix(suffix)))

    def replace(self, old, new, *args, **kwargs):
        r"""SUMMARY

        replace(old, new[, count])

        @Arguments:
        - `old`:
        - `new`:
        - `count`:
        - `kwargs`:

        @Return:

        @Error:
        """
        return PathHandler(unicode.replace(self, old, new, *args, **kwargs))

    def rsplit(self, sep, *args, **kwargs):
        r"""SUMMARY

        rsplit([sep [,maxsplit]])

        @Arguments:
        - `sep`:
        - `args`:
        - `kwargs`:

        @Return:

        @Error:
        """
        return [PathHandler(x) for x in
                unicode.rsplit(self, sep, *args, **kwargs)]

    def rstrip(self, *args, **kwargs):
        r"""SUMMARY

        rstrip([chars])

        @Arguments:
        - `args`:
        - `kwargs`:

        @Return:

        @Error:
        """
        return PathHandler(unicode.rstrip(self, *args, **kwargs))

    def lstrip(self, *args, **kwargs):
        r"""SUMMARY

        lstrip([chars])

        @Arguments:
        - `args`:
        - `kwargs`:

        @Return:

        @Error:
        """
        return PathHandler(unicode.lstrip(self, *args, **kwargs))

    def split(self, *args, **kwargs):
        r"""SUMMARY

        split([sep [,maxsplit]])

        @Arguments:
        - `args`:
        - `kwargs`:

        @Return:

        @Error:
        """
        return [PathHandler(x) for x in
                unicode.split(self, *args, **kwargs)]

    def strip(self, *args, **kwargs):
        r"""SUMMARY

        strip(*args, **kwargs)

        @Arguments:
        - `args`:
        - `kwargs`:

        @Return:

        @Error:
        """
        return PathHandler(unicode.strip(self, *args, **kwargs))

    def swapcase(self, ):
        r"""SUMMARY

        swapcase()

        @Return:

        @Error:
        """
        return PathHandler(unicode.swapcase(self, ))

    def translate(self, table):
        r"""SUMMARY

        translate(table)

        @Arguments:
        - `table`:

        @Return:

        @Error:
        """
        return PathHandler(unicode.translate(table))

    def lower(self, ):
        r"""SUMMARY

        lower()

        @Return:

        @Error:
        """
        return PathHandler(unicode.lower(self))

    def upper(self, ):
        r"""SUMMARY

        upper()

        @Return:

        @Error:
        """
        return PathHandler(unicode.upper(self))

    def partition(self, sep):
        r"""SUMMARY

        partition(sep)

        @Arguments:
        - `sep`:

        @Return:

        @Error:
        """
        return [PathHandler(x) for x in unicode.partition(self, sep)]

    def __repr__(self):
        return '{0.__name__}({1})'.format(type(self), unicode.__repr__(self))

    # def __str__(self):
    #     return self.encode('utf-8')

    def __unicode__(self):
        return unicode(self._path)

    def __eq__(self, other):
        if isinstance(other, (self.__class__, )):
            return unicode(self) == unicode(other)
        return unicode(self) == other

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        if isinstance(other, (PathHandler, )):
            return self.join(other)
        return PathHandler(unicode.__add__(self, other))

    def __iadd__(self, other):
        if isinstance(other, (PathHandler, )):
            return self.join(other)
        return self + other



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _handler2.py ends here
