#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# $Id: client.py 189 2014-05-17 09:44:59Z t1 $
# $Revision: 189 $
# $Date: 2014-05-17 18:44:59 +0900 (Sat, 17 May 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-05-17 18:44:59 +0900 (Sat, 17 May 2014) $
r""" client -- client for aquos

$Revision: 189 $

"""
import socket as _socket
from getpass import getpass as _getpass
from inspect import ismethod as _ismethod


from .cmds import CMDS


# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__revision__ = '$Revision: 189 $'
__version__ = '0.1.0'



class _ConnectAbstract(object):
    """
    """

    _ok = 'OK\r'
    _err = 'ERR\r'

    def __init__(self, sock):
        """
        """
        self._sock = sock
        self._cmds = CMDS[self.__class__.__name__[1:]]

    def _sendcmd(self, cmd):
        """SUMMARY

        @Arguments:

        - `cmd`:

        @Return:
        """
        return self._send(self._getcmd(cmd))

    def _getcmd(self, cmd):
        """SUMMARY

        @Arguments:

        - `cmd`:

        @Return:
        """
        return self._cmds.get(cmd)

    def _send(self, cmd):
        """SUMMARY

        @Arguments:

        - `cmd`:

        @Return:
        """
        self._sock.send(cmd)
        return self._sock.recv(1024)


class _StateAbstract(_ConnectAbstract):
    r"""
    """

    def getstatus(self):
        """SUMMARY

        @Return:
        """
        self._sock.send(self._cmds.get('check'))
        return self._sock.recv(1024)


class _POWR(_StateAbstract):
    """Power
    """

    def on(self):
        """SUMMARY

        @Return:
        """
        return self._sendcmd('on')

    def off(self):
        """SUMMARY

        @Return:
        """
        return self._sendcmd('off')

    def isactive(self):
        r"""SUMMARY

        @Return:
        """
        return ('1\r' == self.getstatus())


class _ITGD(_ConnectAbstract):
    """Input toggle.
    """

    def toggle(self):
        """SUMMARY

        @Return:
        """
        self._sendcmd('toggle')


class _ITVD(_ConnectAbstract):
    """Input TV
    """

    def tv(self):
        """SUMMARY

        @Return:
        """
        self._sendcmd('tv')


class _IAVD(_ConnectAbstract):
    """Input
    """

    def input(self, num):
        """SUMMARY

        @Arguments:

        - `num`:

        @Return:
        """
        assert 1 <= num <= 5
        self._sendcmd(num)


class _IDEG(_ConnectAbstract):
    """Input degital
    """
    def toggle(self):
        """SUMMARY

        @Return:
        """
        self._sendcmd('toggle')


class _CBSD(_StateAbstract):
    """Channel BS
    """

    def setchannel(self, num):
        """SUMMARY

        @Arguments:

        - `num`:

        @Return:
        """
        assert 0 <= num <= 999
        self._send(self._cmds.get('format').format(num))


class _CCSD(_StateAbstract):
    """Channel CS
    """

    def setchannel(self, num):
        """SUMMARY

        @Arguments:

        - `num`:

        @Return:
        """
        assert 0 <= num <= 999
        self._send(self._cmds.get('format').format(num))


class _CTBD(_StateAbstract):
    """Channel CT
    """

    def setchannel(self, num):
        """SUMMARY

        @Arguments:

        - `num`:

        @Return:
        """
        assert 0 <= num <= 999
        self._send(self._cmds.get('format').format(num))


class _CHUP(_ConnectAbstract):
    """Channel Up
    """

    def up(self):
        """SUMMARY

        @Return:
        """
        self._sendcmd('up')


class _CHDW(_ConnectAbstract):
    """Channnel Down.
    """

    def down(self):
        """SUMMARY

        @Return:
        """
        self._sendcmd('down')


class _INP4(_ConnectAbstract):
    """Input4
    """

    def auto(self):
        """SUMMARY

        @Return:
        """
        self._sendcmd(0)

    def d_plug(self):
        """SUMMARY

        @Return:
        """
        self._sendcmd(1)

    def video_plug(self):
        """SUMMARY

        @Return:
        """
        self._sendcmd(4)


