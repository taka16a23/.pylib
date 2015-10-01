#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: server.py 259 2014-12-21 05:20:44Z t1 $
# $Revision: 259 $
# $Date: 2014-12-21 14:20:44 +0900 (Sun, 21 Dec 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-12-21 14:20:44 +0900 (Sun, 21 Dec 2014) $

r"""server -- DESCRIPTION

"""
import SocketServer
import select

from sshforward.log import LOG


class ForwardServer(SocketServer.ThreadingTCPServer):
    """ForwardServer
    """
    daemon_threads = True
    allow_reuse_address = True


class ForwardRequestHandler(SocketServer.BaseRequestHandler):
    """ForwardRequestHandler
    """

    chan = None

    def get_chain_host(self, ):
        raise NotImplementedError()

    def get_chain_port(self, ):
        raise NotImplementedError()

    def get_ssh_transport(self, ):
        raise NotImplementedError()

    def setup(self, ):
        r"""SUMMARY

        setup()

        @Return:

        @Error:
        """
        try:
            self.chan = self.get_ssh_transport().open_channel(
                'direct-tcpip',
                (self.get_chain_host(), self.get_chain_port()),
                self.request.getpeername())
        except Exception, err:
            self.chan = None
            LOG.error('Incoming request to {0}:{1} failed: {2}'
                      .format(self.get_chain_host(), self.get_chain_port(),
                              repr(err)))

    def handle(self):
        if self.chan is None:
            LOG.warn('Incoming request to {0}:{1}'
                      ' was rejected by the SSH server.'
                      .format(self.get_chain_host(), self.get_chain_port()))
            return
        LOG.info('Connected!  Tunnel open {0} -> {1} -> {2}'
                  .format(self.request.getpeername(),
                          self.chan.getpeername(),
                          (self.get_chain_host(), self.get_chain_port())))
        while 1:
            r, w, x = select.select([self.request, self.chan], [], [])
            if self.request in r:
                data = self.request.recv(1024)
                if len(data) == 0:
                    break
                self.chan.send(data)
            if self.chan in r:
                data = self.chan.recv(1024)
                if len(data) == 0:
                    break
                self.request.send(data)

    def finish(self, ):
        r"""SUMMARY

        finish()

        @Return:

        @Error:
        """
        if self.chan:
            self.chan.close()
        if self.request:
            self.request.close()
        LOG.info('Tunnel closed from {}'.format(self.request.getpeername()))


def forward_tunnel(local_port, remote_host, remote_port, transport):
    # this is a little convoluted, but lets me configure things for the Handler
    # object.  (SocketServer doesn't give Handlers any way to access the outer
    # server normally.)
    class SubHander (ForwardRequestHandler):
        chain_host = remote_host
        chain_port = remote_port
        ssh_transport = transport
        def get_chain_host(self, ):
            return self.chain_host
        def get_chain_port(self, ):
            return self.chain_port
        def get_ssh_transport(self):
            return self.ssh_transport

    ForwardServer(('', local_port), SubHander).serve_forever()



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# server.py ends here
