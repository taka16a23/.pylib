#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""sshconnector -- DESCRIPTION

"""
from time import sleep
from paramiko import SSHClient

from mypcs.commons.stdstream import StandardStream
from mypcs.scripts._shell._ssh import SSH
from mypcs._ssh.ssh_param import SSHParameter
from mypcs._ssh.interactive import interactive_shell


class SSHConnector(object):
    """Class SSHConnector
    """
    # Attributes:
    def __init__(self, host, port=22, user=None, keyfile=None, pkey=None,
                 compress=False, password=None, conntimeout=None,
                 readtimeout=None):
        r"""

        @Arguments:
        - `host`:
        - `port`:
        - `user`:
        - `keyfile`:
        - `pkey`:
        - `compress`:
        - `password`:
        - `conntimeout`:
        - `readtimeout`:
        """
        self.sshclient = SSHClient()
        self._sshparams = SSHParameter(host, port, user, keyfile, pkey,
                                       compress, password, conntimeout,
                                       readtimeout)

    # Operations
    def get_hostname(self):
        """function get_hostname

        returns
        """
        return self._sshparams.get_hostname()

    hostname = property(get_hostname)

    def get_port(self):
        """function get_port

        returns
        """
        return self._sshparams.get_port()

    port = property(get_port)

    def get_username(self, ):
        r"""SUMMARY

        get_username()

        @Return:

        @Error:
        """
        return self._sshparams.get_username()

    username = property(get_username)

    def get_keyfile(self):
        """function get_keyfile

        returns
        """
        return self._sshparams.get_keyfile()

    keyfile = property(get_keyfile)

    def get_pkey(self):
        """function get_pkey

        returns
        """
        return self._sshparams.get_pkey()

    pkey = property(get_pkey)

    def load_pkey(self, password):
        """function load_pkey

        password:

        returns
        """
        # TODO: (Atami) [2015/08/16]

        if self.get_keyfile() is None:
            # TODO: (Atami) [2015/08/16]
            raise StandardError()

        return None # should raise NotImplementedError()

    def set_compress(self):
        """function set_compress

        returns
        """
        self._sshparams.set_compress(True)

    def unset_compress(self):
        """function unset_compress

        returns
        """
        self._sshparams.set_compress(False)

    def is_compressed(self):
        """function is_compressed

        returns
        """
        return self._sshparams.is_compress()

    def get_password(self):
        """function get_password

        returns
        """
        return self._sshparams.get_password()

    def set_password(self, passwd):
        """function set_password

        passwd: str

        returns
        """
        self._sshparams.set_password(passwd)

    def get_connection_timeout(self):
        """function get_connection_timeout

        returns
        """
        return self._sshparams.get_connection_timeout()


    def set_connection_timeout(self, timeout):
        """function set_connection_timeout

        timeout: int

        returns
        """
        self._sshparams.set_connection_timeout(timeout)

    connection_timeout = property(
        get_connection_timeout, set_connection_timeout)

    def get_reading_timeout(self):
        """function get_reading_timeout

        returns
        """
        return self._sshparams.get_reading_timeout()

    def set_reading_timeout(self, timeout):
        """function set_reading_timeout

        timeout: int

        returns
        """
        self._sshparams.set_reading_timeout(timeout)

    reading_timeout = property(get_reading_timeout, set_reading_timeout)

    def connect(self):
        """function connect

        returns
        """
        self.sshclient.connect(hostname=str(self.hostname),
                               port=self.port,
                               username=self.username,
                               password=self.get_password(),
                               pkey=self.pkey,
                               key_filename=self.keyfile,
                               timeout=self.connection_timeout,
                               compress=self.is_compressed())
        return self.has_connection()

    def send_command(self, cmdline, get_pty=False):
        """function send_command

        cmdline: str
        get_pty:

        returns StandardStream
        """
        stdin, stdout, stderr = self.sshclient.exec_command(
            cmdline, timeout=self.reading_timeout, get_pty=get_pty)
        # TODO: (Atami) [2015/08/16]
        # agry
        counts = 0
        while not stdout.channel.exit_status_ready():
            sleep(0.01)
            if 10000 < counts:
                break
        returncode = stdout.channel.exit_status
        return StandardStream(stdin, stdout, stderr, returncode)

    def test_command(self, cmdline):
        """function test_command

        cmdline:

        returns bool
        """
        _, stdout, _ = self.sshclient.exec_command(
            cmdline, timeout=self.reading_timeout)
        # TODO: (Atami) [2015/08/16]
        # agry
        counts = 0
        while not stdout.channel.exit_status_ready():
            sleep(0.01)
            if 10000 < counts:
                break
        return stdout.channel.exit_status

    def execute_script(self, script):
        """function execute_script

        script:

        returns
        """
        shell = SSH(self.sshclient, timeout=self.reading_timeout)
        script.execute_script(shell)

    def has_connection(self):
        """function has_connection

        returns bool
        """
        transport = self.sshclient.get_transport()
        if transport is None:
            return False
        return transport.is_active()

    def open_sftp(self):
        """function open_sftp

        returns
        """
        return self.sshclient.open_sftp()

    def start_interactive(self):
        """function start_interactive

        returns
        """
        chan = self.sshclient.invoke_shell()
        interactive_shell(chan)
        chan.close()

    def close(self):
        """function close

        returns
        """
        self.sshclient.close()

    def __enter__(self):
        if not self.has_connection():
            self.connect()
        return self

    def __exit__(self, type, value, traceback):
        if self.has_connection:
            self.close()

    def __del__(self):
        if self.has_connection:
            self.close()

    def __nonzero__(self):
        return self.has_connection()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# sshconnector.py ends here
