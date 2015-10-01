#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: king_service.py 80 2013-11-22 07:02:28Z t1 $
# $Revision: 80 $
# $Date: 2013-11-22 16:02:28 +0900 (Fri, 22 Nov 2013) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2013-11-22 16:02:28 +0900 (Fri, 22 Nov 2013) $

"""\
Name: king_service.py

"""
# TODO: (Atami) [2013/03/07]
# check exists command finger lsof gawk

import socket
import subprocess
import sys
import os
import atexit
import time
from contextlib import closing
from signal import SIGTERM
import logging

LOG_FILENAME = '/var/log/king_service.log'
logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.DEBUG,
                    format='%(asctime)s %(message)s')


class Daemon:
    """
    A generic daemon class.

    Usage: subclass the Daemon class and override the run() method
    """
    def __init__(self, pidfile, stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr
        self.pidfile = pidfile

    def daemonize(self):
        """
        do the UNIX double-fork magic, see Stevens' "Advanced
        Programming in the UNIX Environment" for details (ISBN 0201563177)
        http://www.erlenstar.demon.co.uk/unix/faq_2.html#SEC16
        """
        try:
            pid = os.fork()
            if pid > 0:
                # exit first parent
                sys.exit(0)
        except OSError, e:
            sys.stderr.write("fork #1 failed: %d (%s)\n" % (e.errno, e.strerror))
            sys.exit(1)

        # decouple from parent environment
        os.chdir("/")
        os.setsid()
        os.umask(0)

        # do second fork
        try:
            pid = os.fork()
            if pid > 0:
                # exit from second parent
                sys.exit(0)
        except OSError, e:
            sys.stderr.write("fork #2 failed: %d (%s)\n" % (e.errno, e.strerror))
            sys.exit(1)

        # redirect standard file descriptors
        sys.stdout.flush()
        sys.stderr.flush()
        si = file(self.stdin, 'r')
        so = file(self.stdout, 'a+')
        se = file(self.stderr, 'a+', 0)
        os.dup2(si.fileno(), sys.stdin.fileno())
        os.dup2(so.fileno(), sys.stdout.fileno())
        os.dup2(se.fileno(), sys.stderr.fileno())

        # write pidfile
        atexit.register(self.delpid)
        pid = str(os.getpid())
        file(self.pidfile,'w+').write("%s\n" % pid)

    def delpid(self):
        os.remove(self.pidfile)

    def start(self):
        """
        Start the daemon
        """
        # Check for a pidfile to see if the daemon already runs
        try:
            pf = file(self.pidfile,'r')
            pid = int(pf.read().strip())
            pf.close()
        except IOError:
            pid = None

        if pid:
            message = "pidfile %s already exist. Daemon already running?\n"
            sys.stderr.write(message % self.pidfile)
            sys.exit(1)

        # Start the daemon
        self.daemonize()
        self.run()

    def stop(self):
        """
        Stop the daemon
        """
        # Get the pid from the pidfile
        try:
            pf = file(self.pidfile,'r')
            pid = int(pf.read().strip())
            pf.close()
        except IOError:
            pid = None

        if not pid:
            message = "pidfile %s does not exist. Daemon not running?\n"
            sys.stderr.write(message % self.pidfile)
            return # not an error in a restart

        # Try killing the daemon process
        while 1:
            try:
                os.kill(pid, SIGTERM)
                time.sleep(0.1)
            except OSError, err:
                err = str(err)
                if err.find("No such process") > 0:
                    if os.path.exists(self.pidfile):
                        os.remove(self.pidfile)
                else:
                    print str(err)
                    sys.exit(1)
            except KeyboardInterrupt:
                print('KeyboardInterrupted')
                break

    def restart(self):
        """
        Restart the daemon
        """
        self.stop()
        self.start()

    def run(self):
        """
        You should override this method when you subclass Daemon. It will be called after the process has been
        daemonized by start() or restart().
        """
        pass

def test_cmd(cmd):
    """Test execute command.

    @Arguments:
    - `cmd`: string for executable command.

    @Return:
    Return True if command successed.
    Return False if command failed.
    """
    child = subprocess.Popen(cmd, shell=True,
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)
    out, err = child.communicate()
    if err:
        raise StandardError('[{0}] {1}'.format(err, child.returncode))
    return 0 == child.returncode

def is_user_logged_in():
    """Check user logging.

    @Return:
    Return True if user login.
    Return False if user not login.
    """
    cmd = '/usr/bin/finger'
    child = subprocess.Popen(cmd, shell=True,
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)
    out, err = child.communicate()
    if err:
        raise StandardError('[{0}] {1}'.format(err, child.returncode))
    return 'No one logged on.\n' != out

def is_using_samba():
    """Check using samba by other user.

    @Return:
    Return True if user using samba.
    Return False if user not using samba.
    """
    cmd = "lsof | grep smbd | gawk '{ print $9}' | grep 192.168"
    return test_cmd(cmd)

def is_using_sftp():
    """Check using sftp(SCP).

    @Return:
    Return True if using sftp.
    Return False if not using sftp.
    """
    cmd = 'lsof | grep sftp-serv'
    return test_cmd(cmd)

def isShutdownAble():
    """SUMMARY

    @Return:
    """
    return not (is_user_logged_in() or is_using_samba() or is_using_sftp())


class KiDaemon(Daemon):

    def run(self):
        """SUMMARY

        @Return:
        """
        HOST = ''
        PORT = 65535
        BUFSIZE = 1024
        ADDR = (HOST, PORT)
        with closing(socket.socket(socket.AF_INET, socket.SOCK_DGRAM)) as sock:
            sock.bind(ADDR)
            while 1:
                # print('Waiting for connection...')
                recved, addr = sock.recvfrom(BUFSIZE)
                # print('received {0} from {1}'.format(recved, addr))
                if 'halt' == recved:
                    if isShutdownAble():
                        logging.log(10, 'ACCEPT: halt command accepted from %s' % addr)
                        sock.sendto('accept', addr)
                        os.system('halt')
                    else:
                        logging.log(10, 'USING: halt command rejected from %s.')
                        sock.sendto('using', addr)

def _main():
    daemon = KiDaemon('/tmp/king_service.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print('Unknown Command')
            sys.exit(2)
        sys.exit(0)
    else:
        print('Usage: %s start|stop|restart' % sys.argv[0])
        sys.exit(2)

if __name__ == '__main__':
    _main()


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# king_service.py ends here
