#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""\
Name: test_client.py

"""


from mocker import MockerTestCase, ANY, Mocker
# from ..client import Aquos
from aquos.client import (Aquos, _POWR, _ITGD, _ITVD, _IAVD, _IDEG, _Channel,
                          _INP4, _AVMD, _VOLM, _HPOS, _VPOS, _CLCK, _PHSE,
                          _WIDE, _MUTE, _ACHA, _OFTM)
import socket


class Construction_tests(MockerTestCase):
    r"""
    """
    def setUp(self):
        r"""SUMMARY

        @Return:
        """
        # aquos = Aquos('username', '192.168.1.111', port=12345)

        # kill getpass
        dummygetpass = self.mocker.replace('getpass.getpass')
        dummygetpass(ANY)
        self.mocker.result('dummy_passwd')
        self.mocker.count(0, None)

        # dummy_aquos = self.mocker.proxy(aquos)
        dummy_sock = self.mocker.patch(socket.socket)
        # escape connect
        dummy_sock.connect(ANY)
        self.mocker.result(None)
        self.mocker.count(0, None)
        # escape send
        dummy_sock.send(ANY)
        self.mocker.result(None)
        self.mocker.count(0, None)

        # receive 'Login:'
        dummy_sock.recv(ANY)
        self.mocker.result('Login:')
        # receive 'Password:'
        dummy_sock.recv(ANY)
        self.mocker.result('Password:')
        # receive 'OK'
        dummy_sock.recv(ANY)
        self.mocker.result('OK')

        self.mocker.replay()
        # self.assertTrue(aquos.login())
        self.aquos = Aquos('username', '192.168.1.111', port=12345)


    def test_valid(self):
        r"""SUMMARY

        @Return:
        """
        self.assertEqual(self.aquos._user, 'username')
        self.assertEqual(self.aquos._host, '192.168.1.111')
        self.assertEqual(self.aquos._port, 12345)
        self.assertEqual(type(self.aquos._sock), socket._socketobject)
        # self.assertFalse(aquos._connected)

    # def test_login_true(self):
    #     r"""SUMMARY

    #     @Return:
    #     """
    #     aquos = Aquos('username', '192.168.1.111', port=12345)

    #     # kill getpass
    #     dummygetpass = self.mocker.replace('getpass.getpass')
    #     dummygetpass(ANY)
    #     self.mocker.result('dummy_passwd')
    #     self.mocker.count(0, None)

    #     dummy_aquos = self.mocker.proxy(aquos)
    #     dummy_sock = self.mocker.patch(socket.socket)
    #     # escape connect
    #     dummy_sock.connect(ANY)
    #     self.mocker.result(None)
    #     self.mocker.count(0, None)
    #     # escape send
    #     dummy_sock.send(ANY)
    #     self.mocker.result(None)
    #     self.mocker.count(0, None)

    #     # receive 'Login:'
    #     dummy_sock.recv(ANY)
    #     self.mocker.result('Login:')
    #     # receive 'Password:'
    #     dummy_sock.recv(ANY)
    #     self.mocker.result('Password:')
    #     # receive 'OK'
    #     dummy_sock.recv(ANY)
    #     self.mocker.result('OK')

    #     self.mocker.replay()
    #     self.assertTrue(aquos.login())

    def test_commands_object(self):
        r"""SUMMARY

        @Return:
        """
        # aquos = Aquos('username', '192.168.1.111', port=12345)

        # # kill getpass
        # dummygetpass = self.mocker.replace('getpass.getpass')
        # dummygetpass(ANY)
        # self.mocker.result('dummy_passwd')
        # self.mocker.count(0, None)

        # dummy_aquos = self.mocker.proxy(aquos)
        # dummy_sock = self.mocker.patch(socket.socket)
        # # escape connect
        # dummy_sock.connect(ANY)
        # self.mocker.result(None)
        # self.mocker.count(0, None)
        # # escape send
        # dummy_sock.send(ANY)
        # self.mocker.result(None)
        # self.mocker.count(0, None)

        # # receive 'Login:'
        # dummy_sock.recv(ANY)
        # self.mocker.result('Login:')
        # # receive 'Password:'
        # dummy_sock.recv(ANY)
        # self.mocker.result('Password:')
        # # receive 'OK'
        # dummy_sock.recv(ANY)
        # self.mocker.result('OK')

        # self.mocker.replay()
        # aquos.login()
        self.assertEqual(type(self.aquos.power),
                         type(_POWR(sock=self.aquos._sock)))
        self.assertEqual(type(self.aquos.inputtoggle),
                         type(_ITGD(sock=self.aquos._sock)))
        self.assertEqual(type(self.aquos.inputtv),
                         type(_ITVD(sock=self.aquos._sock)))
        self.assertEqual(type(self.aquos.input),
                         type(_IAVD(sock=self.aquos._sock)))
        self.assertEqual(type(self.aquos.inputdegital),
                         type(_IDEG(sock=self.aquos._sock)))
        self.assertEqual(type(self.aquos.channel),
                         type(_Channel(sock=self.aquos._sock)))
        self.assertEqual(type(self.aquos.input4),
                         type(_INP4(sock=self.aquos._sock)))
        self.assertEqual(type(self.aquos.avposition),
                         type(_AVMD(sock=self.aquos._sock)))
        self.assertEqual(type(self.aquos.volume),
                         type(_VOLM(sock=self.aquos._sock)))
        self.assertEqual(type(self.aquos.horizon),
                         type(_HPOS(sock=self.aquos._sock)))
        self.assertEqual(type(self.aquos.vertical),
                         type(_VPOS(sock=self.aquos._sock)))
        self.assertEqual(type(self.aquos.clock),
                         type(_CLCK(sock=self.aquos._sock)))
        self.assertEqual(type(self.aquos.clockphese),
                         type(_PHSE(sock=self.aquos._sock)))
        self.assertEqual(type(self.aquos.display),
                         type(_WIDE(sock=self.aquos._sock)))
        self.assertEqual(type(self.aquos.mute),
                         type(_MUTE(sock=self.aquos._sock)))
        self.assertEqual(type(self.aquos.audio),
                         type(_ACHA(sock=self.aquos._sock)))
        self.assertEqual(type(self.aquos.offtimer),
                         type(_OFTM(sock=self.aquos._sock)))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_client.py ends here
