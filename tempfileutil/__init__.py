#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py


"""
import os as _os
import tempfile as _tempfile
import shutil as _shutil

__version__ = "0.1.0"

__all__ = [ 'tmp_backup', 'FileNotExistError' ]


class TempfileUtilError(StandardError):
    r"""Base tempfileutil modules errors."""
    pass

class FileNotExistError(TempfileUtilError):
    r"""Error if not exists target files."""

    def __init__(self, path):
        self._path = path

    def __str__(self, ):
        return 'File not exists {}'.format(self._path)


def tmp_backup(path):
    r"""Backup file to temp directory.

    tmp_backup(path)

    @Arguments:
    - `path`: (str)file path

    @Return:
    (str)backuped path
    """
    if not _os.path.isfile(path):
        raise FileNotExistError(path)
    tmpdir = _tempfile.mkdtemp()
    _shutil.copy2(path, tmpdir)
    return _os.path.join(tmpdir, _os.path.basename(path))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