class _AVMD(_StateAbstract):
    """Av position
    """

    def toggle(self):
        """SUMMARY

        @Return:
        """
        self._sendcmd('toggle')

    def standard(self):
        """SUMMARY

        @Return:
        """
        self._sendcmd('standard')

    def movie(self):
        """SUMMARY

        @Return:
        """
        self._sendcmd('movie')

    def game(self):
        """SUMMARY

        @Return:
        """
        self._sendcmd('game')

    def avmemory(self):
        """SUMMARY

        @Return:
        """
        self._sendcmd('avmemory')

    def static_dynamic(self):
        """SUMMARY

        @Return:
        """
        self._sendcmd('static_dynamic')

    def dynamic(self):
        """SUMMARY

        @Return:
        """
        self._sendcmd('dynamic')

    def pc(self):
        """SUMMARY

        @Return:
        """
        self._sendcmd('pc')


class _VOLM(_StateAbstract):
    """
    """

    def setvolume(self, num):
        """SUMMARY

        @Arguments:

        - `num`:

        @Return:
        """
        assert 0 <= num <= 100
        recv = self._send(self._cmds.get('format').format(num))
        if self._ok == recv:
            return True
        elif self._err == recv:
            return False
        else:
            # Unknown Error
            raise StandardError(recv)

    def _volumeupdown(self, flag='up'):
        r"""SUMMARY

        @Return:
        """
        currvol = int(self.getstatus().strip())
        if flag == 'up':
            newvol = currvol + 1
        elif flag == 'down':
            newvol = currvol - 1
        else:
            raise ValueError('"{}" not support action'.format(flag))
        if not (0 <= newvol <= 100):
            print('up to limit "{}" 0-100'.format(newvol))
            return None
        if self.setvolume(newvol):
            return newvol
        else:
            return None

    def volumeup(self):
        r"""SUMMARY

        @Return:
        """
        return self._volumeupdown(flag='up')

    def volumedown(self):
        r"""SUMMARY

        @Return:
        """
        return self._volumeupdown(flag='down')


class _HPOS(_StateAbstract):
    """Horizon.
    """
    pass


class _VPOS(_StateAbstract):
    """Vertical.
    """
    pass


class _CLCK(_ConnectAbstract):
    """Clock.
    """
    pass


class _PHSE(_ConnectAbstract):
    """Clockpese.
    """
    pass


class _WIDE(_StateAbstract):
    """Display.
    """
    _display = {0: 'toggle',
                1: 'normal',
                2: 'smartzoom',
                3: 'wide4:3',
                4: 'cinema',
                5: 'full',
                6: 'full1',
                7: 'full2',
                8: 'underscan',
                9: 'dot_by_dot',
                10: 'wide16:9', }

    def get_current_diaplay(self):
        r"""SUMMARY

        @Return:
        """
        return self._display.get(int(self.getstatus(), ''))

    def toggle(self):
        """SUMMARY

        @Return:
        """
        self._sendcmd('toggle')

    def normal(self):
        """SUMMARY

        @Return:
        """
        self._sendcmd('smartzoom')

    def wide43(self):
        """SUMMARY

        @Return:
        """
        self._sendcmd('wide4:3')

    def cinema(self):
        """SUMMARY

        @Return:
        """
        self._sendcmd('cinema')

    def full(self):
        """SUMMARY

        @Return:
        """
        self._sendcmd('full')

    def full1(self):
        """SUMMARY

        @Return:
        """
        self._sendcmd('full1')

    def full2(self):
        """SUMMARY

        @Return:
        """
        self._sendcmd('full2')

    def underscan(self):
        """SUMMARY

        @Return:
        """
        self._sendcmd('underscan')

    def dot_by_dot(self):
        """SUMMARY

        @Return:
        """
        self._sendcmd('dot_by_dot')

    def wide169(self):
        """SUMMARY

        @Return:
        """
        self._sendcmd('wide:16:9')


