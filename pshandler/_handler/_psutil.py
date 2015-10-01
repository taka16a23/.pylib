#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""_psutil -- DESCRIPTION

Adaptor
"""
import os as _os
import sys as _sys
import subprocess as _subprocess

import psutil

from pshandler._abstract import ProcessHandlerAbstract
from pshandler._compat import wraps
from pshandler import _err, _ntuple


def wrap_exceptions(fun):
    r"""SUMMARY

    wrap_exceptions(fun)

        return (self.pid, self.create_time)

    def get_pid(self):
        """SUMMARY"""
        return self._ps.pid

    pid = property(get_pid)

    @wrap_exceptions
    def get_parent(self):
        return ProcessHandler(self._ps.ppid())

    parent = property(get_parent)

    @wrap_exceptions
    def get_name(self):
        return self._ps.name()

    name = property(get_name)

    @wrap_exceptions
    def get_path(self):
        return self._ps.exe()

    path = property(get_path)

    @wrap_exceptions
    def get_status(self):
        return self._ps.status()

    status = property(get_status)

    @wrap_exceptions
    def get_cmdline(self):
        return self._ps.cmdline()

    cmdline = property(get_cmdline)

    @wrap_exceptions
    def get_username(self):
        return self._ps.username()

    username = property(get_username)

    @wrap_exceptions
    def get_create_time(self):
        return self._ps.create_time()

    create_time = property(get_create_time)

    @wrap_exceptions
    def get_cwd(self):
        return self._ps.cwd()

    cwd = property(get_cwd)

    @wrap_exceptions
    def get_nice(self):
        return self._ps.nice()

    @wrap_exceptions
    def set_nice(self, value):
        self._ps.nice(value)

    nice = property(get_nice, set_nice)

    @wrap_exceptions
    def get_memory_info(self):
        return _ntuple.PSMEM(*self._ps.memory_info_ex())

    meminfo = property(get_memory_info)

    @wrap_exceptions
    def suspend(self):
        self._ps.suspend()

    @wrap_exceptions
    def resume(self):
        self._ps.resume()

    @wrap_exceptions
    def terminate(self):
        self._ps.terminate()

    @wrap_exceptions
    def kill(self):
        self._ps.kill()

    @wrap_exceptions
    def is_running(self):
        return self._ps.is_running()

    @wrap_exceptions
    def list_threads(self):
        return [_ntuple.PSThread(*x) for x in self._ps.threads()]

    threads = property(list_threads)

    @wrap_exceptions
    def list_children(self):
        return [ProcessHandler(x.pid) for x in self._ps.children()]

    @wrap_exceptions
    def recursive_children(self):
        return [ProcessHandler(x.pid) for x in self._ps.children(recursive=True)]

    @wrap_exceptions
    def get_cpu_percent(self):
        return self._ps.cpu_percent()

    cpu_percent = property(get_cpu_percent)

    @wrap_exceptions
    def get_cpu_times(self):
        return _ntuple.PSCpuTimes(*self._ps.cpu_times())

    cpu_times = property(get_cpu_times)

    @wrap_exceptions
    def list_open_files(self):
        return [_ntuple.PSOpenFile(*x) for x in self._ps.open_files()]

    open_files = property(list_open_files)

    @wrap_exceptions
    def list_connections(self, kind='inet'):
        return [_ntuple.PSCONN(*x) for x in self._ps.connections(kind)]

    connections = property(list_connections)

    @wrap_exceptions
    def send_signal(self, sig):
        self._ps.send_signal(sig)

    @wrap_exceptions
    def wait(self, timeout=None):
        try:
            return self._ps.wait(timeout)
        except psutil.TimeoutExpired:
            raise _err.Timeout(timeout, self.pid, self.name)

    # windows
    if _os.name == 'nt':
        @wrap_exceptions
        def get_num_handles(self):
            return self._ps.num_handles()

        num_handles = property(get_num_handles)

        @wrap_exceptions
        def get_ionice(self):
            return _ntuple.PSIONice(*self._ps.ionice())

        @wrap_exceptions
        def set_ionice(self, ioclass, value=None):
            self._ps.ionice(ioclass, value)

        ionice = property(get_ionice, set_ionice)

        @wrap_exceptions
        def get_io_counters(self, ):
            return _ntuple.PSIO(*self._ps.io_counters())

        io_counters = property(get_io_counters)

    # posix
    if _os.name == 'posix':
        @wrap_exceptions
        def get_uids(self):
            return _ntuple.PSUIDs(*self._ps.uids())

        uids = property(get_uids)

        @wrap_exceptions
        def get_gids(self):
            return _ntuple.PSGIDs(*self._ps.gids())

        gids = property(get_gids)

        @wrap_exceptions
        def get_terminal(self):
            return self._ps.terminal()

        terminal = property(get_terminal)

        @wrap_exceptions
        def num_fds(self):
            return self._ps.num_fds()

        fds = property(num_fds)

    # linux
    if _sys.platform.startswith(('linux')):
        @wrap_exceptions
        def get_ionice(self):
            return _ntuple.PSIONice(*self._ps.ionice())

        @wrap_exceptions
        def set_ionice(self, ioclass, value=None):
            self._ps.ionice(ioclass, value)

        ionice = property(get_ionice, set_ionice)

        @wrap_exceptions
        def get_io_counters(self):
            return _ntuple.PSIO(*self._ps.io_counters())

        io_counters = property(get_io_counters)

        @wrap_exceptions
        def get_rlimit(self, resource):
            return self._ps.rlimit(resource)

        @wrap_exceptions
        def set_rlimit(self, resource, limits):
            r"""SUMMARY

            set_rlimit(resource, limits)

            @Arguments:
            - `resource`:
            - `limits`:

            @Return:

            @Error:
            """
            return self._ps.rlimit(resource, limits)

        @wrap_exceptions
        def get_cpu_affinity(self):
            return self._ps.cpu_affinity()

        @wrap_exceptions
        def set_cpu_affinity(self, cpus):
            return self._ps.cpu_affinity(cpus)

        cpu_affinity = property(get_cpu_affinity, set_cpu_affinity)

    # freebsd
    if _sys.platform.startswith(('freebsd')):
        @wrap_exceptions
        def get_io_counters(self):
            return _ntuple.PSIO(*self._ps.io_counters())

        io_counters = property(get_io_counters)


class Popen(ProcessHandler):
    r"""Popen

    Popen is a ProcessHandler.
    Responsibility:
                                     % (self.__class__.__name__, name))

    def wait(self, timeout=None):
        if self.__subproc.returncode is not None:
            return self.__subproc.returncode
        ret = super(Popen, self).wait(timeout)
        self.__subproc.returncode = ret
        return ret



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# _psutil.py ends here
