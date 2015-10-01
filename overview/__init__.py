#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id: __init__.py 98 2014-01-11 10:09:59Z t1 $
# $Revision: 98 $
# $Date: 2014-01-11 19:09:59 +0900 (Sat, 11 Jan 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-01-11 19:09:59 +0900 (Sat, 11 Jan 2014) $
r"""\
Name: __init__.py


"""


from abc import ABCMeta, abstractmethod
import os as _os
import shutil as _shutil
import tempfile as _tempfile
import inspect as inspect

from portable import DRIVE_DIR as _DRIVE_DIR
from pycmd import which as _which
from ref.CMD.doxygen import DOXYGEN as _DOXYGEN


__revision__ = "$Revision: 98 $"
__version__ = "0.1.0"

__all__ = [ '' ]


def path_checker(path):
    """Check exists path. If not exists raise error.

    @Arguments:
    - `path`: file or directory
    """
    if not _os.path.exists(path):
        raise IOError('File does not exists: %s' % _os.path.abspath(path))



class _OverAbstract(object):
    r"""
    """
    __metaclass__ = ABCMeta

    def __init__(self, target, dir_):
        """

        Arguments:
        - `target`:
        - `dir_`:
        """
        self._target = target
        self._dir_ = dir_

    @abstractmethod
    def run(self, ):
        r"""SUMMARY

        run()

        @Return:
        """
        raise NotImplementedError




# class _OverAbstract(object):
#     """
#     """

#     def __init__(self, target, dir_):
#         """

#         Arguments:
#         - `target`:
#         - `dir_`:
#         """
#         self._target = target
#         self._dir_ = dir_


class Pyreverse(_OverAbstract):
    """
    """

    def pyreverse(self, detail=True):
        """Pyreverse command.

        @Arguments:
        - `detail`:

        @Return:
        """
        join, exists, abspath = _os.path.join, _os.path.exists, _os.path.abspath
        basename, system, remove = _os.path.basename, _os.system, _os.remove
        mkdir = _os.mkdir

        # detarmine pyreverse bin_
        if 'nt' == _os.name:
            bin_ = 'pyreverse.bat'
        elif 'posix' == _os.name:
            bin_ = 'pyreverse'
        else:
            raise NotImplementedError('not supported {.name} environment'
                                      .format(_os))

        # check exists pyreverse bin_
        if not _which(bin_):
            raise IOError('File does not exists: %s' % bin_)

        # destination directory
        dst_dir = join(self._dir, 'UML')
        # if not exists create it.
        if not exists(dst_dir):
            mkdir(dst_dir)

        # Do execute, there are two option.
        # simple output or detail output
        name = basename(self._dir)
        if detail:
            cmd = '{0} -SAmy -o png -p {1} {2}'.format(bin_, name, self._target)
        else:
            name = 'Simple_' + name
            cmd = '{0} -o png -p {1} {2}'.format(bin_, name, self._target)
        system(cmd)

        # check output
        src_name = 'classes_{0}.png'.format(name)
        src = abspath(src_name)
        # if not exists src, raise error
        path_checker(src)

        # finalyze
        dst = join(dst_dir, src_name)
        # first then remove it, if exists dst file.
        if exists(dst):
            remove(dst)
        if exists(src):
            _shutil.move(src, dst)
        elif not exists(src):
            raise IOError('File does not exists: %s' % src)

    def run(self, detail=True):
        r"""SUMMARY

        run()

        @Return:
        """
        self.pyreverse(detail=detail)


class Epydoc(_OverAbstract):
    """
    """

    def epydoc(self):
        """Epydoc command.

        @Arguments:
        - `target`:

        @Return:
        """
        join, isabs, exists = _os.path.join , _os.path.isabs, _os.path.exists
        if not isabs(self._target):
            raise ValueError('Set absolute path: %s' % self._target)

        # check exists epydoc
        bin_ = 'epydoc'
        if not _which(bin_):
            raise IOError('File does not exists: %s' % bin_)

        # destination directory
        dst = join(self._dir, 'epydoc_html')

        # do exec
        cmd = '{0} --graph all --html --output {1} {2}'.format(
            bin_, dst, self._target)
        _os.system(cmd)

        # check output
        if not exists(dst):
            raise IOError('File does not exists: {0}'.format(dst))

    def run(self, ):
        r"""SUMMARY

        run()

        @Return:
        """
        self.epydoc()


class Doxygen(_OverAbstract):
    """
    """

    def run(self, ):
        r"""SUMMARY

        run()

        @Return:
        """
        self.doxygen()

    def doxygen(self):
        """Doxygen command.

        @Return:
        """
        isfile = _os.path.isfile
        dox_output = 'doxygen_html'
        # check doxygen exists excutable
        if not _which(_DOXYGEN.get('bin')):
            raise IOError('File does not exists: %s' % _DOXYGEN.get('bin'))

        # check doxygen config and target files
        for item in [_DOXYGEN.get('conf'), self._target]:
            path_checker(item)

        # create tmp directory and go to directory if target is file, .
        orig_dir = _os.path.curdir
        if isfile(self._target):
            tempdir = _tempfile.mkdtemp()
            _shutil.copy2(self._target, tempdir)
            _os.chdir(tempdir)
            # Execute doxygen
            _os.system(_DOXYGEN.get('bin') + ' ' + _DOXYGEN.get('conf'))
            path_checker(dox_output)
            # shutil.copytree(dox_output, _os.path.join(self._dir, dox_output))
        else:
            _os.chdir(_os.path.dirname(self._target))
            # Execute doxygen
            _os.system(_DOXYGEN.get('bin') + ' ' + _DOXYGEN.get('conf'))
            path_checker(dox_output)

        # move outputed directory to orig path if target is file
        _os.chdir(orig_dir)