class _MUTE(_StateAbstract):
    """Mute
    """
    def ismute(self):
        r"""SUMMARY

        @Return:
        """
        status = self.getstatus()
        if '2\r' == status:
            return False
        elif '1\r' == status:
            return True
        elif 'ERR\r' == status:
            raise StandardError('Err')
        else:
            return False

    def toggle(self):
        """SUMMARY

        @Return:
        """
        self._sendcmd(0)

    def on(self):
        """SUMMARY

        @Return:
        """
        self._sendcmd(1)

    def off(self):
        """SUMMARY

        @Return:
        """
        self._sendcmd(0)


class _ACHA(_ConnectAbstract):
    """Audio.
    """

    def toggle(self):
        """SUMMARY

        @Return:
        """
        self._sendcmd('toggle')


class _OFTM(_StateAbstract):
    """Off timer."""
    _timer = {0: 'off',
              1: '30min',
              2: '1h',
              3: '1h30min',
              4: '2h',
              5: '2h30min'}

    def reset(self):
        """SUMMARY

        @Return:
        """
        self._sendcmd('reset')

    def min30(self):
        """SUMMARY

        @Return:
        """
        self._sendcmd('30min')

    def h1(self):
        """SUMMARY

        @Return:
        """
        self._sendcmd('1h')

    def h1min30(self):
        """SUMMARY

        @Return:
        """
        self._sendcmd('1h30min')

    def h2(self):
        """SUMMARY

        @Return:
        """
        self._sendcmd('2h')

    def h2min30(self):
        """SUMMARY

        @Return:
        """
        self._sendcmd('2h30min')

    def get_current_time(self):
        r"""SUMMARY

        @Return:
        """
        return self._timer.get(int(self.getstatus()), '')


class _Channel(object):
    """Channel BS, CS, CT.
    """
    def __init__(self, sock):
        """
        """
        self._sock = sock
        self._channelup = _CHUP(sock=self._sock)
        self._channeldw = _CHDW(sock=self._sock)
        self.BS = _CBSD(sock=self._sock)
        self.CS = _CCSD(sock=self._sock)
        self.CT = _CTBD(sock=self._sock)

    def up(self):
        """SUMMARY

        @Return:
        """
        self._channelup.up()

    def down(self):
        """SUMMARY

        @Return:
        """
        self._channeldw.down()


