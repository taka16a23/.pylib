#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: _abstract.py 307 2015-02-07 03:48:46Z t1 $
# $Revision: 307 $
# $Date: 2015-02-07 12:48:46 +0900 (Sat, 07 Feb 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-02-07 12:48:46 +0900 (Sat, 07 Feb 2015) $

r"""_abstract -- DESCRIPTION

Interface

"""
import os as _os
import sys as _sys
from abc import ABCMeta, abstractmethod


class ProcessHandlerAbstract(object):
    """Abstract class ProcessHandlerAbstract
    """
    __metaclass__ = ABCMeta

    # Operations
    @abstractmethod
    def __init__(self, ):
        raise NotImplementedError()

    @abstractmethod
    def get_pid(self):
        raise NotImplementedError()

    @abstractmethod
    def get_parent(self):
        raise NotImplementedError()

    @abstractmethod
    def get_name(self):
        raise NotImplementedError()

    @abstractmethod
    def get_path(self):
        raise NotImplementedError()

    @abstractmethod
    def get_status(self):
        raise NotImplementedError()

    @abstractmethod
    def get_cmdline(self):
        raise NotImplementedError()

    @abstractmethod
    def get_username(self):
        raise NotImplementedError()

    @abstractmethod
    def get_create_time(self):
        raise NotImplementedError()

    @abstractmethod
    def get_cwd(self):
        raise NotImplementedError()

    @abstractmethod
    def get_nice(self):
        raise NotImplementedError()

    @abstractmethod
    def get_memory_info(self):
        raise NotImplementedError()

    @abstractmethod
    def set_nice(self, value):
        raise NotImplementedError()

    @abstractmethod
    def suspend(self):
        raise NotImplementedError()

    @abstractmethod
    def resume(self):
        raise NotImplementedError()

    @abstractmethod
    def terminate(self):
        raise NotImplementedError()

    @abstractmethod
    def kill(self):
        raise NotImplementedError()

    @abstractmethod
    def is_running(self):
        raise NotImplementedError()

    @abstractmethod
    def list_threads(self):
        raise NotImplementedError()

    @abstractmethod
    def list_children(self):
        raise NotImplementedError()

    @abstractmethod
    def recursive_children(self):
        raise NotImplementedError()

    @abstractmethod
    def get_cpu_percent(self):
        raise NotImplementedError()

    @abstractmethod
    def get_cpu_times(self):
        raise NotImplementedError()

    @abstractmethod
    def list_open_files(self):
        raise NotImplementedError()

    @abstractmethod
    def list_connections(self, kind='inet'):
        raise NotImplementedError()

    @abstractmethod
    def send_signal(self, sig):
        raise NotImplementedError()

    @abstractmethod
    def wait(self, timeout=None):
        raise NotImplementedError()

    # windows
    if _os.name == 'nt':
        @abstractmethod
        def get_num_handles(self):
            raise NotImplementedError()

        @abstractmethod
        def get_ionice(self):
            raise NotImplementedError()

        @abstractmethod
        def set_ionice(self, ioclass, value=None):
            raise NotImplementedError()

        @abstractmethod
        def get_io_counters(self):
            raise NotImplementedError()

    # posix
    if _os.name == 'posix':
        @abstractmethod
        def get_uids(self):
            raise NotImplementedError()

        @abstractmethod
        def get_gids(self):
            raise NotImplementedError()

        @abstractmethod
        def get_terminal(self):
            raise NotImplementedError()

        @abstractmethod
        def num_fds(self):
            raise NotImplementedError()

    # linux
    if _sys.platform.startswith(('linux')):
        @abstractmethod
        def get_ionice(self):
            raise NotImplementedError()

        @abstractmethod
        def set_ionice(self, ioclass, value=None):
            raise NotImplementedError()

        @abstractmethod
        def get_io_counters(self):
            raise NotImplementedError()

        @abstractmethod
        def get_rlimit(self, resource):
            raise NotImplementedError()

        @abstractmethod
        def set_rlimit(self, resource, limits):
            raise NotImplementedError()

        @abstractmethod
        def get_cpu_affinity(self):
            raise NotImplementedError()

        @abstractmethod
        def set_cpu_affinity(self, cpus):
            raise NotImplementedError()

    # freebsd
    if _sys.platform.startswith(('freebsd')):
        @abstractmethod
        def get_io_counters(self):
            raise NotImplementedError()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _abstract.py ends here
