#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""_handler -- DESCRIPTION

"""
import re
import os as _os

import path as _path
import pathlib as _pathlib

from pathhandler._interface import PathHandlerAbstract


# Adapter Pattern
# third party "path.Path", "pathlib.Path" の interface が変更されたら
# ここを修正する。


class PathHandler(PathHandlerAbstract):
    r"""PathHandler

    PathHandler is a PathHandlerAbstract.
    Responsibility:
    """
    def __init__(self, pth):
        r"""

        @Arguments:
        - `path`:
        """
        self._path = _path.Path(pth)

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
        return PathHandler(unicode(self._path.copy2(unicode(dst))))

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
        self._path.copytree(unicode(dst), symlinks=symlinks, ignore=ignore)

    def copymode(self, dst):
        """SUMMARY

        @Arguments:
        - `dst`:

        @Return: None
        """
        self._path.copymode(unicode(dst))

    def copystat(self, dst):
        """SUMMARY

        @Arguments:
        - `dst`:

        @Return: None
        """
        self._path.copystat(unicode(dst))

    def exists(self):
        """SUMMARY

        @Return: bool
        """
        return self._path.exists()

    def expanduser(self):
        """SUMMARY

        @Return: PathHandler
        """
        return PathHandler(unicode(self._path.expanduser()))

    def expandvars(self):
        """SUMMARY

        @Return: PathHandler

        """
        return PathHandler(unicode(self._path.expandvars()))

    def get_absolute(self):
        """SUMMARY

        @Return: PathHandler
        """
        return PathHandler(unicode(self._path.abspath()))

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
        return PathHandler(unicode(self._path.basename()))

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
        return PathHandler(unicode(self._path.drive))

    drive = property(get_drive)

    def get_dirname(self):
        """SUMMARY

        @Return: PathHandler
        """
        return PathHandler(unicode(self._path.dirname()))

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
        return PathHandler(unicode(self._path.normpath()))

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
        return PathHandler(unicode(_pathlib.Path(str(self)).root))

    root = property(get_root)

    def get_relative(self, start='.'):
        """SUMMARY

        @Arguments:
        - `start`:

        @Return: PathHandler
        """
        return PathHandler(unicode(self._path.relpath(start)))

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
        return _pathlib.Path(unicode(self._path)).is_fifo()

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

    def join(self, path):
        """SUMMARY

        @Arguments:
        - `path`:

        @Return: PathHandler
        """
        return PathHandler(_os.path.join(unicode(self._path), unicode(path)))

    def listdir(self, pattern=None):
        """SUMMARY

        @Arguments:
        - `pattern`:

        @Return: list
        """
        regexp = re.compile(pattern or '')
        return [PathHandler(x) for x in self._path.listdir()
                if not regexp.search(x) is None]

    def link(self, path):
        """SUMMARY

        @Arguments:
        - `path`:

        @Return: PathHandler
        """
        return PathHandler(unicode(self._path.symlink(unicode(path))))

    def mkdir(self, mode, parents=False):
        """SUMMARY

        @Arguments:
        - `mode`:
        - `parents`:

        @Return: None
        """
        if parents:
            self._path.makedirs(mode)
        else:
            self._path.mkdir(mode)

    def move(self, dst):
        """SUMMARY

        @Arguments:
        - `dst`:

        @Return: PathHandler
        """
        return PathHandler(unicode(self._path.move(unicode(dst))))

    def open(self, *args, **kwargs):
        """SUMMARY

        @Arguments:
        - `*args`:
        - `**kwargs`:

        @Return: file
        """
        return open(unicode(self._path), *args, **kwargs)

    def readlink(self):
        """SUMMARY

        @Return: PathHandler
        """
        return PathHandler(_os.readlink(unicode(self._path)))

    def remove(self):
        """SUMMARY

        @Return: None
        """
        if self.isdir():
            self._path.rmtree()
        else:
            self._path.remove()

    def rename(self, new, force=False):
        """SUMMARY

        @Arguments:
        - `new`:
        - `force`:

        @Return: PathHandler
        """
        return PathHandler(unicode(self._path.rename(unicode(new))))

    def samefile(self, other):
        """SUMMARY

        @Arguments:
        - `other`:

        @Return: bool
        """
        return self._path.samefile(unicode(other))

    def splitdrive(self):
        """SUMMARY

        @Return: tuple
        """
        return self._path.splitdrive()

    def splitext(self):
        """SUMMARY

        @Return: tuple
        """
        return self._path.splitext()

    def touch(self):
        """SUMMARY

        @Return: None
        """
        self._path.touch()

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
            yield PathHandler(unicode(pth))

    def with_name(self, name):
        """SUMMARY

        @Arguments:
        - `name`:

        @Return: PathHandler
        """
        return PathHandler(unicode(_pathlib.Path(unicode(self._path)).with_name(name)))

    def with_ext(self, suffix):
        """SUMMARY

        @Arguments:
        - `suffix`:

        @Return: PathHandler
        """
        return PathHandler(
            unicode(_pathlib.Path(unicode(self._path)).with_suffix(suffix)))

    def __repr__(self):
        return '{0.__class__.__name__}("{1}")'.format(self, str(self))

    def __str__(self):
        return str(self._path.encode('utf-8'))

    def __unicode__(self):
        return unicode(self._path)

    def __eq__(self, other):
        if isinstance(other, (self.__class__, )):
            return unicode(self) == unicode(other)
        return unicode(self) == other

    def __ne__(self, other):
        return not self == other

    def __hash__(self, ):
        return hash(unicode(self._path))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _handler.py ends here
