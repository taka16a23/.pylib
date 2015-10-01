#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: _interface.py 468 2015-08-19 05:49:01Z t1 $
# $Revision: 468 $
# $Date: 2015-08-19 14:49:01 +0900 (Wed, 19 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-19 14:49:01 +0900 (Wed, 19 Aug 2015) $

r"""_interface -- DESCRIPTION

"""
from abc import ABCMeta, abstractmethod


class PathHandlerAbstract(object):
    """Abstract class PathHandlerAbstract

    Stereotype: Interface

    this class for interface path handle.

    """
    __metaclass__ = ABCMeta

    # Operations
    @classmethod
    @abstractmethod
    def from_cwd(cls):
        pass

    @abstractmethod
    def chmod(self, mode):
        raise NotImplementedError()

    @abstractmethod
    def chown(self, uid, gid):
        raise NotImplementedError()

    @abstractmethod
    def copy(self, dst):
        raise NotImplementedError()

    @abstractmethod
    def copytree(self, dst, symlinks=False, ignore=None):
        raise NotImplementedError()

    @abstractmethod
    def copymode(self, dst):
        raise NotImplementedError()

    @abstractmethod
    def copystat(self, dst):
        raise NotImplementedError()

    @abstractmethod
    def exists(self):
        raise NotImplementedError()

    @abstractmethod
    def expanduser(self):
        raise NotImplementedError()

    @abstractmethod
    def expandvars(self):
        raise NotImplementedError()

    @abstractmethod
    def get_absolute(self):
        raise NotImplementedError()

    @abstractmethod
    def get_atime(self):
        raise NotImplementedError()

    @abstractmethod
    def get_basename(self):
        raise NotImplementedError()

    @abstractmethod
    def get_conf(self, name):
        raise NotImplementedError()

    @abstractmethod
    def get_ctime(self):
        raise NotImplementedError()

    @abstractmethod
    def get_drive(self):
        raise NotImplementedError()

    @abstractmethod
    def get_dirname(self):
        raise NotImplementedError()

    @abstractmethod
    def get_extension(self):
        raise NotImplementedError()

    @abstractmethod
    def get_mtime(self):
        raise NotImplementedError()

    @abstractmethod
    def get_normal(self):
        raise NotImplementedError()

    @abstractmethod
    def get_size(self):
        raise NotImplementedError()

    @abstractmethod
    def get_stat(self, ):
        raise NotImplementedError()

    @abstractmethod
    def get_stem(self):
        raise NotImplementedError()

    @abstractmethod
    def get_root(self):
        raise NotImplementedError()

    @abstractmethod
    def get_relative(self, start='.'):
        raise NotImplementedError()

    @abstractmethod
    def isabsolute(self):
        raise NotImplementedError()

    @abstractmethod
    def isdir(self):
        raise NotImplementedError()

    @abstractmethod
    def isfifo(self):
        raise NotImplementedError()

    @abstractmethod
    def isfile(self):
        raise NotImplementedError()

    @abstractmethod
    def ismount(self):
        raise NotImplementedError()

    @abstractmethod
    def issymlink(self):
        raise NotImplementedError()

    @abstractmethod
    def join(self, path):
        raise NotImplementedError()

    @abstractmethod
    def listdir(self, pattern=None):
        raise NotImplementedError()

    @abstractmethod
    def link(self, path):
        raise NotImplementedError()

    @abstractmethod
    def mkdir(self, mode, parents=False):
        raise NotImplementedError()

    @abstractmethod
    def move(self, dst):
        raise NotImplementedError()

    @abstractmethod
    def open(self, *args, **kwargs):
        raise NotImplementedError()

    @abstractmethod
    def readlink(self):
        raise NotImplementedError()

    @abstractmethod
    def remove(self):
        raise NotImplementedError()

    @abstractmethod
    def rename(self, new, force=False):
        raise NotImplementedError()

    @abstractmethod
    def samefile(self, other):
        raise NotImplementedError()

    @abstractmethod
    def splitdrive(self):
        raise NotImplementedError()

    @abstractmethod
    def splitext(self):
        raise NotImplementedError()

    @abstractmethod
    def touch(self):
        raise NotImplementedError()

    @abstractmethod
    def unlink(self):
        raise NotImplementedError()

    @abstractmethod
    def walk(self):
        raise NotImplementedError()

    @abstractmethod
    def with_name(self, name):
        raise NotImplementedError()

    @abstractmethod
    def with_ext(self, suffix):
        raise NotImplementedError()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _interface.py ends here