class Aquos(object):
    """
    """
    power = None
    inputtoggle = None
    inputtv = None
    input = None
    inputdegital = None
    channel = None
    input4 = None
    avposition = None
    volume = None
    horizon = None
    vertical = None
    clock = None
    clockphese = None
    display = None
    mute = None
    audio = None
    offtimer = None

    def __init__(self, user,  host, port=10000, passwd=None):
        """

        Arguments:
        - `user`:
        - `passwd`:
        - `ip`:
        - `port`:
        """
        self._user = user
        self._host = host
        self._port = port
        self._sock = _socket.socket()
        if not self.login(passwd=passwd):
            raise StandardError()
        else:
            print('LOGIN OK!!')

    def __exit__(self, type, value, tb):
        r"""SUMMARY

        @Return:
        """
        self.close()

    def close(self):
        r"""SUMMARY

        @Return:
        """
        self._sock.close()

    def login(self, user=None, passwd=None):
        """SUMMARY

        @Arguments:

        - `user`:
        - `passwd`:

        @Return:
        """
        if not user:
            user = self._user
        if not passwd:
            passwd = _getpass('Aquos {} password: '.format(user))
        self._sock.connect((self._host, self._port))
        if 'Login:' == self._sock.recv(1024):
            responce = self.send(user)
        if '\r\nPassword:' == responce:
            if not passwd.endswith('\n'):
                passwd += '\n'
            self._sock.send(passwd)
            del passwd
            # determine command
            self.send('POWR?   ')
        if self._sock.recv(1024).strip() in ['0', '1']:
            self._setcommand()
            return True
        return False

    def relogin(self, user, passwd):
        """SUMMARY

        @Arguments:

        - `user`:
        - `passwd`:

        @Return:
        """
        self.login(user=user, passwd=passwd)

    def send(self, cmd):
        r"""SUMMARY

        @Arguments:

        - `cmd`:

        @Return:
        """
        if not cmd.endswith('\n'):
            cmd += '\n'
        self._sock.send(cmd)
        return self._sock.recv(1024)

    def _setcommand(self):
        """SUMMARY

        @Return:
        """
        self.power = _POWR(sock=self._sock)
        self.inputtoggle = _ITGD(sock=self._sock)
        self.inputtv = _ITVD(sock=self._sock)
        self.input = _IAVD(sock=self._sock)
        self.inputdegital = _IDEG(sock=self._sock)
        # self.channelBS = _CBSD(sock=self._sock)
        # self.channelCS = _CCSD(sock=self._sock)
        # self.channelTB = _CTBD(sock=self._sock)
        self.channel = _Channel(sock=self._sock)
        self.input4 = _INP4(sock=self._sock)
        self.avposition = _AVMD(sock=self._sock)
        self.volume = _VOLM(sock=self._sock)
        self.horizon = _HPOS(sock=self._sock)
        self.vertical = _VPOS(sock=self._sock)
        self.clock = _CLCK(sock=self._sock)
        self.clockphese = _PHSE(sock=self._sock)
        self.display = _WIDE(sock=self._sock)
        self.mute = _MUTE(sock=self._sock)
        self.audio = _ACHA(sock=self._sock)
        self.offtimer = _OFTM(sock=self._sock)

    def __str__(self):
        r"""SUMMARY

        @Return:
        """
        strs = ['{0:=^50}'.format(' Main commands ')]
        append = strs.append
        fmt = '{0:<12}: {1}'.format

        def membercmds(obj):
            r"""SUMMARY

            @Return:
            """
            # lis = []
            # for memb in dir(obj):
                # if not memb.startswith('_'):
                    # lis.append(memb)
            return [memb for memb in dir(obj) if not memb.startswith('_')]

        # Main command
        for mem in membercmds(self):
            if _ismethod(getattr(self, mem)):
                append(fmt(mem, type(getattr(self, mem))))

        # Sub class
        append('\n{0:=^50}'.format(' Sub classes '))
        for mem in membercmds(self):
            if not _ismethod(getattr(self, mem)):
                append(fmt(mem, type(getattr(self, mem))))

        # Sub command
        if self.power is not None:
            append('\n{0:=^50}'.format(' Sub commands '))
            append(fmt(
                'power', "'" + "', '".join(membercmds(self.power)) + "'"))
            append(fmt(
                'inputtoggle', "'" + "', '".join(membercmds(self.inputtoggle)) + "'"))
            append(fmt(
                'inputtv', "'" + "', '".join(membercmds(self.inputtv)) + "'"))
            append(fmt(
                'input', "'" + "', '".join(membercmds(self.input)) + "'"))
            append(fmt(
                'channel', "'" + "', '".join(membercmds(self.channel)) + "'"))
            append(fmt(
                'input4', "'" + "', '".join(membercmds(self.input4)) + "'"))
            append(fmt(
                'avposition', "'" + "', '".join(membercmds(self.avposition)) + "'"))
            append(fmt(
                'volume', "'" + "', '".join(membercmds(self.volume)) + "'"))
            append(fmt(
                'horizon', "'" + "', '".join(membercmds(self.horizon)) + "'"))
            append(fmt(
                'vertical', "'" + "', '".join(membercmds(self.vertical)) + "'"))
            append(fmt(
                'clock', "'" + "', '".join(membercmds(self.clock)) + "'"))
            append(fmt(
                'clockphese', "'" + "', '".join(membercmds(self.clockphese)) + "'"))
            append(fmt(
                'display', "'" + "', '".join(membercmds(self.display)) + "'"))
            append(fmt(
                'mute', "'" + "', '".join(membercmds(self.mute)) + "'"))
            append(fmt(
                'audio', "'" + "', '".join(membercmds(self.audio)) + "'"))
            append(fmt(
                'offtimer', "'" + "', '".join(membercmds(self.offtimer)) + "'"))
        return '\n'.join(strs)

    def __repr__(self):
        r"""SUMMARY

        @Return:
        """
        return (str(self) + '\n' + self.__str__())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# constractor.py ends here