class Overview(Pyreverse, Epydoc, Doxygen):
    """
    """

    def __init__(self, target, dir_):
        """

        Arguments:
        - `target`:
        - `dir_`:
        - `detail`:
        """
        self._target = target
        self._dir = dir_
        self._methods = []

    def __iter__(self):
        """SUMMARY

        @Return:
        """
        for m in dir(self):
            if m.startswith('_') or m in ('next', ):
                continue
            if inspect.ismethod(getattr(self, m)):
                self._methods.append(m)
        return self

    def next(self):
        """SUMMARY

        @Return:
        """
        try:
            func = getattr(self, self._methods.pop())
        except IndexError:
            raise StopIteration
        return func

    def do_all(self):
        """SUMMARY

        @Return:
        """
        # for m in dir(self):
        #     if m.startswith('_') or m in ['next']:
        #         continue
        #     if inspect.ismethod(getattr(self, m)):
        #         getattr(self, m)()
        # use iterator
        for func in self:
            func()


### PYREVERSE
def my_pyreverse(target, dir_, detail=True):
    """Pyreverse command.

    @Arguments:
    - `target`:
    - `dst`:
    - `detail`:

    @Return:
    """
    # detarmine pyreverse bin_
    if 'nt' == _os.name:
        bin_ = 'pyreverse.bat'
    elif 'posix' == _os.name:
        bin_ = 'pyreverse'

    # check exists pyreverse bin_
    if not _which(bin_):
        raise IOError('File does not exists: %s' % bin_)

    # destination directory
    dst_dir = _os.path.join(dir_, 'UML')
    # if not exists create it.
    if not _os.path.exists(dst_dir):
        _os.mkdir(dst_dir)

    # do exec
    # there are two option.
    # simple output or detail output
    name = _os.path.basename(dir_)
    if detail:
        _os.system('{0} -SAmy -o png -p {1} {2}'.format(bin_, name, target))
    else:
        name = 'Simple_' + name
        _os.system('{0} -o png -p {1} {2}'.format(bin_, name, target))

    # check output
    src_name = 'classes_{0}.png'.format(name)
    src = _os.path.abspath(src_name)
    # if not exists src, raise error
    path_checker(src)

    # finalyze
    dst = _os.path.join(dst_dir, src_name)
    # first then remove it, if exists dst file.
    if _os.path.exists(dst):
        _os.remove(dst)
    if _os.path.exists(src):
        _shutil.move(src, dst)
    elif not _os.path.exists(src):
        raise IOError('File does not exists: %s' % src)

### epydoc
def my_epydoc(target, dir_):
    """Epydoc command.

    @Arguments:
    - `target`:

    @Return:
    """
    if not _os.path.isabs(target):
        raise ValueError('Set absolute path: %s' % target)

    # check exists epydoc
    bin_ = 'epydoc'
    if not _which(bin_):
        raise IOError('File does not exists: %s' % bin_)

    # destination directory
    dst = _os.path.join(dir_, 'epydoc_html')

    # do exec
    _os.system('{0} --graph all --html --output {1} {2}'.format(bin_, dst, target))

    # check output
    if not _os.path.exists(dst):
        raise IOError('File does not exists: %s' % dst)

def my_doxygen(target, dir_):
    """Doxygen command.

    @Return:
    """
    if 'nt' == _os.name:
        dox_bin = 'doxygen.exe'
        doxygen_conf = _os.path.join(_DRIVE_DIR, 'Dos/graphviz/doxygen.conf')
    elif 'posix' == _os.name:
        dox_bin = 'doxygen'
        doxygen_conf = _os.path.expanduser('~/.emacs.d/data_e/doxygen.conf')

    dox_output = 'doxygen_html'
    # check doxygen exec file
    if not _which(dox_bin):
        raise IOError('File does not exists: %s' % dox_bin)

    # check doxygen config and target files
    for item in (doxygen_conf, target):
        path_checker(item)

    # set flag if exists target
    isfile = _os.path.isfile(target)

    # create tmp directory and go to directory if target is file, .
    orig_dir = _os.path.curdir
    if isfile:
        tempdir = _tempfile.mkdtemp()
        _shutil.copy2(target, tempdir)
        _os.chdir(tempdir)
    else:
        _os.chdir(_os.path.dirname(target))

    # Execute doxygen
    _os.system(dox_bin + ' ' + doxygen_conf)

    path_checker(dox_output)

    # move outputed directory to orig path if target is file
    if isfile:
        _shutil.copytree(dox_output, _os.path.join(dir_, dox_output))
    _os.chdir(orig_dir)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
